"""Track 2 quantitative appendix. All numbers in track2/creative/F_math.md come from here.
Run: python3 f_math.py"""
import math, json, os
from math import log, exp, sqrt

def z(p):  # inverse normal CDF, Acklam
    a=[-3.969683028665376e+01,2.209460984245205e+02,-2.759285104469687e+02,1.383577518672690e+02,-3.066479806614716e+01,2.506628277459239e+00]
    b=[-5.447609879822406e+01,1.615858368580409e+02,-1.556989798598866e+02,6.680131188771972e+01,-1.328068155288572e+01]
    c=[-7.784894002430293e-03,-3.223964580411365e-01,-2.400758277161838e+00,-2.549732539343734e+00,4.374664141464968e+00,2.938163982698783e+00]
    d=[7.784695709041462e-03,3.224671290700398e-01,2.445134137142996e+00,3.754408661907416e+00]
    pl=0.02425
    if p<pl:
        q=sqrt(-2*log(p)); return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5])/((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p<=1-pl:
        q=p-0.5; r=q*q
        return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q/(((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)
    q=sqrt(-2*log(1-p)); return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5])/((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)

print("="*70); print("PROBLEM 1  phase: trans vs cis")
p1,p2=7.87e-5,6.84e-7
print(f"p1={p1:.3g} p2={p2:.3g}  2*p1*p2 (trans genotype prior) = {2*p1*p2:.3e}")
print(f"q under linkage equilibrium = {p1*p2:.3e}; hard ceiling q<=p2 = {p2:.3g}; ceiling R = 1/p1 = {1/p1:,.0f}")
for beta in (1e-3,1e-4,1e-5):
    print(f"\n beta (phenotype from another cause) = {beta:g}")
    print("   R\\alpha " + "".join(f"{a:>12}" for a in (0.3,0.6,0.9)))
    for R in (1,10,100,1000,1/p1):
        row=""
        for al in (0.3,0.6,0.9):
            odds=(1.0/R)*(al/beta); row+=f"{odds/(1+odds):12.4f}"
        print(f"  {R:8,.0f} "+row)
print("\n miscarriage LR=3 applied to R=100,alpha=0.6,beta=1e-4:")
o=(1/100)*(0.6/1e-4)*3; print(f"   posterior P(trans)={o/(1+o):.4f}")

print("="*70); print("PROBLEM 2  mosaicism detection limit")
sd0=0.09455918452092225; v0=sd0**2; DP=44
print(f"empirical baseline sd of (AB-0.5) = {sd0:.5f}, var {v0:.6f}")
print(f"pure binomial at DP={DP}: var {0.25/DP:.6f}, sd {sqrt(0.25/DP):.5f}; overdispersion factor {v0/(0.25/DP):.3f}")
def f_from_delta(d): return 4*d/(1-2*d)
def delta_min(N,zz,k=1,median=False):
    se=v0*sqrt(2.0/N)
    if median: se*= (sqrt(math.pi/2)/sqrt(k))
    elif k>1: se/=sqrt(k)
    return sd0*sqrt(zz*se/v0)
N=3900; nbins_auto=563
print(f"\n N het sites per 5 Mb bin (median over chromosomes) = {N}")
rows=[("single bin, one-sided 95%",delta_min(N,1.645)),
      ("single bin, Bonferroni over 563 bins",delta_min(N,z(1-0.05/nbins_auto))),
      ("chr1 median of 45 bins, 95%",delta_min(N,1.645,45,True)),
      ("chr1 median of 45 bins, Bonf over 23 chr",delta_min(N,z(1-0.05/23),45,True)),
      ("chr21 median of 7 bins, 95%",delta_min(N,1.645,7,True)),
      ("chr21 median of 7 bins, Bonf over 23 chr",delta_min(N,z(1-0.05/23),7,True))]
for lab,d in rows: print(f"   {lab:42s} delta={d:.5f}  f={f_from_delta(d)*100:5.2f}%")
print("\n depth channel: observed autosomal f_depth range")
_here = os.path.dirname(os.path.abspath(__file__))
_mosaic = os.environ.get("MOSAIC_JSON") or os.path.join(_here, "..", "..", "work", "mosaic_robust.json")
if not os.path.exists(_mosaic):
    print("   [skipped: %s not found. This file is derived from the patient VCF and is"
          " not committed. Set MOSAIC_JSON to point at it, or run pipeline/run.sh first.]"
          % _mosaic)
    r = None
else:
    r=json.load(open(_mosaic))
fd=[r[str(i)]['f_depth'] for i in range(1,23)] if r else []
if fd:
    m=sum(fd)/len(fd); s=sqrt(sum((x-m)**2 for x in fd)/(len(fd)-1))
    print(f"   min {min(fd):+.3f} max {max(fd):+.3f} mean {m:+.4f} sd {s:.4f} -> 95% floor 1.645*sd*2sided ~ {1.96*s:.3f} = {1.96*s*100:.1f}% trisomy-equivalent")
print("\n variegated burden: total aneuploid fraction F needed for one chromosome to clear the floor")
for fl,lab in ((0.1166,"per-bin, Bonferroni"),(0.042,"per-chromosome, Bonferroni")):
    for k in (1,5,22):
        print(f"   floor {fl*100:4.1f}% ({lab:22s}) spread over {k:2d} chromosomes -> F >= {fl*k*100:5.1f}%")

print("="*70); print("PROBLEM 3  N-of-1 power")
def detectable(cv_bio,lam,nBN,nper=3,periods=('B','T','W')):
    cv_sc=1/sqrt(lam*nBN/1000.0)
    cv=sqrt(cv_bio**2+cv_sc**2)
    sd=sqrt(log(1+cv**2))                 # log-scale sd
    se=sd*sqrt(1.0/nper+1.0/(2*nper))     # T vs mean(B,W)
    df=3*nper-3
    t1=z(0.975)+ (0.0 if df>30 else 0.0)  # placeholder, use t below
    return cv_sc,cv,sd,se,df
def tcrit(df,p):
    # Cornish-Fisher expansion of t from z
    x=z(p); return x+(x**3+x)/(4*df)+(5*x**5+16*x**3+3*x)/(96*df**2)
def mde(cv_bio,lam,nBN,nper):
    cv_sc,cv,sd,se,df=detectable(cv_bio,lam,nBN,nper)
    k=tcrit(df,0.975)+tcrit(df,0.80)
    d=k*se
    return cv_sc,cv,se,df,1-exp(-d)
print("(a) CBMN micronuclei, log scale, contrast T vs mean(B,W), 80% power, two-sided 0.05")
print(f"{'lam/1000BN':>10}{'BN scored':>10}{'CVbio':>7}{'CVscore':>8}{'CVtot':>7}{'n/period':>9}{'df':>4}{'MDE %red':>10}")
for lam in (4,40):
    for nBN in (1000,2000,4000):
        for cvb in (0.20,0.30):
            for npr in (3,5):
                cs,cv,se,df,m=mde(cvb,lam,nBN,npr)
                print(f"{lam:10d}{nBN:10d}{cvb:7.2f}{cs:8.3f}{cv:7.3f}{npr:9d}{df:4d}{m*100:9.1f}%")
print("\n MN-reticulocyte flow variant: 1e6 cells scored, baseline 0.2% MN-Ret")
lam=2000.0  # per 1e6 -> per 1000 equivalent handled directly
for nRET in (1e5,1e6):
    cnt=0.002*nRET; cs=1/sqrt(cnt)
    for cvb in (0.20,0.30):
        cv=sqrt(cvb**2+cs**2); sd=sqrt(log(1+cv**2)); se=sd*sqrt(1/3+1/6); k=tcrit(6,0.975)+tcrit(6,0.80)
        print(f"   {nRET:.0e} rets, count {cnt:.0f}, CVscore {cs:.3f}, CVbio {cvb:.2f} -> MDE {(1-exp(-k*se))*100:.1f}% reduction")
print("\n(b) interphase FISH aneuploid fraction")
print(f"{'p0':>6}{'nuclei':>8}{'CVbinom':>9}{'CVtech':>8}{'CVtot':>7}{'n/period':>9}{'MDE %red':>10}")
for p0 in (0.05,0.10,0.20):
    for n in (500,1000,2000):
        cb=sqrt(p0*(1-p0)/n)/p0
        for ct in (0.05,0.10):
            for npr in (3,5):
                cv=sqrt(cb**2+ct**2); sd=sqrt(log(1+cv**2)); se=sd*sqrt(1/npr+1/(2*npr))
                df=3*npr-3; k=tcrit(df,0.975)+tcrit(df,0.80)
                print(f"{p0:6.2f}{n:8d}{cb:9.3f}{ct:8.2f}{cv:7.3f}{npr:9d}{(1-exp(-k*se))*100:9.1f}%")

print("="*70); print("PROBLEM 4  decision thresholds")
print(" r_min = h * w / R0 ; w = utility of the added harm / utility of a cancer event")
for w,lab in ((1.0,"event-count neutral (w=1)"),(0.2,"utility weighted, growth deficit w=0.2")):
    print(f"\n {lab}")
    print(f"{'added risk h':>14}"+"".join(f"{f'R0={x:.2f}':>12}" for x in (0.39,0.57,0.75)))
    for h in (0.01,0.02,0.05,0.10,0.20):
        print(f"{h*100:13.0f}%"+"".join(f"{min(1,h*w/R0)*100:11.1f}%" for R0 in (0.39,0.57,0.75)))
print("\n residual-risk correction: child already past the Wilms window (tumours 2-16 months, Kajii 2001)")
for res in (0.30,0.20,0.10):
    print(f"   residual share of lifetime risk {res*100:.0f}%  ->  every threshold multiplied by {1/res:.1f}x")
    for h in (0.02,0.05,0.10):
        for R0 in (0.39,0.75):
            print(f"      h={h*100:.0f}% R0={R0:.2f} -> r_min {min(1,h/(R0*res))*100:.0f}%")

print("="*70); print("PROBLEM 5  parental controls and MVA Society sample size")
lo,hi=3.5,41.7
sdlog=log(hi/lo)/4.0
print(f" carrier PCS 3.5-41.7% (Kajii 2001). If that range = +/-2 SD on the log scale:")
print(f"   sd_log = {sdlog:.3f}, between-carrier CV = {sqrt(exp(sdlog**2)-1)*100:.0f}%, geometric mean {sqrt(lo*hi):.1f}%")
print(" batch-control condition: differencing helps iff sigma_batch^2 > sigma_parent_resid^2 / m (m parents averaged)")
for m in (1,2):
    print(f"   m={m}: need sigma_batch > {1/sqrt(m):.2f} x sigma_parent")
def nsize(cv,d,cross):
    # sd is the occasion-to-occasion within-subject sd; averaging 3 replicates inside a
    # period shrinks only the scoring term, not the biological term, so it is NOT divided by nper
    sd=sqrt(log(1+cv**2)); D=-log(1-d); k=(z(0.975)+z(0.80))**2
    if cross: return 2*k*sd**2/D**2              # total subjects, AB/BA crossover
    return 2*k*sd**2/D**2                        # per arm, parallel (uses between-subject cv)
print(f"\n{'effect':>8}{'parallel n/arm':>16}{'parallel total':>16}{'crossover total':>17}")
for d in (0.20,0.25,0.30,0.40,0.50):
    pa=nsize(0.50,d,False); cr=max(8,nsize(0.229,d,True))
    print(f"{d*100:7.0f}%{math.ceil(pa):16d}{math.ceil(pa)*2:16d}{math.ceil(cr):17d}")
print("\n enrollable ceiling: 31 MVA1 cases published (Pavone 2022), ~40 MVA total (Scott 2006);")
print(" assume 50% alive/eligible/consenting -> 15-20 subjects.")
