"""Per 5 Mb bin BAF excess, printing every bin above the segmental threshold.

mosaic_robust.py reports the chromosome median and records outlier bins in
hi_bins without following them up. This prints them with the depth ratio, so a
reader can tell a candidate segmental event from a mappability artefact.
Input: bcftools query -f '%CHROM\t%POS\t[%GT\t%AD\t%DP]\n'
"""
import sys, math, collections

BIN = 5_000_000
MIN_DP, MAX_DP = 20, 120
hets = collections.defaultdict(list)
dps = collections.defaultdict(list)
autos = [str(i) for i in range(1, 23)]

for line in sys.stdin:
    p = line.rstrip("\n").split("\t")
    if len(p) < 5:
        continue
    c, pos, gt, ad, dp = p
    if c not in autos + ["X"]:
        continue
    try:
        dp = int(dp)
    except ValueError:
        continue
    if dp < MIN_DP or dp > MAX_DP:
        continue
    b = int(pos) // BIN
    dps[(c, b)].append(dp)
    if gt in ("0/1", "0|1", "1|0"):
        try:
            r, a = map(int, ad.split(",")[:2])
        except ValueError:
            continue
        if r + a:
            hets[(c, b)].append(a / (r + a))

allab = [x for (c, b), v in hets.items() if c in autos for x in v]
base = sum((x - .5) ** 2 for x in allab) / len(allab)
g = (sum(sum(dps[k]) for k in dps if k[0] in autos) /
     sum(len(dps[k]) for k in dps if k[0] in autos))
print("baseline variance %.6f, genome mean depth %.2f" % (base, g))
print("chr\tMb\tnhet\texcess\tdepth_ratio\tf_baf\tpasses_depth_filter")
hi = []
for (c, b), v in sorted(hets.items(), key=lambda x: (x[0][0], x[0][1])):
    if len(v) < 500:
        continue
    ratio = sum(dps[(c, b)]) / len(dps[(c, b)]) / g
    var = sum((x - .5) ** 2 for x in v) / len(v)
    ex = math.sqrt(max(0, var - base))
    if ex > 0.06:
        f = 4 * ex / (1 - 2 * ex)
        keep = 0.93 <= ratio <= 1.07
        hi.append(keep)
        print("%s\t%d\t%d\t%.4f\t%.4f\t%.3f\t%s" % (c, b * 5, len(v), ex, ratio, f, keep))
print("\nbins above excess 0.06: %d, of which pass the depth filter: %d"
      % (len(hi), sum(hi)))
