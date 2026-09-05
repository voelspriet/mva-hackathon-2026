#!/usr/bin/env python3
"""Depth/heterozygosity dosage screen over the 1q21.1 TAR-critical region (GRCh38 chr1:145.3-146.0 Mb),
because the RBM8A c.-21G>A hypomorph is only phenotypically relevant in trans with a deletion there.
Input on stdin: CHROM POS GT DP for PASS SNPs on chr1."""
import sys, statistics as st
BIN = 100_000
LO, HI = 144_000_000, 147_500_000
bins, allp = {}, []
for line in sys.stdin:
    f = line.rstrip().split("\t")
    if len(f) < 4: continue
    pos, gt = int(f[1]), f[2]
    try: dp = int(f[3])
    except ValueError: continue
    allp.append(dp)
    if not LO <= pos < HI: continue
    d = bins.setdefault(pos // BIN * BIN, {"dp": [], "het": 0, "n": 0})
    d["dp"].append(dp); d["n"] += 1
    if gt in ("0/1", "0|1", "1|0"): d["het"] += 1
med = st.median(allp)
print(f"# chr1 PASS-SNP median DP {med} (n={len(allp)})")
print("bin\tn\tmeanDP\tratio\thet\thet_frac\tnote")
for b in sorted(bins):
    d = bins[b]; m = st.mean(d["dp"])
    note = "TAR/RBM8A" if 145_300_000 <= b <= 146_000_000 else ""
    print(f"{b}\t{d['n']}\t{m:.1f}\t{m/med:.2f}\t{d['het']}\t{d['het']/d['n']:.2f}\t{note}")
