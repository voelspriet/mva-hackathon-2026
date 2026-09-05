#!/usr/bin/env python3
"""Rank AlphaMissense for BUB1B: the case allele N1002K against MVA alleles with published
functional data (Suijkerbuijk 2010) and against the whole-gene / kinase-domain distributions."""
import sys, re, statistics as st
rows = []
for line in open(sys.argv[1]):
    f = line.rstrip("\n").split("\t")
    if len(f) < 10: continue
    sub, score, cls = f[7], float(f[8]), f[9]
    m = re.match(r"([A-Z])(\d+)([A-Z])", sub)
    if not m: continue
    rows.append((int(m.group(2)), sub, score, cls))
scores = sorted(r[2] for r in rows)
dom = [r for r in rows if 766 <= r[0] <= 1050]
def pct(v, arr): return 100 * sum(1 for x in arr if x < v) / len(arr)
known = {"Y155C": "TPR; protein level normal (Suijkerbuijk 2010)",
         "R550Q": "outside domain; protein level normal",
         "R727C": "near domain; 2-fold faster turnover",
         "R814H": "kinase domain; MVA allele",
         "L844F": "kinase domain; 5-10x reduced level",
         "I909T": "kinase domain; low level, rescued by overexpression",
         "Q921H": "kinase domain; behaves as wild type",
         "L1012P": "kinase domain; low level, rescued by overexpression",
         "N1002K": "THIS CASE, no functional data"}
byname = {}
for pos, sub, sc, cl in rows:
    if sub in known: byname[sub] = (sc, cl, pos)
print("variant\tscore\tclass\tgene_pct\tdomain_pct\tpublished_functional_note")
for k in ["N1002K", "L1012P", "I909T", "L844F", "R814H", "Q921H", "R727C", "Y155C", "R550Q"]:
    if k not in byname: print(f"{k}\tNOT_IN_FILE"); continue
    sc, cl, pos = byname[k]
    dp = pct(sc, [r[2] for r in dom]) if 766 <= pos <= 1050 else float("nan")
    print(f"{k}\t{sc:.4f}\t{cl}\t{pct(sc,scores):.1f}\t{dp:.1f}\t{known[k]}")
n = len(rows)
print(f"\n# BUB1B missense SNVs scored: {n}; median {st.median(scores):.3f}")
for lab, arr in [("whole gene", rows), ("kinase domain 766-1050", dom)]:
    cls = [r[3] for r in arr]
    tot = len(arr)
    frac = {c: round(100 * cls.count(c) / tot, 1) for c in set(cls)}
    print(f"# {lab}: n={tot} median={st.median([r[2] for r in arr]):.3f} class%={frac}")
# neighbourhood of 1002
loc = [r for r in rows if 995 <= r[0] <= 1010]
print(f"# residues 995-1010 mean score {st.mean([r[2] for r in loc]):.3f} (n={len(loc)})")
alt1002 = sorted([r for r in rows if r[0] == 1002], key=lambda r: -r[2])
print("# all substitutions at 1002: " + ", ".join(f"{r[1]}={r[2]:.2f}" for r in alt1002))
