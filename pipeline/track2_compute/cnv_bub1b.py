#!/usr/bin/env python3
"""Depth- and heterozygosity-based screen for a gross deletion/duplication over BUB1B.
Input on stdin: CHROM POS GT AD DP for PASS SNPs on chr15. Aggregates into bins; prints table.
Patient data stays local (stdin from local VCF only)."""
import sys, statistics as st
BINSIZE = 50000
LO, HI = 39_000_000, 41_500_000
bins = {}
chrom_dp = []
for line in sys.stdin:
    f = line.rstrip("\n").split("\t")
    if len(f) < 5: continue
    pos, gt, ad, dp = int(f[1]), f[2], f[3], f[4]
    try: dp = int(dp)
    except ValueError: continue
    chrom_dp.append(dp)
    if not (LO <= pos < HI): continue
    b = pos // BINSIZE * BINSIZE
    d = bins.setdefault(b, {"dp": [], "het": 0, "n": 0, "vaf": []})
    d["dp"].append(dp); d["n"] += 1
    if gt in ("0/1", "0|1", "1|0"):
        d["het"] += 1
        try:
            r, a = (int(x) for x in ad.split(",")[:2])
            if r + a: d["vaf"].append(a / (r + a))
        except ValueError: pass
med = st.median(chrom_dp)
print(f"# chr15 PASS-SNP median DP = {med}  (n={len(chrom_dp)})")
print("bin_start\tn\tmeanDP\tratio_to_chr15\thet\thet_frac\tmedian_het_vaf\tnote")
for b in sorted(bins):
    d = bins[b]
    mdp = st.mean(d["dp"])
    note = "BUB1B" if 40160984 - BINSIZE < b < 40221137 else ""
    v = f"{st.median(d['vaf']):.2f}" if d["vaf"] else "NA"
    print(f"{b}\t{d['n']}\t{mdp:.1f}\t{mdp/med:.2f}\t{d['het']}\t{d['het']/d['n']:.2f}\t{v}\t{note}")
