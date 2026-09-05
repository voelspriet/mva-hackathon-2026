# A grey-literature sweep, and why the earlier searches missed all of it

**Prompted by** the user pasting Google Scholar results the project had never seen. Scholar itself blocks automated access, so this sweep used OpenAlex, which indexes the same material: preprints, dissertations, conference abstracts and non-PubMed journals.

**The method gap it exposes.** Every earlier search in this project went through PubMed. PubMed does not index bioRxiv or medRxiv preprints, does not index dissertations, and indexes conference abstracts inconsistently. Roughly half of what follows was invisible to every search this project ran.

**The uncomfortable comparison.** This one sweep found more that bears on the report than both cross-model passes combined.

---

## Findings that change or could change the report

### 1. A control comparator for premature chromatid separation now exists, and the method decides the number

**Wang and colleagues, Front Endocrinol 2026;17:1838559, doi 10.3389/fendo.2026.1838559, open access.** Two unrelated families with unexplained recurrent pregnancy loss, two novel heterozygous *BUB1B* missense variants, and **20 healthy controls with no history of pregnancy loss**.

| Measure | Proband 1 | Proband 2 | 20 healthy controls |
|---|---|---|---|
| PCS by G-banding | 8.93 percent, 5 of 56 cells | 13.79 percent, 8 of 58 cells | **0.40 ± 1.05 percent**, range 0 to 4 |
| PCS by centromere-specific PNA-FISH | 18.58 percent, 21 of 113 | 24.43 percent, 32 of 131 | **2.95 ± 0.60 percent**, range 2 to 4, 100 cells per subject |

Both comparisons P < 0.001.

**Why this matters here.** The audit forced the withdrawal of an "under 2 percent in controls" figure because Kajii 2001, the paper it was attributed to, has no control group at all. A sourced comparator now exists. It also carries a methodological warning the report should not lose: **the control rate is 0.4 percent by G-banding and 3.0 percent by FISH**, so a gate that asks for a PCS karyotype must say which method, or the comparator is meaningless.

### 2. Heterozygous *BUB1B* carriers have a measurable phenotype, two codons from this child's allele

The same paper's variants are **c.2164T>C p.Trp722Arg** and **c.2215G>T p.Ala739Ser**. This child's null allele is p.Leu737Ter. The second variant sits **two codons away**. Both carriers showed elevated PCS and "a trend toward decreased BUBR1 protein abundance", and in one family the carrier father showed the same trend. The authors propose haploinsufficiency and argue heterozygous *BUB1B* variants contribute to sporadic recurrent pregnancy loss.

**Three consequences.** It supports the report's treatment of carrier parents as an intermediate phenotype rather than a normal reference. It bears on the phase calculation, which applies a likelihood ratio of 3 for parental recurrent miscarriage: that ratio now has published mechanism behind it rather than being an assumption. And it raises a question nobody asked, which is whether anything should be said to the carrier parents about reproductive risk.

### 3. An aneuploidy-selective vulnerability in human cells, which Track 2 concluded did not exist

**Genes Dev, doi 10.1101/gad.352512.124, "Aneuploidy generates enhanced nucleotide dependency and sensitivity to metabolic perturbation."** A genome-wide CRISPR knockout screen in isogenic aneuploid and diploid human mammary epithelial cells. Aneuploid cells show "an increased reliance on pyrimidine biosynthesis and mitochondrial oxidative phosphorylation genes". Diploid cells "switch seamlessly between pyrimidine synthesis and salvage"; cells with increased chromosomal content relying on salvage alone show "p53 activation and S-phase arrest", plus "increased sensitivity to DNA-damaging chemotherapeutics".

**Why this is consequential.** Section 7 removed metformin partly because the only aneuploidy-selective killing data were Tang 2011's mouse embryonic fibroblasts, with no human cell evidence. Here is human cell evidence, in a different pathway, with approved drugs against it: de novo pyrimidine synthesis is the target of the DHODH inhibitors leflunomide and teriflunomide, both marketed, teriflunomide with adolescent exposure in multiple sclerosis.

**Why it is not a recommendation, and the direction problem must be stated first.** This is a cancer-therapeutics paper: the vulnerability is a way to kill tumour cells with imbalanced karyotypes. In a child whose *normal* tissues carry mosaic aneuploidy, a drug that selectively stresses aneuploid cells may damage normal tissue rather than protect it, and the paper's own finding that these cells show increased sensitivity to DNA-damaging chemotherapy points the same way, toward a caution during rhabdomyosarcoma treatment rather than toward a repurposing candidate. It belongs in the ranked hypotheses or in section 9 as a question, with that direction problem named, and it needs the full text before anything is written.

### 4. A published MVA case caused partly by a variant outside the coding sequence

**Chinese J Med Genet 2025, doi 10.3760/cma.j.cn511374-20240716-00393:** two fetuses with MVA from "compound heterozygous variants in *BUB1B* **and its upstream regulatory elements**".

This bears directly on the re-analysis question P1, whether deep intronic or regulatory variants near *BUB1B* were discarded by a coding-only filter. There is now a published precedent for exactly that mechanism in this gene. The Track 1 pipeline filtered to coding sequence. That filter is now known to be capable of missing a real MVA allele.

### 5. The differential is wider than the report says

- **J Med Genet 2026, doi 10.1136/jmg-2025-111325:** mosaic variegated aneuploidy is a novel feature of **Mulibrey nanism**, from biallelic *TRIM37* variants, found in 7 to 36 percent of metaphases. Mulibrey nanism presents with prenatal growth failure, dysmorphism and tumour predisposition, which overlaps this child's presentation.
- **Diagnostics 2025;15:3022:** recessive *SMC5* variants in a family with near-tetraploidy and MVA, a milder phenotype than Atelis syndrome.
- **Neuropediatrics 2025, doi 10.1055/s-0045-1812138:** the first two patients with **biallelic *BUB1*** mutations, distinct from *BUB1B*, with reduced protein and kinase activity, prolonged mitosis and segregation errors. This is the abstract with the reduced phosphorylated H2A at threonine 120.
- **Orbit 2026, doi 10.1080/01676830.2026.2715719:** sequential Wilms tumour and orbital embryonal rhabdomyosarcoma in a child with MVA syndrome 3, the same tumour pair this child's syndrome predicts.

### 6. New primary sources on mechanism the report should have

- **Aging Cell 2025, doi 10.1111/acel.70160:** BubR1 insufficiency drives cardiac hypertrophy, fibrosis and senescence with transcriptomic disruption of ion channel regulation. This is directly relevant to gate item 6, the cardiac baseline and the ECG reading, and to the Baker 2011 cardiac argument.
- **Nat Commun 2026, doi 10.1038/s41467-026-70521-0:** proteostasis failure and mitochondrial dysfunction in a Drosophila MVA microcephaly model. Section 7 excluded chaperone inducers on a correction-versus-tolerance argument; a paper putting proteostasis failure into MVA pathogenesis deserves an answer in that paragraph.

---

## What was checked and is not relevant

Down syndrome metabolic models, chromosome 8 aneuploidy in teratomas, HORMAD1 in triple-negative breast cancer, BUB1 as an oncology biomarker, *TRIP13* in oocyte arrest, BUBR1 in neonatal hypoxic-ischaemic encephalopathy, plant polyploidy, and several bioinformatic tumour-marker papers that mention *BUB1B* only as a proliferation gene. Also checked from the user's own Scholar list and rejected: a systematic review that explicitly excludes mosaic cases, a groundnut tissue-culture thesis, and one indexing error pointing at a book on ancient Judaism.

## Correction applied now

Gate item 3 in `REPORT_track2.md` regains a sourced control comparator, with the G-banding and FISH figures given separately and the warning that the method decides the number. The rest is queued rather than written, because three of the six findings need full texts this project has not yet read.
