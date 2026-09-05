"""stdin: GENE<TAB>GT<TAB>variant. Lists genes with >=2 het or >=1 hom variant (recessive-compatible)."""
import sys, collections
het, hom = collections.defaultdict(list), collections.defaultdict(list)
for l in sys.stdin:
    g, gt, v = l.rstrip("\n").split("\t")
    if g == ".": continue
    for gg in set(g.split(",")):
        if gt in ("0/1", "0|1", "1|0"): het[gg].append(v)
        elif gt in ("1/1", "1|1"): hom[gg].append(v)
rows = sorted([(g, len(het[g]), len(hom[g])) for g in set(het) | set(hom) if len(het[g]) >= 2 or hom[g]],
              key=lambda r: (-r[1], -r[2], r[0]))
for g, h, o in rows: print(f"{g}\t{h}\t{o}\t{','.join(het[g] + hom[g])}")
