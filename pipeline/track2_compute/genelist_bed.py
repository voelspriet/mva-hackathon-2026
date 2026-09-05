#!/usr/bin/env python3
"""Build a BED of gene spans (+/- flank) for a list of gene symbols from an Ensembl GFF3."""
import sys, gzip
gff, listfile, out = sys.argv[1], sys.argv[2], sys.argv[3]
flank = int(sys.argv[4]) if len(sys.argv) > 4 else 0
want = {l.split("#")[0].strip() for l in open(listfile) if l.split("#")[0].strip()}
rows, seen = [], set()
with gzip.open(gff, "rt") as fh:
    for line in fh:
        if line[0] == "#": continue
        f = line.split("\t")
        if f[2] != "gene": continue
        attr = dict(kv.split("=", 1) for kv in f[8].rstrip().split(";") if "=" in kv)
        name = attr.get("Name")
        if name in want:
            rows.append((f[0], max(0, int(f[3]) - 1 - flank), int(f[4]) + flank, name))
            seen.add(name)
def key(r):
    c = r[0]
    return (int(c) if c.isdigit() else 99, c, r[1])
with open(out, "w") as o:
    for r in sorted(rows, key=key):
        o.write("\t".join(map(str, r)) + "\n")
sys.stderr.write(f"{len(rows)} spans for {len(seen)}/{len(want)} symbols; missing: {sorted(want-seen)}\n")
