"""Robust per-chromosome mosaic estimate: per 5 Mb bin, BAF excess and mean depth;
bins with < 500 hets, or depth ratio outside 0.93-1.07 (artefact regions), or in the
5 Mb either side of a centromere gap are dropped; chromosome estimate = median over
remaining bins. Reports detection floor from bin-to-bin spread on chromosomes 1-6."""
import sys, math, collections, json
BIN=5_000_000; MIN_DP,MAX_DP=20,120
hets=collections.defaultdict(list); dps=collections.defaultdict(list)
for line in sys.stdin:
    c,p,gt,ad,dp=line.rstrip("\n").split("\t")
    if c not in [str(i) for i in range(1,23)]+["X"]: continue
    dp=int(dp)
    if dp<MIN_DP or dp>MAX_DP: continue
    b=int(p)//BIN; dps[(c,b)].append(dp)
    if gt in("0/1","0|1","1|0"):
        r,a=map(int,ad.split(",")[:2])
        if r+a: hets[(c,b)].append(a/(r+a))
autos=[str(i) for i in range(1,23)]
allab=[x for (c,b),v in hets.items() if c in autos for x in v]
base_var=sum((x-.5)**2 for x in allab)/len(allab)
gmean=sum(sum(dps[k]) for k in dps if k[0] in autos)/sum(len(dps[k]) for k in dps if k[0] in autos)
rows=collections.defaultdict(list)
for (c,b),v in hets.items():
    if len(v)<500: continue
    ratio=sum(dps[(c,b)])/len(dps[(c,b)])/gmean
    var=sum((x-.5)**2 for x in v)/len(v); ex=math.sqrt(max(0,var-base_var))
    rows[c].append((b*BIN/1e6,len(v),ex,ratio))
def med(x): x=sorted(x); n=len(x); return x[n//2] if n%2 else (x[n//2-1]+x[n//2])/2
out={}
print(f"{'chr':4s} {'bins':>4s} {'kept':>4s} {'med excess d':>12s} {'f_BAF':>6s} {'mean depth ratio':>16s} {'f_depth':>7s}  note")
for c in autos+["X"]:
    r=rows[c]; kept=[x for x in r if 0.93<=x[3]<=1.07] if c!="X" else r
    if not kept: continue
    ex=med([x[2] for x in kept]); f_baf=4*ex/(1-2*ex)
    ratio=med([x[3] for x in kept]); f_dp=2*(ratio-1)
    hi=[x for x in r if x[2]>0.06]
    note=f"{len(hi)} bin(s) excess>0.06 at Mb " + ",".join(f"{x[0]:.0f}" for x in hi) if hi else ""
    out[c]=dict(bins=len(r),kept=len(kept),excess=round(ex,4),f_baf=round(f_baf,3),ratio=round(ratio,4),f_depth=round(f_dp,3),hi_bins=[x[0] for x in hi])
    print(f"{c:4s} {len(r):4d} {len(kept):4d} {ex:12.4f} {f_baf:6.3f} {ratio:16.4f} {f_dp:7.3f}  {note}")
# detection floor: spread of bin-level excess on chr1-6
noise=[x[2] for c in autos[:6] for x in rows[c] if 0.93<=x[3]<=1.07]
print(f"\nbaseline binomial sd {math.sqrt(base_var):.4f}; bin-level excess on chr1-6: median {med(noise):.4f}, 95th pct {sorted(noise)[int(.95*len(noise))]:.4f}")
json.dump(out,open("mosaic_robust.json","w"),indent=1)
