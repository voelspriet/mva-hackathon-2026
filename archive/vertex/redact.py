"""De-identify the corpus for third-party processing.

Replaces patient-derived specifics with stable tokens so the reasoning stays
readable while the DTA-governed content stays local. Every substitution is
listed in archive/vertex/REDACTION_MAP.md so the mapping is auditable and reversible
locally, and is not sent.
"""
import re, os, glob, json, hashlib

SUBS = [
    # sample and proband identifiers
    (r"WGS_EX2312012(_HGWCNDSX7)?(_S16)?(_L00[1-4])?(_R[12])?(_001)?", "SAMPLE_ID"),
    (r"\bPROBAND01\b", "PROBAND_ID"),
    # variant coordinates and nomenclature, allele 1
    (r"(chr)?1?5?:?\s*40[,_]?209[,_]?701", "POS_A"),
    (r"NC_000015\.\d+:g\.POS_A", "chrN:g.POS_A"),
    (r"c\.2210T>G", "c.ALLELE_A"),
    (r"c\.2210(?![0-9])", "c.POS_A"),
    (r"p\.\(?Leu737Ter\)?", "p.ALLELE_A"),
    (r"p\.Leu737\*", "p.ALLELE_A"),
    (r"Leu ?737[A-Za-z]*", "RESIDUE_A"),
    (r"\bL737[A-Z]?\b", "RESIDUE_A"),
    (r"\b737\b(?= *[A-Za-z]*(Ter|\*))", "RESNUM_A"),
    (r"\brs759242053\b", "RSID_A"),
    # allele 2
    (r"(chr)?1?5?:?\s*40[,_]?220[,_]?612", "POS_B"),
    (r"c\.3006T>G", "c.ALLELE_B"),
    (r"c\.3006(?![0-9])", "c.POS_B"),
    (r"p\.\(?Asn1002Lys\)?", "p.ALLELE_B"),
    (r"Asn ?1002[A-Za-z]*", "RESIDUE_B"),
    (r"\bN1002[A-Z]?\b", "RESIDUE_B"),
    # clinical phenotype of this child
    (r"\bHP:\d{7}\b", "HPO_TERM"),
    (r"rhabdomyosarcomas?", "the index malignancy"),
    (r"nephrocalcinosis", "the index renal finding"),
    (r"\b32 weeks\b", "PRETERM_GA"),
    (r"\bfailure to thrive\b", "the index growth finding"),
]

def redact(t):
    for pat, rep in SUBS:
        t = re.sub(pat, rep, t, flags=re.I)
    return t

FILES = ["REPORT_track2.md","REPORT_track1.md"] \
    + sorted(glob.glob("track2/research/*.md")) + sorted(glob.glob("archive/creative/*.md")) \
    + sorted(glob.glob("archive/panel/*.md")) + sorted(glob.glob("archive/panel2/*.md")) \
    + sorted(glob.glob("archive/verify/*.md")) + sorted(glob.glob("archive/referees/*.md")) \
    + sorted(glob.glob("track2/gate/*.md"))

os.makedirs("archive/vertex/bundle", exist_ok=True)
report = []
for f in FILES:
    if not os.path.exists(f): continue
    raw = open(f).read()
    out = redact(raw)
    n = sum(1 for a,b in zip(raw.split("\n"), out.split("\n")) if a!=b)
    dst = "archive/vertex/bundle/" + f.replace("/", "__")
    open(dst,"w").write(f"<<<FILE: {f}>>>\n\n{out}\n")
    report.append((f, len(raw), len(out), n))
print(f"{len(report)} files redacted -> archive/vertex/bundle/")
print(f"total chars: {sum(r[2] for r in report):,}  (~{sum(r[2] for r in report)//4:,} tokens)")
json.dump(report, open("archive/vertex/redaction_report.json","w"), indent=1)
