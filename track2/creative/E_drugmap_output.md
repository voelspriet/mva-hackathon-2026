# Drug map for BUB1B

Generated 2026-09-05 01:28 UTC by pipeline/track2_drugmap/drugmap.py. Run time 350 s, 374 live HTTP calls (cached responses not counted).

API status: opentargets: ok, chembl: ok, openfda: ok.

## Inputs

- Gene: BUB1B (ENSG00000156970), https://platform.opentargets.org/target/ENSG00000156970

- CDKN2A/p16 senescence: CDKN2A (ENSG00000147889), CDK4 (ENSG00000135446), CDK6 (ENSG00000105810), BCL2 (ENSG00000171791), BCL2L1 (ENSG00000171552). p16 itself is undruggable; CDK4/6 sit directly downstream, BCL2 family are the senolytic axis (navitoclax class).
- autophagy/lysosome: TLR7 (ENSG00000196664), TLR9 (ENSG00000239732), PIK3C3 (ENSG00000078142), ULK1 (ENSG00000177169), TFEB (ENSG00000112561), ATP6V1A (ENSG00000114573). Chloroquine and hydroxychloroquine carry TLR7/TLR9 as their ChEMBL mechanism target; autophagy inhibition has no protein target in ChEMBL.
- AMPK: PRKAA1 (ENSG00000132356), PRKAA2 (ENSG00000162409), PRKAB1 (ENSG00000111725). Metformin's ChEMBL mechanism is mitochondrial complex I, so it will not appear under AMPK. Searched separately by name in the seed list.
- mTORC1: MTOR (ENSG00000198793), RPTOR (ENSG00000141564), FKBP1A (ENSG00000088832). Rapalogs (sirolimus, everolimus, temsirolimus) are filed under FKBP1A in ChEMBL, not MTOR.
- HSP90: HSP90AA1 (ENSG00000080824), HSP90AB1 (ENSG00000096384), HSP90B1 (ENSG00000166598), TRAP1 (ENSG00000126602). Pimitespib is approved in Japan only; Open Targets clinical stage may or may not reflect PMDA.
- SIRT2: SIRT2 (ENSG00000068903), SIRT1 (ENSG00000096717), NAMPT (ENSG00000105835). NAD+ axis added via SIRT1/NAMPT.
- cGAS-STING: CGAS (ENSG00000164430), STING1 (ENSG00000184584), TBK1 (ENSG00000183735), IRF3 (ENSG00000126456)
- NMD/readthrough: UPF1 (ENSG00000005007), SMG1 (ENSG00000157106), SMG5 (ENSG00000198952), SMG6 (ENSG00000070366), SMG7 (ENSG00000116698). Readthrough compounds (ataluren, aminoglycosides) have no human protein target in ChEMBL; searched by name in the seed list.
- Seed drugs (mechanism classes without a ChEMBL protein target): AMPK: metformin; autophagy/lysosome: chloroquine, hydroxychloroquine; NMD/readthrough: ataluren, gentamicin; SIRT2: niacin, nicotinamide
- Interaction partners of BUB1B at score >= 0.9: 79 (ANAPC1, ANAPC10, ANAPC11, ANAPC13, ANAPC15, ANAPC16, ANAPC2, ANAPC4, ANAPC5, ANAPC7, ASPM, AURKB, BIRC5, BRCA2, BUB1, BUB3, BUB3, CCNB1, CCNB2, CDC16, CDC20, CDC20, CDC20, CDC23, CDC26, CDC27, CDCA8, CDK1, CENPA, CENPE, CENPF, CEP55, DLGAP5, ESPL1, FOXM1, FZR1, KIF11, KIF20A, KIF2C, KIF4A, KNL1, MAD1L1, MAD2L1, MELK, MIS12, MKI67, MXI1, NCAPG, NDC80, NEK2, NUF2, NUSAP1, PBK, PLK1, PLK4, PPP2CA, PPP2R5A, PPP2R5C, PPP2R5D, PTTG1, RAD51, RAE1, SGO1, SKA1, SKA2, SKA3, SPAG5, SPC25, SPDL1, TACC3, TOP2A, TPX2, TRIM33, TRIP13, TTK, UBE2C, ZW10, ZWILCH, ZWINT)

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

| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Pediatric-use section | Harm flags | Label | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | GENTAMICIN | NMD/readthrough | seed list | yes | US (FDA label found) | Bacterial 70S ribosome inhibitor (INHIBITOR) | present: safety/effectiveness not established | 0:  | Gentamicin Sulfate 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL6067485) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL6067485/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5193ed8d-44c9-46fe-924d-93aaea922cfd) |
| 2 | IMIQUIMOD | autophagy/lysosome | TLR7 (ENSG00000196664) | yes | US (FDA label found) | Toll-like receptor 7 agonist (AGONIST) | present: pediatric information given | 0:  | Imiquimod 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1282) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1282/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=51913a5a-1cab-4b9e-b2c2-e0174062df73) |
| 3 | TRILACICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | Cyclin-dependent kinase 4 inhibitor (INHIBITOR) | Cyclin-dependent kinase 6 inhibitor (INHIBITOR) | present: safety/effectiveness not established | 0:  | COSELA 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL3894860) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3894860/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b3179c19-78f3-4bf1-b73e-7f7638522ab1) |
| 4 | ABEMACICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | Cyclin-dependent kinase 4 inhibitor (INHIBITOR) | Cyclin-dependent kinase 6 inhibitor (INHIBITOR) | present: pediatric information given | 1: myelosuppression | Verzenio 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL3301610) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3301610/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=be4bc0de-0fdc-4d46-8d25-be43c79e6a06) |
| 5 | METFORMIN | AMPK | seed list | yes | US (FDA label found) | Mitochondrial complex I (NADH dehydrogenase) inhibitor (INHIBITOR) | Mitochondrial glycerol-3-phosphate dehydr... | present: pediatric information given | 1: nephrotoxicity | Metformin Hydrochloride 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1431) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1431/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=bfd6ec0f-8264-4877-aa6d-f347f53bc426) |
| 6 | NIACIN | SIRT2 | seed list | yes | US (FDA label found) |  | present: safety/effectiveness not established | 1: nephrotoxicity | Niacin 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL573) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL573/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8eff9205-84ac-e69d-e053-2995a90aad4b) |
| 7 | RIBOCICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | Cyclin-dependent kinase 4 inhibitor (INHIBITOR) | Cyclin-dependent kinase 6 inhibitor (INHIBITOR) | present: pediatric information given | 1: myelosuppression | KISQALI 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL3545110) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3545110/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8) |
| 12 | PIMECROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | present: pediatric information given | 2: immunosuppression;malignancy | Pimecrolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1200686) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1200686/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6601e43e-ce7d-446a-8568-8e7b24b86f06) |
| 16 | CHLOROQUINE | autophagy/lysosome | seed list | yes | US (FDA label found) | Ferriprotoporphyrin IX binding agent (BINDING AGENT) | Ferriprotoporphyrin IX inhibitor (INHIBITOR) | present: pediatric information given | 3: malignancy;nephrotoxicity;retinal | Chloroquine Phosphate 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL76) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL76/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a342f72-45f9-3e12-e063-6394a90ae33e) |
| 17 | HYDROXYCHLOROQUINE | autophagy/lysosome | TLR7 (ENSG00000196664); TLR9 (ENSG00000239732); seed list | yes | US (FDA label found) | Ferriprotoporphyrin IX inhibitor (INHIBITOR) | Toll-like receptor 7 antagonist (ANTAGONIST) | Toll-like recept... | present: pediatric information given | 3: myelosuppression;nephrotoxicity;retinal | HYDROXYCHLOROQUINE SULFATE 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1535) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1535/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebe00e35-ed3d-40f4-9a93-a37b0da01ddb) |
| 18 | NIACINAMIDE | SIRT2 | seed list | yes | US (FDA label found) |  | present: pediatric information given | 3: myelosuppression;nephrotoxicity;retinal | Multiple Vitamins (Pediatric) Pharmacy Bulk Package 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1140) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1140/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d9b6eb9a-4218-5c94-6e35-7cbbf0fba494) |
| 19 | PALBOCICLIB | CDKN2A/p16 senescence | CDK4 (ENSG00000135446); CDK6 (ENSG00000105810) | yes | US (FDA label found) | CDK6/cyclin D1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 4/cyclin D1 inhibitor (INHIBITOR) | present: pediatric information given | 3: growth;myelosuppression;nephrotoxicity | Ibrance 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL189963) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL189963/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792) |
| 20 | TEMSIROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | present: safety/effectiveness not established | 3: immunosuppression;myelosuppression;nephrotoxicity | Torisel 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL1201182) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1201182/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=95b7dc92-2180-42f1-8699-3c28f609e674) |
| 22 | EVEROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | present: safety/effectiveness not established | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Everolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1908360) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1908360/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c7bb6ba1-9a7f-43f5-b058-ef26d4b59221) |
| 23 | SIROLIMUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | present: safety/effectiveness not established | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Sirolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL413) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL413/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=fc81cb86-61e1-4622-b2ce-cde263143aa0) |
| 24 | TACROLIMUS ANHYDROUS | mTORC1 | FKBP1A (ENSG00000088832) | yes | US (FDA label found) | FK506-binding protein 1A inhibitor (INHIBITOR) | present: pediatric information given | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Tacrolimus 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL269732) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL269732/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=213f6047-f897-48a7-b78a-45d7124f2f16) |
| 25 | VENETOCLAX | CDKN2A/p16 senescence | BCL2 (ENSG00000171791) | yes | US (FDA label found) | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | present: pediatric information given | 4: immunosuppression;malignancy;myelosuppression;nephrotoxicity | Venclexta 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL3137309) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3137309/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b118a40d-6b56-cee3-10f6-ded821a97018) |
| 26 | ATALUREN | NMD/readthrough | seed list | yes | ChEMBL max_phase 4 only; no US label, no OT approval stage ( | 80S Ribosome modulator (MODULATOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL256997) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL256997/) |
| 27 | PERHEXILINE | mTORC1 | MTOR (ENSG00000198793) | yes | approved somewhere per ChEMBL/Open Targets; no US prescripti | Carnitine O-palmitoyltransferase 1, muscle isoform inhibitor (INHIBITOR) | Carnitine palmitoyltransferase 2 in... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL75880) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL75880/) |

## Approved drugs acting on interaction partners of the gene (hazard class, listed for avoidance not use)

| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Pediatric-use section | Harm flags | Label | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 8 | DOXORUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | present: safety/effectiveness not established | 1: malignancy | doxorubicin hydrochloride 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL53463) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL53463/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=55889588-c5f1-d9bc-e063-6294a90a5791) |
| 9 | ETOPOSIDE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA topoisomerase II inhibitor (INHIBITOR) | present: pediatric information given | 1: myelosuppression | Avopef 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL44657) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL44657/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=acc1e443-ef7b-486f-a638-710a20e81059) |
| 10 | ETOPOSIDE PHOSPHATE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | present: pediatric information given | 1: myelosuppression | Avopef 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1200645) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1200645/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=acc1e443-ef7b-486f-a638-710a20e81059) |
| 11 | VALRUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | present: safety/effectiveness not established | 1: myelosuppression | Valstar 2024 | [OT](https://platform.opentargets.org/drug/CHEMBL1096885) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1096885/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e96f30a0-6662-11de-8f80-0002a5d5c51b) |
| 13 | DAUNORUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | present: pediatric information given | 2: myelosuppression;nephrotoxicity | Daunorubicin Hydrochloride 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL178) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL178/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9705fa12-499e-41a3-8fb4-f6df0858b851) |
| 14 | DEXRAZOXANE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA topoisomerase II inhibitor (INHIBITOR) | Iron chelating agent (CHELATING AGENT) | Iron sequestering agent ... | present: safety/effectiveness not established | 2: malignancy;myelosuppression | DEXRAZOXANE 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1738) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1738/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cb72203a-0b09-42d5-bf51-7f479feb3adb) |
| 15 | MITOXANTRONE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | present: safety/effectiveness not established | 2: growth;myelosuppression | Mitoxantrone 2025 | [OT](https://platform.opentargets.org/drug/CHEMBL58) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL58/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=accf9569-4b57-4e83-a7db-4e890a75d1ba) |
| 21 | IDARUBICIN | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | US (FDA label found) | DNA inhibitor (INHIBITOR) | DNA topoisomerase II alpha inhibitor (INHIBITOR) | present: pediatric information given | 3: malignancy;myelosuppression;nephrotoxicity | Idamycin PFS 2026 | [OT](https://platform.opentargets.org/drug/CHEMBL1117) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1117/) [label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a5a6d93-cc1e-4d7f-8da1-446c134503b3) |
| 28 | AMSACRINE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | approved somewhere per ChEMBL/Open Targets; no US prescripti | DNA topoisomerase II inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL43) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL43/) |
| 29 | TENIPOSIDE | interaction partner of BUB1B (score 0.98) | TOP2A (ENSG00000131747) | yes | approved somewhere per ChEMBL/Open Targets; no US prescripti | DNA topoisomerase II inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL452231) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL452231/) |

## Not approved (context only)

| # | Drug | Mechanism target | Via | Approved | Jurisdiction | MoA (ChEMBL) | Pediatric-use section | Harm flags | Label | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 30 | 1018 ISS | autophagy/lysosome | TLR9 (ENSG00000239732) | no | not approved | Toll-like receptor 9 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297680) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297680/) |
| 31 | ACADESINE | AMPK | PRKAA1 (ENSG00000132356); PRKAA2 (ENSG00000162409); PRKAB1 ( | no | Open Targets says APPROVAL but ChEMBL max_phase < 4 and no U | AMP-activated protein kinase, AMPK activator (ACTIVATOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1551724) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1551724/) |
| 32 | ADU-S100 | cGAS-STING | STING1 (ENSG00000184584) | no | not approved | Stimulator of interferon genes protein agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297688) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297688/) |
| 33 | AFIMETORAN | autophagy/lysosome | TLR7 (ENSG00000196664) | no | not approved | Toll-like receptor 7 inhibitor (INHIBITOR) | Toll-like receptor 8 inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4650329) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4650329/) |
| 34 | AG-24322 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446) | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3545420) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3545420/) |
| 35 | AGATOLIMOD | autophagy/lysosome | TLR9 (ENSG00000239732) | no | not approved | Toll-like receptor 9 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2103792) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2103792/) |
| 36 | ALVESPIMYCIN | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | Reactive oxygen species () | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL383824) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL383824/) |
| 37 | ALVOCIDIB | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL428690) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL428690/) |
| 38 | APG-2575 | CDKN2A/p16 senescence | BCL2 (ENSG00000171791) | no | not approved | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4650374) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4650374/) |
| 39 | APITOLISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1922094) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1922094/) |
| 40 | AT-7519 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL445813) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL445813/) |
| 41 | AZD-5438 | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446); CDK6 (ENSG00 | no | not approved | Cyclin-dependent kinase inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL488436) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL488436/) |
| 42 | AZD-8055 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1801204) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1801204/) |
| 43 | AZD-8848 | autophagy/lysosome | TLR7 (ENSG00000196664) | no | not approved | Toll-like receptor 7 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297356) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297356/) |
| 44 | BAZLITORAN | autophagy/lysosome | TLR7 (ENSG00000196664); TLR9 (ENSG00000239732) | no | not approved | Toll-like receptor 7 antagonist (ANTAGONIST) | Toll-like receptor 8 antagonist (ANTAGONIST) | Toll-like recept... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297995) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297995/) |
| 45 | BGT-226 FREE BASE | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3218578) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3218578/) |
| 46 | BIIB021 | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL467399) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL467399/) |
| 47 | CC-115 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | DNA-dependent protein kinase inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3586573) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3586573/) |
| 48 | CD24FC | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock 70 kDa protein 1A/1B inhibitor (INHIBITOR) | Heat shock protein HSP90 inhibitor (INHIBITOR) | High ... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297717) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297717/) |
| 49 | COBITOLIMOD | autophagy/lysosome | TLR9 (ENSG00000239732) | no | not approved | Toll-like receptor 9 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297564) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297564/) |
| 50 | CPG-52852 | autophagy/lysosome | TLR7 (ENSG00000196664) | no | not approved | Toll-like receptor 7 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL549344) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL549344/) |
| 51 | DACTOLISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1879463) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1879463/) |
| 52 | DAPORINAD | SIRT2 | NAMPT (ENSG00000105835) | no | not approved | Nicotinamide phosphoribosyltransferase inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL566757) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL566757/) |
| 53 | DS-3078A | mTORC1 | MTOR (ENSG00000198793) | no | not approved | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3544963) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3544963/) |
| 54 | DS-7423 | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL3545248) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3545248/) |
| 55 | EMD-1201081 | autophagy/lysosome | TLR9 (ENSG00000239732) | no | not approved | Toll-like receptor 9 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297993) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297993/) |
| 56 | ENPATORAN | autophagy/lysosome | TLR7 (ENSG00000196664) | no | not approved | Toll-like receptor 7 antagonist (ANTAGONIST) | Toll-like receptor 8 antagonist (ANTAGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4802159) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4802159/) |
| 57 | GANETESPIB | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2103879) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2103879/) |
| 58 | GEDATOLISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL592445) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL592445/) |
| 59 | GSK-2245035 | autophagy/lysosome | TLR7 (ENSG00000196664) | no | not approved | Toll-like receptor 7 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297492) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297492/) |
| 60 | INDOXIMOD | mTORC1 | MTOR (ENSG00000198793); RPTOR (ENSG00000141564) | no | not approved | mTORC1 activator (ACTIVATOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL571209) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL571209/) |
| 61 | LEFITOLIMOD | autophagy/lysosome | TLR9 (ENSG00000239732) | no | not approved | Toll-like receptor 9 agonist (AGONIST) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL4297776) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4297776/) |
| 62 | LUMINESPIB | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL252164) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL252164/) |
| 63 | MILCICLIB | CDKN2A/p16 senescence; interaction partner of BUB1B (score 0.999) | CDK1 (ENSG00000170312); CDK4 (ENSG00000135446) | no | not approved | Cyclin-dependent kinase 1 inhibitor (INHIBITOR) | Cyclin-dependent kinase 2 inhibitor (INHIBITOR) | Cyclin-dep... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL564829) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL564829/) |
| 64 | NAVITOCLAX | CDKN2A/p16 senescence | BCL2 (ENSG00000171791); BCL2L1 (ENSG00000171552) | no | Open Targets says APPROVAL but ChEMBL max_phase < 4 and no U | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | Apoptosis regulator Bcl-W inhibitor (INHIBITOR) | Apoptosis ... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL443684) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL443684/) |
| 65 | OBATOCLAX | CDKN2A/p16 senescence | BCL2 (ENSG00000171791); BCL2L1 (ENSG00000171552) | no | not approved | Apoptosis regulator Bcl-2 inhibitor (INHIBITOR) | Apoptosis regulator Bcl-W inhibitor (INHIBITOR) | Apoptosis ... | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL408194) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL408194/) |
| 66 | OBLIMERSEN | CDKN2A/p16 senescence | BCL2 (ENSG00000171791) | no | Open Targets says APPROVAL but ChEMBL max_phase < 4 and no U | Bcl-2 mRNA antisense inhibitor (ANTISENSE INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2108324) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2108324/) |
| 67 | OBLIMERSEN SODIUM | CDKN2A/p16 senescence | BCL2 (ENSG00000171791) | no | not approved | Bcl-2 mRNA antisense inhibitor (ANTISENSE INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL2109229) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2109229/) |
| 68 | OMIPALISIB | mTORC1 | MTOR (ENSG00000198793) | no | not approved | PI3-kinase class I inhibitor (INHIBITOR) | Serine/threonine-protein kinase mTOR inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1236962) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1236962/) |
| 69 | ONALESPIB | HSP90 | HSP90AA1 (ENSG00000080824); HSP90AB1 (ENSG00000096384) | no | not approved | Heat shock protein HSP90 inhibitor (INHIBITOR) | no label | 0:  | no US prescription label in openFDA | [OT](https://platform.opentargets.org/drug/CHEMBL1214827) [ChEMBL](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1214827/) |

(79 further unapproved candidates omitted; see CSV)

## Harm-flag evidence snippets (approved drugs)

**ABEMACICLIB** (Verzenio, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=be4bc0de-0fdc-4d46-8d25-be43c79e6a06)
- myelosuppression: ease oral fluids, and notify their healthcare provider. ( 2.2 , 5.1 ) Neutropenia: Monitor complete blood counts prior to the start of VERZENIO therapy

**METFORMIN** (Metformin Hydrochloride, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=bfd6ec0f-8264-4877-aa6d-f347f53bc426)
- nephrotoxicity: 5.1) ]. Risk factors for metformin-associated lactic acidosis include renal impairment, concomitant use of certain drugs (e.g., carbonic anhydrase inhibitor

**NIACIN** (Niacin, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8eff9205-84ac-e69d-e053-2995a90aad4b)
- nephrotoxicity: Precautions ( 5.3 )] and should be used with caution in patients with renal impairment. Patients with a past history of jaundice, hepatobiliary disease, or

**RIBOCICLIB** (KISQALI, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aaeaef94-f3f5-4367-8ea2-b181d7be2da8)
- myelosuppression: each subsequent 4 cycles, and as clinically indicated. ( 2.2 , 5.5 ) Neutropenia: Perform complete blood count (CBC) before initiating therapy with KI

**PIMECROLIMUS** (Pimecrolimus, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6601e43e-ce7d-446a-8568-8e7b24b86f06)
- immunosuppression: ( 1 , 5.1 , 8.4 ) 5 WARNINGS AND PRECAUTIONS • Should not be used in immunocompromised adults and children, including patients on systemic immunosuppressive
- malignancy: lthough a causal relationship has not been established, rare cases of malignancy (e.g., skin and lymphoma) have been reported in patients treated with

**CHLOROQUINE** (Chloroquine Phosphate, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a342f72-45f9-3e12-e063-6394a90ae33e)
- malignancy: s the benefit to the patient outweighs the potential risks. Potential Carcinogenic Risk Experimental data showed a potential risk of inducing gene mutat
- nephrotoxicity: scle or nerve toxicity is suspected or demonstrated by tissue biopsy. Renal Toxicity Proteinuria with or without a moderate reduction in glomerular filtra
- retinal: heir blood glucose level checked and treatment reviewed as necessary. Retinopathy 1 Irreversible retinal damage has been observed in some patients who

**HYDROXYCHLOROQUINE** (HYDROXYCHLOROQUINE SULFATE, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=ebe00e35-ed3d-40f4-9a93-a37b0da01ddb)
- myelosuppression: orphyria cutanea tarda. (5.5) • Hematologic Toxicity : Discontinue if myelosuppression occurs. (5.6) • Renal Toxicity : Consider phospholipidosis as a possi
- nephrotoxicity: ematologic Toxicity : Discontinue if myelosuppression occurs. (5.6) • Renal Toxicity : Consider phospholipidosis as a possible cause of renal injury in pa
- retinal: ing cardiomyopathy and ventricular arrhythmias were reported. (5.1) • Retinal Toxicity : Irreversible retinal damage is related to cumulative dosag

**NIACINAMIDE** (Multiple Vitamins (Pediatric) Pharmacy Bulk Package, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d9b6eb9a-4218-5c94-6e35-7cbbf0fba494)
- myelosuppression: l Syndrome in Low-Birth Weight Infants E-Ferol syndrome manifested by thrombocytopenia, renal dysfunction, hepatomegaly, cholestasis, ascites, hypotension a
- nephrotoxicity: GS AND PRECAUTIONS • Risk of Aluminum Toxicity: For at risk patients (renal failure or those with prolonged therapy), consider periodic monitoring of alu
- retinal: has been reported in patients with renal failure receiving 1.5 mg/day retinol and in patients with liver disease. Therefore, supplementation of ren

**PALBOCICLIB** (Ibrance, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792)
- growth: exposure [AUC] at the recommended dose) resulted in abnormalities in growing incisor teeth (discolored, ameloblast degeneration/necrosis, mononuclear cell
- myelosuppression: 5 WARNINGS AND PRECAUTIONS • Neutropenia: Monitor complete blood count prior to start of IBRANCE therapy and a
- nephrotoxicity: , lens degeneration), kidney (tubule vacuolation, chronic progressive nephropathy) and adipose tissue (atrophy) were identified in a 27 week repeat-dos

**TEMSIROLIMUS** (Torisel, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=95b7dc92-2180-42f1-8699-3c28f609e674)
- immunosuppression: lucose and lipid profiles. ( 5.3 , 5.6 ) • Infections may result from immunosuppression. ( 5.4 ) • Monitor for symptoms or radiographic changes of interstiti
- myelosuppression: ns (≥20%) in pediatric patients receiving the 75 mg/m 2 dose included thrombocytopenia, infections, asthenia/fatigue, fever, pain, leukopenia, rash, anemia,
- nephrotoxicity: dominal pain, bloody stools, and/or acute abdomen promptly. ( 5.7 ) • Renal failure, sometimes fatal, has occurred. Monitor renal function at baseline an

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

**TACROLIMUS ANHYDROUS** (Tacrolimus, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=213f6047-f897-48a7-b78a-45d7124f2f16)
- immunosuppression: WARNING: MALIGNANCIES AND SERIOUS INFECTIONS Increased risk for developing serious infections and malignancies wit
- malignancy: WARNING: MALIGNANCIES AND SERIOUS INFECTIONS Increased risk for developing serious infectio
- myelosuppression: c Microangiopathy, Including Hemolytic Uremic Syndrome and Thrombotic Thrombocytopenic Purpura: May occur, especially in patients with infections and certai
- nephrotoxicity: • New Onset Diabetes After Transplant: Monitor blood glucose. (5.4) • Nephrotoxicity (acute and/or chronic): Reduce the dose; use caution with other nephr

**VENETOCLAX** (Venclexta, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b118a40d-6b56-cee3-10f6-ded821a97018)
- immunosuppression: microbials and growth factors (e.g., G-CSF). 5.3 Infections Fatal and serious infections, such as pneumonia and sepsis, have occurred in patients treated with
- malignancy: ctors, particularly reduced renal function, tumor burden, and type of malignancy. Splenomegaly may also increase the risk of TLS in patients with CLL/
- myelosuppression: monitoring, hospitalization) as overall risk increases. ( 2.4 , 5.1 ) Neutropenia: Monitor blood counts. Interrupt dosing and resume at same or reduced
- nephrotoxicity: Lysis Syndrome Tumor lysis syndrome (TLS), including fatal events and renal failure requiring dialysis, has occurred in patients treated with VENCLEXTA [

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

**DEXRAZOXANE** (DEXRAZOXANE, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cb72203a-0b09-42d5-bf51-7f479feb3adb)
- malignancy: luated against the risk of producing irreversible cardiac damage. 5.4 Secondary Malignancies Secondary malignancies such as acute myeloid leukemia (AML) and myelo
- myelosuppression: 5 WARNINGS AND PRECAUTIONS Myelosuppression: Dexrazoxane may increase the myelosuppresive effects of chemotherape

**MITOXANTRONE** (Mitoxantrone, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=accf9569-4b57-4e83-a7db-4e890a75d1ba)
- growth: uring the organogenesis period of gestation was associated with fetal growth retardation at doses ≥0.1 mg/kg/day (0.01 times the recommended human dose on a m
- myelosuppression: of less than 1,500 cells/mm 3 . In order to monitor the occurrence of bone marrow suppression, primarily neutropenia, which may be severe and result in infection,

**IDARUBICIN** (Idamycin PFS, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a5a6d93-cc1e-4d7f-8da1-446c134503b3)
- malignancy: WARNING: CARDIOMYOPATHY, SECONDARY MALIGNANCIES, and EXTRAVASATION AND TISSUE NECROSIS • Cardiomyopathy: IDAMYCIN PFS
- myelosuppression: n if extravasation occurs. ( 2.6 , 5.3 ) 5 WARNINGS AND PRECAUTIONS • Myelosuppression : Severe myelosuppression resulting in severe infection, septic shock
- nephrotoxicity: ypersensitivity reactions and manage as clinically indicated. (5.6) • Renal Impairment : Assess renal function prior to and during treatment. Reduce the dos

## Method notes

- Approval = ChEMBL max_phase 4 AND (a US prescription label in openFDA OR an Open Targets APPROVAL stage). An Open Targets APPROVAL stage alone is not trusted (it marked acadesine and navitoclax as approved in the BUB1B run).
- Label chosen: most recent single-ingredient human prescription label whose generic name matches the ChEMBL preferred name with salt words stripped; labels with a pediatric-use section preferred.
- Harm flags are regular expressions over boxed warning, warnings, warnings and precautions and pediatric use only. Snippets above are the first match; a flag means the term occurs, not that the risk is quantified.
- Rapalogs are filed under FKBP1A in ChEMBL, not MTOR; metformin under mitochondrial complex I, not AMPK; chloroquine class under TLR7/TLR9. The target mapping in the config carries these.
- Run log at the end of this file.

## Run log

```
[01:22:40] Resolving BUB1B and 33 consequence genes in Open Targets
[01:22:54] BUB1B: 79 interaction partners at score >= 0.9
[01:22:54] Pulling drugs and clinical candidates for 110 targets
[01:23:04] 148 unique molecules; querying ChEMBL
[01:25:30] Querying openFDA labels
```
