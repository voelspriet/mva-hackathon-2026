# Round 1: clinical laboratory geneticist

Lens: what the laboratory can still establish about this genotype, how each result would redirect the drug question, and which hypotheses rest on a fact nobody has measured.

## 0. Six unmeasured facts, in order of consequence

**T1. Phase.** The brief says "in trans presumed". The calls sit 10,911 bp apart (chr15:40,209,701 and 40,220,612), inside one long read. Creative F.1: at the ceiling of co-occurrence enrichment R = 12,706, P(trans) falls to 0.19 to 0.42, and R cannot be bounded from gnomAD. In cis, the child retains an intact allele and the list below is void.

**T2. NMD efficiency and allele-specific expression, from one RT-PCR.** The sites are 796 nt apart in the mRNA (NM_001211.6 positions 2362 and 3158), so one cDNA amplicon at single-molecule depth returns phase and allele ratio together. Decay is predicted, not measured: the PTC lies 747 nt upstream of the last junction (dossier 01, 2.1), and 386X and 731X proteins are undetectable in patient cells but reappear when NMD is bypassed (Suijkerbuijk 2010, PMID 20516114). c.3006 lies in the final exon, so the missense transcript escapes NMD.

**T3. Residual BubR1 protein, against both parents and three controls.** No percentage of control is published for any MVA patient, only fold-changes and "more than 50% decrease" (Matsuura 2006, PMID 16411201). The 6% and 13% thresholds in circulation are a HeLa shRNA titration (dossier 01, 2.2).

**T4. Functional class of p.Asn1002Lys.** Suijkerbuijk 2010 splits MVA missense alleles into a destabilising class (HSP90-dependent, proteasome-mediated) and one behaving like wild type; Q921H sits inside the kinase domain and was wild-type-like, so position does not predict class. Creative D reads AlphaFold as a surface defect and notes AlphaMissense calls L844F and R814H benign. A cycloheximide chase settles it.

**T5. Mis-segregation burden, at cell level rather than from WGS.** Creative F.2: the 44x BAF negative bounds a single clonal trisomy in blood near 4%, bounds a variegated burden hardly at all, and is blind to a clone confined to kidney or muscle. PCS karyotype (Kajii 2001, PMID 11746029) and interphase FISH read it instead.

**T6. p16 burden.** The senolytic case is INK-ATTAC clearance in mouse muscle and fat (Baker 2011, PMID 22048312). No MVA patient has had p16 measured.

## 1. Ranked candidates

| # | Drug or rule | Step | Tier | Paediatric status | Phenotype interaction | Harm | Readout | Rank reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Aneugen avoidance: colchicine, griseofulvin, albendazole and mebendazole barred; taxanes and vincas flagged | Kinetochore-microtubule attachment | Cell: partial BubR1 reduction made cells "remarkably more sensitive to low doses of taxol" (Janssen 2009, PMID 19855003) | Approved; a rule needs no dose | Vincristine and dactinomycin are the RMS backbone (dossier 02, 4) | Over-application withholding curative chemotherapy | Micronucleus assay on his lymphocytes plus or minus each agent, against both parents | Survives every unmeasured fact except T1 |
| 2 | Hydrochlorothiazide 0.5 to 1 mg/kg/day plus potassium citrate 0.3 to 0.6 mmol/kg/day, dosed on cystatin C; amiloride add-on | Urinary calcium and citrate, not BubR1 | Human, other disease (Seikaly 2001, PMID 11433085) | Established (dossier 02, 3) | Low muscle mass makes creatinine eGFR overread; hypokalaemia stacks with ondansetron | Volume depletion in failure to thrive | Urine Ca/creatinine, citrate, pH; ultrasound at 6 months | Nephrocalcinosis is not an established MVA feature (dossier 02, 1); a tubular workup comes first |
| 3 | No rhGH, no mecasermin, no bolus vitamin D | Growth signalling and calcium load | Human: mecasermin contraindicated with malignancy history; GH no response in MVA2 and no MVA1 data (PMID 36588761) | Approved; a rule needs no dose | Cancer risk quoted 38.7% to about 75% | Forgoes what families ask for most | Overturned by a measured GH deficiency plus a T6 profile | Prevents the largest harm on the list |
| 4 | Hydroxychloroquine 5 mg/kg/day, conditional on T5 | Autophagy and lysosome in aneuploid cells | Cell, trisomic MEFs; chloroquine selective but "not as dramatic" as AICAR or 17-AAG (Tang 2011, PMID 21315436) | Rheumatology dosing; no renal formula | Nephrocalcinosis, retinopathy screening, QT with ondansetron | Removing aneuploid cells removes tissue he cannot spare; creative G calls the direction tissue-contradictory | Interphase FISH aneuploid fraction | The target has not been shown to exist in him |
| 5 | Metformin, same condition | AMPK, an approved stand-in for AICAR | Inference; untested for aneuploidy-selective killing (dossier 01, 7) | Off-label below age 10; phase I 666 to 2,000 mg/m2/day | Stop rules bite when he is unwell | Lactic acidosis with falling GFR | As rank 4 | Mechanism annotation is complex I, not AMPK (creative E) |
| 6 | Digoxin as deliberate NMD stabilisation, ex vivo first | Decay of the c.2210T>G transcript | Cell: glycosides topped an NMD screen (Nickless 2014, PMID 25064126); engineered 731X was functional when expressed (PMID 22698286) | Dosing exists, narrow index | Moving renal function | Dominant-negative truncate; digoxin toxicity | c.2210 allele fraction by ddPCR plus an 82 kDa band in fibroblasts | Three unmeasured facts behind a narrow-index drug; the first is testable in a dish |

## 2. Creative ideas adopted and rejected

Adopted. A1, ex vivo only. A10, as rank 1, qualified that its data are engineered knockdowns. A8, only if T4 shows the destabilising class. B1, the six-gene interferon score, as the gate on any cGAS-STING idea. B3 and J4, amiloride, into rank 2. C1 and J3, parental lymphocytes first, since each parent is a single-allele control. C2, dish before child. D's pharmacogenetic clearances. F's arithmetic, which puts interphase FISH ahead of micronucleus counting. H's rule that feeding precedes any new drug. J12, the avoid list read backwards off labels.

Rejected. A2, amlexanox: micromolar potency, no reachable exposure. A3, ataluren: the -1 base is G, the weakest context in Floquet 2012 (PMID 22479203), and the EU authorisation lapsed 28 March 2025. A4, caffeine citrate: supratherapeutic concentrations needed. A5, A6, A7 and B8 (arimoclomol, teprenone, phenylbutyrate, acipimox): each aims at a destabilisation premise T4 has not tested. A9, low-dose paclitaxel: the published directions are opposite and the one measured in this genotype class is harmful. B6, pulsed dasatinib: the published senolytic is a pair whose partner is a supplement. B7, lamivudine: the cytosolic DNA here is micronuclear. C5 and G1, NAD+ precursors: the K668 route assumes a SIRT2 axis T3 and T4 have not established, and the lifespan result is contradicted (PMID 38009412). J2 and J5: no approved agent named, no measured spurt rhythm.

## 3. Exclusions

Quercetin, fisetin, NMN and nicotinamide riboside: supplements, out of scope. Navitoclax, AICAR, 17-AAG, Mps1/TTK, Aurora B, PLK1 and KIF18A inhibitors: not approved, the last four harmful in a SAC-weak child. Pimitespib: Japan only, and HSP90 inhibition accelerates turnover of the only BubR1 he makes. Proteasome inhibitors: they raise BubR1 but block mitotic exit. Systemic aminoglycosides: nephrotoxicity, for a codon context predicted to respond poorly. Acetazolamide and topiramate: hypercalciuria (PMC5976810). Hydroxyurea: it raises micronucleated reticulocytes and corrupts the T5 readout.

## 4. Strongest objection to my own top candidate

The avoidance rule may have the sign wrong. Suppressing BUBR1 produces paclitaxel resistance, not hypersensitivity (Sudo 2004, PMID 15059905), and a CRISPR screen found BUB1B knockdown attenuates paclitaxel-induced death (dossier 02, 4). The two disagree because one counts segregation errors and the other counts killing, and neither used MVA cells: dossier 01, 4.3 records that no study shows MVA cells are hypersensitive to any aneugen. A wrong sign could cost a child a vincristine backbone carrying 90% five-year survival at low risk. The rule must therefore cover elective non-oncological aneugens only, with the ex vivo test run before it is cited against a cancer regimen.

## 5. What would change the ranking

Phase in cis (T1) voids the list. An inefficiently degraded c.2210 transcript with a detectable 82 kDa band (T2, T3) moves rank 6 to the head of the mechanism-facing candidates. Wild-type-like turnover for N1002K (T4) removes the premise from the chaperone and NAD+ arm and reframes the deficit as transcript loss, not misfolding. Residual BubR1 at or above the parental heterozygote level (T3) returns the case to variant interpretation. Normal PCS and micronucleus frequency (T5) drops ranks 4 and 5 below rank 6. Elevated p16 (T6) gives the senolytic hypothesis its first human baseline. A per-genotype tumour fraction for MVA1, which no source reports (dossier 01, 7), would change how much risk is worth accepting.
