# C. Analogies, non-drug interventions, and trial designs that make an N-of-1 interpretable

Directions 7, 8 and 9 of PROMPT_track2_creative.md, written without reading track2/panel/. Evidence tiers: human, animal, cell, inference. Nothing here is evidence that a medicine works. Directions 7 and 9 yield arguments and designs rather than molecules, so for those entries the "step" field names the inferential step acted on. Named drugs are outside the excluded list.

---

## Ranked ideas

### 1. Use the two parents as allele-specific within-family controls, not as a single carrier control

**Step.** Each parent carries exactly one of the two alleles: one c.2210T>G p.Leu737Ter, one p.Asn1002Lys. Any allele-directed intervention has a predicted asymmetry between them.
**Intervention.** Any allele-directed candidate, including readthrough or NMD-modulating agents, tested first in adults who consent for themselves.
**Evidence tier.** Human for the assay: carrier parents show premature chromatid separation in 3.5 to 41.7% of lymphocytes (Kajii 2001, PMID 11746029), and parental lines show intermediate BubR1 by quantitative immunoblot (Suijkerbuijk 2010, PMID 20516114). Inference for the asymmetry prediction.
**Why it might fail.** Phase is unproven in the child, and the parents' single-allele state may sit above the assay's sensitivity range, giving no measurable movement in either direction.
**Measurement.** Paired PCS rate per 50 metaphases and quantitative BubR1 immunoblot in each parent, on and off drug, read blind to which parent carries which allele.

### 2. Run the N-of-1 in a dish before running it in the child

**Step.** Convert a mechanism hypothesis into a falsifiable pre-gate using patient and parent cells rather than patient exposure.
**Intervention.** Ex vivo exposure of PHA-stimulated patient lymphocytes and a parental line to each shortlisted approved drug at achievable plasma concentrations.
**Evidence tier.** Cell. The rescue direction is established: forced expression of poorly expressed MVA missense alleles to wild-type levels fully restored the nocodazole response (Suijkerbuijk 2010, PMID 20516114).
**Why it might fail.** Cultured lymphocytes are not muscle, kidney or growth plate, and the readout is a 72-hour culture, so a drug acting through weeks-long tissue remodelling scores as inactive.
**Measurement.** Fold change in BubR1 protein and in PCS frequency versus vehicle, with a pre-declared threshold below which the drug does not advance to in-vivo testing.

### 3. Pick a biomarker whose turnover matches the crossover, which lymphocyte PCS does not

**Step.** Crossover period length must exceed the turnover time of the cell pool being sampled, or a real effect is unreadable.
**Intervention.** Flow-cytometric micronucleated reticulocyte frequency as the primary cellular endpoint, with lymphocyte PCS as a secondary.
**Evidence tier.** Human, from a paediatric setting: micronucleated reticulocytes were tracked serially in infants on hydroxyurea in BABY-HUG, rising by three months without further escalation over twelve years (PMC3277805; PMID 20230905).
**Why it might fail.** Micronuclei have both aneugenic and clastogenic origins, so the readout is not specific to spindle checkpoint failure, and anaemia or transfusion collapses the reticulocyte pool.
**Measurement.** Micronucleated reticulocytes per 10^6, monthly, with each crossover period set at eight weeks and a two-week washout, keyed to marrow rather than memory-lymphocyte turnover.

### 4. One shared aggregated N-of-1 protocol across the roughly 40 known patients, held by the MVA Society

**Step.** A single N-of-1 in an ultra-rare disease is uninterpretable in isolation; a series of identically run N-of-1 trials is analysable.
**Intervention.** A protocol with randomised treatment-order, blinding and placebo where feasible, reported to the CENT 2015 standard (Vohra and Shamseer, BMJ 2015, PMID 25976398), following the aggregated model of Vrinten 2015 (PMID 26185179).
**Evidence tier.** Human, methodological. Around 40 known cases globally, roughly 25 in the UK and EU (mvasociety.org; NORD listing).
**Why it might fail.** Genotypic heterogeneity across MVA1, MVA2 and MVA3 means the pooled series may average away a real allele-specific effect.
**Measurement.** Number of centres returning a complete, protocol-conformant dataset within twelve months, reported before any efficacy analysis.

### 5. Niacin as the approved-medicine route to NAD+ repletion, in place of NMN or nicotinamide riboside

**Step.** SIRT2 is NAD+-dependent, deacetylates BubR1 and raises its stability; NMN raised NAD+ and BubR1 protein in mouse testis (North 2014, PMID 24825348).
**Approved drug.** Niacin (nicotinic acid), approved for dyslipidaemia and pellagra; NMN and nicotinamide riboside are supplements and are context only.
**Evidence tier.** Human for the NAD+ effect in muscle: niacin escalated to 750 to 1,000 mg/day raised blood NAD+ up to eightfold, brought patient muscle NAD+ to control level and increased muscle strength in adult-onset mitochondrial myopathy (Pirinen 2020, Cell Metab, PMID 32386566). Animal and inference for the BubR1 link; SIRT2 transgene extended BubR1^H/H median lifespan by 58% (North 2014) but SIRT2 overexpression did not extend lifespan in a later study (Wu 2023, PMID 38009412).
**Why it might fail.** Pirinen reported an anaemia tendency, and the trial was in adults; there is no paediatric dose, and NAD+ repletion has never been tested in a BubR1 model.
**Measurement.** Whole-blood NAD+ by LC-MS at baseline, week 4 and week 12, paired with BubR1 protein in stimulated lymphocytes.

### 6. Treat fasting avoidance as an intervention, not as background

**Step.** BubR1 loss changes the response to food withdrawal specifically. Whole-body and fat-body BubR1 depletion in Drosophila increased lipid degradation and shortened lifespan under fasting but not under feeding (Liu 2024, Aging, PMID 38334966).
**Intervention.** No drug. A written fasting-minimisation rule: shortest permitted pre-anaesthetic fast for the three-monthly renal ultrasound and any procedure, and no caloric restriction, time-restricted feeding or fasting-mimicking regimen.
**Evidence tier.** Animal (invertebrate), plus mouse fat loss and cachectic dwarfism in BubR1^H/H (Baker 2004, PMID 15208629), plus the child's documented failure to thrive.
**Why it might fail.** Drosophila fat body is not human adipose, and the mechanism runs through IMD/Relish signalling with no vertebrate confirmation.
**Measurement.** Weight-for-age z-score trajectory across procedure weeks versus non-procedure weeks.

### 7. Copy the Fanconi anaemia metformin design, not the drug

**Step.** The argument that carried it was feasibility-and-tolerability first, efficacy second, in a population too small to power an RCT.
**Intervention.** Design transfer. Single institution, 6 months, 14 non-diabetic patients, median age 9.4 years, primary endpoints feasibility and tolerability; 93% tolerated maximal dosing for age, response in 4 of 13 evaluable, median time to response 84.5 days (Blood Adv 2022, PMID 35500223).
**Evidence tier.** Human, methodological.
**Why it might fail.** Fanconi anaemia has a continuous, cheap, clinically meaningful endpoint in the blood count. MVA1 has no equivalent continuous endpoint, which is the gap this design transfer exposes rather than fills.
**Measurement.** Before any MVA trial: whether a candidate primary endpoint moves measurably in untreated MVA patients over 6 months.

### 8. Pre-register the falsification criterion, on the ataluren precedent

**Step.** A mechanism-first argument with an endpoint chosen after the fact does not survive re-evaluation.
**Intervention.** Ataluren reached EU conditional authorisation for nonsense-mutation Duchenne on a mechanistic argument; CHMP recommended non-renewal in January 2024 and again in June 2024, October 2024 and March 2025, and the European Commission did not renew the authorisation on 28 March 2025 (ema.europa.eu; ec.europa.eu newsroom item 834969).
**Evidence tier.** Human, regulatory.
**Why it might fail.** A pre-registered falsification threshold in a disease with no natural-history data will be set arbitrarily and may reject a real effect.
**Measurement.** A single pre-specified primary endpoint, its minimum clinically meaningful change and its stopping rule, filed publicly before first dose. Note that this precedent applies directly to any readthrough candidate proposed for the c.2210T>G allele.

### 9. Mine incidental drug exposures in the existing patients, on the propranolol logic

**Step.** The strongest paediatric repurposing signals have come from observation of a drug given for another reason, then formalised.
**Intervention.** No new drug. A structured retrospective capture, through the MVA Society, of every medicine each known patient has received, with dates, and of any coincident change in growth, infection frequency, seizure count or hospital days.
**Evidence tier.** Inference for MVA; human for the method (propranolol in infantile haemangioma; alpelisib in PROS built on compassionate-use data, EPIK-P1, NCT04285723).
**Why it might fail.** With roughly 40 patients, confounding by indication is close to unresolvable and the output is hypothesis-generating only.
**Measurement.** Patient-years of exposure per drug class, published as a denominator before any signal is claimed.

### 10. Build the natural-history control before choosing the drug

**Step.** Lonafarnib in progeria was approved against untreated natural-history comparators, not a randomised arm (Genet Med 2023, PMID 36507973).
**Intervention.** Prospective natural-history capture: growth velocity, lean mass, renal ultrasound findings, hospital days and infection episodes, on a fixed schedule, in all consenting known patients.
**Evidence tier.** Human, regulatory precedent.
**Why it might fail.** Progeria had a hard endpoint, survival, and an untreated cohort assembled over years. MVA1 has no pooled survival analysis at all, and outcomes are reported case by case.
**Measurement.** Within-patient variance of each candidate endpoint over 12 months untreated. Any endpoint whose noise exceeds the expected drug effect is disqualified before a trial is designed.

### 11. Fix exercise as a co-intervention, and note that it has never been tested here

**Step.** Muscle and fat are the earliest-affected tissues in BubR1 mice, carrying high p16^Ink4a (Baker 2008, PMID 18516091).
**Intervention.** Supervised, load-bearing physiotherapy held constant across crossover periods.
**Evidence tier.** Animal, and only as an outcome. A PubMed search on Bub1b or BubR1 with exercise, treadmill or running returns one record, Wijshake 2012 (PMID 23300461), where impaired exercise capacity is a phenotype. Treadmill distance in Baker 2011 (PMID 22048312) is likewise an outcome of senescent-cell clearance. No exercise intervention study in a BubR1 model exists. Caloric restriction in these models is equally absent.
**Why it might fail.** Sarcopenia predisposition in BubR1 carriers correlates with mTORC1 hyperactivity (Sieben 2020, PMID 31738183), so a loading stimulus that further raises mTORC1 has an argued-for opposite direction. Inference.
**Measurement.** Weekly physiotherapy minutes logged as a covariate; lean mass by DXA at each period boundary.

### 12. Pre-specify a negative-control outcome

**Step.** In an unblinded or partly unblinded N-of-1 with an involved family, observer drift affects all outcomes in the same direction.
**Intervention.** Design rule. Declare one outcome the drug should not change over the crossover period, for example height velocity across 8 weeks, alongside the primary.
**Evidence tier.** Inference, methodological.
**Why it might fail.** In a multi-system disease almost any outcome is defensibly on-pathway, so the negative control may be contested once the result is known, which is why it must be filed first.
**Measurement.** Change in the negative-control outcome, reported alongside the primary in every period.

---

## Ideas rejected during this round and why

**Nicotinamide as the NAD+ precursor.** It has the better paediatric-adjacent safety record and a phase 3 chemoprevention result at 500 mg twice daily (NEJM 2015, PMID 26488693), but nicotinamide inhibits sirtuins at high concentration, and the mechanism sought here runs through SIRT2 activity. Using it to raise BubR1 could be self-cancelling. Inference; not tested in this system. Niacin routes through NAPRT without that liability and was ranked instead.

**Caloric restriction, time-restricted feeding, or a fasting-mimicking diet.** No study of caloric restriction in any BubR1 model was found. The one relevant result runs the other way (PMID 38334966), and the child has documented failure to thrive. Entry 6 inverts this into fasting avoidance.

**Leucine or high-protein loading for low muscle mass.** Same mTORC1 objection as entry 11, without entry 11's mechanical benefit. Inference; no data in this model.

**Nicotinamide riboside and NMN.** Excluded by scope. They are supplements in both the US and EU, not market-approved medicines. Their value here is as a design precedent: the ataxia telangiectasia trials are the closest paediatric analogue, a genome-instability disorder in children with serial NAD+ measurement over two years (Presterud 2024, Mov Disord, PMID 37899683). That analogy is used in entries 3 and 5; the compounds themselves are not proposed.

**Parents as an efficacy control.** Carrier parents are not clinically affected and cannot show clinical benefit. They serve only as mechanism and specificity controls, which is what entry 1 restricts them to.

**A single-patient open-label trial with a clinical primary endpoint.** Rejected because no MVA endpoint has a published within-patient variance. Entry 10 is the prerequisite.

**Whole-body MRI surveillance as a trial endpoint.** No validated imaging-based rhabdomyosarcoma surveillance protocol for MVA exists; the current guideline recommends clinical review of systems (Nakano 2024, PMID 39264246), and any schedule would be extrapolated from Li-Fraumeni practice. It is a care question, not a measurable trial endpoint on a crossover timescale.
