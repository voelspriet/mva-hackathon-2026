"""Score a pharmacogenomic and thrombophilia panel against the proband VCF.

Two traps this script exists to avoid, both of which produced wrong answers in
a first version and were caught by cross-checking against an independent
ClinVar drug-response screen.

1. Do not match on rsID. 8.9 percent of PASS calls in this VCF carry no rsID at
   all, and the missing ones include Factor V Leiden and CYP3A5*3. An rsID join
   silently reported both as absent. Everything here is matched on coordinate
   and allele instead, with the rsID used only as a label.

2. An absent panel variant is ambiguous in a single-sample VCF, which lists
   variant sites only: it can mean reference homozygous or never callable.
   So each absent position is queried a second time against the unfiltered
   source VCF, and a record that exists but failed filtering is reported as
   filtered rather than as reference. Note the source VCF names contigs without
   the "chr" prefix while the working copy adds it.

Usage: python3 pgx_scan.py <panel.tsv> <clinvar.vcf.gz> <pass.vcf.gz> <source.vcf.gz>
"""
import gzip
import subprocess
import sys


def query(vcf, region):
    q = subprocess.run(["bcftools", "view", "-H", "-r", region, vcf],
                       capture_output=True, text=True)
    return [l.split("\t") for l in q.stdout.strip().split("\n") if l]


def main():
    panel_p, clinvar_p, pass_p, src_p = sys.argv[1:5]

    panel = []
    with open(panel_p) as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if line.strip():
                panel.append(dict(zip(hdr, line.rstrip("\n").split("\t"))))
    want = {r["rsid"] for r in panel}

    cv = {}
    with gzip.open(clinvar_p, "rt") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            f = line.rstrip("\n").split("\t")
            info = f[7]
            i = info.find("RS=")
            if i < 0:
                continue
            rs = "rs" + info[i + 3:].split(";")[0].split("|")[0]
            if rs not in want:
                continue
            sig = "."
            for kv in info.split(";"):
                if kv.startswith("CLNSIG="):
                    sig = kv[7:]
            e = cv.setdefault(rs, {"chrom": f[0], "pos": f[1], "pairs": set(), "sig": set()})
            for alt in f[4].split(","):
                if alt != ".":
                    e["pairs"].add((f[3], alt))
            e["sig"].add(sig)

    idx = {}
    q = subprocess.run(["bcftools", "query", "-i", 'FILTER="PASS" && ID!="."',
                        "-f", "%CHROM\t%POS\t%ID\t%REF\t%ALT\t%QUAL\t%FILTER\t%INFO/DP\t[%GT:%AD:%DP:%GQ]\n",
                        pass_p], capture_output=True, text=True)
    for line in q.stdout.split("\n"):
        if not line:
            continue
        f = line.split("\t")
        for rid in f[2].split(";"):
            if rid in want:
                v = f[8].split(":")
                idx[rid] = [f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7],
                            "GT:AD:DP:GQ", ":".join(v)]

    out = ["\t".join(["rsid", "gene", "allele", "drug_or_risk", "call", "genotype",
                      "AD", "DP", "GQ", "position", "clinvar_sig"])]
    for r in panel:
        rs = r["rsid"]
        c = cv.get(rs)
        if not c:
            # ClinVar does not carry this rsID. Fall back to the VCF's own ID
            # field, which resolves it when the caller annotated the site.
            f = idx.get(rs)
            if f:
                fmt = dict(zip(f[8].split(":"), f[9].rstrip("\n").split(":")))
                g = fmt.get("GT", ".")
                n = g.replace("|", "/").split("/").count("1")
                out.append("\t".join([
                    rs, r["gene"], r["allele"], r["drug_or_risk"],
                    {2: "CARRIED homozygous", 1: "CARRIED heterozygous"}.get(
                        n, "CARRIED %s" % g) + " (matched by rsID, not in ClinVar)",
                    g, fmt.get("AD", "."), fmt.get("DP", "."), fmt.get("GQ", "."),
                    "%s:%s" % (f[0], f[1]), "not in ClinVar"]))
            else:
                out.append("\t".join([rs, r["gene"], r["allele"], r["drug_or_risk"],
                                      "UNRESOLVED not in ClinVar and no rsID in VCF", ".",
                                      ".", ".", ".", "unknown", "."]))
            continue
        loc = "chr%s:%s" % (c["chrom"], c["pos"])
        sig = ";".join(sorted(c["sig"]))
        call = gt = ad = dp = gq = "."

        hit = None
        for rec in query(pass_p, loc):
            if rec[1] != c["pos"]:
                continue
            alts = rec[4].split(",")
            for k, alt in enumerate(alts, start=1):
                if (rec[3], alt) in c["pairs"]:
                    hit = (rec, k)
                    break
            if hit:
                break

        if hit:
            rec, k = hit
            fmt = rec[8].split(":")
            val = dict(zip(fmt, rec[9].rstrip("\n").split(":")))
            gt = val.get("GT", ".")
            ad, dp, gq = val.get("AD", "."), val.get("DP", "."), val.get("GQ", ".")
            n = gt.replace("|", "/").split("/").count(str(k))
            call = {2: "CARRIED homozygous", 1: "CARRIED heterozygous"}.get(n, "CARRIED %s" % gt)
        else:
            src = [rec for rec in query(src_p, "%s:%s" % (c["chrom"], c["pos"]))
                   if rec[1] == c["pos"]]
            if not src:
                call, gt = "not carried, no record at position", "assumed reference"
            else:
                filts = sorted({rec[6] for rec in src})
                matched = any((rec[3], a) in c["pairs"] for rec in src for a in rec[4].split(","))
                if matched and "PASS" not in filts:
                    call = "PRESENT BUT FILTERED (%s), not counted" % ",".join(filts)
                    gt = src[0][9].split(":")[0]
                else:
                    call = "not carried, other allele at position (%s)" % ",".join(filts)
                    gt = src[0][9].split(":")[0]
        out.append("\t".join([rs, r["gene"], r["allele"], r["drug_or_risk"], call,
                              gt, ad, dp, gq, loc, sig]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
