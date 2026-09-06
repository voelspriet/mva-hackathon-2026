# R12. The mitochondrial genome R7 silently skipped, and the causal gene's own introns

**Asked 6 September 2026.** Two gaps, one of them created by this project two commits ago.

## Part 1. R7 never screened the mitochondrial genome, and said nothing about it

### The fault

R7 reported a genome-wide ClinVar screen. It was not genome-wide. ClinVar names the mitochondrial contig **`MT`**, and R7 built its query regions by prefixing every ClinVar contig with `chr`, producing **`chrMT`**. The proband VCF calls that contig **`chrM`**.

| | |
|---|---|
| ClinVar mitochondrial records | 3,130 |
| Positions R7 wrote to its BED as `chrMT` | 184 |
| Positions R7 wrote as `chrM` | **0** |
| Mitochondrial hits reported by R7 | **0** |

The zero in the last row reads like a result. It was an empty intersection between two spellings. **`bcftools -R` does not warn when a region names a contig that does not exist**, so the screen returned a clean answer for a compartment it never looked at. This is the third time in this project that a filter has been mistaken for a measurement, after the missing PASS filter in `DATA_CLAIM_CHECKS.md` and the rsID join in R8.

### The screen, run properly

All 11 PASS mitochondrial variants against all 3,130 ClinVar `MT` records.

| | |
|---|---|
| Unconflicted pathogenic mitochondrial records in ClinVar | 78 |
| **Carried by this child** | **0** |

Five of the eleven carry a ClinVar record at all, and none of them is pathogenic.

| Variant | Depth | ClinVar |
|---|---|---|
| m.263A>G | 2,110 | not provided |
| m.750A>G | 4,321 | Benign |
| m.1438A>G | 5,212 | Benign |
| m.14470T>A | 4,939 | Likely benign |
| m.15326A>G | 4,572 | Benign |

R8 had already established that the two aminoglycoside-ototoxicity alleles, m.1555A>G and m.1494C>T, are absent at depth 5,212. **The mitochondrial genome is now screened against curated pathogenicity as well, and it is clean.** R4's conclusion that there is no mitochondrial explanation stands, and it now rests on a screen rather than on inspection.

### Maternal ancestry, as far as it can honestly be taken

The child differs from the rCRS reference at **11 positions**. rCRS is itself a West Eurasian sequence, so a small number of differences is what a West Eurasian maternal lineage produces, and lineages rooted outside that group differ at substantially more positions. That is consistent with R9's autosomal result and is genuinely independent of it, since R9 used autosomes and this is the maternal line alone.

**No haplogroup is assigned.** Doing that properly needs a phylogeny file this project does not hold offline, which is exactly what `SUMMARY.md` item P4 says. The direction of the evidence is reportable; the label is not.

## Part 2. The introns of *BUB1B*, which item P1 proposed and nobody computed

### Why

`track2/reanalysis/SUMMARY.md` lists as **P1**: "Deep intronic and regulatory variants near *BUB1B*. In hand. Needs a splice and regulatory prediction model this project does not hold offline." The report separately established that a regulatory allele class exists in this gene, because Matsuura's seven families carry a causal substitution 44 kb upstream that no coding analysis would find. The **60 kb upstream** was therefore searched, and was clean.

**The gene body itself was never searched.** The 44 kb upstream result is precisely the reason that was an odd place to stop.

### Result

Every PASS variant across chr15:40,155,000 to 40,230,000, with gnomAD frequency by a single byte-range read and distance to the nearest annotated splice site computed from the local exon structure.

**23 PASS variants across 75 kb. Four are rare or absent.**

| Position | Zygosity | gnomAD AF | Distance to nearest splice site | |
|---|---|---|---|---|
| 40209701 | het | 3.29e-05 | 67 bp | **Allele 1. Positive control** |
| 40220612 | het | 6.84e-07 | 49 bp | **Allele 2. Positive control** |
| 40192892 | het | 0.0021 | 3,590 bp | Deep intronic, rs185599777, too common and too far to matter |
| **40216470** | **het** | **absent** | **1,025 bp** | **The one novel variant in the gene** |

### chr15:40216470 A>G

**It is real.** A>G, heterozygous, AD 28,18, depth 46, **GQ 99, MQ 60**, QUAL 383.77, QD 8.34, FS 4.376. Allele balance 0.39 and QD 8.34 are moderate rather than excellent, and the rest is clean.

**It is genuinely absent, not merely unqueried.** gnomAD genomes carries **248 records in the 400 bp around it**, several at frequencies near 1e-05, so the region is densely covered and the absence of this allele is a real absence across roughly 800,000 sampled individuals rather than a coverage hole.

**It is deep intronic.** It sits between the exons at 40,213,331 to 40,213,474 and 40,217,495 to 40,217,513, which puts it 1,025 bp before the next exon.

**What it is not.** It is not a second explanation for anything. The child already carries two coding alleles that account for the diagnosis. It is not the Matsuura-type allele, which lies upstream of the transcription start and not inside the gene. It is not assessable for a splicing effect here, because a cryptic-splice or branch-point prediction needs the model P1 says this project does not hold, and because phase is unreadable: R1 established that the longest read-backed phase set anywhere in this genome spans 288 bp, so whether this variant sits in cis with allele 1 or allele 2 cannot be determined.

**Status: recorded, not built on.** It is the only novel variant in the causal gene and it would be dishonest to leave it unrecorded, and equally dishonest to present a deep intronic variant of unknown effect as a finding. The RNA assay the gate already proposes, which exists to measure allele-specific expression and decay, is the same experiment that would show whether this variant does anything.

### Two things this settles that nobody had checked

**The causal gene is well covered.** Nobody had verified it. Mean depth across the *BUB1B* region is **42.3**, against a control median of 41.9 across ten 75 kb windows spread over chromosome 15, and a genome autosomal median of 44. **The project's confidence that it found both alleles and did not miss a third now rests on a measurement.**

**The region is genuinely variant-poor.** 23 variants against a control median of **103**, and fewer than the lowest of the ten controls at 29.

| | Variants | Mean depth |
|---|---|---|
| *BUB1B*, 75 kb | **23** | 42.3 |
| Ten chr15 controls, 75 kb each | median 103, range 29 to 251 | median 41.9 |

Because coverage is equal, this is not a callability artefact. It is the same direction as R5's finding that the checkpoint network carries fewer rare coding variants than its coding length predicts, which is what constraint on essential mitotic genes should look like. Ten windows is a small comparison and local variant density varies several-fold, so it is offered as an observation, not as a statistic.

## What R12 changes

| | |
|---|---|
| Faults found in this project's own recent work | One. R7's mitochondrial screen was an empty contig-name intersection |
| Compartments screened for the first time | One. The mitochondrial genome, against 78 pathogenic records, clean |
| Proposed items now executed | **P1**, the *BUB1B* gene body |
| Novel variants found | One, deep intronic, recorded and not built on |
| Facts established that were previously assumed | The causal gene's coverage is normal, measured against ten controls |
| Recommendations added | **None** |

A region query against a contig name that does not exist returns nothing and raises nothing, so an empty result and an unasked question look identical in the output. R7's and R8's faults both had that shape.
