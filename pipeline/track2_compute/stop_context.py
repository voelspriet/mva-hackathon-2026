#!/usr/bin/env python3
"""Reconstruct the BUB1B ENST00000287598 CDS from local FASTA + GFF3, place the c.2210T>G PTC,
and print the stop codon, its +4 / -1 context and the downstream exon-junction geometry.
Local reference files only; the patient's allele is applied in memory."""
import gzip, sys, pysam
GFF, FA = sys.argv[1], sys.argv[2]
TX = "ENST00000287598"
cds = []
with gzip.open(GFF, "rt") as fh:
    for line in fh:
        if line[0] == "#": continue
        f = line.split("\t")
        if f[2] != "CDS" or TX not in f[8]: continue
        cds.append((int(f[3]), int(f[4])))
    cds.sort()
fa = pysam.FastaFile(FA)
seq, coords = [], []
for s, e in cds:
    seq.append(fa.fetch("15", s - 1, e).upper())
    coords.extend(range(s, e + 1))
cds_seq = "".join(seq)
print(f"CDS length {len(cds_seq)} nt = {len(cds_seq)//3} codons; {len(cds)} CDS blocks")
POS = 40209701           # the c.2210 base
i = coords.index(POS)    # 0-based CDS offset
print(f"genomic {POS} = CDS position c.{i+1}; codon {i//3+1}")
c0 = (i // 3) * 3
wt = cds_seq[c0:c0 + 3]
mut = wt[:i - c0] + "G" + wt[i - c0 + 1:]
print(f"wild-type codon {wt}  mutant codon {mut}")
print(f"-1 base (c.{c0}) = {cds_seq[c0-1]}   +4 base (c.{c0+4}) = {cds_seq[c0+3]}   +4..+6 = {cds_seq[c0+3:c0+6]}")
print(f"context -6..+6: {cds_seq[c0-6:c0]}|{mut}|{cds_seq[c0+3:c0+9]}")
# downstream in-frame stops if the PTC is read through
stops = {"TAA", "TAG", "TGA"}
nxt = [j for j in range(c0 + 3, len(cds_seq) - 2, 3) if cds_seq[j:j+3] in stops]
print(f"next in-frame stop after readthrough: CDS pos c.{nxt[0]+1} (codon {nxt[0]//3+1}) = {cds_seq[nxt[0]:nxt[0]+3]}"
      if nxt else "no further in-frame stop before the native terminator")
print(f"native terminator codon {len(cds_seq)//3} = {cds_seq[-3:]}")
# NMD geometry
junc = []
run = 0
for s, e in cds[:-1]:
    run += e - s + 1
    junc.append(run)
print(f"PTC at CDS {i+1}; last CDS junction at {junc[-1]}; distance {junc[-1]-(i+1)} nt; "
      f"downstream CDS junctions = {sum(1 for j in junc if j > i+1)}")
