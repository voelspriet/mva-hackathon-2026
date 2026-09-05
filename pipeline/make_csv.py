"""Build the Track 1 CSV from coding candidates in the known MVA genes.

Rule set (automated, no manual curation):
  score each coding/ClinVar-flagged variant: stop/frameshift/splice = 3, missense = 2, other = 1;
  +2 if ClinVar pathogenic or likely pathogenic; +1 if gnomAD exome AC <= 5 and no homozygotes;
  -3 if gnomAD AF > 1e-3.  Take the two top-scoring heterozygous variants in the same gene as the
  compound-het pair (row 1), then each alone, then alternative pairings with the next variants.
  EPCR is a monotone map of the score, capped at 10 rows, chr prefix added.
"""
import sys, csv, re
cands, gnomad = sys.argv[1], sys.argv[2]; out = sys.argv[3]
freq = {}
for l in open(gnomad):
    t, c, p, r, a, ac, an, nh = l.rstrip("\n").split("\t")
    k = (c.replace("chr", ""), p, r, a); ac, an = int(ac.split("=")[1]), int(an.split("=")[1])
    f = freq.setdefault(k, dict(ac=0, an=0, hom=0)); f["ac"] += ac; f["an"] += an; f["hom"] += int(nh.split("=")[1])
rows = []
for l in open(cands):
    c, p, r, a, gt, ad, cln, bcsq = l.rstrip("\n").split("\t")[:8]
    if gt not in ("0/1", "0|1", "1|0"): continue
    s = 3 if re.search(r"stop_gained|frameshift|splice_(acceptor|donor)", bcsq) else 2 if "missense" in bcsq else 1
    if re.search(r"Pathogenic|Likely_pathogenic", cln): s += 2
    f = freq.get((c, p, r, a))
    if f and f["an"]:
        if f["ac"] <= 5 and f["hom"] == 0: s += 1
        if f["ac"] / f["an"] > 1e-3: s -= 3
    gene = re.search(r"\|(\w+)\|ENST", bcsq); gene = gene.group(1) if gene else "?"
    rows.append(dict(c="chr" + c, p=p, r=r, a=a, s=s, gene=gene, cln=cln, bcsq=bcsq.split(",")[0], f=f))
rows.sort(key=lambda x: -x["s"])
def note(x): return f"{x['gene']} {x['bcsq'].split('|')[0]} {x['bcsq'].split('|')[5] if x['bcsq'].count('|')>5 else ''}; ClinVar {x['cln']}; gnomAD AC={x['f']['ac'] if x['f'] else 'NA'}".replace("  ", " ")
sub = []
def add(v1, v2, epcr, ft, n):
    if len(sub) >= 10: return
    sub.append(dict(proband_id="PROBAND01", chrom_1=v1["c"], pos_1=v1["p"], ref_1=v1["r"], alt_1=v1["a"],
        chrom_2=v2["c"] if v2 else "", pos_2=v2["p"] if v2 else "", ref_2=v2["r"] if v2 else "", alt_2=v2["a"] if v2 else "",
        epcr=f"{epcr:.2f}", finding_type=ft, notes=n))
if len(rows) >= 2:
    a, b = rows[0], rows[1]
    add(a, b, 0.95, "primary", f"compound heterozygous pair; phase not determinable from single-sample VCF. {note(a)} + {note(b)}")
    add(a, None, 0.60, "primary", note(a)); add(b, None, 0.50, "primary", note(b))
    for i, x in enumerate(rows[2:]): add(a, x, max(0.05, 0.20 - 0.03 * i), "primary", f"alternative pairing: {note(a)} + {note(x)}")
elif rows: add(rows[0], None, 0.9, "primary", note(rows[0]))
with open(out, "w", newline="") as o:
    w = csv.DictWriter(o, fieldnames=["proband_id","chrom_1","pos_1","ref_1","alt_1","chrom_2","pos_2","ref_2","alt_2","epcr","finding_type","notes"])
    w.writeheader(); w.writerows(sub)
print(f"wrote {out}: {len(sub)} rows", file=sys.stderr)
