# R17. The raw reads, and why a better measurement still cannot see this disease

**Asked 6 September 2026.** Every analysis in this project so far used one of the thirteen supplied files: the VCF. The other eight, 78.85 GB of raw reads across four lanes, had never been touched. The recorded reason (`R1`) covers only phasing, where re-processing genuinely cannot help. It says nothing about the one measurement the reads are actually good for.

The report states a mosaicism detection floor of about 10%, derived from allele balance in the VCF. That floor is a property of the chosen input, not of the biology. Coverage depth from the reads is the independent channel.

## Method

All four lanes aligned to GRCh38 no-alt (the same reference the supplied VCF was called against) with minimap2 2.24 `-ax sr` on 20 threads, sorted and merged with samtools 1.13: 57 GB, about 4 hours 35 minutes wall clock. Coverage in 100 kb windows with mosdepth 0.3.8. 29,374 windows retained after dropping those below 30% of the autosomal median, which removes unmappable sequence.

Median autosomal coverage **51x**.

Per-window GC content computed from the reference, and each window divided by the median coverage of all windows in its GC bin. This is the step that matters: without it the residual scatter is dominated by library GC bias and no floor below 8% is reachable.

## Result 1: the correction works, and the floor drops

| Chromosome | Ratio before GC correction | After |
|---|---|---|
| chr19 | 1.043 | 1.019 |
| chr17 | 1.033 | 1.014 |
| chr16 | 1.027 | 1.012 |
| chr22 | 1.030 | 1.008 |
| chr4 | 0.988 | 0.998 |
| chr13 | 0.994 | 1.001 |

The chromosomes that looked elevated are the GC-rich ones and those that looked low are the AT-rich ones, in rank order. That is library preparation, not biology, and correcting for it removes most of it.

| | |
|---|---|
| Largest autosomal deviation after correction | **1.94%** |
| Mean absolute deviation | 0.39% |
| **Implied detection floor for a mosaic trisomy** | **about 4% of cells** |

A trisomy present in a fraction *f* of cells raises coverage by *f*/2, so 1.94% residual noise corresponds to *f* = 3.9%. Against the 10% floor currently stated in the report.

## Result 2: nothing is there, and the sex chromosomes check out

Every autosome falls between 0.994 and 1.019 after correction. No whole-chromosome gain or loss is present in more than about 4% of the cells in this blood sample.

chrX 0.498 and chrY 0.512, precisely half the autosomal level. This independently confirms from raw reads what the VCF's heterozygosity pattern showed: one X, one Y.

## Result 3, and the one that matters: this measurement is structurally blind to this disease

The negative above is close to uninformative about the diagnosis, and the reason is in the name of the condition. Mosaic **variegated** aneuploidy means different cells carry different chromosome gains and losses, not the same one. If a fifth of this child's cells were aneuploid but each for a different chromosome, then per chromosome only about 1% of cells are affected. That sits below any floor this method can reach, including the improved 4%.

Bulk sequencing averages over millions of cells. A defect that sits somewhere different in each cell disappears into that average. This is why karyotyping, which counts chromosomes one cell at a time, remains the diagnostic standard for MVA, and why whole genome sequencing cannot replace it.

## What to take from this

Three things, in order of usefulness.

1. **A stated limit with a measurement behind it.** "No whole-chromosome aneuploidy above about 4% of cells in this blood sample" replaces a floor of 10% that was a consequence of using the VCF rather than the reads.
2. **A reason, not an apology, for why the genome cannot confirm this diagnosis.** The instrument is wrong for a variegated phenotype, by construction. That belongs in the limitations section, written by us rather than asked by a reviewer.
3. **A second, independent confirmation of the sex-chromosome configuration**, arrived at from coverage rather than from genotypes.

**Reproduce:** `align.sh` on the server (minimap2, samtools, mosdepth), then the GC-binned normalisation described above. Raw reads and BAMs must be deleted after the hackathon under the data use terms, with notification to Sage Bionetworks.
