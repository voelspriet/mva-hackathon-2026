# Track 2 report: drug repurposing for PROBAND01

Team: henkvaness (individual). Date: 6 September 2026. Genotype from Track 1: *BUB1B* compound heterozygous, c.2210T>G p.Leu737Ter and c.3006T>G p.Asn1002Lys.

Every drug and intervention named here is a **hypothesis for follow-up**. Nothing is a prescription. Any dose, schedule or sequence is an **illustrative design only, not to be initiated outside an approved, registered protocol under the treating team**. Statements are marked shown (a cited source states it) or inferred.

---

## 1. Lay summary

This child has two changes in one gene, *BUB1B*. It makes BubR1, the protein that checks chromosomes are shared out correctly when a cell divides. Too little BubR1 and cells end up with the wrong number of chromosomes. That is mosaic variegated aneuploidy, and it is why children with this diagnosis are watched for cancer.

No approved medicine acts on BubR1. Every medicine below acts on something downstream. No repurposed medicine has ever been given to a person with this syndrome for the syndrome, and no case report of one exists (creative G §7).

**Nothing in this report is expected to reduce this child's risk of cancer, and no test here can show whether it has. Three-monthly surveillance remains the only thing that acts on that risk.**

What the work produces, most useful first: a written list of ordinary medicines to avoid or substitute, because they damage chromosome separation at the step the gene already fails, with a carve-out so it can never be read as a reason to change cancer treatment; three additions to existing surveillance that cost nothing; a kidney work-up before any kidney medicine, because two causes are possible and need opposite treatments; and measurements that would show whether the gene-directed ideas have a target in him at all. It has not been shown that the two changes sit on different copies of the gene, and nobody has ever measured how much BubR1 a person with this syndrome has.

We do not know whether the target is present in him.

---

## 2. Mechanism: shown and inferred

BubR1 is a spindle assembly checkpoint protein; biallelic *BUB1B* mutation causes MVA1 (shown; Hanks 2004, PMID 15475955; OMIM 257300). Patient cells show impaired checkpoint, misalignment and low BubR1, rescued by ectopic BubR1; the model is quantitative, instability following low BubR1 abundance (shown; Suijkerbuijk 2010, PMID 20516114).

**Allele 1, p.Leu737Ter.** Codon 737 is TTA at c.2209 to c.2211, so c.2210T>G gives **TGA**, with **G at minus 1 and A at plus 4** (computed from ENST00000287598). UGA is the leakiest stop and the best readthrough substrate (shown; Welch 2007, PMID 17450125), but the minus 1 base is the main determinant of gentamicin response and U at minus 1 is strongest, which this is not (shown; Floquet 2012, PMID 22479203). Inference: readthrough-competent codon in a poor context, single-digit percent at best.

The stop sits in exon 17 of 23, 747 nucleotides upstream of the last exon junction, with six downstream junctions (computed from NM_001211.6), so the 50 to 55 nucleotide rule **predicts** nonsense-mediated decay (shown for the rule; Nagy and Maquat 1998, PMID 9644970). That is a prediction, not a measurement on this allele. Indirect support: the 386X patient transcript was undetectable and the 731X line showed two-fold mRNA reduction, and both truncated proteins are expressed once NMD is bypassed by plasmid-driven expression (Suijkerbuijk 2010). No rare variant in the NMD machinery or EJC core exists in this genome (creative D §6), so NMD efficiency should be assumed normal.

**A verified correction.** The truncation 731X was characterised in Cancer Res 2010 Figures 5A to 5C, not Dev Cell 2012 (V1 §2a): it rescues checkpoint, alignment and unperturbed segregation and runs at **1.44 times wild type** once NMD is bypassed. Four panel files had rejected transcript stabilisation because a stabilised transcript "still stops at 737 and yields no kinase domain"; that ground is wrong. Boundaries: 731X encodes only 715 residues, no construct terminating at 737 was tested, and every result is transient replacement **in HeLa and U2OS, never in an organism**. So for allele 1 the therapeutic object is the transcript, not the fold, and no approved agent stabilises it at an acceptable therapeutic index.

**Allele 2, p.Asn1002Lys: class unknown.** Final exon, kinase domain, gnomAD 1 of 1,461,878, no ClinVar record for this nucleotide. Position does not predict class here: Q921H sits in the kinase domain and was indistinguishable from wild type on level and function (Suijkerbuijk 2010, Fig 4D). Known kinase-domain MVA missense alleles act by destabilisation: I909T and R727C turn over about two-fold faster, HSP90-dependent and proteasome-mediated, and forced overexpression of I909T and L1012P restored checkpoint function fully. N1002 is predicted partially exposed, 9.14 A from T1008 (creative D §4). Inference, untested: more likely a stability allele than a catalytic one, since human BubR1 catalysis is dispensable for error-free segregation (Suijkerbuijk 2012, PMID 22698286).

**The number nobody has.** Residual BubR1 has never been published as a percentage of control for **any** MVA patient: only fold-changes (2 to 6 fold decreased) and ">50% decrease" (Matsuura 2006, PMID 16411201). The quoted 6 and 13 percent thresholds are a **HeLa shRNA titration**, not patient data; the best-quantified figure is murine, about 10 percent in BubR1^H/H (Sieben 2020, PMID 31738183). Every claim here about remaining function is inferred.

**Consequences measured in models.** BubR1 hypomorphs show aneuploidy, dwarfism, cataracts, fat loss and a median lifespan of about six months (Baker 2004, PMID 15208629); p16^Ink4a and p19^Arf rise in muscle, fat and eye, p16 inactivation attenuating and p19Arf inactivation worsening (Baker 2008, PMID 18516091); genetic clearance of p16-positive cells attenuates sarcopenia, fat loss and cataract (Baker 2011). Sustained high BubR1 reduces aneuploidy and tumorigenesis "even in the presence of genetic alterations that strongly promote aneuplodization and cancer, such as oncogenic Ras", and extends lifespan (Baker 2013, PMID 23242215, verified V2 §2).

**Reading rule for the Track 1 mosaicism result.** It bounds a single clonal trisomy near 4 percent, a burden spread over five chromosomes hardly at all (about 21 percent total would be needed), and a clone confined to kidney or muscle not at all (creative F §2). The CIN biologist's sentence on this is printed in §10.

---

## 3. Method

Five dossiers were compiled first (mechanism and models, clinical care and the approved-drug landscape, family perspective from published text only, variant context, phenotype-driven ranking), each statement tagged shown or inferred. Two panels then worked on them blind to each other.

- **Team 1, five seats**: clinical geneticist, mitosis cell biologist, paediatric oncologist, clinical pharmacologist, family representative. Three rounds: ranked lists, cross-objections with revision, moderator's record.
- **A divergent round, ten files (creative A to J)**, written without access to the panel directory: allele/expression/segregation; consequence/tissue/schedule; analogies and trial design; computation on the VCF; a target-to-drug mapping tool; a quantitative appendix; open-source intelligence; nutrition; pharmacy; lateral and measurement-first.
- **Team 2, eight seats**: laboratory geneticist, CIN biologist, predisposition oncologist, nephrologist, endocrinologist, immunologist, PK pharmacologist, second family representative. Two rounds, the second with four compulsory cross-checks.
- **Two verification passes** on seven contested claims: full text for Tang 2011, Suijkerbuijk 2010, North 2014, Bakhoum 2018 and the EMA, MHRA and FDA records; abstracts for Suijkerbuijk 2012, Baker 2013, Wu 2023. Four settled positions changed.
- **A final objection round**: all eight remaining seats wrote against the integrated record, then signed off or dissented. Every correction is applied here.

**On agreement between the teams.** Both reached the same harm screen, the same gate-first procedure, the same rejection of micronucleus frequency as a primary endpoint, and the same wording rule. This is not independent convergence: **both teams read the same five dossiers**, so agreement on a point traceable to a dossier measures dossier agreement as much as expert agreement, and only team 2 saw the divergent round.

**Automated candidate identification.** `pipeline/track2_drugmap/drugmap.py` takes a gene and a mechanism list and returns a ranked, harm-screened table of approved drugs from Open Targets GraphQL, ChEMBL REST and the openFDA label API. For *BUB1B* it queried 110 targets (gene, 33 consequence genes, 76 interaction partners at STRING/IntAct 0.9 or above), returned 148 molecules and passed 29 through a three-way approval test, in 350 seconds. It surfaced six approved drugs the manual route missed (palbociclib, ribociclib, abemaciclib, trilaciclib, venetoclax, temsirolimus) with label evidence, including palbociclib's juvenile-rat cataracts, lens degeneration, kidney tubule vacuolation and abnormal growing incisor teeth. Its top hit is its own limitation: trilaciclib ranks first because the direction check compares drug action against a protein rather than against the phenotype, and a CDK4/6 inhibitor mimics p16, the effector in this gene's own mouse model. It also missed the taxane hazard, because TUBB is not a STRING partner at 0.9. It is a shortlist for a human.

**Mechanism characterisation.** Loss of function, quantitative not qualitative: allele 1 by predicted transcript loss, allele 2 by an unknown mechanism most plausibly destabilisation. Pathway: spindle assembly checkpoint and kinetochore-microtubule attachment. Consequences treated as separate druggable objects: mis-segregation rate, aneuploidy tolerance, senescence and p16, innate sensing and clearance, growth signalling.

**Effort.** One machine, about two days wall-clock.

**Generative AI.** Anthropic, Claude Code, Max plan, model-improvement sharing disabled, no output rating. Used to search public sources, write and run the tool and the quantitative scripts, write the panel and verification files, and draft this report. No patient-level data left the machine.

**Sources, all public**, no proprietary data, no contact with the family or the MVA Society: PubMed and PMC, OMIM, Orphanet, ClinVar, gnomAD v4.1, ClinicalTrials.gov API v2, EU CTR/CTIS, Open Targets, ChEMBL, openFDA and DailyMed, EMA EPARs, MHRA-approved SmPC text, Ensembl REST, published MVA Society and family text.

---

## 4. The measurement gate

**These are proposed investigations, not scheduled ones.** Items 3 and 9 need a sample taken for this purpose. Items 1, 2, 3, 5 and 8 make both parents research subjects. Ordered by yield per cost.

**1. Tubular panel, one visit.** The nephrologist's panel, as written:

> **Serum:** sodium, potassium, chloride, bicarbonate (venous gas acceptable), albumin-corrected or ionised calcium, phosphate, magnesium, creatinine, cystatin C, alkaline phosphatase, urate, PTH, 25-OH-D.
> **Paired second-void urine:** calcium, citrate, protein, retinol binding protein or alpha-1-microglobulin, sodium, magnesium, urate and glucose, each as a ratio to urine creatinine, plus amino acids and pH on a fresh sample.
> **Derived:** tubular phosphate reabsorption (TmP/GFR), fractional excretion of calcium, phosphate, magnesium, urate and sodium, cystatin C eGFR.
> **Records:** neonatal furosemide and parenteral nutrition calcium and vitamin D exposure; cumulative ifosfamide in g/m2 and any platinum; every current product containing vitamin D or calcium, including growing-up milk.
> **Imaging:** baseline ultrasound reported for medullary versus cortical pattern and stone burden, anchoring the two-year trajectory.
> Acid loading is not part of this panel; if bicarbonate is low and urine pH will not fall below 5.3, the renal team decides, not this page.

It decides which cause operates, which alkali is right, whether a thiazide is indicated at all, and gives the baseline cystatin C eGFR from which renal thresholds are set, repeated before and during any renally cleared drug. Creatinine-based eGFR overestimates filtration at low muscle mass, so cystatin C, not creatinine, sets every threshold here (inferred).

**2. One long-amplicon RT-PCR with an NMD-block arm, and parental genotyping alongside.** Illustrative design: forward primer in exon 16 or the 5' half of exon 17, reverse in exon 23; cDNA product 950 to 1,150 bp across six junctions so genomic template cannot amplify; 500 consensus reads by single-molecule sequencing; both parents, three controls, a synthetic 1:1 template mix for amplification bias; block arm a paired lymphoblastoid culture, vehicle against cycloheximide 100 micrograms per mL for 4 to 6 hours. Under 1,000 EUR, 3 to 5 working days.

**The failure mode, stated correctly.** Efficient decay does **not** make trans look like cis. In trans the surviving transcript carries c.3006G, so cDNA shows c.3006G near 100 percent. In cis both changes sit on one molecule, decay removes both, and c.3006G falls near zero: opposite signatures. The real limit is that under efficient decay phase cannot be read off a single molecule and becomes an inference from allele fraction, which is why the block arm is mandatory. **Only the block arm needs living cells;** phase and allele-specific expression run from stabilised RNA in a PAXgene tube at a scheduled visit. **Parental genotyping at the two sites 10.9 kb apart runs alongside, not instead**: it is a segregation test immune to the artefact and detects a de novo allele. Run this before item 4. It decides whether the allele-directed hypotheses have a premise.

**3. Aneuploid fraction per tissue.** FISH or single-cell sequencing on blood, buccal cells and skin, plus a PCS karyotype, child and both parents. Carrier parents are an intermediate phenotype, not a normal reference: PCS runs 3.5 to 41.7 percent in carrier lymphocytes against under 2 percent in controls (Kajii 2001, PMID 11746029).

**4. BubR1 immunoblot** as a percentage of control against both parents and three controls: a figure that exists for no MVA patient.

**5. Cycloheximide chase and forced-expression rescue on p.Asn1002Lys**, Suijkerbuijk 2010 design. Decides its functional class.

**6. Cardiac baseline: ECG read for the J point, and echocardiography.** BubR1 hypomorphs died of cardiac failure after senescent-cell clearance improved every other measured outcome (Baker 2011), and BubR1^H/L1002P shows low cardiac stress tolerance with an ECG J-point defect, the one endpoint the SIRT2 transgene reversed (Sieben 2020; North 2014, PMID 24825348). It sets the ceiling on any healthspan claim and is the baseline for the QT problem in §6.

**7. Endocrine gate.** IGF-1 and IGFBP-3 SDS on stable intake, bone age, thyroid function, morning cortisol, imaging if IGF-1 is low.

**8. Immune panel.** Interferon score (PMID 24183309), immunophenotype, immunoglobulins, vaccine titres, child and both parents. No immune measurement has been published in any MVA patient, so nothing here can confirm or rule out what families describe. The tests that would answer it are listed here.

**9. p16 in patient tissue.** Decides whether the senescence hypothesis has a human baseline.

**Already in hand, at zero cost** (creative D §6): *MT-RNR1* clean, *G6PD* normal (which is what permits the hydroxychloroquine hypothesis to be discussed at all), *CYP3A5* \*3/\*3 non-expressor, *DPYD* rs1801160 normal function. Add **UGT1A1 \*28 and \*6**, readable from the same WGS, before any irinotecan.

### Consent architecture

Parents consent for the child. Both parents are separately **research subjects** for items 1, 2, 3, 5 and 8, with their own consent and their own plan for what they are told about their own results, carrier and PCS status included. **Items 3 and 9 need tissue taken for this purpose**; items 2, 4 and 5 can largely be attached to visits already scheduled, if the family agrees to a longer scan and to the same blood sample being used for more tests. **A cis result is a re-diagnosis, not a research finding**: the child would retain an intact allele, the explanation the family has absorbed would be unsettled, and recurrence information for both parents would change, so it needs pre-test counselling of the diagnostic kind with all three answers named in advance, prepared before the sample is taken. Before any monitored n-of-1: off-label status disclosed in writing, information far enough ahead to weigh, the withdrawal period consented to before it starts, the negative-control outcome pre-filed, publication of negatives committed in advance, and named answers to who prescribes, who pays, and what happens to access if something appears to help. Visit load is a cost to be counted, and draws should be keyed to visits already scheduled.

---

## 5. The avoidance rule with its carve-out

The first-ranked output is a rule, not a drug. **Hypothesis for follow-up.**

> **SCOPE.** Elective, non-oncological prescribing only.
>
> **DOES NOT APPLY TO any antineoplastic agent given with curative, maintenance, relapse, disease-control or palliative intent.** Do not reduce, omit, delay or substitute any agent in a rhabdomyosarcoma protocol, or in any other cancer treatment plan, on the basis of this page. EpSSG RMS 2005 maintenance gives 5-year overall survival of 85.0 percent against 72.4 percent (Bisogno 2019, PMID 31562043). No study has shown MVA or *BUB1B* patient cells to be hypersensitive to any spindle agent: the sensitisation data come from engineered knockdown tumour cells (Janssen 2009, PMID 19855003), and the opposing data show *BUB1B* suppression producing taxane resistance (Sudo 2004, PMID 15059905). It also does not withhold a loop diuretic, corticosteroid, antibiotic or antiemetic given for an acute indication where no equivalent alternative exists. Decisions on a cancer regimen belong to the treating oncologist and the tumour board.
>
> **APPLIES TO** colchicine, griseofulvin, albendazole, mebendazole, acetazolamide, topiramate, elective loop diuretics, high-dose intermittent vitamin D, somatotropin, mecasermin. Substitutes: terbinafine; an NSAID or anakinra; levetiracetam; a thiazide; daily vitamin D to a measured 25-OH-D; for growth, the endocrine gate.

The protecting clause states intent rather than listing drug names on purpose: a closed list protects only what it names and would leave vinblastine, topotecan, doxorubicin and etoposide unprotected by omission. It is repeated verbatim in §7. Basis: colchicine is a reference aneugen in the human lymphocyte micronucleus assay (Vanhauwaert 1998, PMID 9412992) and benzimidazoles bind the same site; carbonic anhydrase inhibition promotes hypercalciuria and stones, documented for topiramate in children with resolution on withdrawal (PMC5976810) and inferred for acetazolamide; high-dose intermittent vitamin D has caused nephrocalcinosis (PMID 2386055).

---

## 6. Ranked hypotheses for follow-up

**1. The avoidance rule with its carve-out (§5). Hypothesis for follow-up.** Tier: human genotoxicity and label data per agent, inference for transfer to this genotype. Condition: the carve-out printed in the same type size everywhere. Harm: over-application, meaning curative chemotherapy withheld. Readout: avoid-list agents prescribed per patient-year through the UK MVA National Audit, not individual compliance.

**2. Three surveillance additions, at no cost. Hypothesis for follow-up.** Tier: human. This is the part of the answer that is not a refusal.
(a) **Read *UGT1A1* \*28 and \*6 from the WGS already in hand, before any irinotecan.** Irinotecan is the backbone of standard salvage after prior alkylator exposure; the genotype is free and already sequenced.
(b) **Extend the three-monthly renal ultrasound to bladder wall and, in girls, vagina.** MVA rhabdomyosarcoma is characteristically genitourinary and botryoid (Schneider 2020, PMID 33209717). No extra visit, no extra cost, and it is the tumour this child has already had.
(c) **Surveillance must not stop at age 7.** An adult-onset MVA1 phenotype exists: homozygous intronic *BUB1B*, ampullary adenocarcinoma at 34, later colon and gastric primaries, with PCS and MVA in patient cells (Rio Frio and Foulkes 2010, PMID 21190457). The guideline horizon of renal ultrasound to age 7 (Nakano 2024, PMID 39264246) is a floor, not a ceiling.

**3. Tubular work-up, then the renal agents the panel indicates. Hypothesis for follow-up.** *Sequence and agents for the renal team to consider; not a prescription.* Tier: human, from other paediatric hypercalciuric disease (Seikaly 2001, PMID 11433085). This is the only entry whose lesion is documented in this child, although its mechanism is not, and it tests no *BUB1B* hypothesis; its proponents in both teams conceded that. It has a paediatric licence, a dose, a readout inside six weeks, and a measured effect on urinary calcium in other conditions. Whether it changes this child's kidney findings is not known.

> Hypercalciuria for age **with normocalcaemia** and normal TmP/GFR: thiazide plus potassium citrate, amiloride as escalation.
> Low TmP/GFR with low molecular weight proteinuria, glycosuria, aminoaciduria or bicarbonate wasting: alkali with phosphate and alfacalcidol first, thiazide as adjunct.
> Normal urine calcium with a resolving ultrasound: no drug.

Normocalcaemia matters because a thiazide raises serum calcium, so hypercalciuria driven by hypercalcaemia is where it does harm. The second branch matters because ifosfamide proximal tubulopathy is one of the two competing causes; the avoid-list bar on high-dose intermittent vitamin D must not be read as barring alfacalcidol for a tubulopathy. **Dietary calcium continues, inside meals**, because restriction raises oxalate absorption and threatens bone (PMC3426770; Habbig, Beck and Hoppe, Kidney Int 2011;80:1278-91): milk in the porridge, yoghurt with the fruit, cheese sauce on the pasta. A family reading "no calcium" removes milk. Sodium is the lever instead, since urinary calcium tracks urinary sodium.

Citations for the other cause, corrected: **PMID 19460127 is the preterm risk-factor study identifying furosemide and carries no resolution figure.** Resolution comes from two cohorts: **70 percent at 12 months and 90 percent at 24 months (PMID 16705005)**, and **61 percent at 12 to 18 months (PMC9587072)**. **Neither reports an untreated arm; both are observational follow-up.** Harm: hypokalaemia, volume depletion, hypercalcaemia. Readout: urine calcium to creatinine at baseline and six weeks, with citrate, potassium and bicarbonate, and the ultrasound trajectory over two years as the outcome.

| # | Hypothesis for follow-up | Tier | Condition | Harm | Readout |
|---|---|---|---|---|---|
| 4 | Cyproheptadine, after a food-first run-in of 8 to 12 weeks | Human, small uncontrolled paediatric series (PMID 18989154; 24941960) | A body-composition readout, so weight gained as fat is not reported as benefit | Sedation, rare hepatotoxicity | MUAC z-score monthly; lean mass index at 0 and 12 weeks |
| 5 | Vaccination completed with serology; immunoglobulin only on a documented deficit | Human in other populations, inference for MVA | Gate item 8 first; live vaccines withheld under any immunosuppressant | False reassurance if titres go unchecked | Titres at 4 to 6 weeks; infection days per year |
| 6 | If rhabdomyosarcoma recurs: cyclophosphamide with mesna in place of ifosfamide, and dexrazoxane alongside an anthracycline. Relapse-conditional, for the treating oncologist, governed by the carve-out | Human other for the regimens; BubR1 mouse for cardiac organ overlap only | RMS 2005 randomised patients already in remission after nine IVA-based cycles, so 85.0 against 72.4 percent sits downstream of ifosfamide induction and does not transfer unchanged to a VAC induction | Haemorrhagic cystitis, gonadal toxicity, alkylator second malignancy; for dexrazoxane a secondary-malignancy flag in its own warnings | Tubular handling, strain, troponin |
| 7 | Hydroxychloroquine, ex vivo gated, time-limited, never chronic | Cell, and the experiment used **chloroquine** at 25 micromolar, called the weakest of three aneuploidy-selective compounds by its own authors and without effect on human tumour lines (Tang 2011, PMID 21315436, verified V1 §1c) | A measured aneuploid fraction in this child, plus an achievable retinal screening plan | Retinopathy against a syndromic eye phenotype, antigen-presentation blockade, QT | Aneuploid fraction by FISH |

**The QT collision, a co-prescribing problem and not a choice between items.** The thiazide at item 3 produces hypokalaemia; hydroxychloroquine is QT-listed; ondansetron accompanies every VAC or IVA cycle. Three contributions stack with no paediatric precedent. Required alongside: **baseline ECG (gate item 6), potassium and magnesium before each ondansetron cycle, and a non-QT antiemetic named in advance.**

**Not ranked, deliberately: metformin and dasatinib.** Neither is a candidate at any rank; both are named experiments in §9, for the reasons in §7.

---

## 7. Explicitly not recommended, and why

**The carve-out is repeated here verbatim, because this is the section that will be photocopied:**

> **DOES NOT APPLY TO any antineoplastic agent given with curative, maintenance, relapse, disease-control or palliative intent.** Do not reduce, omit, delay or substitute any agent in a rhabdomyosarcoma protocol, or in any other cancer treatment plan, on the basis of this page. Decisions on a cancer regimen belong to the treating oncologist and the tumour board.

**Metformin, as a prescription.** Tang 2011 tested it at **0.5 and 1.0 mM** in trisomy 13 and 16 MEFs at 72 hours (Figure S1A, Table S1): Ts13 73 plus or minus 2.9 against wild type 86 plus or minus 2.4, Ts16 72 plus or minus 2.4 against 82 plus or minus 2.1, both P<0.005, an effect the authors call "not as dramatic" and "subtle" (verified V1 §1b). Paediatric plasma metformin is **7.7 to 15.5 micromolar**: a gap of **32 to 130 fold** that cannot be closed by dose, salt, formulation or tissue. Metformin is not appreciably protein bound, distribution is transporter-driven, extended release lowers Cmax rather than raising it, renal cortical accumulation is a few fold rather than two orders, and the ceiling is toxicological, since plasma above roughly 5 mg/L, about **39 micromolar**, is the range associated with lactic acidosis, allowing at most a further 2.5 to 5 fold. The paper reports no IC50, no dose above 1 mM, no human cell line and no in vivo arm. Metformin moves to §9 as an experiment. Two seats asked that it not appear in a ranked list at all; that is followed, and both dissents are printed in §10.

**Dasatinib is not a candidate at any rank.** The senolytic rationale rests on genetic clearance of p16-positive cells in a mouse, which is not a drug. Three objections fail **independently**: the tumour direction is unresolved (§9 question 8); TKI growth deceleration is prepubertal with normal IGF-1 and IGFBP-3, so it acts on cartilage and is not avoided by lowering occupancy with intermittent dosing (PMID 21592517); and dasatinib blocks TCR and NK activating signalling within hours, suppressing the same clearance arm that may be restraining the aneuploid compartment. There is no paediatric senolytic dose in any condition. A formulation asymmetry compounds it: the powder for oral suspension is authorised in the EU (X/0056/G, Commission Decision 2 July 2018) and **not** in the US, where every product on record is a tablet and the sub-10 kg exclusion has no alternative offered (verified V2 §5).

**Growth hormone and mecasermin outside the endocrine gate.** No MVA1 efficacy data; no response in the two MVA2 patients tested (PMID 36588761); mecasermin carries a labelled contraindication with a malignancy history. Growth hormone should not be started without a documented growth hormone deficiency. If the tests in §4 show one, the decision returns to the family with the endocrine and oncology teams together, with the one-disease-free-year condition (Sklar 2018, PMID 29982476) in the discussion.

**Chaperone inducers, chemical chaperones including phenylbutyrate, and rapalogs.** This bar stands, on a distinction stated explicitly: **correction versus tolerance.** Raising BubR1 lowers the production of new mis-segregation events at source. Raising chaperone or HSF1 capacity does not touch the mis-segregation rate; it makes aneuploid cells easier to keep, and HSF1 capacity is the documented aneuploidy-tolerating change in human cells (Donnelly 2014, PMID 25205676), while single-chromosome gains otherwise behave as tumour suppressors and tumours arise when a clone acquires tolerance (Sheltzer 2017, PMID 28089890). Rapalogs add immunosuppression against clearance, and proteinuria; the claim that aneuploid cells grow better under rapamycin traces to budding yeast disomes, was not verified against a primary source here, and has not been shown in human cells.

**The BubR1-raising bar is withdrawn.** One seat's rule barred agents that raise BubR1, on the premise that raising it in every cell raises aneuploid-cell fitness. Verification defeats that premise: sustained high BubR1 **reduces** aneuploidy and tumorigenesis even against oncogenic Ras and extends lifespan (Baker 2013, verified V2 §2). Withdrawn on that half; standing on the tolerance half above.

**The expression-directed arm (niacin, acipimox), with its surviving reason for exclusion.** With the bar withdrawn this arm must be restored or excluded for a stated reason. It is excluded, for weaker but real reasons. SIRT2 deacetylates BubR1 at K668, blocking CBP-primed ubiquitylation and degradation (North 2014); a SIRT2 transgene on BubR1^H/H gave **+58 percent median and +21 percent maximal lifespan, P=0.0384, n=31 against 33, driven entirely by males at +123 percent (P=0.004), with no effect in females (P=0.7915)** (verified V2 §3c). The link from an approved NAD+ precursor to BubR1 in this genotype is untested: the NMN experiment was 500 mg/kg/day intraperitoneally for **seven days** in wild-type mice, clean only in testes, with no aneuploidy or lifespan endpoint. Wu 2023 (PMID 38009412) does not refute North 2014, it bounds it to the hypomorph, and its authors hold a commercial interest in the opposite result. Baker 2013 is a germline transgene at supra-normal level, which no approved drug reproduces. Acipimox has human data for raised muscle NAD+ (PMID 25352640), no paediatric indication, and flushing that limits tolerability. Net: a marginal, male-driven rescue of a deficit in one progeroid model, joined to an approved drug by an untested link. Not a candidate; retained as the immunoblot experiment in §9. High-dose **nicotinamide** opposes this axis, inhibiting sirtuins by base exchange.

**Also not recommended, with the surviving reason.**

| Agent or class | Surviving reason |
|---|---|
| CDK4/6 inhibitors | No MVA evidence; they mimic p16, the effector in this gene's own mouse model |
| Hydroxyurea | It raises micronucleated reticulocytes, which is the readout |
| Colchicine, griseofulvin, albendazole, mebendazole | Approved aneugens |
| Acetazolamide, topiramate, elective loop diuretics | Hypercalciuria into an established lesion |
| Systemic aminoglycosides | Nephrotoxicity in the organ under treatment, whatever the clean *MT-RNR1* result |
| Digoxin as an NMD-stabilising agent | Therapeutic index in a child whose filtration is unmeasured, not mechanism; the mechanism objection was withdrawn after the 731X correction |
| Proteasome inhibitors | They block mitotic exit |
| HSP90 inhibitors including pimitespib | They accelerate turnover of the only BubR1 this child makes |
| Low-dose paclitaxel | The measured direction in this genotype class is sensitisation (Janssen 2009), not the CIN suppression of Ertych 2014 (PMID 24976383) |
| **Ataluren** | **Not authorised outside Great Britain, obtainable elsewhere only by named-patient import or single-patient IND** (Great Britain PLGB 44221/0004, renewed 24/02/2026, after the European Commission declined to renew the EU conditional authorisation on 28 March 2025; verified V2 §4); also argued against by the minus 1 G codon context |
| Every non-approved compound and supplement | Out of scope: quercetin, fisetin, NMN, nicotinamide riboside, navitoclax, AICAR, 17-AAG, and the Mps1, Aurora B, PLK1 and KIF18A inhibitors |

---

## 8. Endpoints and their power limits

Arithmetic from creative F; script at `pipeline/track2_math/f_math.py`.

**Rejected as a primary endpoint: micronucleus frequency** for aneuploidy-selective agents, on two grounds both teams reached. It scores ongoing mis-segregation, while the published activity of the chloroquine class was selective killing of cells already aneuploid, so a fall is not predicted and its absence would falsify nothing. And with no baseline in this child, a pre-specified 30 percent fall may sit inside OECD TG 487 variance. It stays as a baseline and a stopping rule.

**Power.** In a three-period N-of-1 with three measurements per period, interphase FISH detects a **22 percent** relative change at an aneuploid fraction of 0.10 with 1,000 nuclei; micronuclei at an elevated MVA baseline reach **41 percent** with 2,000 binucleated cells; a flow micronucleated-reticulocyte readout counting 1e6 cells drives scoring CV to 0.022 and still lands at **37.5 percent**. The three-per-period design, not the assay, binds. Periods follow pool turnover: about 12 weeks plus a 4-week washout for lymphocyte endpoints, roughly 11 months in total, or 4-week periods on a reticulocyte readout. A parallel randomised design is out of reach below about a 50 percent effect; an aggregated crossover across families reaches a 20 percent change with **17 subjects**, inside an enrollable population of roughly 15 to 20, and needs one shared protocol, one central scoring laboratory and a pre-registered endpoint.

**Decision thresholds.** The timing correction dominates: a child already treated for rhabdomyosarcoma faces a residual, not a lifetime, risk, and every threshold multiplies by 1/s where s is the residual share. At s = 0.2 and added harm 5 percent, the required relative reduction exceeds 60 percent. Since no approved drug has a measured effect on cancer incidence in MVA, every figure is a requirement, not an estimate. The cancer risk is deliberately not written as a range, because 38.7 percent (Pavone 2022, PMID 35804254) and about 75 percent (Orphanet ORPHA 1052) are unreconciled and probably ascertainment-driven.

**Endpoints by entry.** Renal as in §6; aneuploidy-selective entries FISH or single-cell sequencing per tissue; nutrition MUAC z-score and lean mass index; immunology titres and infection days; relapse entries tubular handling, strain and troponin. Growth safety, if any agent with a growth signal is ever considered: knemometry at 0.09 to 0.16 mm resolution over 2 to 4 weeks, not height velocity and bone age at 6 and 12 months (PMID 26854116). Family-collected endpoints kept: buccal micronucleus cytome posted and blind-scored, home urine calcium to creatinine strips, grip strength and a timed five-rise test, a three-day diary. Rejected: parents dosed in vivo as a comparison arm, and whole-body MRI, since no validated imaging surveillance protocol for MVA exists.

---

## 9. Unresolved questions, each with the experiment that settles it

1. **Phase, allele-specific expression, NMD efficiency.** The paired long-amplicon RT-PCR with cycloheximide arm **plus parental genotyping**. Under 1,000 EUR, 3 to 5 working days. Holder: the referring clinical genetics laboratory.
2. **Residual BubR1 as a percentage of control.** Immunoblot against both parents and three controls. It would also test whether a normal transcript level at c.2210 puts the pathogenicity of the nonsense allele itself in question, given 115 gnomAD heterozygotes and no published MVA patient carrying it.
3. **The functional class of p.Asn1002Lys.** Cycloheximide chase and forced-expression rescue. Holder: a mitosis laboratory with the shRNA replacement system.
4. **Whether an aneuploidy-selective target exists in him.** FISH or single-cell sequencing per tissue, child and both parents.
5. **Metformin: does it select against aneuploid cells at a reachable exposure?** Concentration-response in patient or Pallister-Killian fibroblasts over three to four passages. **The ladder must include a 1.0 mM metformin arm as an internal positive control alongside AICAR**, because the only concentrations at which anything was seen are 0.5 and 1.0 mM, and a ladder topping out below them cannot separate "does not work at reachable exposure" from "the assay failed". **Pre-declare before the run: a null below 500 micromolar is uninformative, does not refute the mechanism, and must not be reported as reassurance.** If the 500 micromolar and control arms do not clear a pre-filed threshold, the arm closes.
6. **Are this child's cells more or less sensitive to vinca alkaloids?** Micronucleus frequency and apoptotic fraction under vincristine and vinorelbine at clinically achievable concentrations, in stimulated lymphocytes and fibroblasts, against both parents and three controls, blind, threshold pre-declared. Janssen 2009 predicts amplified errors, Sudo 2004 reduced killing, and no MVA cell has been tested. Whichever way it comes out, the carve-out stands until a clinical trial says otherwise.
7. **Tolerance or correction?** Patient fibroblasts with and without a chaperone inducer, immunoblot and FISH at days 0 and 14. Tolerance predicts BubR1 unchanged with aneuploid fraction stable or rising; correction predicts BubR1 up and aneuploid fraction down. Precondition: question 3 first.
8. **Is senescence the lesion or the brake?** A senolytic given **as a drug** to BubR1^H/H or BubR1^H/L1002P mice, tumour incidence co-primary, bone length secondary. Never done. It is why dasatinib appears here rather than not at all, and settling it in favour of senolysis would still not make dasatinib a candidate (§10).
9. **Is immune clearance rate-limiting?** Interferon score and NK cytotoxicity in patients and carriers. The literature was misread in both directions and corrected: Bakhoum 2018 (PMID 29342134) shows chronic cGAS-STING signalling in chromosomally unstable **tumour** cells is pro-metastatic and is not an immune-clearance paper; clearance of **untransformed** aneuploid cells stands on Santaguida 2017 (PMID 28633018) and Wang 2021 (PMID 34105235).
10. **Within-patient variance of every endpoint over 12 untreated months.** Without it no endpoint is known to be measurable in this disease.
11. **A shared aggregated N-of-1 protocol across the roughly 40 known patients**, 17 subjects for a 20 percent change. A cell-line panel plus a few-hundred-compound screen sizes inside one year of the MVA Society's fundraising (GBP 325k target for 2026). Holders: the Society and the GOSH conference network.
12. **A per-genotype embryonal-tumour fraction, and a residual risk for a treated MVA1 child.** Neither is published, and §8's threshold table cannot be closed without the second.
13. **Any approved drug tested in a BubR1 model with a healthspan endpoint, and any paediatric senolytic dose in any condition.** Neither exists.

---

## 10. Dissents, printed as the seats wrote them

**Family representative 2, on metformin:**
> "Metformin should not appear in the ranked list. The only concentrations at which it did anything are 32 to 130 times a child's blood level, and its own authors called the effect subtle; printing a cheap, licensed, familiar drug at rank 6 of 7 puts it in front of families as a candidate when it is an experiment, and it belongs in the named-experiments list with the others."

**PK pharmacologist, on the same:**
> "Metformin cannot reach the concentration at which its effect on aneuploid cells was measured, at any dose or formulation a child can tolerate, a shortfall of 32 to 130 fold; it is excluded as a prescription on that basis and retained only as a cell experiment, and a positive result at a reachable concentration would reverse this."

**Mitosis cell biologist (team 1), on dasatinib, against his own earlier rank 2:**
> "Settling the tumour-direction question in favour of senolysis would not by itself make dasatinib a candidate in this child: the cartilage and immune-clearance objections are independent of it, and each would still need its own answer."

**Clinical geneticist (team 1), on phase:**
> "One test does not settle phase: where nonsense-mediated decay is efficient, the mutant allele disappears from the cDNA and its absence is indistinguishable from cis, so parental genotypes or long-read genomic sequencing must run alongside the RT-PCR, not instead of it."

**Clinical laboratory geneticist, on ordering:**
> "Gate item 2 should be run first and alone, because it is the only test that can void gate items 3, 4, 5 and 8, and the only one whose result could return this case to variant interpretation rather than to prescribing."

**Paediatric nephrologist, on the renal item:**
> "The tubular panel is not a formality before a thiazide: if it shows proximal tubulopathy, the first prescription is alkali with phosphate and an active vitamin D analogue, and the thiazide enters only as an adjunct against the calcification that the replacement itself causes."

**CIN biologist, on the mosaicism result:**
> "Mosaic aneuploidy was not detected above about 10 percent of cells in one blood sample; that bounds a single clonal trisomy near 4 percent and bounds a variegated or tissue-confined burden hardly at all, so it must not be read as showing that this child is largely euploid, nor as showing that no aneuploidy-selective target exists in him."

**Paediatric cancer-predisposition oncologist, on the carve-out:**
> "The carve-out protects only what it names, so it must be repeated verbatim wherever an antineoplastic agent appears in this report, section 6(d) included, and it must read 'any antineoplastic agent given with curative, maintenance, relapse, disease-control or palliative intent', because a closed list of protected drug names is what allows a regimen to be de-escalated by a clinician who will never see another case of this disease."

Two positions remain unreconciled rather than dissenting: whether senescence in this gene is lesion or brake, and whether an aneuploidy-selective drug would subtract cells from organs with no reserve. On the second, the objection came in part from the proponent of the senolytic hypothesis arguing against his own rank, which is what makes the disagreement load-bearing rather than a split between advocates and sceptics.

---

## 11. Scalability

**To another gene.** The drug-mapping tool changes two things and keeps the rest: the gene symbol and the mechanism-to-gene mapping change, the code does not. For a single-mechanism gene the command line suffices (`--gene TP53 --targets "MDM2 axis:MDM2,MDM4;p21:CDKN1A"`). Where the useful targets are consequences rather than the gene, a JSON config carries the biologist's decisions in reviewable form: which genes stand for a mechanism, which direction is wanted, which hits are excluded and why, and which drugs must be seeded by name because the databases file them elsewhere (rapalogs under FKBP1A, metformin under complex I, the chloroquine class under TLR7/9). Those decisions are the scientific content; the tool makes them explicit and attaches evidence links. It **is designed to transfer** to another chromosomal instability disorder with the gene and partner set swapped. **The transfer has not been run.** What does not transfer is judgement about direction at the phenotype level (the trilaciclib result) and hazards that live in the literature rather than in an interaction graph (taxanes).

**To another N-of-1 case, independent of gene.** Seven transferable parts: a measurement gate before any mechanism-directed prescribing, which both teams reached separately; a verification pass against primary sources, which changed four settled positions here and moved a drug each time; exposure arithmetic as a gate, which removed one candidate outright and is one division; a harm screen as a first-class output, deliverable without a trial; an endpoint power calculation before the endpoint is chosen, which rejected the intuitive endpoint in favour of FISH and turned the design question into a shared crossover protocol; a consent architecture; and a family representative with a veto over wording, a constraint that changed the report and not only its tone.

---

## 12. Limitations, and what a critic will attack first

**What this can claim.** A documented, citable procedure, run twice by panels that did not read each other, with a verification pass against primary sources that changed four settled positions, and a final round in which every seat wrote against the integrated record.

**What it cannot claim.** Nothing here is evidence that a medicine works. No candidate has been tested in an MVA patient or in MVA patient cells. No case report exists of any repurposed agent given to an MVA patient for the syndrome. No approved drug has a measured effect on cancer incidence in this disease, and ClinicalTrials.gov API v2 and EU CTR/CTIS return zero interventional trials for "mosaic variegated aneuploidy" or "BUB1B". Phase is unproven, residual BubR1 unmeasured, and the missense allele a variant of uncertain significance.

**First attack.** The two top-ranked outputs are a prescribing rule and a work-up, so a repurposing brief has been answered largely by declining to prescribe; five of thirteen seats said as much in their own strongest-objection sections. The reply: the three surveillance changes in §6 item 2 cost nothing and are not a refusal, and a rule that prevents an aneugen being prescribed to a child with a segregation defect acts this month, while every mechanism-directed candidate acts in a hypothetical future.

**Second.** Independence is partial. Both teams read the same five dossiers, so their agreement measures dossier agreement as much as expert agreement, and only team 2 saw the divergent round.

**Third.** Two verified rows rest on abstracts: Baker 2013 and Wu 2023, the latter including its competing-interest statement. Body-of-paper effect sizes for Baker 2013 were not retrieved.

**Fourth.** A panel of assigned roles reproduces the caution its brief rewards. No structural defence is offered; the counter-evidence is that verification overturned four panel positions and that four seats changed rank against their own earlier argument.

**Where the panels may share a blind spot.** No member of either team found an error inside a dossier; every correction concerned a reading of one. Both reasoned from a mouse hypomorph whose allelic identity differs from this child's, although Sieben 2020 is the paper showing that allelic identity, not total level, drives outcome. Both worked without the child's age, weight, current medications, or whether ifosfamide was given, and every renal, PK and dosing conclusion turns on that last item. Both accepted p.Leu737Ter as pathogenic while the record shows 115 gnomAD v4 heterozygotes at AF 7.87e-5 and no published MVA patient carrying it, so its ClinVar classification reads as reasoning from mechanism rather than from patient evidence. **Neither team asked whether the diagnosis is right.**

**One resolved discrepancy.** A dossier gave c.2209T>G where the prompt and the other files give c.2210T>G. Codon 737 is TTA at c.2209 to c.2211, so c.2210T>G gives TGA while c.2209T>G would give GTA, valine. The prompt is correct; the automated HGVS in `04_exomiser_model2.md` is wrong.

---

## Repository

`track2/research/` (five dossiers), `track2/creative/` (ten divergent files), `track2/panel/` and `track2/panel2/` (thirteen seats, four rounds plus the final objection round), `track2/verify/` (two primary-source verification passes), `pipeline/track2_drugmap/` (tool, config, output), `pipeline/track2_math/f_math.py` (quantitative appendix).
