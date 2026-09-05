"""Figure: depth ratio, BAF excess, BAF histograms per chromosome. Inputs: mosaic_robust.json, mosaic.hist.json."""
import json, sys, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
r=json.load(open(sys.argv[1])); h=json.load(open(sys.argv[2])); out=sys.argv[3]
chroms=[str(i) for i in range(1,23)]; x=list(range(len(chroms)))
fig,ax=plt.subplots(3,1,figsize=(11,9),gridspec_kw=dict(height_ratios=[1,1,1.6]))
ax[0].bar(x,[r[c]["ratio"] for c in chroms],color="#4a6fa5"); ax[0].axhline(1,color="k",lw=.8)
ax[0].axhspan(0.95,1.05,color="grey",alpha=.15); ax[0].set_ylim(0.9,1.1); ax[0].set_ylabel("depth ratio\n(vs autosomal mean)")
ax[0].set_xticks(x); ax[0].set_xticklabels(chroms)
ax[0].set_title("Proband WGS, 44x: per-chromosome copy number and allele balance (artefact bins excluded)")
ax[1].bar(x,[r[c]["excess"] for c in chroms],color="#b8431f"); ax[1].set_ylim(0,0.1)
ax[1].axhline(0.024,color="k",ls="--",lw=.8); ax[1].text(21.6,0.027,"expected for trisomy in 10% of cells",ha="right",fontsize=8)
ax[1].set_ylabel("BAF excess d\n(median over 5 Mb bins)"); ax[1].set_xticks(x); ax[1].set_xticklabels(chroms)
n=len(next(iter(h.values()))); bins=[(i+0.5)/n for i in range(n)]
for c in chroms:
    v=h[c]; s=sum(v); ax[2].plot(bins,[y/s for y in v],lw=.8,alpha=.7)
ax[2].set_xlabel("alternate-allele fraction at heterozygous SNVs, all autosomes overlaid (low-fraction shoulder = segmental-duplication artefact)")
ax[2].set_ylabel("fraction of sites"); ax[2].axvline(0.5,color="k",lw=.6)
top=ax[2].get_ylim()[1]
for f,lab,yy in [(0.2,"trisomy, 20% of cells",0.92),(0.5,"trisomy, 50% of cells",0.80)]:
    for xx in (1/(2+f),(1+f)/(2+f)): ax[2].axvline(xx,color="grey",ls=":",lw=.8)
    ax[2].text((1+f)/(2+f)+0.006,top*yy,lab,fontsize=7,color="grey")
plt.tight_layout(); plt.savefig(out,dpi=140); print("saved",out)
