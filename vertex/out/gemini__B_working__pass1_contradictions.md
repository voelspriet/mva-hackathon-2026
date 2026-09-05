# gemini-3.1-pro-preview / B_working / pass1_contradictions

Here are the pairs of files from the corpus that state incompatible things about the same fact, along with what would have to be true for both statements to hold at once.

**Pair 1: Sirolimus formulation**
* **Statement 1:** "Sirolimus: same mechanism as everolimus without the paediatric formulation."
  *File:* `track2/panel/round1_geneticist.md`, Section: `Excluded`
* **Statement 2:** "Sirolimus has an oral solution and an established paediatric evidence base, including a prospective paediatric trial in complicated vascular anomalies"
  *File:* `track2/panel/round2_oncologist.md`, Section: `(c) Factual error in a round-1 file`
* **To be true at once:** The oral solution of sirolimus is not officially considered a "paediatric formulation" (e.g., it is an adult formulation used off-label in paediatrics), whereas everolimus has a specific, approved paediatric formulation.

**Pair 2: Dasatinib oral suspension approval**
* **Statement 1:** "Approved from age 1 for Ph+ chronic-phase CML, with a powder for oral suspension at 72 mg/m² approved alongside the tablet in November 2017"
  *File:* `track2/panel/round1_pharmacologist.md`, Section: `4. Dasatinib, intermittent senolytic monotherapy`
* **Statement 2:** "Authorised in the EU (X/0056/G, decision 2 July 2018) and not in the US, where every product on record is a tablet and the sub-10 kg exclusion has no alternative"
  *File:* `track2/panel/round4_grand_moderator.md`, Section: `4. The verified-fact table`
* **To be true at once:** The powder for oral suspension was approved in the US but is not currently on record, or the pharmacologist's source (OncLive) incorrectly reported an EU approval as a US approval, or the verified-fact table is incorrect.

**Pair 3: Hydroxychloroquine retinopathy risk**
* **Statement 1:** "retinopathy risk is low under age five"
  *File:* `track2/panel/round1_family.md`, Section: `3. Hydroxychloroquine.`
* **Statement 2:** "Those figures are exposure durations, not ages: risk negligible below 6 months and unlikely below 5 years of treatment at 5 mg/kg/day or less"
  *File:* `track2/panel/round2_cellbiologist.md`, Section: `(c) Factual error`
* **To be true at once:** The child in question started treatment at birth, so being "under age five" is synonymous with having "under 5 years of treatment".

**Pair 4: Enzyme-inducing antiepileptics**
* **Statement 1:** "45% of MVA1 children may need [enzyme-inducing antiepileptics]"
  *File:* `track2/panel/round1_pharmacologist.md`, Section: `Excluded`
* **Statement 2:** "The 45% is the seizure frequency (Pavone 2022, PMID 35804254; 02 §1), not the proportion on inducers"
  *File:* `track2/panel/round2_oncologist.md`, Section: `(a) Objections`
* **To be true at once:** 45% of MVA1 children have seizures, and all of those children might potentially need enzyme-inducing antiepileptics at some point, even if it is not the proportion currently on them or the first-line practice.

**Pair 5: Thiazide plus citrate visits**
* **Statement 1:** "the only entry addressing a present symptom with paediatric dosing, at zero extra visits."
  *File:* `track2/panel/round1_family.md`, Section: `1. Hydrochlorothiazide plus potassium citrate (the index renal finding).`
* **Statement 2:** "thiazide plus citrate needs serum potassium after initiation and after each increment, plus urine pH titration (02 §3), so it adds draws and home testing between the three-monthly scans."
  *File:* `track2/panel/round2_pharmacologist.md`, Section: `(a) Objections`
* **To be true at once:** The extra blood draws and home testing can be done without requiring extra *clinic visits* (e.g., done at home or at a local lab), or the "zero extra visits" refers to the long-term maintenance phase after the initial titration is complete.

**Pair 6: Dexrazoxane link**
* **Statement 1:** "Link: BubR1-insufficient mice die of cardiac failure even after senescent-cell clearance improves every other outcome... and BubR1^H/L1002P mice show low cardiac stress tolerance and an ECG J-point defect"
  *File:* `track2/panel/round1_oncologist.md`, Section: `1. Ranked candidates`
* **Statement 2:** "Dexrazoxane acts on topoisomerase IIβ and iron-mediated damage, so the organ overlaps and the mechanism does not; the tightness you claim for the link is not there."
  *File:* `track2/panel/round2_pharmacologist.md`, Section: `(a) Objections`
* **To be true at once:** The link is purely based on the organ (heart) being vulnerable in both BubR1 insufficiency and anthracycline use, even though the specific molecular mechanisms of damage are different.

**Pair 7: RMS 2005 outcomes**
* **Statement 1:** "Cyclophosphamide with mesna in place of ifosfamide (VAC rather than IVA)... both regimens are standard of care with comparable outcomes (COG 2023 Blueprint, PMC10519430; 02 §4)."
  *File:* `track2/panel/round1_oncologist.md`, Section: `1. Ranked candidates`
* **Statement 2:** "RMS 2005 randomised patients in remission after nine IVA-based cycles (02 §4), so that estimate sits downstream of ifosfamide induction; a VAC induction changes the population it came from."
  *File:* `track2/panel/round2_geneticist.md`, Section: `(a) Objections`
* **To be true at once:** VAC and IVA have comparable outcomes overall as standard of care regimens, but the specific survival benefit from vinorelbine maintenance in the RMS 2005 trial was measured in a population that specifically received IVA induction, so applying that maintenance benefit to a VAC-induced population is an extrapolation.

**Pair 8: cGAS-STING output**
* **Statement 1:** "cGAS-STING output from micronuclei is part of the clearance constraining aneuploid clones (Bakhoum 2018, PMID 29342134)."
  *File:* `track2/panel2/round1_cinbiologist.md`, Section: `2. Creative-round ideas`
* **Statement 2:** "Chronic cGAS-STING signalling in unstable tumour cells is pro-metastatic through non-canonical NF-kB (V2 §1, PMID 29342134)"
  *File:* `track2/panel/round4_grand_moderator.md`, Section: `4. The verified-fact table`
* **To be true at once:** cGAS-STING output from micronuclei constrains aneuploid clones in some contexts (e.g., early stages or untransformed cells) but chronic signalling in unstable tumour cells is pro-metastatic.

**Pair 9: BubR1 and aneuploid fitness**
* **Statement 1:** "raising BubR1 in every cell also raises aneuploid fitness"
  *File:* `track2/panel2/round1_cinbiologist.md`, Section: `2. Creative-round ideas`
* **Statement 2:** "Sustained high BubR1 reduces tumorigenesis "even in the presence of genetic alterations that strongly promote aneuplodization and cancer, such as oncogenic Ras", reduces aneuploidy and extends lifespan (V2 §2, PMID 23242215)"
  *File:* `track2/panel/round4_grand_moderator.md`, Section: `4. The verified-fact table`
* **To be true at once:** Raising BubR1 increases the fitness of individual aneuploid cells (allowing them to survive), but simultaneously reduces the overall rate of new aneuploidy generation and tumorigenesis at the organism level.

**Pair 10: RT-PCR phase**
* **Statement 1:** "one cDNA amplicon at single-molecule depth returns phase and allele ratio together."
  *File:* `track2/panel2/round1_labgeneticist.md`, Section: `0. Six unmeasured facts, in order of consequence`
* **Statement 2:** "under efficient decay phase cannot be read off a single molecule and must be inferred from the c.POS_B fraction."
  *File:* `track2/panel/final_labgeneticist.md`, Section: `1. Errors`
* **To be true at once:** The single cDNA amplicon returns phase directly when NMD is inefficient (both alleles present), but when NMD is efficient, phase is returned indirectly (inferred) from the allele ratio of the surviving transcripts.

**Pair 11: Nicotinamide renal impairment**
* **Statement 1:** "Accumulates in renal impairment (thrombocytopenia in dialysis trials): cap 100 mg/day below eGFR 45."
  *File:* `track2/creative/I_pharmacist.md`, Section: `Nicotinamide (prescription forms)`
* **Statement 2:** "Rejecting niacin and nicotinamide on dialysis-trial thrombocytopenia extrapolates from end-stage disease to preserved filtration."
  *File:* `track2/panel2/round2_predispositiononcologist.md`, Section: `(a) Objections`
* **To be true at once:** The thrombocytopenia was observed in dialysis trials (end-stage disease), and the pharmacist is extrapolating this risk to recommend a dose cap for moderate renal impairment (eGFR < 45), which the oncologist points out is an extrapolation.

**Pair 12: Ataluren availability**
* **Statement 1:** "Unlicensed everywhere here: named-patient import in DE (section 73(3) AMG), NL (artsenverklaring, IGJ), UK (MHRA notification); single-patient IND plus IRB in the US."
  *File:* `track2/creative/I_pharmacist.md`, Section: `Ataluren`
* **Statement 2:** "It remains authorised in Great Britain, PLGB 44221/0004, renewed 24/02/2026, after the EU decision; Northern Ireland follows EU law (V2 §4)"
  *File:* `track2/panel/round4_grand_moderator.md`, Section: `4. The verified-fact table`
* **To be true at once:** Great Britain is not considered part of "everywhere here" (which might refer to the specific countries listed, though UK is listed), or the authorisation in Great Britain does not constitute being "licensed", or the MHRA notification is required despite the authorisation.

**Pair 13: Metformin concentration**
* **Statement 1:** "OCT1 partitioning concentrates it in liver and gut rather than muscle or kidney parenchyma, so the gap widens (inference)."
  *File:* `track2/panel2/round1_pkpharmacologist.md`, Section: `3. Drugs excluded`
* **Statement 2:** "Metformin is cleared unchanged renally by OCT2 uptake at the proximal tubule basolateral membrane then MATE1 and MATE2-K secretion... Renal cortex sees multiples of plasma."
  *File:* `track2/panel2/round2_nephrologist.md`, Section: `(c) Factual error`
* **To be true at once:** OCT1 partitioning does not concentrate it in the kidney parenchyma, but OCT2 uptake does, so both statements about the specific transporters and their effects are technically true, even though the first implies it doesn't concentrate in the kidney at all.

**Pair 14: Patient alleles**
* **Statement 1:** "Both patient alleles act by lowering protein amount, not by making a poison (Suijkerbuijk 2010, PMID 20516114; 01 §1.3, §2.2)"
  *File:* `track2/panel/round1_cellbiologist.md`, Section: `Framing before the list`
* **Statement 2:** "Shown for neither allele; both are inference"
  *File:* `track2/panel/round4_grand_moderator.md`, Section: `4. Factual corrections established during the rounds`
* **To be true at once:** The alleles do act by lowering protein amount, but this is an inference that has not been directly shown experimentally for these specific alleles.

**Pair 15: Furosemide risk factor**
* **Statement 1:** "the index renal finding of prematurity, where furosemide is the strongest risk factor (PMID 19460127) and 61 to 90% resolve by 12 to 24 months (PMID 16705005; PMC9587072)"
  *File:* `track2/panel2/round1_nephrologist.md`, Section: `0. The premise the panel has to accept first`
* **Statement 2:** "PMID 19460127 is the preterm risk-factor study identifying furosemide and carries no resolution figure. The resolution numbers are two cohorts: 70 percent at 12 months and 90 percent at 24 months (PMID 16705005), and 61 percent at 12 to 18 months in a VLBW cohort (PMC9587072)."
  *File:* `track2/panel/final_nephrologist.md`, Section: `1. Errors`
* **To be true at once:** The first statement is a summary citing multiple papers for a combined claim, where PMID 19460127 supports the furosemide risk factor part, and the other two papers support the resolution figures, which the second statement clarifies.

**Pair 16: Exomiser HGVS**
* **Statement 1:** "c.ALLELE_A converts TTA to **TGA**, so p.ALLELE_A is a **UGA** premature termination codon."
  *File:* `track2/creative/A_allele_expression_segregation.md`, Section: `0. The stop-codon context, determined from the reference sequence`
* **Statement 2:** "Codon 737 is TTA at c.2209 to c.2211, so c.ALLELE_A gives TGA while c.2209T>G would give GTA, valine (creative A section 0). The Exomiser HGVS is wrong."
  *File:* `track2/panel/final_labgeneticist.md`, Section: `1. Errors`
* **To be true at once:** c.ALLELE_A is a mutation that results in TGA (e.g., c.2210T>G), whereas the Exomiser file incorrectly lists the mutation as c.2209T>G which would result in GTA.
