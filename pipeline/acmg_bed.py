"""GFF3 + gene list -> BED of gene spans."""
import gzip, re, sys
gff, genes_txt, out = sys.argv[1:4]
want = set(open(genes_txt).read().split()); found = {}
with gzip.open(gff, "rt") as f:
    for l in f:
        if l[0] == "#": continue
        p = l.split("\t")
        if p[2] != "gene": continue
        m = re.search(r"Name=([^;]+)", p[8])
        if m and m.group(1) in want: found[m.group(1)] = (p[0], int(p[3]), int(p[4]))
with open(out, "w") as o:
    for g, (c, s, e) in sorted(found.items(), key=lambda x: (x[1][0].zfill(2), x[1][1])): o.write(f"{c}\t{s-1}\t{e}\t{g}\n")
print(f"ACMG genes located: {len(found)} of {len(want)}; missing: {sorted(want - set(found))}", file=sys.stderr)
