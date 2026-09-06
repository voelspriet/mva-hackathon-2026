# R21. The gene labels tested, and what two measured filters leave standing

**Asked 6 September 2026, closing the second pass promised in R19.** In `OBSERVATIONS_2000.md` every gene carrying two or more rare coding variants was labelled by a name prefix: anything beginning MUC, HLA, TRBV, IGHV, LILR, KIR, OR, TAS2R, PRAME, GOLGA, NBPF, KRTAP or ZNF was called `artefact-prone`, the rest `raw`. Not one number stood behind that. This note replaces it with four measurements per gene.

## Method

For each gene with two or more coding variants absent from the common catalogue, measured from the alignment and the calls themselves:

- **coverage ratio** across the gene body, against the genome median
- **median allele balance** of its heterozygous variants, where 0.5 is the expectation
- **median genotype quality**
- **minimum distance between its variants**, since variants under 1 kb apart are usually one misaligned indel

A gene is `artefact-prone` if any of these fails: coverage above 1.25, allele balance outside 0.30 to 0.70, quality below 60, or variants closer than 1 kb.

164 of the 224 genes could be tested. The rest lacked heterozygous calls with allele depths, or no gene of that name exists in Ensembl 116.

## Result 1: the name label was wrong in the direction that matters

| Name said | Measurement says | Genes |
|---|---|---|
| artefact-prone | artefact-prone | 69 |
| artefact-prone | clean | 1 |
| **clean** | **artefact-prone** | **78** |
| clean | clean | 16 |

The prefix list caught 69 of 147 measured artefacts, so under half. Its single false condemnation was *PRAMEF10*. Its 78 false clearances are the real problem: those genes were sitting in the file marked `raw`, meaning "worth examining", when a four-line measurement disposes of them.

**A heuristic that fails safe is tolerable. This one failed open.**

## Result 2: two measured filters leave two genes

Combining the frequency filter from R15 with the quality filter here:

| Filter | Genes remaining |
|---|---|
| two or more rare coding variants | 224 |
| both variants below gnomAD 1e-4, the candidate's own threshold | 8 |
| **and passing the four call-quality measurements** | **2** |

The two are **ADGRA3** and **BUB1B**.

The six that drop out are *ADAMTS1*, *KIR3DL3*, *MUC4*, *RBM39*, *SERPINA1* and *VPS41*, each on a measurement rather than on a name.

*BUB1B*: coverage ratio 1.00, median allele balance 0.50, quality 99. *ADGRA3*: coverage 0.96, allele balance 0.44, quality 99. Both are clean calls. *ADGRA3* is an adhesion G protein-coupled receptor with no established link to this phenotype, and it is named here because it is the only gene besides the diagnosis that survives two independent measured filters. It is a candidate for exclusion, not a rival diagnosis.

## An error in my own rule, stated rather than buried

The coverage test flagged genes above 1.25 but nothing below. Two genes therefore passed with coverage ratios of 0.05 (*CD99*) and 0.00 (*GTPBP6*), both pseudoautosomal, where the window matching fails. They should have been flagged. Corrected, 15 genes pass rather than 17, and the two-gene result above is unaffected because neither is among the eight.

## What this is worth

The compound-heterozygote candidate space in this genome is 224 genes on the raw criterion. Two orthogonal measured filters, population frequency and call quality, reduce it to 2, and one of those is the diagnosis. Neither filter uses the phenotype, a gene panel, or any disease knowledge.

That is a reusable statement about the method rather than about this child: for a recessive candidate search in a single exome or genome, frequency plus call quality removes roughly 99 percent of the field before any clinical reasoning begins.
