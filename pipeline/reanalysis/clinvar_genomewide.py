"""Genome-wide ClinVar pathogenic screen against a single-sample germline VCF.

Why this exists: every earlier screen in this project was bounded by a gene list.
Track 1 screened the 81 ACMG secondary-findings genes; the modifier scan (R5)
screened an 80-gene mitotic and decay network. R5 named its own blind spot,
"any gene outside the 80". This closes that gap by asking the whole genome
against the whole of ClinVar, with no gene list at all.

Method: take every ClinVar record asserted Pathogenic or Likely_pathogenic
without conflict, reduce to unique positions, query the proband VCF at those
positions with the PASS filter applied, then require an exact ref and alt match
in Python. bcftools -R matches positions, not alleles, so the Python step is
what makes a hit a hit.

Nothing is sent anywhere. ClinVar is read as a downloaded static file.

Usage: python3 clinvar_genomewide.py <clinvar.vcf.gz> <proband.vcf.gz> [outdir]
"""
import gzip
import os
import subprocess
import sys

# Which ClinVar assertions to keep. Overridable so the same screen can be run for
# drug response as well as for pathogenicity, without a second copy of the code.
KEEP = [k for k in os.environ.get(
    "CLNSIG_KEEP", "Pathogenic,Likely_pathogenic").split(",") if k]
DROP = [k for k in os.environ.get("CLNSIG_DROP", "Conflicting").split(",") if k]


def keep_sig(sig):
    if any(x in sig for x in DROP):
        return False
    return any(x in sig for x in KEEP)


def clinvar_plp(path, bed_path):
    """Write a BED of unique positions carrying an unconflicted P/LP assertion."""
    seen = set()
    kept = 0
    total = 0
    with gzip.open(path, "rt") as fh, open(bed_path, "w") as bed:
        for line in fh:
            if line.startswith("#"):
                continue
            total += 1
            f = line.rstrip("\n").split("\t")
            info = f[7]
            sig = ""
            for kv in info.split(";"):
                if kv.startswith("CLNSIG="):
                    sig = kv[7:]
                    break
            if not keep_sig(sig):
                continue
            kept += 1
            key = (f[0], f[1])
            if key in seen:
                continue
            seen.add(key)
            pos = int(f[1])
            bed.write("chr%s\t%d\t%d\n" % (f[0], pos - 1, pos))
    return total, kept, len(seen)


def clinvar_alleles(path):
    """Map (chrom, pos, ref, alt) -> the INFO fields we report."""
    out = {}
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            f = line.rstrip("\n").split("\t")
            info = f[7]
            d = {}
            for kv in info.split(";"):
                if "=" in kv:
                    k, v = kv.split("=", 1)
                    d[k] = v
            sig = d.get("CLNSIG", "")
            if not keep_sig(sig):
                continue
            for alt in f[4].split(","):
                out[(f[0], f[1], f[3], alt)] = d
    return out


def main():
    cv, proband = sys.argv[1], sys.argv[2]
    outdir = sys.argv[3] if len(sys.argv) > 3 else "."
    os.makedirs(outdir, exist_ok=True)
    bed = os.path.join(outdir, "clinvar_plp.bed")

    sys.stderr.write("[1/4] reading ClinVar (keep=%s drop=%s)\n" % (KEEP, DROP))
    total, kept, positions = clinvar_plp(cv, bed)
    sys.stderr.write("      %d records, %d P/LP unconflicted, %d unique positions\n"
                     % (total, kept, positions))

    sys.stderr.write("[2/4] querying proband at those positions (PASS only)\n")
    q = subprocess.run(
        ["bcftools", "query", "-i", 'FILTER="PASS"', "-R", bed,
         "-f", "%CHROM\t%POS\t%REF\t%ALT\t%QUAL\t[%GT]\t[%AD]\t[%DP]\t[%GQ]\n",
         proband],
        capture_output=True, text=True)
    if q.returncode != 0:
        sys.exit("bcftools failed: %s" % q.stderr[:500])
    rows = [r.split("\t") for r in q.stdout.strip().split("\n") if r]
    sys.stderr.write("      %d proband PASS calls at ClinVar P/LP positions\n" % len(rows))

    sys.stderr.write("[3/4] loading ClinVar alleles for exact matching\n")
    alleles = clinvar_alleles(cv)

    sys.stderr.write("[4/4] exact ref/alt matching\n")
    out = os.path.join(outdir, "clinvar_genomewide_hits.tsv")
    n = 0
    with open(out, "w") as fh:
        fh.write("\t".join(["chrom", "pos", "ref", "alt", "qual", "gt", "ad", "dp",
                            "gq", "gene", "clnsig", "revstat", "mc", "rs", "clndn"]) + "\n")
        for r in rows:
            chrom = r[0].replace("chr", "")
            for alt in r[3].split(","):
                d = alleles.get((chrom, r[1], r[2], alt))
                if not d:
                    continue
                n += 1
                fh.write("\t".join([r[0], r[1], r[2], alt, r[4], r[5], r[6], r[7], r[8],
                                    d.get("GENEINFO", "."), d.get("CLNSIG", "."),
                                    d.get("CLNREVSTAT", "."), d.get("MC", "."),
                                    d.get("RS", "."), d.get("CLNDN", ".")]) + "\n")
    sys.stderr.write("      %d exact matches -> %s\n" % (n, out))
    print("ClinVar records %d; P/LP unconflicted %d; unique positions %d; "
          "proband PASS calls there %d; exact allele matches %d"
          % (total, kept, positions, len(rows), n))


if __name__ == "__main__":
    main()
