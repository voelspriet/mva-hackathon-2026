"""Per-megabase heterozygosity, and runs of homozygosity from it.

Input: bcftools query -f '%CHROM\t%POS\t[%GT]\n' over the autosomes.
Writes work/roh_windows.json and prints the runs found.
"""
import sys, json, collections, statistics

W = 1_000_000
het = collections.Counter()
tot = collections.Counter()
for line in sys.stdin:
    p = line.split()
    if len(p) < 3:
        continue
    c, pos, gt = p
    if not c.isdigit():
        continue
    k = (c, int(pos) // W)
    tot[k] += 1
    if gt in ('0/1', '0|1', '1|0', '1/2'):
        het[k] += 1

d = {'%s:%d' % k: [t, het[k], round(het[k] / t, 4)]
     for k, t in tot.items() if t >= 200}
json.dump(d, open('work/roh_windows.json', 'w'))
fr = [v[2] for v in d.values()]
med = statistics.median(fr)
print("windows %d, autosomal variants %d, genome-wide het fraction %.4f, median window %.4f"
      % (len(d), sum(v[0] for v in d.values()),
         sum(v[1] for v in d.values()) / sum(v[0] for v in d.values()), med))

for frac, minlen in ((0.20, 3), (0.50, 4)):
    thr = frac * med
    bychr = collections.defaultdict(list)
    for k, v in d.items():
        if v[2] < thr:
            c, w = k.split(':')
            bychr[c].append(int(w))
    runs = []
    for c, ws in bychr.items():
        ws.sort()
        cur = [ws[0]]
        for w in ws[1:]:
            if w == cur[-1] + 1:
                cur.append(w)
            else:
                if len(cur) >= minlen:
                    runs.append((c, cur[0], cur[-1] + 1, len(cur)))
                cur = [w]
        if len(cur) >= minlen:
            runs.append((c, cur[0], cur[-1] + 1, len(cur)))
    print("threshold %.0f%% of median (%.4f), runs of >=%d Mb: %d"
          % (frac * 100, thr, minlen, len(runs)))
    for r in sorted(runs, key=lambda x: -x[3])[:10]:
        print("   chr%s %d-%d Mb, %d Mb" % r)
