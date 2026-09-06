# R15. Two changes to the R14 shortlist: real frequencies, and phase as an eliminator

**Asked 6 September 2026, after R14.** R14 asked whether any other gene in this genome looks like *BUB1B* and answered no. It used two things this note replaces: absence of an rsID as the rarity proxy, and a hand-curated exclusion list for artefact-prone families. Both are defensible, and both are judgement calls. This note repeats the question with a measured threshold instead of a proxy, and adds one filter R14 did not use.

## Change 1. Measured frequency instead of the rsID proxy

The candidate's own rarity is documented as gnomAD AF 7.9e-5 and 6.8e-7. Applying **that same threshold to the background** is the like-for-like comparison. 876 heterozygous coding variants in genes carrying two or more were queried against the gnomAD v4.1 API; 850 returned.

| Threshold on both variants | Genes |
|---|---|
| none (the raw grouping) | 138 |
| AF < 1e-2 | 18 |
| AF < 1e-3 | 10 |
| **AF < 1e-4 (the candidate's own threshold)** | **8** |
| AF < 1e-5 | 2 |

The eight: *ADAMTS1*, *ADGRA3*, **BUB1B**, *KIR3DL3*, *MUC4*, *RBM39*, *SERPINA1*, *VPS41*.

At AF < 1e-5 only two survive: *BUB1B* and *KIR3DL3*.

**Note the disagreement with R14, which matters more than either number.** R14's fifteen and this note's eight share only *BUB1B*. The two shortlists are otherwise disjoint, because R14 filtered on HIGH/MODERATE impact plus no rsID plus a curated family list, and this note filtered on measured allele frequency alone. The shortlist is therefore highly sensitive to how "rare" is defined, and any claim of the form "only N genes look like this" should state its criterion. What survives both criteria is *BUB1B*, which is the useful result: the candidate is robust to the choice, and its competitors are not.

## Change 2. Read-backed phase as an eliminator, not a check

R1 asked whether phase resolves the *BUB1B* pair and correctly answered no. That question can also be asked of every other candidate, where it is not a check but a filter: if a gene's two variants sit in the same phase set with the same orientation, they are on one haplotype, the other allele is intact, and the gene cannot be a recessive cause.

Applied to the eight:

| Gene | Phase evidence | Outcome |
|---|---|---|
| *ADAMTS1* | both variants, same PID, same PGT | eliminated |
| *KIR3DL3* | both variants, same PID, same PGT | eliminated |
| *VPS41* | both variants, same PID, same PGT | eliminated |
| *ADGRA3*, **BUB1B**, *MUC4*, *RBM39*, *SERPINA1* | no shared phase set | undecided |

Eight becomes five. The elimination of *KIR3DL3* is the substantive one: it was the only other gene meeting the strictest threshold, and it is removed by evidence in the file rather than by argument.

Applied to the wider grouping the same filter eliminates 79 of 151 genes, so it is not specific to this shortlist.

## What this is and is not

It does not change the diagnosis, and it does not overturn R14. It replaces one judgement call with a measurement, records that the shortlist depends on that call, and removes the candidate's nearest competitor with evidence rather than reasoning.

It cannot resolve *BUB1B* itself. Those two variants are 10,911 bp apart, far beyond read-backed phasing, exactly as R1 established. Parental genotyping or a long-read amplicon remains the only route.

**Reproduce:** `pipeline/alien/fetch_gnomad_af.py` (batched gnomAD v4.1 API queries, 20 variants per request), then the phase test on `PGT`/`PID` in the supplied VCF.
