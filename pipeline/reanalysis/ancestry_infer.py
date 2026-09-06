"""Infer continental ancestry from the proband's own genotypes, to test whether
this project's frequency arguments used the right denominator.

Why it matters. Every rarity claim in this project is stated against gnomAD's
global allele frequency. Global frequency is the wrong denominator if the child
is not drawn from the population that dominates gnomAD, and the claim that
carries the most weight, that BUB1B allele 2 is vanishingly rare, is a frequency
claim. This measures which denominator applies.

Design, and the two things it is careful about.

1. The marker panel is chosen from gnomAD alone, never from the child. Within
   each window the SNV with the largest variance in allele frequency across
   populations is taken. Choosing on cross-population spread is what makes a
   marker informative; choosing on the child's genotype would make the answer
   circular.
2. Markers are at least one megabase apart, so linkage disequilibrium does not
   inflate confidence. One marker per window, windows spread across all 22
   autosomes in proportion to their length.

A no-call at a panel position is read as reference homozygous, which is the
standard reading of a variant-only VCF. The script checks that assumption
rather than asserting it: it compares observed heterozygosity across the panel
with the value the winning population predicts.

Usage: python3 ancestry_infer.py <pass.vcf.gz> [n_windows]
"""
import math
import subprocess
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import gnomad_range as G

# gnomAD v4.1 genomes carries only about 292 Middle Eastern alleles, too few for a
# stable frequency, so mid is excluded from the panel rather than scored unreliably.
POPS = ["afr", "amr", "asj", "eas", "fin", "nfe", "sas"]
NAMES = {"afr": "African/African-American", "amr": "Admixed American",
         "asj": "Ashkenazi Jewish", "eas": "East Asian", "fin": "Finnish",
         "mid": "Middle Eastern", "nfe": "Non-Finnish European", "sas": "South Asian"}
LEN = {1: 248956422, 2: 242193529, 3: 198295559, 4: 190214555, 5: 181538259,
       6: 170805979, 7: 159345973, 8: 145138636, 9: 138394717, 10: 133797422,
       11: 135086622, 12: 133275309, 13: 114364328, 14: 107043718, 15: 101991189,
       16: 90338345, 17: 83257441, 18: 80373285, 19: 58617616, 20: 64444167,
       21: 46709983, 22: 50818468}
WIN = 40000
EDGE = 12000000


def windows(n):
    total = sum(max(0, LEN[c] - 2 * EDGE) for c in LEN)
    out = []
    for c in sorted(LEN):
        span = LEN[c] - 2 * EDGE
        if span <= 0:
            continue
        k = max(1, round(n * span / total))
        for i in range(k):
            pos = EDGE + int(span * (i + 0.5) / k)
            if c == 15 and 38000000 < pos < 42000000:
                continue  # the causal locus, kept out of the panel
            out.append((str(c), pos))
    return out


def pick(recs):
    """The most ancestry-informative usable SNV in one window."""
    best = None
    for f in recs:
        if f[6] != "PASS" or "," in f[4]:
            continue
        if len(f[3]) != 1 or len(f[4]) != 1:
            continue
        info = f[7]
        try:
            af = {p: float(G.info_get(info, "AF_" + p)) for p in POPS}
            an = {p: int(G.info_get(info, "AN_" + p)) for p in POPS}
        except ValueError:
            continue
        if min(an.values()) < 1000:
            continue
        g = float(G.info_get(info, "AF", "0"))
        if not 0.05 <= g <= 0.95:
            continue
        v = max(af.values()) - min(af.values())
        if best is None or v > best[0]:
            best = (v, f[0].replace("chr", ""), int(f[1]), f[3], f[4], af)
    return best


def main():
    vcf = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 90

    panel = []
    for chrom, pos in windows(n):
        try:
            recs = G.query_region(chrom, pos - WIN // 2, pos + WIN // 2, "genomes")
        except Exception:
            continue
        b = pick(recs)
        if b:
            panel.append(b)
    sys.stderr.write("panel: %d markers\n" % len(panel))
    if not panel:
        sys.exit("no markers")

    regions = "\n".join("chr%s\t%d\t%d" % (b[1], b[2] - 1, b[2]) for b in panel)
    open("/tmp/anc.bed", "w").write(regions + "\n")
    q = subprocess.run(["bcftools", "query", "-i", 'FILTER="PASS"', "-R", "/tmp/anc.bed",
                        "-f", "%CHROM\t%POS\t%REF\t%ALT\t[%GT]\n", vcf],
                       capture_output=True, text=True)
    call = {}
    for line in q.stdout.strip().split("\n"):
        if line:
            f = line.split("\t")
            call[(f[0].replace("chr", ""), int(f[1]))] = (f[2], f[3], f[4])

    ll = {p: 0.0 for p in POPS}
    used = het = 0
    exp_het = {p: 0.0 for p in POPS}
    for _, chrom, pos, ref, alt, af in panel:
        c = call.get((chrom, pos))
        if c and c[0] == ref and alt in c[1].split(","):
            k = c[2].replace("|", "/").split("/")
            dose = k.count(str(c[1].split(",").index(alt) + 1))
        elif c:
            continue  # a different allele here; skip rather than guess
        else:
            dose = 0
        used += 1
        if dose == 1:
            het += 1
        for p in POPS:
            f = min(max(af[p], 1e-4), 1 - 1e-4)
            pr = {0: (1 - f) ** 2, 1: 2 * f * (1 - f), 2: f * f}[dose]
            ll[p] += math.log(pr)
            exp_het[p] += 2 * f * (1 - f)

    order = sorted(POPS, key=lambda p: -ll[p])
    top = order[0]
    print("markers used            : %d" % used)
    print("observed heterozygous   : %d (%.1f%%)" % (het, 100.0 * het / used))
    print("predicted by best fit   : %.1f (%.1f%%)  <- checks the reference-homozygous assumption"
          % (exp_het[top], 100.0 * exp_het[top] / used))
    print()
    print("%-26s %14s %12s" % ("population", "log-likelihood", "vs best"))
    for p in order:
        print("%-26s %14.1f %12.1f" % (NAMES[p], ll[p], ll[p] - ll[top]))
    print()
    print("Best fit: %s. Next best is %.1f log units behind, a likelihood ratio of about e^%.0f."
          % (NAMES[top], ll[top] - ll[order[1]], ll[top] - ll[order[1]]))


if __name__ == "__main__":
    main()
