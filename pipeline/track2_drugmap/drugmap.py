#!/usr/bin/env python3.11
"""
track2_drugmap: gene + mechanism description -> ranked table of market-approved
drugs with a label-based harm screen. Public APIs only, no patient data.

Usage
    python3.11 drugmap.py --config targets_bub1b.json --out ../../track2/creative/E_drugmap_output
    python3.11 drugmap.py --gene TP53 --targets "MDM2:MDM2,CDKN1A" --out /tmp/tp53

Steps
    1. Open Targets Platform GraphQL: resolve gene symbol -> Ensembl ID, pull
       physical interaction partners (STRING/IntAct, score threshold), pull
       drugs and clinical candidates per target (drugAndClinicalCandidates).
    2. ChEMBL REST: parent molecule, max_phase, first approval, mechanism of
       action (looked up by parent_molecule_chembl_id).
    3. openFDA drug label API: most recent single-ingredient prescription
       label; boxed warning, warnings, warnings and precautions, pediatric use;
       regex harm flags.
    4. Rank: approved (ChEMBL max_phase 4 AND a US label or an Open Targets
       APPROVAL stage), pediatric-use section present, fewest harm flags.
       Emit CSV + Markdown with evidence links.

Dependencies: Python 3.11 standard library + certifi (SSL on macOS).
Every HTTP response is cached as JSON under --cache so reruns are offline.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:  # fall back to system store
    SSL_CTX = ssl.create_default_context()

OT_URL = "https://api.platform.opentargets.org/api/v4/graphql"
CHEMBL_URL = "https://www.ebi.ac.uk/chembl/api/data"
FDA_URL = "https://api.fda.gov/drug/label.json"
UA = "track2_drugmap/0.1 (open tool, MVA hackathon)"

SALT_WORDS = {
    "SUCCINATE", "SULFATE", "SULPHATE", "MESYLATE", "TARTRATE", "DITARTRATE",
    "HYDROCHLORIDE", "DIHYDROCHLORIDE", "ANHYDROUS", "SODIUM", "POTASSIUM",
    "CALCIUM", "MALEATE", "CITRATE", "ACETATE", "PHOSPHATE", "HYDRATE",
    "MONOHYDRATE", "DIHYDRATE", "TRIHYDRATE", "HEMIHYDRATE", "FUMARATE",
    "BROMIDE", "CHLORIDE", "TOSYLATE", "BESYLATE", "LACTATE", "HYDROBROMIDE",
    "DISODIUM", "TROMETHAMINE", "PAMOATE", "ETHANOLATE", "PROPIONATE",
}

# Harm flags. Deliberately narrow so that an oncology label's indication text
# ("breast cancer") does not trip the malignancy flag. Applied only to boxed
# warning, warnings, warnings and precautions and pediatric use sections.
HARM_PATTERNS = {
    "growth": r"\b(growth (retardation|suppression|impairment|failure|velocity|delay|inhibition)|"
              r"(reduced|decreased|impaired|delayed|slowed|stunted) (linear |bone )?growth|"
              r"short stature|bone growth|linear growth|growing bones?|growth plates?|"
              r"epiphyse\w*|physeal|growing (incisor|teeth))",
    "malignancy": r"\b(malignan\w+|neoplasm\w*|lymphoproliferative|second(ary)? (primary )?"
                  r"(cancers?|malignanc\w+)|skin cancers?|carcinogen\w*|lymphomas?|"
                  r"tumou?rigen\w*|new primary (cancers?|malignanc\w+))",
    "immunosuppression": r"\b(immunosuppress\w*|immunocompromis\w*|serious infections?|"
                         r"opportunistic infections?|reactivation of (hepatitis|tuberculosis)|"
                         r"progressive multifocal leukoencephalopathy)",
    "nephrotoxicity": r"\b(nephrotoxic\w*|nephrocalcinosis|renal (failure|impairment|toxicity|injury|"
                      r"tubular)|acute kidney injury|nephropath\w*|proteinuria|nephrolithiasis|"
                      r"hypercalciuria|kidney stones?)",
    "myelosuppression": r"\b(myelosuppress\w*|neutropeni\w*|thrombocytopeni\w*|pancytopeni\w*|"
                        r"cytopeni\w*|bone marrow (suppression|failure)|agranulocytosis|"
                        r"aplastic an(a)?emia|leukopeni\w*)",
    "retinal": r"\b(retina\b|retinal\b|retinopath\w*|maculopath\w*|macular (degeneration|toxicity|damage)|"
               r"visual field (defect|loss)|photoreceptor\w*)",
}
HARM_RE = {k: re.compile(v, re.IGNORECASE) for k, v in HARM_PATTERNS.items()}

STAGE_ORDER = {"APPROVAL": 4, "PHASE_3": 3, "PHASE_2_3": 2.5, "PHASE_2": 2,
               "PHASE_1_2": 1.5, "PHASE_1": 1}

LOG = []


def log(msg):
    stamp = datetime.now(timezone.utc).strftime("%H:%M:%S")
    line = f"[{stamp}] {msg}"
    LOG.append(line)
    print(line, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------
# HTTP with JSON cache and graceful degradation
# --------------------------------------------------------------------------
class Http:
    def __init__(self, cache_dir, min_interval=0.25):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.min_interval = min_interval
        self.last = 0.0
        self.calls = 0
        self.failures = {}

    def _key(self, url, body):
        h = hashlib.sha1((url + "|" + (body or "")).encode()).hexdigest()
        return os.path.join(self.cache_dir, h + ".json")

    def request(self, url, body=None, retries=3):
        path = self._key(url, body)
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
        wait = self.min_interval - (time.time() - self.last)
        if wait > 0:
            time.sleep(wait)
        data = body.encode() if body else None
        headers = {"User-Agent": UA, "Accept": "application/json"}
        if body:
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=headers)
        for attempt in range(retries):
            try:
                with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as r:
                    payload = json.load(r)
                self.last = time.time()
                self.calls += 1
                with open(path, "w") as f:
                    json.dump(payload, f)
                return payload
            except urllib.error.HTTPError as e:
                self.last = time.time()
                if e.code == 404:
                    payload = {"_http": 404}
                    with open(path, "w") as f:
                        json.dump(payload, f)
                    return payload
                if e.code == 429 and attempt < retries - 1:
                    time.sleep(5 * (attempt + 1))
                    continue
                if e.code == 400:
                    try:
                        detail = e.read().decode()[:400]
                    except Exception:
                        detail = ""
                    return {"_http": 400, "_detail": detail}
                self.failures[url.split("?")[0]] = e.code
                if attempt == retries - 1:
                    return {"_http": e.code}
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                self.last = time.time()
                if attempt == retries - 1:
                    self.failures[url.split("?")[0]] = str(e)
                    return {"_error": str(e)}
                time.sleep(2 * (attempt + 1))
        return {"_error": "unreachable"}


# --------------------------------------------------------------------------
# Step 1: Open Targets
# --------------------------------------------------------------------------
OT_SEARCH = """query($s:String!){ search(queryString:$s, entityNames:["target"], page:{index:0,size:5}){
  hits{ id object{ ... on Target { approvedSymbol } } } } }"""

OT_INTERACTIONS = """query($id:String!,$thr:Float!,$n:Int!){ target(ensemblId:$id){ approvedSymbol approvedName
  interactions(page:{index:0,size:$n}, scoreThreshold:$thr){ count rows{
    targetB{ approvedSymbol id } sourceDatabase score intB } } } }"""

OT_DRUGS = """query($ids:[String!]!){ targets(ensemblIds:$ids){ id approvedSymbol approvedName
  drugAndClinicalCandidates{ count rows{ maxClinicalStage drug{ id name drugType maximumClinicalStage
    tradeNames{ label } parentMolecule{ id name }
    mechanismsOfAction{ rows{ mechanismOfAction actionType targetName targets{ approvedSymbol } } }
    drugWarnings{ warningType toxicityClass description country year } }
    diseases{ disease{ name id } } } } } }"""


def ot_query(http, query, variables):
    body = json.dumps({"query": query, "variables": variables})
    r = http.request(OT_URL, body)
    if "_http" in r or "_error" in r:
        return None, r
    if "errors" in r and not r.get("data"):
        return None, r
    return r.get("data"), None


def ot_resolve(http, symbol):
    data, err = ot_query(http, OT_SEARCH, {"s": symbol})
    if not data:
        return None
    for hit in data["search"]["hits"]:
        obj = hit.get("object") or {}
        if (obj.get("approvedSymbol") or "").upper() == symbol.upper():
            return hit["id"]
    hits = data["search"]["hits"]
    return hits[0]["id"] if hits else None


def ot_interactions(http, ensembl_id, threshold, size):
    data, err = ot_query(http, OT_INTERACTIONS, {"id": ensembl_id, "thr": threshold, "n": size})
    if not data or not data.get("target"):
        return [], err
    t = data["target"]
    best = {}
    for r in t["interactions"]["rows"]:
        if r["targetB"] and r["targetB"]["approvedSymbol"]:
            eid = r["targetB"]["id"]
            cur = best.get(eid)
            if cur is None or (r["score"] or 0) > (cur["score"] or 0):
                best[eid] = {"symbol": r["targetB"]["approvedSymbol"], "id": eid,
                             "score": r["score"], "source": r["sourceDatabase"]}
    return sorted(best.values(), key=lambda x: -(x["score"] or 0)), None


def ot_drugs_for_targets(http, ensembl_ids, batch=10):
    out = {}
    for i in range(0, len(ensembl_ids), batch):
        chunk = ensembl_ids[i:i + batch]
        data, err = ot_query(http, OT_DRUGS, {"ids": chunk})
        if not data:
            log(f"Open Targets drug query failed for {chunk}: {err}")
            continue
        for t in data["targets"]:
            out[t["id"]] = t
    return out


# --------------------------------------------------------------------------
# Step 2: ChEMBL
# --------------------------------------------------------------------------
def chembl_molecule(http, chembl_id):
    r = http.request(f"{CHEMBL_URL}/molecule/{chembl_id}.json")
    if "_http" in r or "_error" in r:
        return None
    return r


def chembl_find_by_name(http, name):
    q = urllib.parse.quote(name.upper())
    r = http.request(f"{CHEMBL_URL}/molecule.json?pref_name__iexact={q}&limit=3")
    mols = r.get("molecules") or []
    if not mols:
        r = http.request(f"{CHEMBL_URL}/molecule.json?molecule_synonyms__molecule_synonym__iexact={q}&limit=3")
        mols = r.get("molecules") or []
    if not mols:
        return None
    # prefer the parent
    for m in mols:
        h = m.get("molecule_hierarchy") or {}
        if h.get("parent_chembl_id") == m["molecule_chembl_id"]:
            return m
    return mols[0]


def chembl_mechanisms(http, parent_id):
    r = http.request(f"{CHEMBL_URL}/mechanism.json?parent_molecule_chembl_id={parent_id}&limit=50")
    return r.get("mechanisms") or []


# --------------------------------------------------------------------------
# Step 3: openFDA labels
# --------------------------------------------------------------------------
def base_name(name):
    words = [w for w in re.split(r"[\s,]+", name.upper()) if w and w not in SALT_WORDS]
    return " ".join(words).strip()


def fda_label(http, name):
    """Most recent single-ingredient human prescription label for a generic name.
    Returns (label_dict or None, note)."""
    b = base_name(name)
    if not b:
        return None, "empty name"
    search = f'openfda.generic_name:"{b}" AND openfda.product_type:"HUMAN PRESCRIPTION DRUG"'
    url = f"{FDA_URL}?search={urllib.parse.quote(search)}&limit=25&sort=effective_time:desc"
    r = http.request(url)
    if r.get("_http") == 404:
        return None, "no US prescription label in openFDA"
    if "_http" in r or "_error" in r:
        return None, f"openFDA error {r.get('_http') or r.get('_error')}"
    results = r.get("results") or []
    if not results:
        return None, "no US prescription label in openFDA"

    def single(res):
        g = [x.upper() for x in (res.get("openfda", {}).get("generic_name") or [])]
        if len(g) != 1:
            return False
        gn = g[0]
        if " AND " in gn or "," in gn:
            return False
        return base_name(gn).startswith(b.split()[0])

    singles = [x for x in results if single(x)]
    pool = singles or results
    systemic = {"ORAL", "INTRAVENOUS", "INTRAMUSCULAR", "SUBCUTANEOUS", "INTRATHECAL", "INTRAVESICAL",
                "SUBLINGUAL", "BUCCAL", "RECTAL", "TRANSDERMAL", "INTRAPERITONEAL"}

    def warn_len(x):
        return sum(len(" ".join(x.get(k) or [])) for k in
                   ("boxed_warning", "warnings", "warnings_and_cautions", "warnings_and_precautions"))

    def score(x):
        routes = {r.upper() for r in (x.get("openfda", {}).get("route") or [])}
        return (bool(routes & systemic), "boxed_warning" in x, warn_len(x) > 400,
                "pediatric_use" in x, x.get("effective_time", ""))

    # conservative choice for a harm screen: systemic route, boxed warning, fullest warnings text
    pool.sort(key=score, reverse=True)
    chosen = pool[0]
    routes = ",".join(chosen.get("openfda", {}).get("route") or [])
    note = ("single-ingredient label" if singles else "combination or mixed label (no single-ingredient label found)")
    note += f"; route {routes or 'unknown'}"
    return chosen, note


def harm_screen(label):
    sections = {}
    for key in ("boxed_warning", "warnings", "warnings_and_cautions", "warnings_and_precautions",
                "pediatric_use"):
        val = label.get(key)
        if val:
            sections[key] = " ".join(val) if isinstance(val, list) else str(val)
    text = " ".join(sections.values())
    flags = {}
    for name, rx in HARM_RE.items():
        m = rx.search(text)
        if m:
            s = max(0, m.start() - 70)
            snippet = re.sub(r"\s+", " ", text[s:m.end() + 70]).strip()
            flags[name] = snippet
    ped = sections.get("pediatric_use", "")
    ped_status = "absent"
    if ped:
        if re.search(r"not (been )?established", ped, re.I) and not re.search(
                r"(is|are) (indicated|approved)|established in pediatric|pediatric patients (aged|\d)", ped, re.I):
            ped_status = "present: safety/effectiveness not established"
        else:
            ped_status = "present: pediatric information given"
    return flags, sections, ped_status


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------
def parse_targets_arg(s):
    out = {}
    for part in s.split(";"):
        part = part.strip()
        if not part:
            continue
        name, genes = part.split(":", 1)
        out[name.strip()] = {"genes": [g.strip() for g in genes.split(",") if g.strip()], "note": ""}
    return out


def stage_rank(stage):
    return STAGE_ORDER.get(stage or "", 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", help="JSON config (gene, consequence_targets, seed_drugs)")
    ap.add_argument("--gene", help="gene symbol (overrides config)")
    ap.add_argument("--targets", help='"name:GENE1,GENE2;name2:GENE3" (overrides config)')
    ap.add_argument("--out", required=True, help="output prefix (writes .csv and .md)")
    ap.add_argument("--cache", default=None, help="cache dir (default: <out dir>/.drugmap_cache)")
    ap.add_argument("--partner-threshold", type=float, default=None)
    ap.add_argument("--partner-max", type=int, default=None)
    ap.add_argument("--no-partners", action="store_true", help="skip interaction partner drugs")
    args = ap.parse_args()

    t0 = time.time()
    cfg = {}
    if args.config:
        with open(args.config) as f:
            cfg = json.load(f)
    gene = args.gene or cfg.get("gene")
    if not gene:
        ap.error("need --gene or config with gene")
    targets = parse_targets_arg(args.targets) if args.targets else cfg.get("consequence_targets", {})
    # optional per-mechanism action direction and curated exclusions
    wanted_action = {m: {a.upper() for a in spec.get("action", [])} for m, spec in targets.items()}
    excluded = {}
    for m, spec in targets.items():
        for dn, why in (spec.get("exclude") or {}).items():
            excluded[dn.upper()] = f"{m}: {why}"
    seeds = {k: v for k, v in cfg.get("seed_drugs", {}).items() if k != "description"} if not args.targets else {}
    thr = args.partner_threshold or cfg.get("partner_score_threshold", 0.9)
    pmax = args.partner_max or cfg.get("partner_max", 80)

    out_dir = os.path.dirname(os.path.abspath(args.out)) or "."
    os.makedirs(out_dir, exist_ok=True)
    cache = args.cache or os.path.join(out_dir, ".drugmap_cache")
    http = Http(cache)
    api_status = {"opentargets": "ok", "chembl": "ok", "openfda": "ok"}

    # ---- Step 1a: resolve all symbols
    log(f"Resolving {gene} and {sum(len(v['genes']) for v in targets.values())} consequence genes in Open Targets")
    gene_id = ot_resolve(http, gene)
    if not gene_id:
        api_status["opentargets"] = "unreachable or gene not found"
        log("Open Targets did not resolve the gene; continuing with ChEMBL/openFDA seeds only")
    symbol_to_id = {}
    id_to_mech = {}
    for mech, spec in targets.items():
        for sym in spec["genes"]:
            eid = ot_resolve(http, sym)
            if eid:
                symbol_to_id[sym] = eid
                id_to_mech.setdefault(eid, []).append(mech)
            else:
                log(f"  {sym}: not resolved")

    # ---- Step 1b: interaction partners
    partners = []
    if gene_id and not args.no_partners:
        partners, err = ot_interactions(http, gene_id, thr, pmax)
        if err:
            log(f"interactions failed: {err}")
        log(f"{gene}: {len(partners)} interaction partners at score >= {thr}")
    partner_ids = {p["id"]: p for p in partners}

    # ---- Step 1c: drugs per target
    all_ids = ([gene_id] if gene_id else []) + list(symbol_to_id.values()) + list(partner_ids)
    all_ids = list(dict.fromkeys(all_ids))
    log(f"Pulling drugs and clinical candidates for {len(all_ids)} targets")
    tdata = ot_drugs_for_targets(http, all_ids)
    if not tdata and all_ids:
        api_status["opentargets"] = "drug query failed"

    # candidate rows keyed by ChEMBL parent id
    drugs = {}

    def add_drug(chembl_id, name, role, mech, via_symbol, via_id, ot_row=None, seed=False):
        key = chembl_id
        d = drugs.setdefault(key, {
            "chembl_id": chembl_id, "name": name, "roles": set(), "mechanisms": set(),
            "via": set(), "ot_stage": None, "ot_moa": set(), "ot_warnings": set(),
            "ot_diseases": set(), "trade_names": set(), "seed": seed,
        })
        d["roles"].add(role)
        d["mechanisms"].add(mech)
        d["via"].add(f"{via_symbol} ({via_id})" if via_id else via_symbol)
        if ot_row:
            st = ot_row.get("maxClinicalStage")
            if stage_rank(st) > stage_rank(d["ot_stage"]):
                d["ot_stage"] = st
            dr = ot_row["drug"]
            for tn in dr.get("tradeNames") or []:
                d["trade_names"].add(tn["label"])
            for m in ((dr.get("mechanismsOfAction") or {}).get("rows") or []):
                tg = ",".join(t["approvedSymbol"] for t in (m.get("targets") or []))
                d["ot_moa"].add(f"{m['mechanismOfAction']} [{tg}]")
            for w in dr.get("drugWarnings") or []:
                d["ot_warnings"].add(f"{w['warningType']}: {w.get('toxicityClass') or w.get('description') or ''} ({w.get('country') or ''} {w.get('year') or ''})".strip())
            for dis in ot_row.get("diseases") or []:
                if dis.get("disease") and dis["disease"].get("name"):
                    d["ot_diseases"].add(dis["disease"]["name"])
        return d

    for eid, t in tdata.items():
        sym = t["approvedSymbol"]
        if eid == gene_id:
            role, mechs = "gene", [f"{gene} itself"]
        elif eid in id_to_mech:
            role, mechs = "consequence", id_to_mech[eid]
        else:
            role, mechs = "partner", [f"interaction partner of {gene} (score {partner_ids[eid]['score']})"]
        for row in t["drugAndClinicalCandidates"]["rows"]:
            dr = row["drug"]
            parent = (dr.get("parentMolecule") or {}).get("id") or dr["id"]
            pname = (dr.get("parentMolecule") or {}).get("name") or dr["name"]
            for mech in mechs:
                add_drug(parent, pname, role, mech, sym, eid, ot_row=row)

    # ---- seeds
    for mech, names in seeds.items():
        for n in names:
            m = chembl_find_by_name(http, n)
            if not m:
                log(f"  seed {n}: not found in ChEMBL")
                drugs[f"SEED:{n}"] = {"chembl_id": "", "name": n.upper(), "roles": {"seed"},
                                      "mechanisms": {mech}, "via": {"seed list"}, "ot_stage": None,
                                      "ot_moa": set(), "ot_warnings": set(), "ot_diseases": set(),
                                      "trade_names": set(), "seed": True}
                continue
            parent = (m.get("molecule_hierarchy") or {}).get("parent_chembl_id") or m["molecule_chembl_id"]
            add_drug(parent, m.get("pref_name") or n.upper(), "seed", mech, "seed list", None, seed=True)

    log(f"{len(drugs)} unique molecules; querying ChEMBL")

    # ---- Step 2: ChEMBL
    for key, d in drugs.items():
        if not d["chembl_id"]:
            d.update({"chembl_max_phase": None, "chembl_first_approval": None, "chembl_moa": [],
                      "chembl_type": None, "chembl_black_box": None})
            continue
        m = chembl_molecule(http, d["chembl_id"])
        if m is None:
            api_status["chembl"] = "partial failures"
            d.update({"chembl_max_phase": None, "chembl_first_approval": None, "chembl_moa": [],
                      "chembl_type": None, "chembl_black_box": None})
            continue
        d["chembl_max_phase"] = m.get("max_phase")
        d["chembl_first_approval"] = m.get("first_approval")
        d["chembl_type"] = m.get("molecule_type")
        d["chembl_black_box"] = m.get("black_box_warning")
        if m.get("pref_name"):
            d["name"] = m["pref_name"]
        mechs = chembl_mechanisms(http, d["chembl_id"])
        d["chembl_moa"] = sorted({f"{x['mechanism_of_action']} ({x.get('action_type') or ''})" for x in mechs})

    # ---- Step 3: openFDA
    log("Querying openFDA labels")
    for key, d in drugs.items():
        label, note = fda_label(http, d["name"])
        d["fda_note"] = note
        if label is None:
            if "error" in note:
                api_status["openfda"] = "partial failures"
            d.update({"fda_setid": "", "fda_brand": "", "fda_effective": "", "harm_flags": {},
                      "ped_status": "no label", "fda_sections": []})
            continue
        flags, sections, ped_status = harm_screen(label)
        d["fda_setid"] = label.get("set_id", "")
        d["fda_brand"] = ";".join((label.get("openfda", {}).get("brand_name") or [])[:2])
        d["fda_effective"] = label.get("effective_time", "")
        d["harm_flags"] = flags
        d["ped_status"] = ped_status
        d["fda_sections"] = sorted(sections)

    # ---- Step 4: approval logic and ranking
    rows = []
    for key, d in drugs.items():
        ph4 = str(d.get("chembl_max_phase")) in ("4", "4.0")
        has_label = bool(d.get("fda_setid"))
        ot_appr = d.get("ot_stage") == "APPROVAL"
        if ph4 and has_label:
            approved, jurisdiction = True, "US (FDA label found)"
        elif ph4 and ot_appr:
            approved, jurisdiction = True, "approved somewhere per ChEMBL/Open Targets; no US prescription label (check EMA/PMDA)"
        elif ph4:
            approved, jurisdiction = True, "ChEMBL max_phase 4 only; no US label, no OT approval stage (verify manually)"
        elif ot_appr:
            approved, jurisdiction = False, "Open Targets says APPROVAL but ChEMBL max_phase < 4 and no US label: treat as unverified"
        else:
            approved, jurisdiction = False, "not approved"
        ped_present = d.get("ped_status", "").startswith("present")
        nflags = len(d.get("harm_flags", {}))
        hazard = "partner" in d["roles"] and not ({"consequence", "seed"} & d["roles"])
        # action direction: compare ChEMBL action types with what the mechanism asks for
        actions = set()
        for moa in d.get("chembl_moa") or []:
            m_ = re.search(r"\(([A-Z ]+)\)$", moa)
            if m_ and m_.group(1).strip():
                actions.add(m_.group(1).strip())
        wants = set()
        for mech in d["mechanisms"]:
            wants |= wanted_action.get(mech, set())
        if not wants or not actions:
            direction = "not checked"
        elif actions & wants:
            direction = "match"
        else:
            direction = f"mismatch: drug is {'/'.join(sorted(actions))}, mechanism asks {'/'.join(sorted(wants))}"
        curated_out = excluded.get(base_name(d["name"]), "") or excluded.get(d["name"].upper(), "")
        rows.append({
            "rank_key": (0 if approved else 1, 0 if not hazard else 1, 0 if not curated_out else 1,
                         0 if not direction.startswith("mismatch") else 1, 0 if ped_present else 1, nflags, d["name"]),
            "drug": d["name"], "chembl_id": d["chembl_id"], "role": "/".join(sorted(d["roles"])),
            "hazard_class": "yes: acts on a mitotic partner of the gene" if hazard else "",
            "direction": direction, "curated_out": curated_out,
            "mechanism_targets": "; ".join(sorted(d["mechanisms"])),
            "via_targets": "; ".join(sorted(d["via"])),
            "approved": "yes" if approved else "no", "jurisdiction": jurisdiction,
            "chembl_max_phase": d.get("chembl_max_phase"), "chembl_first_approval": d.get("chembl_first_approval"),
            "ot_stage": d.get("ot_stage") or "", "chembl_moa": " | ".join(d.get("chembl_moa") or sorted(d["ot_moa"])),
            "ot_warnings": " | ".join(sorted(d["ot_warnings"])),
            "ot_indications": "; ".join(sorted(d["ot_diseases"])[:6]),
            "fda_brand": d.get("fda_brand", ""), "fda_setid": d.get("fda_setid", ""),
            "fda_effective": d.get("fda_effective", ""), "fda_note": d.get("fda_note", ""),
            "fda_sections": ",".join(d.get("fda_sections", [])),
            "pediatric_use": d.get("ped_status", ""), "n_harm_flags": nflags,
            "harm_flags": ";".join(sorted(d.get("harm_flags", {}))),
            "harm_snippets": " || ".join(f"{k}: {v}" for k, v in sorted(d.get("harm_flags", {}).items())),
            "chembl_black_box": d.get("chembl_black_box"),
            "link_ot_drug": f"https://platform.opentargets.org/drug/{d['chembl_id']}" if d["chembl_id"] else "",
            "link_chembl": f"https://www.ebi.ac.uk/chembl/compound_report_card/{d['chembl_id']}/" if d["chembl_id"] else "",
            "link_label": f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={d['fda_setid']}" if d.get("fda_setid") else "",
        })
    rows.sort(key=lambda r: r["rank_key"])
    for i, r in enumerate(rows, 1):
        r["rank"] = i
        del r["rank_key"]

    elapsed = time.time() - t0
    cols = ["rank", "drug", "chembl_id", "role", "hazard_class", "direction", "curated_out", "mechanism_targets", "via_targets", "approved",
            "jurisdiction", "chembl_max_phase", "chembl_first_approval", "ot_stage", "chembl_moa", "ot_warnings",
            "ot_indications", "fda_brand", "fda_setid", "fda_effective", "fda_note", "fda_sections",
            "pediatric_use", "n_harm_flags", "harm_flags", "harm_snippets", "chembl_black_box",
            "link_ot_drug", "link_chembl", "link_label"]
    csv_path = args.out + ".csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # ---- Markdown
    md = []
    md.append(f"# Drug map for {gene}\n")
    md.append(f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by pipeline/track2_drugmap/drugmap.py. "
              f"Run time {elapsed:.0f} s, {http.calls} live HTTP calls (cached responses not counted).\n")
    md.append("API status: " + ", ".join(f"{k}: {v}" for k, v in api_status.items()) + ".\n")
    if http.failures:
        md.append("Endpoints with failures: " + "; ".join(f"{k} ({v})" for k, v in http.failures.items()) + "\n")
    md.append("## Inputs\n")
    md.append(f"- Gene: {gene} ({gene_id or 'unresolved'}), https://platform.opentargets.org/target/{gene_id}\n")
    for mech, spec in targets.items():
        resolved = [f"{g} ({symbol_to_id[g]})" if g in symbol_to_id else f"{g} (unresolved)" for g in spec["genes"]]
        md.append(f"- {mech}: {', '.join(resolved)}" + (f". {spec.get('note')}" if spec.get("note") else ""))
    if seeds:
        md.append("- Seed drugs (mechanism classes without a ChEMBL protein target): " +
                  "; ".join(f"{k}: {', '.join(v)}" for k, v in seeds.items()))
    md.append(f"- Interaction partners of {gene} at score >= {thr}: {len(partners)} "
              f"({', '.join(sorted(p['symbol'] for p in partners))})\n")

    md.append("## Drugs per target (Open Targets drugAndClinicalCandidates)\n")
    md.append("| Target | Role | Candidates (any stage) | Approved names |")
    md.append("|---|---|---|---|")
    for eid, t in sorted(tdata.items(), key=lambda kv: kv[1]["approvedSymbol"]):
        sym = t["approvedSymbol"]
        role = "gene" if eid == gene_id else ("consequence: " + ", ".join(id_to_mech[eid]) if eid in id_to_mech else "partner")
        rws = t["drugAndClinicalCandidates"]["rows"]
        appr = sorted({((r["drug"].get("parentMolecule") or {}).get("name") or r["drug"]["name"]) for r in rws if r["maxClinicalStage"] == "APPROVAL"})
        if not rws and role == "partner":
            continue
        md.append(f"| [{sym}](https://platform.opentargets.org/target/{eid}) | {role} | {t['drugAndClinicalCandidates']['count']} | {', '.join(appr) or '-'} |")
    md.append("")

    def table(title, subset):
        md.append(f"## {title}\n")
        if not subset:
            md.append("(none)\n")
            return
        md.append("| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Direction | Pediatric-use section | Harm flags | Label | Evidence |")
        md.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in subset:
            links = []
            if r["link_ot_drug"]:
                links.append(f"[OT]({r['link_ot_drug']})")
            if r["link_chembl"]:
                links.append(f"[ChEMBL]({r['link_chembl']})")
            if r["link_label"]:
                links.append(f"[label]({r['link_label']})")
            moa = r["chembl_moa"][:110] + ("..." if len(r["chembl_moa"]) > 110 else "")
            lbl = f"{r['fda_brand']} {r['fda_effective'][:4]}".strip() if r["fda_setid"] else r["fda_note"]
            dirn = r["direction"][:60] + (f"; curated out ({r['curated_out'][:70]})" if r["curated_out"] else "")
            md.append(f"| {r['rank']} | {r['drug']} | {r['mechanism_targets'][:80]} | {r['via_targets'][:60]} | {r['approved']} | "
                      f"{r['jurisdiction'][:60]} | {moa} | {dirn} | {r['pediatric_use']} | {r['n_harm_flags']}: {r['harm_flags']} | {lbl} | {' '.join(links)} |")
        md.append("")

    cand = [r for r in rows if r["approved"] == "yes" and not r["hazard_class"] and not r["curated_out"] and not r["direction"].startswith("mismatch")]
    demoted = [r for r in rows if r["approved"] == "yes" and not r["hazard_class"] and (r["curated_out"] or r["direction"].startswith("mismatch"))]
    haz = [r for r in rows if r["approved"] == "yes" and r["hazard_class"]]
    rest = [r for r in rows if r["approved"] == "no"]
    table("Ranked: approved drugs acting on consequence targets or seeds (approved, pediatric section, fewest flags)", cand)
    table("Approved but demoted: wrong action direction for the mechanism, or curated out in the config", demoted)
    table("Approved drugs acting on interaction partners of the gene (hazard class, listed for avoidance not use)", haz)
    table("Not approved (context only)", rest[:40])
    if len(rest) > 40:
        md.append(f"({len(rest) - 40} further unapproved candidates omitted; see CSV)\n")

    md.append("## Harm-flag evidence snippets (approved drugs)\n")
    for r in cand + haz:
        if r["harm_snippets"]:
            md.append(f"**{r['drug']}** ({r['fda_brand']}, {r['link_label']})")
            for part in r["harm_snippets"].split(" || "):
                md.append(f"- {part}")
            md.append("")

    md.append("## Method notes\n")
    md.append("- Approval = ChEMBL max_phase 4 AND (a US prescription label in openFDA OR an Open Targets APPROVAL stage). "
              "An Open Targets APPROVAL stage alone is not trusted (it marked acadesine and navitoclax as approved in the BUB1B run).")
    md.append("- Label chosen: among the 25 most recent human prescription labels whose single generic name matches the ChEMBL preferred name (salt words stripped), the one with a systemic route, a boxed warning and the fullest warnings text wins (conservative for a harm screen); topical and ophthalmic labels lose.")
    md.append("- Direction: ChEMBL action type (INHIBITOR, AGONIST, ...) compared with the action the config asks for per mechanism; mismatches are demoted, not deleted. Curated exclusions in the config are shown with their reason.")
    md.append("- Harm flags are regular expressions over boxed warning, warnings, warnings and precautions and pediatric use only. Snippets above are the first match; a flag means the term occurs, not that the risk is quantified.")
    md.append("- Rapalogs are filed under FKBP1A in ChEMBL, not MTOR; metformin under mitochondrial complex I, not AMPK; chloroquine class under TLR7/TLR9. The target mapping in the config carries these.")
    md.append("- Run log at the end of this file.\n")
    md.append("## Run log\n")
    md.append("```")
    md.extend(LOG)
    md.append("```")
    md_path = args.out + ".md"
    with open(md_path, "w") as f:
        f.write("\n".join(md) + "\n")
    log(f"Wrote {csv_path} and {md_path} ({len(rows)} molecules, {len(cand)} approved candidates, {len(demoted)} demoted, {len(haz)} approved hazards) in {elapsed:.0f} s")


if __name__ == "__main__":
    main()
