# G3. Residual BubR1: the dose-response scale, and where it breaks

**Question this file answers.** If a laboratory returned a number, "this child expresses X% of control BubR1", what would that number mean? Today nothing, because no published scale connects a residual percentage in a human patient to an expected phenotype. This file assembles the closest thing that can be built from published data, and marks every point where the assembly is held together by assumption rather than measurement.

Compiled 5 September 2026. Every quantitative claim below was pulled from the primary text of the cited paper (PMC full text or the publisher record) unless flagged otherwise. Conventions used throughout:

- **[SHOWN]**: a number or statement printed in the primary source.
- **[SHOWN, figure-only]**: the source says a value was quantified and displayed in a figure panel, but the numeric value does not appear in retrievable text.
- **[INFERRED]**: reasoning by me, not a published observation.
- **[NOT REPORTED]**: the source does not state it. Not estimated.

**The one-line answer, stated before the tables so it cannot be lost in them.** The scale can be built, but its two anchor points come from different species and different systems and they disagree with each other in the exact region where a patient measurement would land. A HeLa knockdown says ~13% residual BubR1 is functionally silent. A mouse hypomorph says ~10% residual BubR1 produces a lethal progeroid syndrome. Meanwhile the only human patients ever quantified sit at roughly 17-50% residual, above both thresholds, while being clinically affected. And the group that built the mouse allelic series concluded in print that **"BUBR1 levels do not closely track with phenotypic severity"** (Sieben 2020). A percentage alone is therefore a weak instrument, and this file's main product is a specification for what would have to accompany it.

---

## 0. The residue-numbering trap, stated first

Mouse BubR1 is 1,052 aa; human BUBR1 is 1,050 aa (UniProt O60566). The alignment offset in the C-lobe is +10.

- **Mouse residue 1002 corresponds to human residue 1012.** Sieben 2020 states it directly: "we mimicked the BUBR1 L1012P mutation in mice (*BubR1*^L1002P^)". **[SHOWN]**
- Therefore **BubR1^H/L1002P^ is a mouse model of human L1012P**, the Hanks 2004 / Suijkerbuijk 2010 MVA missense allele.
- The variant in the case at hand is **human p.(Asn1002Lys)**, in *human* numbering. Human N1002 is not mouse 1002 and is not L1012. **No mouse model of N1002K exists.** The numerical coincidence between "mouse 1002" and "human 1002" is a trap that will produce a wrong literature citation if not caught. **[SHOWN + INFERRED: the trap itself is my flag, the residue correspondence is Sieben's]**

Human N1002 lies inside the kinase/pseudokinase domain (766-1050), in the C-lobe, 10 residues N-terminal to the PLK1 site T1008, and 10 residues N-terminal to L1012. It has never been functionally tested.

---

## 1. THE ALLELIC SERIES (mouse)

### 1.1 Master table

All lifespans in days. Where a source gives weeks, the day conversion is given in brackets and marked as arithmetic, not as a published figure. Percentages are "residual BubR1 as % of wild type" only where the source states one.

| Genotype | BubR1 level (% of WT) | Median lifespan | Max lifespan | Growth | Fat / lipodystrophy | Sarcopenia | Cataract | Aneuploidy | Tumour | Cardiac | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **BubR1^+/+^** | 100 (definitional) | **691 d** (Sieben 2020 Fig 6F); **102 wk [=714 d]** (Wijshake 2012 Fig 2) | not stated numerically | normal | normal | normal | 50% affected at **116 wk** (Wijshake Fig 4A) | MEF baseline **9%** or **12%** depending on cohort (Wijshake Table S1) | spontaneous lymphoma/sarcoma with age; **100% DMBA tumour incidence** (Baker 2013 Fig 2a) | normal | Sieben 2020; Wijshake 2012; Baker 2013 |
| **BubR1^-/-^** (null) | **"0%"** | dies **before E3.5** | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Baker 2004 via Sieben 2020 |
| **BubR1^-/H^** | **"approximately 5%"** (Sieben 2020) / **"about 4%"** (Wijshake 2012), *same lab, two numbers for the same genotype* | dies **postnatal day 1**, respiratory failure | n/a | severe | n/a | n/a | n/a | MEF **72%** aneuploid | not assessable | n/a | Baker 2004 via Sieben 2020, Wijshake 2012 |
| **BubR1^H/X753^** | not stated as a %; "not significantly different" from H/L1002P in MEFs (Suppl Fig 8A); "similar reduction" to -/H | dies **within 18 h of birth** | n/a | failure to thrive | n/a | n/a | n/a | MEF **65%** aneuploid; **nearly all** MEFs whole-chromosome aneuploid by single-cell DNA-seq; highest missegregation rate of the three biallelic models | not assessable | n/a | Sieben 2020 |
| **BubR1^H/H^** | **"approximately 10%"** (Sieben 2020). *A value of ~11% also circulates in the secondary literature; ~10% is what the primary-lab text says.* | **196 d** (Sieben Fig 6F); **30 wk [=210 d]** (Wijshake Fig 2); **~20 wk** implied in Baker 2008, *three values from one lab* | not stated numerically | cachectic dwarfism, growth retardation, facial dysmorphism | lipodystrophy, subdermal fat loss | grip strength ↓, fibre atrophy, work output ↓; **kyphosis median onset 175 d** | yes, accelerated; median onset **[NOT VERIFIED in retrieved text]** | MEF ~equal to H/L1002P (about half of MEFs aneuploid by scDNA-seq); mitotic **splenocytes 15%** aneuploid | **highly DMBA-susceptible**, but "**do not live long enough to assess predisposition to spontaneous tumors**" | reduced cardiac stress tolerance; cardiac failure is the presumed cause of death | Baker 2004; Baker 2008; Baker 2011; Wijshake 2012; Sieben 2020 |
| **BubR1^H/L1002P^** (models human **X753/L1012P**) | not significantly different from H/H in MEFs or in most tissues; **only the spleen differed significantly** (Fig 6E) | **343 d** (P<0.05 vs H/H) | not stated numerically | growth retarded, but **less severely than H/H** | lipodystrophy, **similar severity to H/H** | muscle wasting **milder than H/H**; **kyphosis median onset 238 d** (P<0.001 vs H/H) | cataractogenesis, **similar severity to H/H** | MEF ≈ H/H; mitotic **splenocytes 38%**, 2.5× the H/H rate despite the same protein level | carcinogen-induced susceptibility **similar to H/H** | cardiac stress sensitivity **milder than H/H** | Sieben 2020 |
| **BubR1^X753/L1002P^** (models the human patient) | [NOT REPORTED] | **embryonic lethal**, 0 of 388 newborns, 0 of 39 at E13.5, viable at E3.5 | n/a | n/a | n/a | n/a | n/a | presumed extensive | n/a | n/a | Sieben 2020 |
| **BubR1^+/-^** | not stated as a %; **lower** than +/L1002P in MEFs and testis (P significant) | **90 wk [=630 d]** vs 102 wk WT, "modest but significant" | **no significant reduction** | normal | normal | normal | normal | MEF modestly ↑; mitotic **splenocytes 2%** | spontaneous incidence and spectrum WT-like but **significantly reduced latency**; DMBA lung tumour **multiplicity and size ↑**, incidence not ↑ | normal | Wijshake 2012 Fig 7; Sieben 2020 |
| **BubR1^+/X753^** = **BubR1^+/GTTA^** *(the same 2211insGTTA allele, renamed between the 2012 and 2020 papers)* | truncated product **undetectable even on long exposure**; residual WT protein **similar to +/-** | **93 wk [=651 d]** vs 102 wk WT, P significant | **significantly reduced** | normal | fat loss, accelerated | muscle wasting, impaired exercise, lordokyphosis, **appearing in the second year of life** | 50% affected at **101 wk** vs 116 wk WT | MEF aneuploidy **+6 percentage points** over a 12% WT baseline; **PCS elevated** (unlike +/-); mitotic **splenocytes 18%** | **not** spontaneously tumour-prone; DMBA incidence and multiplicity "very similar" (n=19 vs 20), **tumour size increased** (P<0.01) | no cardiac abnormality detected (Fig S2) | Wijshake 2012; Sieben 2020 |
| **BubR1^+/L1002P^** | **"markedly reduced"**, but **significantly higher** than +/- and +/X753 in MEFs and testis, i.e. the L1002P allele yields *some* protein, the truncating alleles yield none. Numeric value **[SHOWN, figure-only]** (Fig 1B, +/+ normalised to 1) | reduced, **P = 0.0516** (strong trend, not significant) | [NOT REPORTED] | normal | normal | normal | normal | MEF markedly ↑; **PCS elevated**; mitotic **splenocytes 28%**, the highest of the three heterozygotes, despite having the *highest* protein level of the three | spontaneous spectrum WT-like but **reduced latency**; lymphomas have significantly **increased mitotic index**; DMBA lung tumour **size ↑** | [NOT REPORTED] | Sieben 2020 |
| **BubR1^H/+^** | [NOT REPORTED in any source I could retrieve] | [NOT REPORTED] | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | strain used in Sieben 2020 intercrosses; no phenotype panel published there |
| **BubR1^L/L^** (independent "Tmats" hypomorph) | [NOT REPORTED in Sieben's text] | [NOT REPORTED] | n/a | n/a | **absent** | n/a | **absent** | n/a | n/a | n/a | cited in Sieben 2020 as ref 36: this hypomorph shows **none** of the overt progeroid features (kyphosis, lipodystrophy, cataract) of H/H |

### 1.2 The crosses

| Cross | BubR1 background | Effect | Source |
|---|---|---|---|
| **p16^Ink4a^ -/-** | H/H | Attenuates senescence and premature ageing in skeletal muscle and fat. Atrophic fibres reduced ~3-fold; lordokyphosis median onset ~3-fold longer; adipose substantially preserved; cataract latency modestly but significantly delayed. Reported median-lifespan extension **~25%**; the absolute week values (20 → 25 wk) were **derived, not printed**, treat as unverified. | Baker 2008 |
| **p19^Arf^ -/-** | H/H | **Worsens** everything: significantly smaller gastrocnemius fibres at 6 wk (P<0.0001), accelerated fat depletion, accelerated cataract (P<0.0001) and lordokyphosis. | Baker 2008 |
| **INK-ATTAC + AP20187** (senescent-cell suicide) | H/H | Fat mass preserved, adipocyte size ↑, muscle fibre diameter ↑, treadmill distance ↑, cataract and lordokyphosis onset substantially delayed. **Overall survival "not substantially extended."** Authors attribute this to p16-independent pathologies, cardiac arrhythmia, arterial stiffening, persisting. Cardiac failure presumed cause of death. | Baker 2011 |
| **SIRT2 transgene** | H/H | **+58% median and +21% maximal lifespan** vs H/H (n=31 vs 33, P=0.0384); **+123% median in males**, no change in females; ECG J-point defect reversed. Dwarfism, lordokyphosis, cataract **not** reversed. Contradicted for the general lifespan claim by Wu 2023 (SIRT2 overexpression did not extend lifespan). | North 2014; Wu 2023 |
| **NMN** | *not* H/H, young and 30-month C57BL/6 | 500 mg/kg/d IP × 7 d raised NAD+ in heart and testis and raised BubR1 protein in testis. **Never given to BubR1^H/H^ mice.** No lifespan or healthspan data. | North 2014 |
| **BubR1 overexpression transgene, line T23** | WT background (and rescues H/H) | Verbatim: "BubR1 protein levels in T23 MEFs were about 2-fold higher than in T7 MEFs and **10-fold higher than in wildtype MEFs**", mitotic MEF extracts, actin loading control. Median **and** maximum lifespan extended (max: P=0.05 vs WT, P=0.0056 vs T-GFP, one-sided Wang-Allison). **Only 33% of T23 developed DMBA tumours vs 100% of wild type.** Ras-induced and age-related aneuploidy suppressed. Mitotic checkpoint and attachment-error correction reinforced. Both Flag-BubR1 transgenes **correct the growth retardation and ageing phenotypes of BubR1^H/H^ mice**. Numeric median/max lifespan values **[NOT REPORTED]**, the paper gives survival curves and P values, no numbers. | Baker 2013 |
| **BubR1 overexpression transgene, line T7** | WT background | ~half of T23's level. **No significant tumour protection**, "tumor protection requires a threshold of BubR1 overexpression." | Baker 2013 |

### 1.3 What the mouse series actually establishes

**[SHOWN]** Sieben 2020's own summary threshold scheme, verbatim: *"A reduction of approximately 40%-90% in BUBR1 protein levels results in tumor predisposition or mild premature-aging phenotypes, whereas a reduction of greater than 90% results in progeroid phenotypes or early postnatal lethality."*

Restated as residual: **10-60% residual → tumour predisposition or mild premature ageing. Below 10% residual → progeroid syndrome or perinatal death.**

**[SHOWN]** The same paragraph immediately disowns a simple dose model: *"although BUBR1 levels do not closely track with phenotypic severity, this study identifies several critical BUBR1 thresholds in vivo"*, and notes that **BubR1^X753/L1002P^ does not fit the scheme at all.**

Three findings inside the series that a percentage scale cannot accommodate:

1. **H/H and H/L1002P have statistically indistinguishable BubR1 levels in MEFs and in every tissue except spleen, yet differ by 147 days of median lifespan** (196 vs 343), by 63 days of kyphosis onset, and in growth, cardiac stress tolerance and muscle wasting. Sieben's explanation: in H/L1002P the residual pool is a *mixture* of wild-type and L1002P protein, whereas in H/H it is wild-type protein only. Identity of the residual protein, not its quantity.
2. **+/L1002P has a higher BubR1 level than +/- and +/X753, and the worst splenocyte aneuploidy of the three** (28% vs 2% and 18%). The rank order of protein level and the rank order of aneuploidy are inverted.
3. **The human patient with BUBR1 X753/L1012P lived 3.6 months after birth. The mouse with the equivalent genotype dies before E13.5.** The species do not tolerate the same genotype, so any mouse-derived percentage threshold transferred to a human is transferred across a demonstrated tolerance gap in the wrong direction. **[SHOWN, Sieben 2020 states both facts and calls the mouse model "unattainable"]**

---

## 2. THE HUMAN SIDE, every quantitative BubR1 statement

### 2.1 The table

| Statement | Value | System | Patient or engineered? | Denominator | Source |
|---|---|---|---|---|---|
| Full-length substitution-mutant BUBR1 in patient lines | **"decreased 2-6 fold"** | EBV-transformed lymphoblastoid + SV40-transformed fibroblast lines from four patients: **absent/I909T, 386X/R727C, 753X/R814H, 731X/Y155C** | **Patient-derived, but immortalised** | band intensity BUBR1/Tubulin **relative to healthy control cells**; average of **4** experiments (LCL) or **5** (fibroblast) | Suijkerbuijk 2010, Fig 2A |
| Truncated proteins (386X, 731X, 753X) | **not detectable** in patient or parental lysates; the antibodies used *can* see truncations when they are overexpressed in HeLa, so this is a real absence, not an epitope artefact | same lines | **Patient** | same blot | Suijkerbuijk 2010, Fig 2A |
| Carrier parent lines (one mutant allele) | **"consistently in between those of patients and unrelated healthy controls"**, no number given | parental LCL/fibroblast | **Patient family** | same blot | Suijkerbuijk 2010, Fig 2A |
| Positional gradient | BUBR1 reduction **most severe** for kinase-domain mutations, **less** for the N-terminal TPR mutation (Y155C) | same lines | **Patient** | same blot | Suijkerbuijk 2010, Fig 2A |
| Transfected LAP-BUBR1 kinase-domain mutants (I909T, R727C, L844F, L1012P and others) | **"5-10 fold decrease"** vs wild-type BUBR1 | **HeLa and U2OS** | **Engineered** | band intensity BUBR1/Tubulin relative to wild type; average of ≥3 experiments | Suijkerbuijk 2010, Fig 2D |
| Y155C and R550Q (outside kinase domain) | **no effect on protein level** | HeLa/U2OS | Engineered | as above | Suijkerbuijk 2010, Fig 2D |
| Q921H (inside kinase domain) | **indistinguishable from wild type** on level *and* function | HeLa/U2OS | Engineered | as above | Suijkerbuijk 2010 |
| **Doxycycline shRNA titration, the source of the circulating thresholds** | **"saturating amounts of doxycycline reduced BUBR1 protein to ~6% and caused chromosome mis-segregation in the majority of cells, low amounts of doxycycline, while still significantly reducing BUBR1 levels to ~13%, had virtually no impact on the fidelity of chromosome segregation"** | **HeLa** cell line stably carrying inducible anti-BUBR1 shRNA, plus H2B-EYFP | **ENGINEERED, no patient material** | BUBR1/Tubulin **relative to untreated control of the same line**; average of 3 experiments; **doses were 0, 1 and 1000 ng/ml, a three-point curve with one point at zero knockdown** | Suijkerbuijk 2010, Fig 4D lower |
| Turnover of I909T and R727C | **~2-fold increased** (5 h cycloheximide); HSP90-dependent, proteasome-mediated | patient LCL | **Patient** | CHX-treated vs untreated, same line, average of 3 | Suijkerbuijk 2010, Fig 3B |
| Mitotic exit under STLC | 50% of cells exited within **68 min** (753X/R814H) and **114 min** (731X/Y155C) | patient fibroblasts | **Patient** | n/a | Suijkerbuijk 2010, Fig 1B |
| Chromosome misalignment | **2-3 fold increase** vs control lines | patient fibroblasts + MG132 | **Patient** | n/a | Suijkerbuijk 2010, Fig 1C |
| Rescue | transient LAP-BUBR1 gave a **2-fold increase** in nocodazole response in patient cells; forced overexpression of I909T and L1012P to wild-type levels **fully restored** the nocodazole response | patient fibroblasts / HeLa | Patient + engineered | n/a | Suijkerbuijk 2010, Fig 1D and 4D upper |
| Matsuura's threshold statement | **">50% decrease in expression (or activity) of BubR1 is involved in the PCS syndrome"**, a conclusion, not a measurement; the paper reports "reduced protein expression", "a modest decrease" of transcript, and diminished kinetochore localisation, with **no percentage** | patient cells, 7 Japanese PCS families | **Patient** | qualitative western + RT-PCR | Matsuura 2006 |
| Hanks 2004 | **contains no western blot.** No residual-protein claim may be attributed to it. | n/a | n/a | n/a | Hanks 2004 |
| Premature chromatid separation (a proxy, not a protein level) | **48.5-83.2%** of lymphocytes in two karyotyped infants; **3.5-41.7%** in carrier parents | patient and parent lymphocytes | **Patient** | % of scored metaphases | Kajii 2001 |

### 2.2 The three things this table means

**(a) There is no published percentage for any MVA patient.** Every human number is either a fold-change against an unspecified control set, or a qualitative statement. Converting "2-6 fold decrease" to "17-50% residual" is arithmetic I am doing, not a published figure. **[INFERRED]**

**(b) The thresholds in circulation, ~6% and ~13%, are HeLa numbers.** They come from a doxycycline titration of an shRNA in a hypotriploid cervical carcinoma line, measured against that same line's untreated state, over an acute time course, at **three doxycycline doses of which one is zero**. There is no measurement anywhere between 6% and 13%, and none between 13% and 100%. The "threshold" is a two-point discrimination with nothing in the gap. **[SHOWN, the dose list and replicate count are in the figure legend]**

**(c) Even the "patient cells" are immortalised.** The lymphoblastoid lines are EBV-transformed and the fibroblasts SV40-transformed (stated in Suijkerbuijk 2010 Methods). Immortalisation selects on proliferation, and BubR1 abundance is proliferation-coupled. A number from an EBV-LCL is not a number from the child's tissue. **[SHOWN that the lines are transformed; the selection concern is INFERRED]**

---

## 3. THE MAPPING, with its error bars

### 3.1 The step function

Read as: residual BubR1 as % of a matched control → expected phenotype → what holds it up.

| Residual | Expected phenotype | Evidence | How thin |
|---|---|---|---|
| **0%** | Pre-implantation lethality | Mouse *BubR1^-/-^* dies before E3.5 | One species, one paper. No human null homozygote exists or could. |
| **~4-5%** | Perinatal lethality (respiratory failure); MEF aneuploidy 65-72% | Mouse *BubR1^-/H^* and *BubR1^H/X753^* | Two mouse genotypes, one lab. The **same lab prints 4% and 5% for the same genotype in two papers**, which is the size of the disagreement at the steepest part of the curve. |
| **~6%** | Chromosome mis-segregation in the **majority** of cells | **HeLa shRNA at saturating doxycycline** | One cell line, one paper, acute knockdown, 3 replicates, ≥350 cells. Not a patient, not a primary cell, not a developmental time course. |
| **~10%** | Viable but severe: cachectic dwarfism, lipodystrophy, sarcopenia, cataract, kyphosis at 175 d, cardiac failure, median lifespan 196-210 d, carcinogen-hypersensitive | Mouse *BubR1^H/H^* | Best-characterised point on the whole curve, but it is a mouse, and its own lab has printed three different median lifespans for it (196 d, 30 wk, ~20 wk implied). |
| **~13%** | **"virtually no impact on the fidelity of chromosome segregation"** | **HeLa shRNA at 1 ng/ml doxycycline** | Same three-point titration. **This is the single most consequential number in the field and it rests on one dose of one drug in one immortal line.** |
| **17-50%** *(= the "2-6 fold decrease")* | **This is where actual MVA patients were measured.** Impaired SAC, premature mitotic exit (68-114 min under STLC), 2-3× misalignment, MVA syndrome, ~37% cancer rate | Suijkerbuijk 2010, four patient lines | Fold-changes only, no percentages; immortalised lines; control set size not stated. |
| **~50%** | Obligate carriers. Mouse: median lifespan 90-93 wk vs 102 wk, mild aneuploidy, reduced tumour latency, second-year sarcopenia/lipodystrophy/cataract in the +/X753 allele only. Human: carrier parents show PCS in 3.5-41.7% of lymphocytes and "mild mitotic defects", and are clinically unaffected in childhood | Wijshake 2012; Sieben 2020; Kajii 2001; Suijkerbuijk 2010 | Reasonable. But **which** 50% matters: mouse +/L1002P has a *higher* level than +/- and *worse* aneuploidy. |
| **60-100%** | Normal, per Sieben's scheme (a 40% reduction is the top of the "tumour predisposition or mild premature ageing" band) | Sieben 2020 discussion | A summary sentence over the paper's own allelic series, not an independent measurement. |
| **~200%** (T7) | No tumour protection | Baker 2013 | One transgenic line. |
| **~1000%** (T23) | Protective: median and max lifespan extended, DMBA tumours 33% vs 100%, Ras- and age-related aneuploidy suppressed, **rescues BubR1^H/H^** | Baker 2013 | The upper arm of the curve is real but the level (10× WT in mitotic MEFs) is far outside anything achievable pharmacologically. |

### 3.2 The region where the answer would change management, and how wide it is

**The decision region is 5% to 20% residual.** Everything above ~25% is already occupied by patients who are demonstrably affected, so a value there confirms nothing new. Everything below ~4% is incompatible with a living child, by the mouse data. The whole interpretive action is in the ~15-percentage-point band between them.

**The width of the uncertainty in that band is a factor of at least two, and arguably the band is not resolvable at all.** Concretely:

- The HeLa titration puts the functional cliff **between 6% and 13%** with nothing measured in between. **[SHOWN]**
- The mouse puts a severe, lethal phenotype **at 10%** and perinatal lethality **at 4-5%**. **[SHOWN]**
- These two do not agree. **A HeLa cell at 13% is fine. A mouse at 10% is dying of a progeroid syndrome by seven months.** Three percentage points cannot be the whole difference; the systems differ in what they are asked to do (one cell division vs an organism's development and lifespan). **[INFERRED that the discrepancy is systemic rather than a measurement error, but the discrepancy itself is SHOWN]**
- Therefore the honest error bar on "the threshold" is not ±2%. It is: **the threshold is somewhere between 4% and 20%, its position depends on cell type, proliferation rate and duration of exposure, and it may not be a single number.**

**And there is a fourth problem that makes the band worse, not better.** The measured patients sit at 17-50% residual, *above* the HeLa "tolerated" 13% and *above* the mouse H/H 10%, and are nevertheless severely affected. Suijkerbuijk's own framing is that patient defects are caused by low BUBR1 abundance, and they showed that forcing I909T and L1012P back up to wild-type levels fully restores checkpoint function, which supports it. But the arithmetic does not close: a patient at 17-50% should, by the HeLa scale, be segregating chromosomes normally. Candidate resolutions, all **[INFERRED]**:

1. The immortalised patient lines have been selected for higher BubR1 than the child's tissues carry.
2. Chronic lifelong insufficiency is not equivalent to a 72-hour knockdown; aneuploidy is cumulative.
3. The relevant denominator is not total protein but functional protein at unattached kinetochores, where Suijkerbuijk showed patient cells are additionally depleted.
4. The "fold-change vs healthy control" and the "% of untreated same line" denominators are not the same quantity and should never have been placed on one axis, which is the argument this whole file is making.

**None of these has been tested.** Until one is, the region 5-20% is where a returned number would change the hypothesis, and it is exactly the region where the published evidence is a two-point curve in a cervical carcinoma line.

---

## 4. WHAT A MEASUREMENT WOULD AND WOULD NOT SETTLE

Assume a lab returns "this child has X% of control BubR1", with the assay caveats of section 5 satisfied.

### X = 5%

- **Survives:** the severe-depletion model. Places the child below the mouse H/H level and at the HeLa mis-segregation level. Predicts high aneuploidy, and by the mouse data predicts progeroid pathology and cardiac involvement as the dominant long-run risks.
- **Excluded:** nothing therapeutic. There is no drug that raises BubR1 in a patient. SIRT2 and NMN raised BubR1 in mice, NMN was **never given to BubR1^H/H^ mice** and produced no lifespan or healthspan data anywhere.
- **Diagnosis:** strongly consistent. Does not confirm which allele causes what.
- **Management change, real:** it strengthens the argument for avoiding taxanes and spindle poisons if chemotherapy is ever needed, because the Janssen 2009 sensitisation was produced by *partial* BubR1 reduction. But that argument comes from engineered tumour cells, and **no study has shown MVA patient cells are taxane-hypersensitive.**
- **Surprise flag:** 5% is below every living mouse except H/H. If a child is at 5% and clinically stable, that is itself a finding about human tolerance exceeding mouse tolerance, which Sieben already documented for X753/L1012P.

### X = 15%

- **Survives:** essentially every hypothesis. This is the worst possible answer, because it lands in the exact gap between the HeLa 13% ("no impact") and the mouse 10% (lethal progeroid). **It discriminates nothing.**
- **Excluded:** nothing.
- **Diagnosis:** unchanged.
- **What it would actually do:** demonstrate that the published scale is unusable at the value that matters. That is a legitimate result but not a clinical one.

### X = 30%

- **Survives:** the "patients sit at 17-50%" observation, i.e. the child is where the four measured MVA patients were. Consistent with biallelic MVA.
- **Excluded:** the strong form of "MVA is caused by dropping below the ~6-13% mis-segregation threshold". At 30% that threshold is not being crossed, so either the threshold is wrong for primary human tissue or the mechanism is not pure abundance.
- **Diagnosis:** consistent, and it puts the case squarely in Suijkerbuijk's "low abundance" class rather than his "specific functional defect" class, **provided** the residual protein is functional. If N1002K is a *specific-defect* allele like Q921H (normal level, but Q921H was also normal in function) or like a hypothetical stable-but-broken variant, a normal-ish level would be actively misleading.
- **This is the value at which the measurement most changes hypothesis choice**, because it forces the question: is the residual 30% wild-type-equivalent protein, or 30% of a protein that folds but does not work?

### X = 50%

- **Survives:** the carrier-equivalent model. 50% is what an obligate heterozygote should show.
- **Excluded / reopened:** **the diagnosis comes back into question.** A biallelic patient with one NMD'd nonsense allele and one destabilising missense allele should not be at carrier level. Either (i) c.2210T>G is not escaping NMD as predicted and is instead producing stable protein, (ii) p.(Asn1002Lys) does not destabilise, which is entirely possible, since Q921H sits inside the same domain and behaved exactly like wild type, or (iii) the phenotype is not driven by BubR1 abundance at all, and the differential is *TRIP13*, *CEP57*, or an unrelated cause. Yost 2017's stratification becomes relevant: biallelic *BUB1B* and *TRIP13* cells show **severe** SAC impairment, *CEP57* minimal.
- **Action:** a functional SAC assay (nocodazole/STLC mitotic-arrest duration, PCS scoring) becomes more informative than any further protein quantification.

### X = 80%

- **Survives:** almost nothing on the abundance axis. By Sieben's scheme a 20% reduction is inside the normal band.
- **Excluded:** the destabilisation hypothesis for p.(Asn1002Lys). It would join Q921H, Y155C and R550Q as a level-neutral variant.
- **Diagnosis:** genuinely in question. Either the nonsense allele is not doing what the 50-55 nt NMD rule predicts, or the variant interpretation needs revisiting, or BubR1 abundance is not this child's lesion.
- **Where the hypothesis goes:** to function, not quantity. A level-neutral kinase-domain variant that is pathogenic would have to act through the domain's **non-catalytic** role, KARD phosphorylation and PP2A-B56 recruitment (Gama Braga 2020), which is a testable and completely different mechanism, and one that no abundance measurement can see.

### What no protein level can settle, at any X

1. **Whether the deficit is transcript-level or fold-level.** A blot returns one number for a pool made from two alleles. It cannot say whether the missing protein is missing because the mRNA was degraded (NMD of L737X) or because the protein was made and destroyed (turnover of N1002K). These have different implications: a transcript-level deficit is in principle addressable by NMD modulation; a fold-level deficit is a chaperone/proteasome problem, and Suijkerbuijk showed the MVA missense turnover is **HSP90-dependent and proteasome-mediated**, which is a different intervention space entirely. **Required alongside: allele-specific expression measurement**, allelic ratio by RNA-seq or allele-specific RT-qPCR across the c.2210 and c.3006 sites, ± a translation-inhibition arm (puromycin/cycloheximide) to demonstrate NMD, plus a cycloheximide-chase and MG132 arm on the protein as Suijkerbuijk ran (5 h CHX, ~2-fold turnover increase for I909T and R727C).
2. **Whether the residual protein works.** Sieben's H/H vs H/L1002P comparison is the proof of this: **same level, different disease.** A number cannot distinguish a pool of pure wild-type protein from a mixture containing a folded-but-impaired variant.
3. **Where the protein is.** Matsuura 2006 and Suijkerbuijk 2010 both found reduced BubR1 *at kinetochores* and, in Matsuura's case, abolished CDC20 kinetochore association despite normal CDC20 expression. Total cellular abundance and kinetochore-loaded abundance are different quantities and the second is the functional one.
4. **Tissue heterogeneity.** BubR1 is only meaningfully expressed in proliferative tissue (Sieben blotted testis, thymus, spleen for exactly this reason). A number from blood says little about kidney, muscle or lens.
5. **Cancer risk.** No source reports a per-genotype tumour fraction in MVA, and the mouse data say reduced BubR1 changes tumour **latency, multiplicity and size** more than **initiation**. A percentage will not produce a surveillance recommendation that Nakano 2024's genotype-based consensus does not already give.

---

## 5. THE METHOD PROBLEM

Quantitative immunoblots are not comparable across labs. Below is what the assay would need, and then the honest verdict on whether any published MVA study reported enough to be reproduced.

### 5.1 What the assay needs

**Control cells.** The single biggest failure mode is comparing unlike cells. BubR1 abundance is cell-cycle coupled and peaks in mitosis, so any difference in proliferative fraction between patient and control reads out as a difference in BubR1.
- Same cell type, same source, same handling. If the patient sample is a primary dermal fibroblast, the controls must be primary dermal fibroblasts, not LCLs and not an immortalised line.
- Same passage range and same confluence at harvest. Sieben used passage-5 MEFs throughout for this reason.
- **Minimum three, preferably five or more, unrelated healthy donors**, age-matched where possible. Suijkerbuijk's Fig 2A is expressed "relative to healthy control cells" and **the number of control individuals is not stated in the retrievable text**, that alone makes the 2-6 fold uninterpretable as a percentage.
- **Both parents.** This is the strongest available internal anchor and it costs nothing extra. Obligate heterozygotes should sit near 50%, and Suijkerbuijk showed carrier parent lines fall "consistently in between" patient and control. A parental pair converts an uncalibrated blot into a three-point standard: 100% (controls), ~50% (parents), X% (child). **[INFERRED as a design recommendation; the parental intermediacy is SHOWN]**
- **A proliferation covariate on the same blot**: phospho-histone H3 Ser10 as a mitotic-index marker, as Wijshake ran. Without it, a 30% difference in cycling fraction is indistinguishable from a 30% difference in BubR1.

**Loading control.** The published practice, and what to copy:
- Sieben 2020 used **two independent loading controls in parallel**, α-tubulin (Cell Signaling 2125) *and* total protein by Ponceau S, and normalised to either.
- Wijshake 2012 used β-actin plus Ponceau S.
- Suijkerbuijk 2010 used **tubulin only**.
- **Recommendation:** total-protein normalisation (Ponceau or stain-free) as primary, with a single-protein control as a secondary check. Tubulin and actin are themselves proliferation- and cell-type-sensitive, which is the failure mode you are trying to avoid.

**A standard curve.** No recombinant BubR1 standard is used in any of these papers, and none exists as a shared reagent.
- **The closest published design, and the one to copy, is Wijshake 2012 Supplementary Figure S1**: serially dilute wild-type lysate, load a graded percentage series, blot for BubR1 with actin as loading control, plot mean signal from **three independent wild-type lines** against percentage of lysate loaded, fit the curve, then read the unknowns off it. This is the only method in the MVA/BubR1 literature that produces a defensible *percentage* rather than a fold-change, and it is buried in a supplementary figure of a mouse paper.
- **A recombinant full-length human BUBR1 calibrant would have to be made.** It does not exist as a standard. Suijkerbuijk 2012 produced recombinant BUBR1 for thermal-denaturation work (recombinant K795A denatured at 34.7 °C vs 39.1 °C wild type), so the protein is expressible, but nothing in this literature is offered as a quantitative standard.
- **Dynamic range matters here more than usual.** A scale that must distinguish 5% from 15% from 30% spans a 6-fold range against a 100% control, a 20-fold span overall. ECL on film is not linear over that. Fluorescent secondary detection with a demonstrated linear range, or the dilution series itself, is required. Without a demonstrated linear range, "5%" and "15%" are the same measurement.

**Antibody and epitope.** For this case specifically: the anti-BubR1 antibody's epitope must be mapped relative to **residue 737**. If the epitope is C-terminal to 737, the assay is structurally incapable of detecting any product from the L737X allele, and a "no truncated protein" result would be an artefact. Suijkerbuijk explicitly addressed this, *"Antibodies can recognize truncated proteins if overexpressed in HeLa"*, and that control must be repeated with whatever antibody is used. Sieben used **BD Transduction 612503** (mouse anti-BUBR1, 1:1000); Wijshake used "BubR1 (BD)" without a catalogue number.

**Quantification software and replicate structure.** Sieben: ImageJ, normalised to α-tubulin or Ponceau, minimum three independent MEF lines. Suijkerbuijk: 4 experiments (LCL), 5 (fibroblast), ≥3 (transfections). A patient measurement should state both the number of biological replicates (independent cultures/harvests) and technical replicates, and report individual points, not only a mean.

**The cross-lab-comparable alternative.** Immunoblot densitometry is inherently relative. **Targeted mass spectrometry (PRM/SRM) with heavy-isotope-labelled BUBR1 peptide standards** would give absolute copy number per cell and would be portable between labs without shared lysates. **No such measurement of BUBR1 exists in any MVA paper reviewed here.** **[INFERRED as a proposal, the absence is SHOWN]**

### 5.2 Has any published MVA study reported its quantification well enough to reproduce?

**No. And the specific failure is where it hurts most.**

| Study | Antibody named | Catalogue no. | Loading control | Detection chemistry stated | Linear range shown | Standard curve | Control n stated | Reproducible from text? |
|---|---|---|---|---|---|---|---|---|
| **Sieben 2020** (mouse) | yes (BD Transduction anti-BUBR1) | **yes, 612503** | α-tubulin (CST 2125) **and** Ponceau S | no | no | no | ≥3 MEF lines | **Closest to reproducible.** Antibody, loading controls, ImageJ, replicate structure all stated. Missing: detection chemistry and linearity. |
| **Wijshake 2012** (mouse) | yes ("BubR1 (BD)") | no | β-actin + Ponceau S | no | **implied by the dilution series** | **yes, serial dilution of wild-type lysate, Fig S1** | 3 wild-type lines | **The only published design that yields a percentage.** Reproducible in concept; the antibody clone is under-specified. |
| **Suijkerbuijk 2010** (the human data) | **not stated in retrievable text** | no | tubulin | no | no | no | **not stated** | **No.** The paper that supplies every human number, the 2-6 fold patient reductions, the 5-10 fold mutant reductions, and the ~6%/~13% thresholds that the whole field quotes, does not, in its retrievable text, name the anti-BUBR1 antibody, the detection system, or how many healthy controls the "relative to healthy control cells" denominator represents. |
| **Matsuura 2006** | n/a | n/a | n/a | n/a | n/a | n/a | n/a | **No.** Reports "reduced protein expression" and a "modest decrease" of transcript, with no quantification. Its ">50% decrease" is a conclusion, not a measurement. |
| **Hanks 2004** | n/a | n/a | n/a | n/a | n/a | n/a | n/a | **N/A, contains no western blot at all.** |
| **Baker 2004** | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Not retrievable (paywalled). The ~10% H/H figure reaches us only via the same lab's later papers, where it appears as "approximately 10%" (Sieben) and the -/H figure as both "about 4%" (Wijshake) and "approximately 5%" (Sieben). |

**The verdict in one sentence.** The mouse papers report their quantification well enough to copy; the human paper does not; and the two thresholds that everyone quotes for human MVA come from a three-dose doxycycline titration in HeLa, in a paper whose antibody and control-set size are not stated in its own text.

---

## 6. What to actually do with this

**[INFERRED throughout this section, it is a recommendation, not a finding.]**

A residual-BubR1 percentage on its own is a weak instrument, for the reasons above. It becomes a strong one only as part of a three-part measurement:

1. **Quantitative immunoblot** on primary patient cells, against ≥3 matched primary controls **and both parents**, on a serial-dilution standard curve of pooled control lysate (Wijshake Fig S1 design), with total-protein normalisation and a pH3 mitotic-index covariate, with the antibody epitope mapped relative to residue 737 and a truncation-detection control run. Report individual replicate points.
2. **Allele-specific expression** at c.2210 and c.3006 by RNA-seq allelic ratio or allele-specific RT-qPCR, ± translation inhibition, to separate the transcript-level deficit (NMD of L737X, *predicted* from the 50-55 nt rule at 747 nt upstream of the last junction with 6 downstream EJCs, **never measured on this allele**) from the protein-fold deficit (turnover of N1002K, untested).
3. **A functional readout that does not depend on abundance at all**: SAC integrity (nocodazole or STLC mitotic-arrest duration), chromosome misalignment under MG132, PCS rate on metaphase spreads, and kinetochore-loaded BubR1 by immunofluorescence. Sieben's H/H vs H/L1002P result, same level, 147 days of median lifespan apart, is the reason this cannot be skipped.

Without (2) and (3), a number from (1) will land in the 5-20% band where the published literature cannot interpret it, or above 25% where it will not distinguish a destabilising allele from a functionally broken one.

---

## Sources used, with retrieval status

**Retrieved as primary full text and quoted directly:** Sieben CJ 2020 *J Clin Invest* 130:171, PMID 31738183, [PMC6934189](https://pmc.ncbi.nlm.nih.gov/articles/PMC6934189/) · Suijkerbuijk SJ 2010 *Cancer Res* 70:4891, PMID 20516114, [PMC2887387](https://pmc.ncbi.nlm.nih.gov/articles/PMC2887387/) · Wijshake T 2012 *PLoS Genet* 8:e1003138, PMID 23300461, [PMC3531486](https://pmc.ncbi.nlm.nih.gov/articles/PMC3531486/) · Baker DJ 2013 *Nat Cell Biol* 15:96, PMID 23242215, [PMC3707109](https://pmc.ncbi.nlm.nih.gov/articles/PMC3707109/)

**Retrieved as full text via summarisation, not verbatim-verified line by line:** Baker DJ 2011 *Nature* 479:232, PMID 22048312, [PMC3468323](https://pmc.ncbi.nlm.nih.gov/articles/PMC3468323/) · Baker DJ 2008 *Nat Cell Biol* 10:825, PMID 18516091, [PMC2594014](https://pmc.ncbi.nlm.nih.gov/articles/PMC2594014/), the 20 wk / 25 wk lifespan pair from this paper is flagged unverified above.

**Abstract only (paywalled or no PMC deposit):** Baker DJ 2004 *Nat Genet* 36:744, PMID 15208629, **the origin of the entire H-allele series, and it could not be read.** Its percentages reach this file only second-hand through Sieben 2020 and Wijshake 2012, which disagree with each other on the -/H value · Matsuura S 2006 *Am J Med Genet A* 140:358, PMID 16411201 · Hanks S 2004 *Nat Genet* 36:1159, PMID 15475955 · North BJ 2014 *EMBO J* 33:1438, PMID 24825348 · Suijkerbuijk SJ 2012 *Dev Cell* 22:1321, PMID 22698286

**Carried forward from `track2/research/01_mechanism_models.md` without re-verification here:** Kajii 2001 PMID 11746029 (PCS percentages) · Yost 2017 PMID 28553959 · Janssen 2009 PMID 19855003 · Gama Braga 2020 PMID 33207204 · Nakano 2024 PMID 39264246 · Wu 2023 PMID 38009412 · Kops 2004 PMID 15159543.

**Not consulted and therefore not used:** OMIM 257300, Malumbres 2024 (PMID 39169218). Any figure attributed to either would be fabricated.
