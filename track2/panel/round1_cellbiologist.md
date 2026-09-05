# Round 1: mitosis / cell biology

Lens: which consequence of reduced BubR1 is addressable with a marketed medicine, what the *Bub1b* hypomorph licenses, and which approved drugs would worsen segregation.

## Framing before the list

Four consequences of reduced BubR1 are documented: (a) weakened SAC and raised mis-segregation; (b) aneuploidy with proteotoxic, energetic and autophagic stress; (c) p16^Ink4a-driven senescence in muscle, fat and eye; (d) p53/p21-limited proliferation of aneuploid cells and their immune clearance (01_mechanism_models.md §3, §5).

(a) is not druggable in the correcting direction. Nothing marketed raises BubR1 abundance, and the intervention that fixed segregation in the model, BubR1 overexpression, is genetic (01 §4.1). Both patient alleles act by lowering protein amount, not by making a poison (Suijkerbuijk 2010, PMID 20516114; 01 §1.3, §2.2), so a real fix is protein restoration, not receptor occupancy. That leaves (b), (c) and (d), and caps what any candidate below can claim.

The hypomorph licenses one claim: lowering senescent-cell burden improves muscle fibre diameter, fat mass, treadmill distance, cataract and lordokyphosis onset, late as well as early (Baker 2011, PMID 22048312; 01 §4.1). It does not license a lifespan claim (Baker 2011 found none), a senolytic-drug claim (no senolytic has been given to a BubR1 mouse; 01 §4.2, correction 1), or a tumour claim in either direction (Sieben 2020: H/H mice do not live long enough to score spontaneous tumours; 01 §3).

## Ranked candidates

**1. Dasatinib, intermittent low dose (BCR-ABL/SRC-family kinases; senolytic via survival-pathway dependence in senescent cells).** Target = consequence (c), the only one with a causal intervention in this gene model. Evidence tier: BubR1 mouse for the *target* (Baker 2008 PMID 18516091, Baker 2011); human-other for the *drug* (Hickson 2019, senescent-cell burden in diabetic kidney disease; 02 §5). Paediatric approval exists: FDA 9 Nov 2017 for Ph+ CML, weight-banded 40-100 mg daily (02 §5), so a hit-and-run schedule (Zhu 2015 / Xu 2018 design; 01 §4.2) has a dosing scaffold. Phenotype interaction: the label warns on effects on growth, colliding with short stature and failure to thrive; myelosuppression is unwelcome after chemotherapy; no renal signal. Harm I see: quercetin, the tested partner, is a supplement and out of scope, so dasatinib would run without the component that carried much of the published effect. Readout: p16^INK4A transcript in sorted T cells plus a muscle-function measure, the pairing used in NCT04733534 (02 §6). Rank 1 because the target, not the drug, has model-level causal support in *Bub1b* itself.

**2. Hydroxychloroquine (lysosomal acidification / autophagic flux).** Aneuploid cells run a TFEB lysosomal stress response and depend on autophagic degradation, and chloroquine was one of three aneuploidy-selective compounds in Tang 2011 (PMID 21315436; Santaguida 2015 PMID 26404941; 01 §5). Consequence (b). Evidence tier: cell. Paediatric dosing is established in rheumatology, 5 mg/kg actual body weight (02 §5). Phenotype interaction: MVA carries ocular anomalies including cataract, and HCQ retinopathy in children has no screening guideline, so the organ already at risk is the one the drug threatens. Harm: selective pressure against aneuploid cells in a constitutionally mosaic child may deplete functional tissue. Readout: aneuploid fraction by single-cell DNA-seq in blood, LC3-II/p62 in patient fibroblasts. Rank 2 because Tang's own description of chloroquine is the weakest of the three compounds ("not as dramatic").

**3. Sirolimus (mTORC1).** Sarcopenia predisposition in the allelic series correlates with mTORC1 hyperactivity (Sieben 2020, PMID 31738183; 01 §3), and mTOR inhibition is senomorphic. Evidence tier: inference from a mouse correlation; no rapamycin study exists in any BubR1 model (01 §4.2). Two objections from my side: aneuploid yeast grow better under rapamycin, so the drug may relieve rather than exploit proteotoxic stress (02 §5), and immunosuppression works against clearance of mis-segregating, SASP-positive cells (Santaguida 2017, PMID 28633018). Paediatric off-label use is routine in vascular anomalies (Adams 2016). Readout: p-S6 in PBMC, lean mass. Rank 3: plausible target, wrong-direction risk on two counts.

**4. Metformin (AMPK).** The approved stand-in for AICAR, the strongest of Tang's three compounds; metformin itself impaired accumulation of trisomy 13 and 16 cells (02 §5). Evidence tier: cell, and the AICAR-to-metformin substitution is labelled inference in 01 §7. Paediatric approval from age 10 only; lactic-acidosis risk rises with reduced renal function, and creatinine-based eGFR overestimates function at low muscle mass (02 §3). Readout: micronucleus frequency and aneuploid fraction. Rank 4: cheapest and safest of the aneuploidy-selective ideas, weakest mechanistic fidelity.

**5. Pimitespib (HSP90).** 17-AAG was the compound that inhibited proliferation of every aneuploid line at 100 nM and synergised with AICAR (Tang 2011), and aneuploid human cells are specifically impaired in HSP90-mediated folding (Donnelly 2014, PMID 25205676; 01 §5). Pimitespib is approved, but only in Japan and only for advanced GIST (01 §5), with no paediatric data. Note the trap: HSP90 stress itself induces aneuploidy (02 §5), and HSP90-dependent turnover is what governs destabilised BubR1 missense protein (Suijkerbuijk 2010, 01 §2.2), so inhibition could lower residual BubR1 further. Readout: mitotic error rate by live imaging in patient fibroblasts. Rank 5 on access and on that self-defeating mechanism.

**6. Potassium citrate ± hydrochlorothiazide.** Included as the floor: the only entry with an established paediatric indication matching a documented finding in this child (02 §3), no interaction with segregation, and no BubR1 hypothesis attached. Readout: urine calcium/creatinine, renal ultrasound.

## Excluded, one line each

- Vincristine, vinblastine, vinorelbine, paclitaxel, docetaxel: partial BubR1 reduction amplifies segregation errors under low-dose taxol (Janssen 2009, PMID 19855003; 01 §4.3). Unavoidable in RMS therapy, never a repurposing candidate.
- Colchicine, griseofulvin: approved aneugens, colchicine being the OECD TG 487 positive control (01 §4.3).
- Hydroxyurea: raises micronucleated reticulocytes (02 §5); adding a micronucleus inducer to a constitutional CIN disorder is unjustifiable.
- Growth hormone, mecasermin: growth signalling does not address a senescence-driven phenotype; no efficacy in MVA2; mecasermin is contraindicated with a malignancy history (02 §2, §5).
- Acetazolamide, topiramate: carbonic-anhydrase-driven hypercalciuria against established nephrocalcinosis (02 §3).
- Navitoclax, AICAR, 17-AAG, KIF18A and Mps1 inhibitors, fisetin, quercetin, NMN: not approved medicines; context only.

## Strongest objection to my own top candidate

Senescence in this child is plausibly protective, not pathogenic. Mis-segregation produces arrested cells with complex karyotypes, senescence features and pro-inflammatory signalling that recruits immune clearance (Santaguida 2017), and aneuploid proliferation is held back p53-dependently (Thompson & Compton 2010, PMID 20123995). Clearing p16-positive cells in a child whose reported cancer risk runs from 38.7% to about 75% (02 §1) may remove a brake on the karyotypically complex cells that matter. The locus is not one-directional: in the same mouse, p16 ablation helped and p19^Arf ablation made things worse (Baker 2008). Baker 2011 did not test tumour incidence.

## What would change my ranking

1. Residual BubR1 in this child's fibroblasts as a percentage of control, with a live-imaging mis-segregation rate and micronucleus frequency. No such percentage exists for any MVA patient (01 §2.2), and it sets which consequence dominates.
2. Functional data on p.Asn1002Lys: abundance and half-life versus wild type. Q921H, also inside the domain, behaved as wild type (01 §7), so position predicts nothing.
3. A senolytic given to BubR1^H/H or ^H/L1002P mice with tumour incidence as a co-primary endpoint. That experiment settles rank 1 against my own objection.
4. p16^INK4A burden measured in MVA patient tissue. Without it the senescence hypothesis rests on mouse muscle and fat.
5. Aneuploid-cell fraction by tissue. Blood shows no clone above ~10% (PROMPT_track2.md, Facts), so an aneuploidy-selective agent may have almost no target in the compartment where response is measurable, demoting candidates 2, 4 and 5 together.
