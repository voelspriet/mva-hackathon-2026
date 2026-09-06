# R4. The mitochondrial genome

**Question.** Growth failure, low muscle mass and failure to thrive are the presenting features that a mitochondrial disorder also produces. The mitochondrial genome is in the VCF and no analysis in this project has looked at it.

**Data.** In hand.

**Computed answer. Eleven PASS variants of thirteen called, all at or near homoplasmy, no heteroplasmy of note.** An earlier version said thirteen without noting that two of them, at positions 4769 and 8860, fail quality filtering. Both are near-universal differences from the reference sequence, so nothing of substance turns on it, but the count in the table below is of called records rather than of passing ones.

| Position | Change | Genotype | Allele depth | Depth | Minor fraction |
|---|---|---|---|---|---|
| 263 | A>G | 1/1 | 0,2110 | 2110 | 0 |
| 302 | A>AC,ACC | 1/2 | 16,1324,289 | 1671 | length variant in the homopolymer |
| 310 | T>TC | 1/1 | 2,1813 | 1827 | 0.001 |
| 750 | A>G | 1/1 | 0,4319 | 4321 | 0 |
| 1438 | A>G | 1/1 | 0,5212 | 5212 | 0 |
| 4769 | A>G | 1/1 | 0,4174 | 4177 | 0 |
| 8860 | A>G | 1/1 | 0,4026 | 4026 | 0 |
| 13830 | T>C | 1/1 | 1,3688 | 3689 | 0.000 |
| 14470 | T>A | 1/1 | 1,4938 | 4939 | 0.000 |
| 15326 | A>G | 1/1 | 0,4572 | 4572 | 0 |
| 16093 | T>C | 1/1 | 90,4129 | 4219 | 0.021 |
| 16221 | C>T | 1/1 | 9,4532 | 4546 | 0.002 |
| 16519 | T>C | 1/1 | 0,3396 | 3401 | 0 |

Coverage is 1,700 to 5,200 reads, so a heteroplasmy of a few percent would have been visible. The highest minor fraction is 2.1 percent at position 16093, in the hypervariable control region.

**What each possible result would change.** A pathogenic heteroplasmic variant at a meaningful load would have introduced a second explanation for the growth and muscle phenotype and changed both the differential and the drug-avoidance list, since several agents are contraindicated in mitochondrial disease. There is none.

**Limit.** These positions are haplogroup-defining background variants in the control region and the common coding polymorphisms. This analysis reports the genotypes and the allele fractions; it does not assign a haplogroup and it does not run them against a curated pathogenicity set, which is the step that remains.

**Tier.** Computed here. **Cost.** Seconds.

**Why it was not asked before.** The gene-list and phenotype-driven approaches both operate on the nuclear genome, so the mitochondrial contig was never in scope for either.
