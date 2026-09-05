# Round 1: clinical geneticist

Lens: what this genotype does and does not establish, and which drug claims survive once the unmeasured steps are removed.

## Genotype constraints that bound every candidate

1. **Phasing is assumed, not shown.** No parental testing or read-backed phasing is reported (PROMPT_track2.md, 04_exomiser_model2.md); Exomiser's AR comp-het is a model. In cis, the child is a carrier and the relevant models are BubR1^+/- and ^+/GTTA (Wijshake 2012, PMID 23300461), not the biallelic state.
2. **Residual BubR1 is unmeasured.** 01_mechanism_models.md §2.2: fold-changes only, no published patient percentage, and the quoted 6% and 13% thresholds come from a HeLa shRNA titration. The one quantified figure (~10%) is murine.
3. **The missense allele is a VUS with no functional data** (ClinVar VCV004600147.1, single submitter, condition "Inborn genetic diseases"; 01 §2.4). Position does not predict class: Q921H sits in the same domain and behaved as wild type in Suijkerbuijk 2010 (PMID 20516114). N1002 lying six residues from PLK1 site T1008 (00_variant_context.md) is a hypothesis, not evidence.
4. **NMD of p.Leu737Ter is inferred from transcript geometry** (PTC 747 nt upstream of the last junction; 01 §2.1), not measured. That allele is in no published MVA patient and sits at gnomAD v4 AF 7.87e-5 with 115 heterozygotes (01 §2.4).

Phenotype-side: mosaic aneuploidy was not detected above ~10% of cells. Any drug whose selectivity depends on an aneuploid population has an unverified target here.

Consequence: candidates justified by a measured feature of this patient outrank candidates justified by a chain of inferences through BubR1 dose.

## Ranked list

**1. Potassium citrate, plus hydrochlorothiazide only if hypercalciuria is documented.** Target: urinary citrate and calcium, not BubR1. 02_clinical_care_drugs.md §1 found no report of nephrocalcinosis as an MVA feature, so it is worked up on its own merits. Tier: human other (02 §3; Seikaly 2001, PMID 11433085). Paediatric dosing established: potassium citrate 0.1-0.2 g/kg/day, HCTZ 0.5-1 mg/kg/day divided. Interaction: hypokalaemia and volume depletion are less well tolerated with failure to thrive; creatinine-based eGFR overestimates function at low muscle mass, so dose on cystatin C (02 §3). Harm: alkalinisation above urine pH 7.5 precipitating calcium phosphate; hypokalaemia. Readout: urine calcium/creatinine, urine citrate, serum potassium and bicarbonate, renal ultrasound at baseline and 6 months. Rank: the only entry whose target is measured in this child.

**2. Deferred pharmacotherapy pending three assays: BubR1 immunoblot on patient cells, PCS/micronucleus karyotype, parental phasing.** It competes for the same slot as entries 3-6. Harm: delay, plus a blood draw or biopsy. Rank: every claim below changes if BubR1 is near-normal or the variants are in cis.

**3. Hydroxychloroquine.** Target: autophagic/lysosomal degradation, one of three aneuploidy-selective compounds in Tang 2011 (PMID 21315436), supported by Santaguida 2015 (PMID 26404941). Tier: cell only, and Tang calls chloroquine the least effective of the three. Paediatric dosing from rheumatology, 5 mg/kg actual body weight, max 400 mg (02 §5). Interaction: retinopathy risk with no paediatric screening guideline, against MVA's own ocular pathology (cataract, corneal opacity, glaucoma; Orphanet ORPHA 1052), which confounds monitoring. Readout: micronucleus frequency and PCS rate in lymphocytes, before and during. Rank: the only approved drug with a published aneuploidy-selective signal, but the target is undemonstrated in this child.

**4. Metformin.** Target: AMPK, standing in for AICAR, which is not approved. Tier: inference plus cell. Tang 2011 reports impaired accumulation of trisomy 13 and 16 cells; 01 §4.2 records that no study tests metformin for aneuploidy-selective killing. Approved from age 10 for T2DM; paediatric oncology phase I at 666-2000 mg/m²/day (02 §6). Interaction: lactic acidosis risk rises if nephrocalcinosis reduces renal function; GI intolerance against failure to thrive. Harm: appetite and weight loss in a child already failing to thrive. Readout: micronucleus frequency, with weight velocity as a stopping rule. Rank: below HCQ because the link is substitution of one AMPK activator for another, labelled inference.

**5. Dasatinib, senolytic arm, without quercetin.** Target: senescent-cell clearance, keyed to p16^Ink4a as effector in BubR1^H/H muscle and fat (Baker 2008, PMID 18516091; Baker 2011, PMID 22048312). Tier: BubR1 mouse for the genetic intervention, human other for the drug. 01 §4.2 corrects the standard error: D+Q was tested in Ercc1 and aged mice, never in BubR1^H/H, and quercetin is a supplement with a renal-toxicity signal, so the studied combination cannot be reproduced with approved products. Paediatric dosing exists (Ph+ CML, 40-100 mg by weight band, FDA 2017). Interaction: labelled warning on effects on growth, in a child with short stature; myelosuppression in a child with cancer predisposition and MDS/AML reported in MVA1. Readout: blood p16^INK4A, grip strength, lean mass by DXA. Rank: strongest mouse-genetic rationale in the file, weakest bridge from that mouse's known BubR1 level to this child's unknown one.

**6. Everolimus, low dose.** Target: mTORC1, on Sieben 2020's correlation between sarcopenia predisposition and mTORC1 hyperactivity (01 §3). Tier: BubR1 mouse, correlative; no mTOR inhibitor has been given to any BubR1 model. Approved from age 1 for TSC-associated SEGA, 4.5 mg/m²/day to trough 5-15 ng/mL (02 §5). Interaction: immunosuppression in a child whose one published MVA1 HSCT ended in fatal sepsis (Laberko 2019, PMID 31053147); stomatitis 43% in EXIST-1. Harm: infection, and mTOR inhibition may relieve rather than aggravate the proteotoxic stress that limits aneuploid-cell fitness (yeast data, 02 §5), which points the wrong way. Rank: last, concrete harm against a mouse correlation.

## Excluded

- **Recombinant GH**: no efficacy in MVA2, no MVA1 data, cancer predisposition treated as contraindication (02 §2).
- **Mecasermin**: FDA label contraindicates it with a history of malignancy (02 §5).
- **Vitamin D beyond deficiency correction**: unsafe with hypercalciuria; high-dose intermittent dosing has caused nephrocalcinosis (02 §3).
- **Acetazolamide, topiramate**: carbonic anhydrase inhibition promotes hypercalciuria and stones (02 §3).
- **Hydroxyurea**: raises micronucleated reticulocytes (02 §5), inverting the readout I use to judge every other candidate.
- **Colchicine, griseofulvin, vinca alkaloids, taxanes outside cancer therapy**: approved aneugens (01 §4.3). Vinca and dactinomycin inside RMS treatment are an oncology decision, not a repurposing candidate.
- **Navitoclax, fisetin, quercetin, AICAR, 17-AAG, NMN, nicotinamide riboside, resveratrol**: not approved medicines, out of scope.
- **Sirolimus**: same mechanism as everolimus without the paediatric formulation.

## Strongest objection to my own top candidate

Potassium citrate treats nephrocalcinosis, and nephrocalcinosis has not been shown to be part of MVA1 at all (02 §1). My top entry is therefore not a BUB1B repurposing hypothesis: it is standard paediatric nephrology any competent team would already have started, and it does nothing about aneuploidy, senescence or tumour risk. My defence is that the brief ranks on evidence and this is the only chain whose every link is measured in this patient. It also fails a second test: if the nephrocalcinosis is ifosfamide tubulopathy from prior RMS therapy, the alkali choice changes.

## What would change my ranking

- **BubR1 immunoblot in patient cells.** Near-normal levels demote entries 4-6 to zero and reopen the diagnosis; low-end levels move entry 5 up.
- **Phasing.** Trans firms the frame; cis collapses it.
- **A functional assay on p.Asn1002Lys** in the Suijkerbuijk 2010 design (expression, turnover, nocodazole response under forced expression). A wild-type-like result, as for Q921H, makes this a monoallelic case.
- **PCS/micronucleus karyotype.** A high PCS fraction (Kajii 2001 range 48.5-83.2%, PMID 11746029) gives entries 3 and 4 a measured target and a within-patient readout; a near-normal fraction removes it.
- **Any approved drug tested in a BubR1 model.** No senolytic, mTOR inhibitor or AMPK activator has been given to a BubR1 mouse (01 §4.1-4.2); one such experiment outranks every inference above.
- **A per-genotype tumour fraction in MVA.** None is published (01 §7); it sets how much harm is acceptable against a hypothetical risk reduction.
