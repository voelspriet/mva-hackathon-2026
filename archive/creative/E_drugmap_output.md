# Drug map for BUB1B

Generated 2026-09-05 01:30 UTC by pipeline/track2_drugmap/drugmap.py. Run time 0 s, 0 live HTTP calls (cached responses not counted).

API status: opentargets: ok, chembl: ok, openfda: ok.

## Inputs

- Gene: BUB1B (ENSG00000156970), https://platform.opentargets.org/target/ENSG00000156970

- CDKN2A/p16 senescence: CDKN2A (ENSG00000147889), CDK4 (ENSG00000135446), CDK6 (ENSG00000105810), BCL2 (ENSG00000171791), BCL2L1 (ENSG00000171552). p16 itself is undruggable; CDK4/6 sit directly downstream, BCL2 family are the senolytic axis (navitoclax class).
- autophagy/lysosome: TLR7 (ENSG00000196664), TLR9 (ENSG00000239732), PIK3C3 (ENSG00000078142), ULK1 (ENSG00000177169), TFEB (ENSG00000112561), ATP6V1A (ENSG00000114573). Chloroquine and hydroxychloroquine carry TLR7/TLR9 as their ChEMBL mechanism target; autophagy inhibition has no protein target in ChEMBL. Direction asked: antagonist/inhibitor (chloroquine class); TLR7 agonists such as imiquimod are the opposite direction and get demoted.
- AMPK: PRKAA1 (ENSG00000132356), PRKAA2 (ENSG00000162409), PRKAB1 (ENSG00000111725). Metformin's ChEMBL mechanism is mitochondrial complex I, so it will not appear under AMPK. Searched separately by name in the seed list.
- mTORC1: MTOR (ENSG00000198793), RPTOR (ENSG00000141564), FKBP1A (ENSG00000088832). Rapalogs (sirolimus, everolimus, temsirolimus) are filed under FKBP1A in ChEMBL, not MTOR.
- HSP90: HSP90AA1 (ENSG00000080824), HSP90AB1 (ENSG00000096384), HSP90B1 (ENSG00000166598), TRAP1 (ENSG00000126602). Pimitespib is approved in Japan only; Open Targets clinical stage may or may not reflect PMDA.
- SIRT2: SIRT2 (ENSG00000068903), SIRT1 (ENSG00000096717), NAMPT (ENSG00000105835). NAD+ axis added via SIRT1/NAMPT.
- cGAS-STING: CGAS (ENSG00000164430), STING1 (ENSG00000184584), TBK1 (ENSG00000183735), IRF3 (ENSG00000126456). Direction asked: antagonist (dampen sterile inflammation from micronuclei); STING agonists are oncology candidates and the opposite direction.
- NMD/readthrough: UPF1 (ENSG00000005007), SMG1 (ENSG00000157106), SMG5 (ENSG00000198952), SMG6 (ENSG00000070366), SMG7 (ENSG00000116698). Readthrough compounds (ataluren, aminoglycosides) have no human protein target in ChEMBL; searched by name in the seed list.
- Seed drugs (mechanism classes without a ChEMBL protein target): AMPK: metformin; autophagy/lysosome: chloroquine, hydroxychloroquine; NMD/readthrough: ataluren, gentamicin; SIRT2: niacin, nicotinamide
- Interaction partners of BUB1B at score >= 0.9: 76 (ANAPC1, ANAPC10, ANAPC11, ANAPC13, ANAPC15, ANAPC16, ANAPC2, ANAPC4, ANAPC5, ANAPC7, ASPM, AURKB, BIRC5, BRCA2, BUB1, BUB3, CCNB1, CCNB2, CDC16, CDC20, CDC23, CDC26, CDC27, CDCA8, CDK1, CENPA, CENPE, CENPF, CEP55, DLGAP5, ESPL1, FOXM1, FZR1, KIF11, KIF20A, KIF2C, KIF4A, KNL1, MAD1L1, MAD2L1, MELK, MIS12, MKI67, MXI1, NCAPG, NDC80, NEK2, NUF2, NUSAP1, PBK, PLK1, PLK4, PPP2CA, PPP2R5A, PPP2R5C, PPP2R5D, PTTG1, RAD51, RAE1, SGO1, SKA1, SKA2, SKA3, SPAG5, SPC25, SPDL1, TACC3, TOP2A, TPX2, TRIM33, TRIP13, TTK, UBE2C, ZW10, ZWILCH, ZWINT)

## Drugs per target (Open Targets drugAndClinicalCandidates)

| Target | Role | Candidates (any stage) | Approved names |
|---|---|---|---|
| [ATP6V1A](https://platform.opentargets.org/target/ENSG00000114573) | consequence: autophagy/lysosome | 0 | - |
| [AURKB](https://platform.opentargets.org/target/ENSG00000178999) | partner | 18 | - |
| [BCL2](https://platform.opentargets.org/target/ENSG00000171791) | consequence: CDKN2A/p16 senescence | 7 | NAVITOCLAX, OBLIMERSEN, VENETOCLAX |
| [BCL2L1](https://platform.opentargets.org/target/ENSG00000171552) | consequence: CDKN2A/p16 senescence | 3 | NAVITOCLAX |
| [BIRC5](https://platform.opentargets.org/target/ENSG00000089685) | partner | 2 | - |
| [BUB1B](https://platform.opentargets.org/target/ENSG00000156970) | gene | 0 | - |
| [CDK1](https://platform.opentargets.org/target/ENSG00000170312) | partner | 12 | - |
| [CDK4](https://platform.opentargets.org/target/ENSG00000135446) | consequence: CDKN2A/p16 senescence | 17 | ABEMACICLIB, PALBOCICLIB, RIBOCICLIB, TRILACICLIB |
| [CDK6](https://platform.opentargets.org/target/ENSG00000105810) | consequence: CDKN2A/p16 senescence | 12 | ABEMACICLIB, PALBOCICLIB, RIBOCICLIB, TRILACICLIB |
| [CDKN2A](https://platform.opentargets.org/target/ENSG00000147889) | consequence: CDKN2A/p16 senescence | 0 | - |
| [CGAS](https://platform.opentargets.org/target/ENSG00000164430) | consequence: cGAS-STING | 0 | - |
| [FKBP1A](https://platform.opentargets.org/target/ENSG00000088832) | consequence: mTORC1 | 7 | EVEROLIMUS, PIMECROLIMUS, SIROLIMUS, TACROLIMUS ANHYDROUS, TEMSIROLIMUS, ZOTAROLIMUS |
| [HSP90AA1](https://platform.opentargets.org/target/ENSG00000080824) | consequence: HSP90 | 10 | - |
| [HSP90AB1](https://platform.opentargets.org/target/ENSG00000096384) | consequence: HSP90 | 10 | - |
| [HSP90B1](https://platform.opentargets.org/target/ENSG00000166598) | consequence: HSP90 | 0 | - |
| [IRF3](https://platform.opentargets.org/target/ENSG00000126456) | consequence: cGAS-STING | 0 | - |
| [KIF11](https://platform.opentargets.org/target/ENSG00000138160) | partner | 4 | - |
| [MTOR](https://platform.opentargets.org/target/ENSG00000198793) | consequence: mTORC1 | 26 | PERHEXILINE, RIDAFOROLIMUS |
| [NAMPT](https://platform.opentargets.org/target/ENSG00000105835) | consequence: SIRT2 | 3 | - |
| [PIK3C3](https://platform.opentargets.org/target/ENSG00000078142) | consequence: autophagy/lysosome | 0 | - |
| [PLK1](https://platform.opentargets.org/target/ENSG00000166851) | partner | 8 | - |
| [PLK4](https://platform.opentargets.org/target/ENSG00000142731) | partner | 3 | - |
| [PPP2CA](https://platform.opentargets.org/target/ENSG00000113575) | partner | 1 | - |
| [PRKAA1](https://platform.opentargets.org/target/ENSG00000132356) | consequence: AMPK | 1 | ACADESINE |
| [PRKAA2](https://platform.opentargets.org/target/ENSG00000162409) | consequence: AMPK | 1 | ACADESINE |
| [PRKAB1](https://platform.opentargets.org/target/ENSG00000111725) | consequence: AMPK | 1 | ACADESINE |
| [RPTOR](https://platform.opentargets.org/target/ENSG00000141564) | consequence: mTORC1 | 1 | - |
| [SIRT1](https://platform.opentargets.org/target/ENSG00000096717) | consequence: SIRT2 | 1 | - |
| [SIRT2](https://platform.opentargets.org/target/ENSG00000068903) | consequence: SIRT2 | 0 | - |
| [SMG1](https://platform.opentargets.org/target/ENSG00000157106) | consequence: NMD/readthrough | 0 | - |
| [SMG5](https://platform.opentargets.org/target/ENSG00000198952) | consequence: NMD/readthrough | 0 | - |
| [SMG6](https://platform.opentargets.org/target/ENSG00000070366) | consequence: NMD/readthrough | 0 | - |
| [SMG7](https://platform.opentargets.org/target/ENSG00000116698) | consequence: NMD/readthrough | 0 | - |
| [STING1](https://platform.opentargets.org/target/ENSG00000184584) | consequence: cGAS-STING | 1 | - |
| [TBK1](https://platform.opentargets.org/target/ENSG00000183735) | consequence: cGAS-STING | 0 | - |
| [TFEB](https://platform.opentargets.org/target/ENSG00000112561) | consequence: autophagy/lysosome | 0 | - |
| [TLR7](https://platform.opentargets.org/target/ENSG00000196664) | consequence: autophagy/lysosome | 12 | HYDROXYCHLOROQUINE, IMIQUIMOD |
| [TLR9](https://platform.opentargets.org/target/ENSG00000239732) | consequence: autophagy/lysosome | 11 | HYDROXYCHLOROQUINE |
| [TOP2A](https://platform.opentargets.org/target/ENSG00000131747) | partner | 24 | AMRUBICIN, AMSACRINE, DAUNORUBICIN, DEXRAZOXANE, DOXORUBICIN, ETOPOSIDE, IDARUBICIN, MITOXANTRONE, PAZUFLOXACIN, TENIPOSIDE, VALRUBICIN, VOSAROXIN |
| [TRAP1](https://platform.opentargets.org/target/ENSG00000126602) | consequence: HSP90 | 0 | - |
| [TTK](https://platform.opentargets.org/target/ENSG00000112742) | partner | 2 | - |
| [ULK1](https://platform.opentargets.org/target/ENSG00000177169) | consequence: autophagy/lysosome | 0 | - |
| [UPF1](https://platform.opentargets.org/target/ENSG00000005007) | consequence: NMD/readthrough | 0 | - |

## Ranked: approved drugs acting on consequence targets or seeds (approved, pediatric section, fewest flags)

| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Direction | Pediatric-use section | Harm flags | Label | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | TRILACICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | Cyclin-dependent kinase 4 inhibitor (INHIBITOR) | Cyclin-dependent kinase 6 inhibitor (INHIBITOR) | match | present: safety/effectiveness not established | 0:  | COSELA 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL3894860) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3894860/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b3179c19-78f3-4bf1-b73e-7f7638522ab1) |
| 2 | ABEMACICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | Cyclin-dependent kinase 4 inhibitor (INHIBITOR) | Cyclin-dependent kinase 6 inhibitor (INHIBITOR) | match | present: pediatric information given | 1: myelosuppression | Verzenio 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL3301610) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3301610/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=be4bc0de-0fdc-4d46-8d25-be43c79e6a06) |
| 3 | NIACIN | SIRT2 | seed list | yes | US (FDA label found) |  | not checked | present: safety/effectiveness not established | 1: nephrotoxicity | Niacin 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL573) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL573/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8eff9205-84ac-e69d-e053-2995a90aad4b) |
| 4 | NIACINAMIDE | SIRT2 | seed list | yes | US (FDA label found) |  | not checked | present: pediatric information given | 1: nephrotoxicity | Vitafol Fe Plus 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL1140) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1140/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3927b074-d72a-4d8c-9f7e-15c42a830945) |
| 5 | RIBOCICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | Cyclin-dependent kinase 4 inhibitor (INHIBITOR) | Cyclin-dependent kinase 6 inhibitor (INHIBITOR) | match | present: pediatric information given | 1: myelosuppression | KISQALI 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL3545110) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3545110/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8) |
| 6 | CHLOROQUINE | autophagy/lysosome | seed list | yes | US (FDA label found) | Ferriprotoporphyrin IX binding agent (BINDING AGENT) | Ferriprotoporphyrin IX inhibitor (INHIBITOR) | match | present: pediatric information given | 3: malignancy;nephrotoxicity;retinal | Chloroquine Phosphate 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL76) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL76/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a342f72-45f9-3e12-e063-6394a90ae33e) |
| 7 | HYDROXYCHLOROQUINE | autophagy/lysosome | TLR7 (ENSG00000196664); TLR9 (ENSG00000239732); seed list | yes | US (FDA label found) | Ferriprotoporphyrin IX inhibitor (INHIBITOR) | Toll-like receptor 7 antagonist (ANTAGONIST) | Toll-like recept... | match | present: pediatric information given | 3: myelosuppression;nephrotoxicity;retinal | HYDROXYCHLOROQUINE SULFATE 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1535) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1535/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebe00e35-ed3d-40f4-9a93-a37b0da01ddb) |
| 8 | PALBOCICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | CDK6/cyclin D1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 4/cyclin D1 inhibitor (INHIBITOR) | match | present: pediatric information given | 3: growth;myelosuppression;nephrotoxicity | Ibrance 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL189963) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL189963/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792) |
| 9 | TEMSIROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | match | present: safety/effectiveness not established | 3: immunosuppression;myelosuppression;nephrotoxicity | Temsirolimus 2020 | [OT](https://platform.opentargets.org/drug/CHEMBL1201182) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1201182/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1c207bed-10e3-46f0-ad2c-69d5e5c97736) |
| 10 | EVEROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | match | present: safety/effectiveness not established | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Everolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1908360) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1908360/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c7bb6ba1-9a7f-43f5-b058-ef26d4b59221) |
| 11 | SIROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | match | present: safety/effectiveness not established | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Sirolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL413) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL413/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fc81cb86-61e1-4622-b2ce-cde263143aa0) |
| 12 | VENETOCLAX | CDKN2A/p16 senescence | BCL2 (ENSG00000171791) | yes | US (FDA label found) | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | match | present: pediatric information given | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Venclexta 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL3137309) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3137309/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b118a40d-6b56-cee3-10f6-ded821a97018) |
| 13 | ATALUREN | NMD/readthrough | seed list | yes | ChEMBL max_phase 4 only; no US label, no OT approval stage ( | 80S Ribosome modulator (MODULATOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL256997) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL256997/) |
| 14 | GENTAMICIN | NMD/readthrough | seed list | yes | US (FDA label found) | Bacterial 70S ribosome inhibitor (INHIBITOR) | match | absent | 1: nephrotoxicity | Gentamicin Sulfate 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL6067485) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL6067485/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=977180b3-a222-4282-d485-4a3217674305) |

## Approved but demoted: wrong action direction for the mechanism, or curated out in the config

| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Direction | Pediatric-use section | Harm flags | Label | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | METFORMIN | AMPK | seed list | yes | US (FDA label found) | Mitochondrial complex I (NADH dehydrogenase) inhibitor (INHIBITOR) | Mitochondrial glycerol-3-phosphate dehydr... | mismatch: drug is INHIBITOR, mechanism asks ACTIVATOR | present: pediatric information given | 1: nephrotoxicity | Metformin Hydrochloride 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1431) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1431/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=bfd6ec0f-8264-4877-aa6d-f347f53bc426) |
| 16 | IMIQUIMOD | autophagy/lysosome | TLR7 (ENSG00000196664) | yes | US (FDA label found) | Toll-like receptor 7 agonist (AGONIST) | mismatch: drug is AGONIST, mechanism asks ANTAGONIST/INHIBIT | present: safety/effectiveness not established | 2: immunosuppression;malignancy | Imiquimod 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL1282) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1282/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=59af8153-4cf8-4f22-9000-f239798d52d1) |
| 17 | PIMECROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | match; curated out (mTORC1: topical calcineurin inhibitor via FKBP12, not mTORC1) | present: pediatric information given | 2: immunosuppression;malignancy | Pimecrolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1200686) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1200686/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6601e43e-ce7d-446a-8568-8e7b24b86f06) |
| 18 | TACROLIMUS ANHYDROUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | match; curated out (mTORC1: binds FKBP12 but inhibits calcineurin, not mTORC1) | present: pediatric information given | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Tacrolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL269732) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL269732/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=213f6047-f897-48a7-b78a-45d7124f2f16) |
| 19 | PERHEXILINE | mTORC1 | MTOR (ENSG00000198793) | yes | approved somewhere per ChEMBL/Open Targets; no US prescripti | Carnitine O-palmitoyltransferase 1, muscle isoform inhibitor (INHIBITOR) | Carnitine palmitoyltransferase 2 in... | match; curated out (mTORC1: CPT1 inhibitor; MTOR listed as a secondary ChEMBL mechanism, n) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL75880) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL75880/) |

## Approved drugs acting on interaction partners of the gene (hazard class, listed for avoidance not use)

| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Direction | Pediatric-use section | Harm flags | Label | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20 | DOXORUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | not checked | present: safety/effectiveness not established | 1: malignancy | doxorubicin hydrochloride 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL53463) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL53463/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=55889588-c5f1-d9bc-e063-6294a90a5791) |
| 21 | ETOPOSIDE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA topoisomerase II inhibitor (INHIBITOR) | not checked | present: pediatric information given | 1: myelosuppression | Avopef 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL44657) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL44657/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=acc1e443-ef7b-486f-a638-710a20e81059) |
| 22 | ETOPOSIDE PHOSPHATE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | not checked | present: pediatric information given | 1: myelosuppression | Avopef 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1200645) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1200645/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=acc1e443-ef7b-486f-a638-710a20e81059) |
| 23 | VALRUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | not checked | present: safety/effectiveness not established | 1: myelosuppression | Valstar 2024 | [OT](https://platform.opentargets.org/drug/CHEMBL1096885) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1096885/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e96f30a0-6662-11de-8f80-0002a5d5c51b) |
| 24 | DAUNORUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | not checked | present: pediatric information given | 2: myelosuppression;nephrotoxicity | Daunorubicin Hydrochloride 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL178) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL178/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9705fa12-499e-41a3-8fb4-f6df0858b851) |
| 25 | DEXRAZOXANE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA topoisomerase II inhibitor (INHIBITOR) | Iron chelating agent (CHELATING AGENT) | Iron sequestering agent ... | not checked | present: safety/effectiveness not established | 2: malignancy;myelosuppression | Dexrazoxane 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL1738) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1738/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9cbd2987-10bb-eceb-153d-ee7be1ed0c84) |
| 26 | MITOXANTRONE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | not checked | present: safety/effectiveness not established | 2: growth;myelosuppression | Mitoxantrone 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL58) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL58/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=accf9569-4b57-4e83-a7db-4e890a75d1ba) |
| 27 | IDARUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | not checked | present: pediatric information given | 3: malignancy;myelosuppression;nephrotoxicity | Idamycin PFS 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1117) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1117/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a5a6d93-cc1e-4d7f-8da1-446c134503b3) |
| 28 | AMSACRINE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | approved somewhere per ChEMBL/Open Targets; no US prescripti | DNA topoisomerase II inhibitor (INHIBITOR) | not checked | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL43) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL43/) |
| 29 | TENIPOSIDE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | approved somewhere per ChEMBL/Open Targets; no US prescripti | DNA topoisomerase II inhibitor (INHIBITOR) | not checked | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL452231) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL452231/) |

## Not approved (context only)

| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Direction | Pediatric-use section | Harm flags | Label | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | ACADESINE | AMPK | PRKAA1 (ENSG00000132356); PRKAA2 (ENSG00000162409); PRKAB1 ( | no | Open Targets says APPROVAL but ChEMBL max_phase < 4 and no U | AMP-activated protein kinase, AMPK activator (ACTIVATOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1551724) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1551724/) |
| 31 | AFIMETORAN | autophagy/lysosome | TLR7 (ENSG00000196664) | no | not approved | Toll-like receptor 7 inhibitor (INHIBITOR) | Toll-like receptor 8 inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4650329) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4650329/) |
| 32 | AG-24322 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446) | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3545420) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3545420/) |
| 33 | ALVESPIMYCIN | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | Reactive oxygen species () | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL383824) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL383824/) |
| 34 | ALVOCIDIB | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL428690) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL428690/) |
| 35 | APG-2575 | CDKN2A/p16 senescence | BCL2 (ENSG00000171791) | no | not approved | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4650374) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4650374/) |
| 36 | APITOLISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1922094) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1922094/) |
| 37 | AT-7519 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL445813) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL445813/) |
| 38 | AZD-5438 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL488436) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL488436/) |
| 39 | AZD-8055 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1801204) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1801204/) |
| 40 | BAZLITORAN | autophagy/lysosome | TLR7 (ENSG00000196664); TLR9 (ENSG00000239732) | no | not approved | Toll-like receptor 7 antagonist (ANTAGONIST) | Toll-like receptor 8 antagonist (ANTAGONIST) | Toll-like recept... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297995) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297995/) |
| 41 | BGT-226 FREE BASE | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3218578) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3218578/) |
| 42 | BIIB021 | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL467399) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL467399/) |
| 43 | CC-115 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | DNA-dependent protein kinase inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3586573) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3586573/) |
| 44 | CD24FC | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock 70 kDa protein 1A/1B inhibitor (INHIBITOR) | Heat shock protein HSP90 inhibitor (INHIBITOR) | High ... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297717) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297717/) |
| 45 | DACTOLISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1879463) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1879463/) |
| 46 | DS-3078A | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3544963) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3544963/) |
| 47 | DS-7423 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3545248) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3545248/) |
| 48 | ENPATORAN | autophagy/lysosome | TLR7 (ENSG00000196664) | no | not approved | Toll-like receptor 7 antagonist (ANTAGONIST) | Toll-like receptor 8 antagonist (ANTAGONIST) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4802159) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4802159/) |
| 49 | GANETESPIB | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2103879) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2103879/) |
| 50 | GEDATOLISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL592445) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL592445/) |
| 51 | LUMINESPIB | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL252164) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL252164/) |
| 52 | MILCICLIB | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446) | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL564829) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL564829/) |
| 53 | NAVITOCLAX | CDKN2A/p16 senescence | BCL2 (ENSG00000171791); BCL2L1 (ENSG00000171552) | no | Open Targets says APPROVAL but ChEMBL max_phase < 4 and no U | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | Apoptosis regulator Bcl-W inhibitor (INHIBITOR) | Apoptosis ... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL443684) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL443684/) |
| 54 | OBATOCLAX | CDKN2A/p16 senescence | BCL2 (ENSG00000171791); BCL2L1 (ENSG00000171552) | no | not approved | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | Apoptosis regulator Bcl-W inhibitor (INHIBITOR) | Apoptosis ... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL408194) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL408194/) |
| 55 | OMIPALISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1236962) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1236962/) |
| 56 | ONALESPIB | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1214827) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1214827/) |
| 57 | ONATASERTIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3586404) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3586404/) |
| 58 | OSI-027 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3120215) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3120215/) |
| 59 | PALOMID-529 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2141712) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2141712/) |
| 60 | PANULISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | Serine... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL5095025) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL5095025/) |
| 61 | PF-04691502 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1234354) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1234354/) |
| 62 | PHA-793887 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1230607) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1230607/) |
| 63 | PKI-179 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase p110-alpha subunit inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITO... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1258517) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1258517/) |
| 64 | RETASPIMYCIN | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1184904) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1184904/) |
| 65 | RG-547 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446) | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL384304) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL384304/) |
| 66 | RG-7603 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2331680) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2331680/) |
| 67 | RGB-286638 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446) | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3545083) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3545083/) |
| 68 | RIDAFOROLIMUS | mTORC1 | MTOR (ENSG00000198793) | no | Open Targets says APPROVAL but ChEMBL max_phase < 4 and no U | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2103839) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2103839/) |
| 69 | RONICICLIB | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase inhibitor (INHIBITOR) | match | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4442620) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4442620/) |

(79 further unapproved candidates omitted; see CSV)

## Harm-flag evidence snippets (approved drugs)

**ABEMACICLIB** (Verzenio, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=be4bc0de-0fdc-4d46-8d25-be43c79e6a06)
- myelosuppression: ease oral fluids, and notify their healthcare provider. ( 2.2 , 5.1 ) Neutropenia: Monitor complete blood counts prior to the start of VERZENIO therapy

**NIACIN** (Niacin, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8eff9205-84ac-e69d-e053-2995a90aad4b)
- nephrotoxicity: Precautions ( 5.3 )] and should be used with caution in patients with renal impairment. Patients with a past history of jaundice, hepatobiliary disease, or

**NIACINAMIDE** (Vitafol Fe Plus, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3927b074-d72a-4d8c-9f7e-15c42a830945)
- nephrotoxicity: mia such as hyperparathyroidism and those who form calcium-containing kidney stones. High doses of vitamin D can lead to elevated levels of calcium that

**RIBOCICLIB** (KISQALI, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8)
- myelosuppression: each subsequent 4 cycles, and as clinically indicated. ( 2.2 , 5.5 ) Neutropenia: Perform complete blood count (CBC) before initiating therapy with KI

**CHLOROQUINE** (Chloroquine Phosphate, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a342f72-45f9-3e12-e063-6394a90ae33e)
- malignancy: s the benefit to the patient outweighs the potential risks. Potential Carcinogenic Risk Experimental data showed a potential risk of inducing gene mutat
- nephrotoxicity: scle or nerve toxicity is suspected or demonstrated by tissue biopsy. Renal Toxicity Proteinuria with or without a moderate reduction in glomerular filtra
- retinal: heir blood glucose level checked and treatment reviewed as necessary. Retinopathy 1 Irreversible retinal damage has been observed in some patients who

**HYDROXYCHLOROQUINE** (HYDROXYCHLOROQUINE SULFATE, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebe00e35-ed3d-40f4-9a93-a37b0da01ddb)
- myelosuppression: orphyria cutanea tarda. (5.5) • Hematologic Toxicity : Discontinue if myelosuppression occurs. (5.6) • Renal Toxicity : Consider phospholipidosis as a possi
- nephrotoxicity: ematologic Toxicity : Discontinue if myelosuppression occurs. (5.6) • Renal Toxicity : Consider phospholipidosis as a possible cause of renal injury in pa
- retinal: ing cardiomyopathy and ventricular arrhythmias were reported. (5.1) • Retinal Toxicity : Irreversible retinal damage is related to cumulative dosag

**PALBOCICLIB** (Ibrance, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792)
- growth: exposure [AUC] at the recommended dose) resulted in abnormalities in growing incisor teeth (discolored, ameloblast degeneration/necrosis, mononuclear cell
- myelosuppression: 5 WARNINGS AND PRECAUTIONS • Neutropenia: Monitor complete blood count prior to start of IBRANCE therapy and a
- nephrotoxicity: , lens degeneration), kidney (tubule vacuolation, chronic progressive nephropathy) and adipose tissue (atrophy) were identified in a 27 week repeat-dos

**TEMSIROLIMUS** (Temsirolimus, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1c207bed-10e3-46f0-ad2c-69d5e5c97736)
- immunosuppression: glucose and lipid profiles. ( 5.3 , 5.6 ) Infections may result from immunosuppression. ( 5.4 ) Monitor for symptoms or radiographic changes of interstitial
- myelosuppression: ns (≥20%) in pediatric patients receiving the 75 mg/m 2 dose included thrombocytopenia, infections, asthenia/fatigue, fever, pain, leukopenia, rash, anemia,
- nephrotoxicity: abdominal pain, bloody stools, and/or acute abdomen promptly. ( 5.7 ) Renal failure, sometimes fatal, has occurred. Monitor renal function at baseline an

**EVEROLIMUS** (Everolimus, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c7bb6ba1-9a7f-43f5-b058-ef26d4b59221)
- immunosuppression: WARNING: MALIGNANCIES and SERIOUS INFECTIONS; KIDNEY GRAFT THROMBOSIS; NEPHROTOXICITY; and MORTALITY IN HEART TRAN
- malignancy: WARNING: MALIGNANCIES and SERIOUS INFECTIONS; KIDNEY GRAFT THROMBOSIS; NEPHROTOXICITY; and
- myelosuppression: Drug Interactions (7) ] . 5.15 Thrombotic Microangiopathy/Thrombotic Thrombocytopenic Purpura/Hemolytic Uremic Syndrome The concomitant use of everolimus w
- nephrotoxicity: ARNING: MALIGNANCIES and SERIOUS INFECTIONS; KIDNEY GRAFT THROMBOSIS; NEPHROTOXICITY; and MORTALITY IN HEART TRANSPLANTATION WARNING: MALIGNANCIES and SER

**SIROLIMUS** (Sirolimus, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fc81cb86-61e1-4622-b2ce-cde263143aa0)
- immunosuppression: WARNING: IMMUNOSUPPRESSION, USE IS NOT RECOMMENDED IN LIVER OR LUNG TRANSPLANT PATIENTS Increase
- malignancy: Increased susceptibility to infection and the possible development of lymphoma and other malignancies may result from immunosuppression Increased su
- myelosuppression: Calcineurin Inhibitor-Induced. Hemolytic Uremic Syndrome/ Thrombotic Thrombocytopenic Purpura/ Thrombotic Microangiopathy (5.13) Embryo-Fetal Toxicity: Can
- nephrotoxicity: nd Healing (5.6) Hyperlipidemia (5.7) Decline in Renal Function (5.8) Proteinuria (5.9) Latent Viral Infections (5.10) Interstitial Lung Disease/Non-In

**VENETOCLAX** (Venclexta, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b118a40d-6b56-cee3-10f6-ded821a97018)
- immunosuppression: microbials and growth factors (e.g., G-CSF). 5.3 Infections Fatal and serious infections, such as pneumonia and sepsis, have occurred in patients treated with
- malignancy: ctors, particularly reduced renal function, tumor burden, and type of malignancy. Splenomegaly may also increase the risk of TLS in patients with CLL/
- myelosuppression: monitoring, hospitalization) as overall risk increases. ( 2.4 , 5.1 ) Neutropenia: Monitor blood counts. Interrupt dosing and resume at same or reduced
- nephrotoxicity: Lysis Syndrome Tumor lysis syndrome (TLS), including fatal events and renal failure requiring dialysis, has occurred in patients treated with VENCLEXTA [

**GENTAMICIN** (Gentamicin Sulfate, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=977180b3-a222-4282-d485-4a3217674305)
- nephrotoxicity: her aminoglycosides, Gentamicin Sulfate Injection, USP is potentially nephrotoxic. The risk of nephrotoxicity is greater in patients with impaired rena

**DOXORUBICIN** (doxorubicin hydrochloride, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=55889588-c5f1-d9bc-e063-6294a90a5791)
- malignancy: osome injection if HFS is severe and debilitating. 5.4 Secondary Oral Neoplasms Secondary oral cancers, primarily squamous cell carcinoma, have been

**ETOPOSIDE** (Avopef, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=acc1e443-ef7b-486f-a638-710a20e81059)
- myelosuppression: WARNING: SEVERE MYELOSUPPRESSION AVOPEF can cause severe myelosuppression resulting in infection or bl

**ETOPOSIDE PHOSPHATE** (Avopef, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=acc1e443-ef7b-486f-a638-710a20e81059)
- myelosuppression: WARNING: SEVERE MYELOSUPPRESSION AVOPEF can cause severe myelosuppression resulting in infection or bl

**VALRUBICIN** (Valstar, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e96f30a0-6662-11de-8f80-0002a5d5c51b)
- myelosuppression: ladder who received 800 mg of VALSTAR intravesically developed severe leukopenia and neutropenia approximately two weeks after drug administration [se

**DAUNORUBICIN** (Daunorubicin Hydrochloride, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9705fa12-499e-41a3-8fb4-f6df0858b851)
- myelosuppression: ears of age, or 10 mg/kg in children less than 2 years of age. Severe myelosuppression occurs when used in therapeutic doses; this may lead to infection or
- nephrotoxicity: ment. Evaluation of Hepatic and Renal Function Significant hepatic or renal impairment can enhance the toxicity of the recommended doses of daunorubicin hyd

**DEXRAZOXANE** (Dexrazoxane, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9cbd2987-10bb-eceb-153d-ee7be1ed0c84)
- malignancy: luated against the risk of producing irreversible cardiac damage. 5.4 Secondary Malignancies Secondary malignancies such as acute myeloid leukemia (AML) and myelo
- myelosuppression: 5 WARNINGS AND PRECAUTIONS • Myelosuppression: Dexrazoxane for Injection may increase the myelosuppresive effects o

**MITOXANTRONE** (Mitoxantrone, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=accf9569-4b57-4e83-a7db-4e890a75d1ba)
- growth: uring the organogenesis period of gestation was associated with fetal growth retardation at doses ≥0.1 mg/kg/day (0.01 times the recommended human dose on a m
- myelosuppression: of less than 1,500 cells/mm 3 . In order to monitor the occurrence of bone marrow suppression, primarily neutropenia, which may be severe and result in infection,

**IDARUBICIN** (Idamycin PFS, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a5a6d93-cc1e-4d7f-8da1-446c134503b3)
- malignancy: WARNING: CARDIOMYOPATHY, SECONDARY MALIGNANCIES, and EXTRAVASATION AND TISSUE NECROSIS • Cardiomyopathy: IDAMYCIN PFS
- myelosuppression: n if extravasation occurs. ( 2.6 , 5.3 ) 5 WARNINGS AND PRECAUTIONS • Myelosuppression : Severe myelosuppression resulting in severe infection, septic shock
- nephrotoxicity: ypersensitivity reactions and manage as clinically indicated. (5.6) • Renal Impairment : Assess renal function prior to and during treatment. Reduce the dos

## Method notes

- Approval = ChEMBL max_phase 4 AND (a US prescription label in openFDA OR an Open Targets APPROVAL stage). An Open Targets APPROVAL stage alone is not trusted (it marked acadesine and navitoclax as approved in the BUB1B run).
- Label chosen: among the 25 most recent human prescription labels whose single generic name matches the ChEMBL preferred name (salt words stripped), the one with a systemic route, a boxed warning and the fullest warnings text wins (conservative for a harm screen); topical and ophthalmic labels lose.
- Direction: ChEMBL action type (INHIBITOR, AGONIST, ...) compared with the action the config asks for per mechanism; mismatches are demoted, not deleted. Curated exclusions in the config are shown with their reason.
- Harm flags are regular expressions over boxed warning, warnings, warnings and precautions and pediatric use only. Snippets above are the first match; a flag means the term occurs, not that the risk is quantified.
- Rapalogs are filed under FKBP1A in ChEMBL, not MTOR; metformin under mitochondrial complex I, not AMPK; chloroquine class under TLR7/TLR9. The target mapping in the config carries these.
- Run log at the end of this file.

## Run log

```
[01:30:20] Resolving BUB1B and 33 consequence genes in Open Targets
[01:30:20] BUB1B: 76 interaction partners at score >= 0.9
[01:30:20] Pulling drugs and clinical candidates for 110 targets
[01:30:20] 148 unique molecules; querying ChEMBL
[01:30:20] Querying openFDA labels
```
