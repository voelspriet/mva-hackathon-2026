"""GFF3 -> sorted, bgzipped BED of CDS intervals with gene name (chrom, start0, end, gene)."""
import gzip, re, sys, subprocess
gff, out = sys.argv[1], sys.argv[2]
tx2gene, genes, cds = {}, {}, []
with gzip.open(gff, "rt") as f:
    for l in f:
        if l[0] == "#": continue
        c, _, t, s, e, _, _, _, a = l.rstrip("\n").split("\t")
        if t == "gene":
            gid = re.search(r"ID=gene:([^;]+)", a); nm = re.search(r"Name=([^;]+)", a)
            if gid: genes[gid.group(1)] = nm.group(1) if nm else gid.group(1)
        elif "ID=transcript:" in a:
            tid = re.search(r"ID=transcript:([^;]+)", a); par = re.search(r"Parent=gene:([^;]+)", a)
            if tid and par: tx2gene[tid.group(1)] = par.group(1)
        elif t == "CDS":
            par = re.search(r"Parent=transcript:([^;]+)", a)
            if par: cds.append((c, int(s) - 1, int(e), par.group(1)))
rows = sorted({(c, s, e, genes.get(tx2gene.get(t, ""), "?")) for c, s, e, t in cds},
              key=lambda r: (r[0].zfill(2), r[1]))
plain = out[:-3] if out.endswith(".gz") else out
with open(plain, "w") as o:
    for r in rows: o.write("%s\t%d\t%d\t%s\n" % r)
subprocess.run(["bgzip", "-f", plain], check=True); subprocess.run(["tabix", "-f", "-p", "bed", out], check=True)
print("CDS intervals:", len(rows), file=sys.stderr)
