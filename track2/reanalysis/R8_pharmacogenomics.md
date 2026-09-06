# R8. What does this genome say about the drugs this child may receive, and about the family's own history?

**Asked 6 September 2026.** A 40-gene pharmacogenomic and renal BED file, `work/track2/genes_pgx.bed`, was built earlier in this project and **never systematically scanned**. The string `genes_pgx` appears nowhere else in the repository. What exists instead is three spot checks in `track2/creative/D_compute.md`: G6PD, one *DPYD* allele and one *SLC34A1* allele. This is the scan.

## Method, and two errors it produced first

`pipeline/reanalysis/pgx_scan.py` against a 36-variant panel in `pipeline/reanalysis/pgx_panel.tsv`. Both files are committed and the panel is a plain table, so a reader can see exactly which alleles were interrogated and which were not.

**The first version of this scan was wrong, in the direction that matters.** It reported Factor V Leiden as absent in a child who carries it. Two faults, both recorded because both are generic.

1. **It matched on rsID.** 423,432 of the 4,740,790 PASS calls in this VCF, **8.9 percent**, carry no rsID at all, and the unlabelled set includes Factor V Leiden and *CYP3A5\*3*. An rsID join reported both as not carried. Everything is now matched on coordinate and allele, with the rsID used only as a label.
2. **Its fallback query used the wrong contig names.** The supplied VCF names contigs `1`, `2`, `3`; the working copy adds the `chr` prefix. Every fallback lookup silently returned nothing, so every absent variant was reported as reference.

Both faults produced confident output. Neither raised an error. The scan was caught only because an independent genome-wide ClinVar drug-response screen, run first, had already found Factor V Leiden by coordinate. **A pharmacogenomic report that says "absent" without distinguishing "not carried" from "not looked at" is the specific failure this file is now built to prevent**, and it is the same failure as the missing PASS filter in `DATA_CLAIM_CHECKS.md` and the unaudited exclusions in `SIMULATED_PANELS.md`: absence asserted from a filter rather than measured.

The current script resolves every absent panel variant a second way, against the unfiltered source VCF, and reports a filtered record as filtered rather than as reference.

## What is carried

| Gene | Allele | Genotype | Depth | What it means |
|---|---|---|---|---|
| *CYP2C19* | \*2 and \*17, one of each | 0/1 and 0/1 | 44, 50 | **Intermediate metaboliser.** See below |
| *F5* | Factor V Leiden, rs6025 | 0/1 | 54 | **Thrombophilia.** See below |
| *CYP2D6* | \*4, plus the rs1065852 tag | 0/1 and 0/1 | 75, 70 | Probable intermediate metaboliser, but see the limitation below |
| *CYP3A5* | \*3 homozygous | 1/1 | 48 | Non-expresser. The common European state. Not guideline-actionable |
| *MTHFR* | 677C>T homozygous | 1/1 | 44 | Found, and deliberately not acted on. See below |
| *CYP2B6* | \*6 | 0/1 | 44 | Oxazaphosphorine activation. Not guideline-actionable |
| *SLC19A1* | 80G>A | 0/1 | 32 | Reduced folate carrier. Not guideline-actionable |
| *DPYD* | \*6 | 0/1 | 32 | **Normal function per CPIC.** Listed because it is often over-called |
| *CBR3* | V244M | 0/1 | 65 | Anthracycline research literature only |

### *CYP2C19*, the one with a guideline behind it

The child carries one no-function allele (\*2) and one increased-function allele (\*17). CPIC assigns \*2/\*17 as an **intermediate metaboliser**, because \*17 does not fully compensate for \*2, and CPIC marks this assignment **provisional** because the supporting data have not been consistently replicated ([CPIC/Medical Genetics Summaries](https://www.ncbi.nlm.nih.gov/books/NBK379740/table/diazepam.T.the_cpic_assignment_of_cyp2c1/)).

This is recorded and not acted on. The reason it is recorded is voriconazole. A child treated for a solid tumour who becomes neutropenic and febrile may receive an azole antifungal, and *CYP2C19* is the gene with a CPIC guideline for voriconazole dosing. Proton pump inhibitors are the other common exposure. Nothing here says to change a dose. It says the genotype is already in hand if a dose ever needs explaining.

### The limitation that applies to *CYP2D6* and is not optional

*CYP2D6* cannot be reliably star-called from short-read whole-genome sequencing. The gene sits beside the *CYP2D7* pseudogene, and whole-gene deletions, duplications and hybrid genes are common and are exactly what a variant-only VCF does not represent. The two variants found are consistent with one \*4 haplotype, which would make the child an intermediate metaboliser, **but copy number was not assessed and cannot be assessed from this file.** Any real report would use a dedicated caller. This row should be read as a flag, not a phenotype.

### *MTHFR*, found and deliberately not acted on

The child is homozygous for 677C>T. This is the single most over-interpreted result in consumer and clinical genetics. CPIC and ClinGen do not support *MTHFR*-guided methotrexate dosing, and the genotype is carried by roughly one European in ten. **It is listed here so that a reader who finds it elsewhere already knows this project found it and declined to build anything on it.**

## What is not carried, which is most of the clinical value

The negatives are stated as measurements, with the alleles tested named, rather than left implicit.

| Gene | Alleles tested | Result |
|---|---|---|
| *DPYD* | \*2A, \*13, c.2846A>T, HapB3 | **All absent.** No fluoropyrimidine dose reduction indicated |
| *TPMT* | \*2, \*3B, \*3C | **All absent** |
| *NUDT15* | \*3 | **Absent.** With *TPMT*, normal predicted thiopurine handling |
| *G6PD* | A- V68M, A- N126D, Mediterranean S188F | **All absent.** See the whole-gene check below |
| *F2* | prothrombin G20210A | **Absent** |
| *SLCO1B1* | \*5 | **Absent** |
| *CYP2C9* / *VKORC1* | \*2, \*3, -1639G>A | **All absent** |
| *RARG*, *SLC28A3*, *UGT1A6* | anthracycline cardiotoxicity risk alleles | **All absent** |

**G6PD, checked properly rather than by panel alone.** The child is male, so the X is hemizygous and any deficiency allele would be unopposed, which matters because G6PD deficiency is a contraindication to rasburicase. The whole gene carries **seven variants, all hemizygous, and only one falls in coding sequence**: chrX:154532439 A>G. gnomAD v4.1 puts that allele at **frequency 0.867 with 280,377 homozygotes**, and fails the site on its own InbreedingCoeff filter. An allele carried by 87 percent of people is not a deficiency allele; the reference genome simply carries the minor base here. **No G6PD deficiency allele is present.**

**Aminoglycoside ototoxicity, checked because febrile neutropenia invites aminoglycosides.** The mitochondrial alleles m.1555A>G and m.1494C>T are **both absent** at read depth 5,212. The only variant in that stretch is m.1438A>G, a common haplogroup marker. This is a clean negative at very high confidence, and it is the highest-depth measurement anywhere in this project.

## *UGT1A1* \*28 cannot be read from this file, and the family card said it could

`FAMILY_CARD.md` asks, as one of three questions worth putting to the specialist team:

> **Can the *UGT1A1* result be read from genetic testing already done, before any irinotecan is ever needed?**
> The sequencing is already done and paid for. This costs nothing to look up.

**For the allele that matters, that is wrong, and this scan is how it was found.**

*UGT1A1*\*28 is a TA dinucleotide repeat in the promoter TATA box at chr2:233760233. It is not a substitution, and short-read callers routinely fail on it.

| | |
|---|---|
| Records at chr2:233760233, any filter | **none** |
| Records at chr2:233759924, the \*80 proxy rs887829 | **none** |
| Nearest record before, any filter | 233,759,599 |
| Nearest record after, any filter | 233,763,429 |
| **Size of the no-call gap** | **3,830 bp** |
| Gaps this large in the surrounding 1 Mb | 15 of 1,751, **the top 0.9 percent** |

Absence of a call is not proof of absence of coverage, and without the aligned reads the two cannot be separated. But a 3,830 bp stretch with no record of any kind, spanning both the repeat and its proxy, in the top one percent of local gaps, in a region short reads are known to fail on, is not a basis for reporting \*1/\*1. **The honest answer is that \*28 status is undetermined, and reading it needs a targeted fragment-length assay, not a lookup.** \*6 (rs4148323) is separately absent, so that one allele is excluded.

The card has been corrected.

## Factor V Leiden, and the phenotype feature the report never addressed

**The measurement.** rs6025, chr1:169549811 C>T, heterozygous, 27 reference and 27 alternate reads, depth 54, GQ 99, QUAL 808.77. gnomAD v4.1 gives AF 0.0219 with 413 homozygotes. ClinVar carries it as an **expert-panel reviewed** record.

**Why the earlier screen missed it.** R7 required a Pathogenic or Likely_pathogenic assertion. ClinVar classifies Factor V Leiden as `drug_response`, not as pathogenic. It fell through a filter boundary, not through a data gap, and it was recovered by widening the same script to the drug-response class. Worth noting for anyone reusing R7: **a pathogenicity screen alone does not return the commonest inherited thrombophilia in Europeans.**

**What it means for the child.** Heterozygous Factor V Leiden raises venous thrombosis risk several-fold from a low baseline. It is carried by roughly one European in 25 to 50. **Heterozygosity alone is not an indication for prophylactic anticoagulation.** Where it can matter is around a central venous catheter, and a child treated for a solid tumour is likely to have had one. This is a fact worth being in the record if a thrombotic event ever occurs. It is not a reason to do anything now, and nothing here should change a line placement decision.

### The connection the report never made

`track2/anomalies/ANOMALIES.md` D2 measured that the supplied phenotype document lists **eight** features and the report names only some of them. Its exact finding for one of them:

> Recurrent spontaneous abortion HP:0200067 | "miscarriage" zero; "pregnancy loss" twice, both about published cohorts rather than this family

D2 concluded that resolving this needed "an edit, not a measurement". **There is a measurement.**

Factor V Leiden is an ancient founder allele and is effectively never de novo, so a heterozygous child inherited it from a parent. The supplied document records "Multiple pregnancy losses prior to the proband's birth, reported as maternal/parental history". ClinVar's own condition list for this allele includes "Pregnancy loss, recurrent, susceptibility to, 1".

**So the one variant in this genome with a recognised link to recurrent pregnancy loss is present, and the report never named the family's recurrent pregnancy loss at all.**

Now the reasons this is a question and not an answer, which are strong enough that it must not be presented as a finding.

1. **A better explanation is already in the diagnosis.** Both parents are obligate *BUB1B* carriers. One conception in four is compound heterozygous, and aneuploid conceptuses are an established cause of recurrent loss. This requires no new hypothesis at all.
2. **Parent of origin is unknown and unobtainable here.** If the father carries the allele, maternal placental thrombosis is not the mechanism. A single sample cannot say, parental samples are not in the dataset, and the standing rule of this project forbids recontact.
3. **The base rates make coincidence entirely plausible.** Factor V Leiden is carried by 2 to 5 percent of Europeans, and recurrent pregnancy loss affects 1 to 2 percent of couples. Co-occurrence in one family is unremarkable.
4. **Even if true, it changes nothing.** The association with recurrent loss is real in meta-analysis ([62 studies, 10,410 cases](https://pmc.ncbi.nlm.nih.gov/articles/PMC7313225/)), but the trials of the intervention it would imply are negative: SPIN and ALIFE2 show no benefit from low molecular weight heparin or aspirin in women with recurrent miscarriage and inherited thrombophilia, and a targeted evidence review found no study showing that testing improves outcomes ([Genetics in Medicine](https://www.nature.com/articles/gim0b013e31822e575b)). **An association that no intervention acts on is not a clinical finding.**

**Status: a question the data makes askable, recorded because D2 says this feature was never addressed, and explicitly not carried into any recommendation.** It cannot be resolved without parental genotypes, and obtaining those is outside what this project permits itself to do.

## What R8 changes

| | |
|---|---|
| Guideline-relevant genotypes found | One, *CYP2C19* \*2/\*17, recorded not acted on |
| Clinically recognised variants found | One, Factor V Leiden, recorded not acted on |
| Documents corrected | One. `FAMILY_CARD.md`, the *UGT1A1* question |
| Clean negatives established | *DPYD*, *TPMT*, *NUDT15*, *G6PD*, *F2*, *SLCO1B1*, *CYP2C9*, *VKORC1*, three anthracycline alleles, and both mitochondrial ototoxicity alleles |
| Phenotype features addressed that the report never named | One, and only as a question |
| Own errors found and recorded | Two, both of which produced confident wrong output |
| Recommendations added | **None** |

A screen that cannot tell "not carried" from "not looked at" reports the second as the first, without an error message. The first version of this one did.
