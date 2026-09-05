"""Mosaic aneuploidy profile from a single-sample germline VCF.

Reads PASS biallelic SNVs (GT, AD, DP) and, per chromosome and per 10 Mb bin,
estimates the B-allele-frequency shift of heterozygous sites and the depth ratio
against the autosomal median. For a trisomy present in a fraction f of cells,
heterozygous sites split to AB = 1/(2+f) and (1+f)/(2+f) and depth rises by
(2+f)/2. Both estimates are reported independently.

Usage: bcftools query -i 'FILTER="PASS" && TYPE="snp"' -f '%CHROM\t%POS\t[%GT\t%AD\t%DP]\n' in.vcf.gz | python3 mosaic_baf.py out_prefix
"""
import sys, math, collections, json
MIN_DP, MAX_DP, BIN = 20, 120, 10_000_000
out = sys.argv[1]
het = collections.defaultdict(list)           # chrom -> list of AB
hetbin = collections.defaultdict(list)        # (chrom,bin) -> AB
dp_all = collections.defaultdict(list)        # chrom -> DP (het+hom)
dpbin = collections.defaultdict(list)
n_hom = collections.Counter(); n_het = collections.Counter()
for line in sys.stdin:
    c, p, gt, ad, dp = line.rstrip("\n").split("\t")
    if c not in [str(i) for i in range(1, 23)] + ["X", "Y"]: continue
    try: dp = int(dp)
    except ValueError: continue
    if dp < MIN_DP or dp > MAX_DP: continue
    b = int(p) // BIN
    dp_all[c].append(dp); dpbin[(c, b)].append(dp)
    if gt in ("0/1", "0|1", "1|0"):
        r, a = ad.split(",")[:2]; r, a = int(r), int(a)
        if r + a == 0: continue
        ab = a / (r + a)
        het[c].append(ab); hetbin[(c, b)].append(ab); n_het[c] += 1
    elif gt in ("1/1", "1|1"):
        n_hom[c] += 1
def med(x): x = sorted(x); return x[len(x)//2] if x else float("nan")
autos = [str(i) for i in range(1, 23)]
gdp = med([d for c in autos for d in dp_all[c]])
# baseline binomial spread from all autosomal hets
allab = [ab for c in autos for ab in het[c]]
base_var = sum((x-0.5)**2 for x in allab)/len(allab)
res = {}
print(f"autosomal median depth {gdp}, het sites used {len(allab)}, baseline sqrt(var) {math.sqrt(base_var):.4f}")
print(f"{'chr':4s} {'hets':>7s} {'homs':>7s} {'het/hom':>7s} {'depth':>6s} {'ratio':>6s} {'f_depth':>8s} {'|AB-.5| mean':>12s} {'excess d':>9s} {'f_BAF':>7s}")
for c in autos + ["X", "Y"]:
    abs_ = het[c]
    if not dp_all[c]: continue
    d = med(dp_all[c]); ratio = d / gdp
    f_dp = 2 * (ratio - 1)
    if abs_:
        var = sum((x-0.5)**2 for x in abs_)/len(abs_)
        excess = math.sqrt(max(0.0, var - base_var))
        f_baf = 4*excess/(1-2*excess) if excess < 0.5 else float("nan")
        mad = sum(abs(x-0.5) for x in abs_)/len(abs_)
    else:
        excess = f_baf = mad = float("nan")
    hh = n_het[c]/max(1, n_hom[c])
    res[c] = dict(hets=n_het[c], homs=n_hom[c], depth=d, ratio=round(ratio,3), f_depth=round(f_dp,3), mad=round(mad,4) if mad==mad else None, excess=round(excess,4) if excess==excess else None, f_baf=round(f_baf,3) if f_baf==f_baf else None)
    print(f"{c:4s} {n_het[c]:7d} {n_hom[c]:7d} {hh:7.2f} {d:6.0f} {ratio:6.3f} {f_dp:8.3f} {mad:12.4f} {excess:9.4f} {f_baf:7.3f}")
# bins: flag any 10 Mb bin with excess > 0.03 or depth ratio outside 0.9-1.1
flags = []
for (c, b), abs_ in hetbin.items():
    if len(abs_) < 300: continue
    var = sum((x-0.5)**2 for x in abs_)/len(abs_)
    excess = math.sqrt(max(0.0, var - base_var))
    ratio = med(dpbin[(c, b)])/gdp
    if excess > 0.03 or not (0.9 <= ratio <= 1.1):
        flags.append((c, b*BIN//1_000_000, (b+1)*BIN//1_000_000, len(abs_), round(excess,3), round(ratio,3)))
flags.sort(key=lambda x: -x[4])
print("\nbins flagged (chr, Mb start, Mb end, hets, excess d, depth ratio):")
for f in flags[:30]: print("  ", f)
if not flags: print("   none")
json.dump(dict(genome_depth=gdp, baseline_sd=base_var**0.5, per_chrom=res, flagged_bins=flags), open(out + ".json", "w"), indent=1)
# histograms per chromosome for the plot
hist = {c: [0]*49 for c in het}
for c, abs_ in het.items():
    for x in abs_: hist[c][min(48, int(x*49))] += 1
json.dump(hist, open(out + ".hist.json", "w"))
