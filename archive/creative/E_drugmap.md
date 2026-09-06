# E. Drug map: from a gene and a mechanism list to a ranked, harm-screened table of approved drugs

Tool: `pipeline/track2_drugmap/drugmap.py` with config `pipeline/track2_drugmap/targets_bub1b.json`. Output: `archive/creative/E_drugmap_output.md` and `.csv`. Python 3.11 standard library plus certifi. Public APIs only, no patient data.

## What the tool does

Input is a gene symbol and a mechanism list. Each mechanism names the human genes that carry it in the drug databases, the action direction wanted (inhibitor, antagonist, activator), optional curated exclusions with a stated reason, and optional seed drugs for mechanism classes that have no protein target in ChEMBL (readthrough, autophagy inhibition, AMPK activation by metformin).

Four steps, one HTTP cache so a rerun is offline and reproducible:

1. Open Targets Platform GraphQL. Resolve every symbol to an Ensembl ID, pull the gene's physical interaction partners (STRING and IntAct, score at or above 0.9), then pull `drugAndClinicalCandidates` for the gene, the consequence genes and the partners in batches of ten. The documented `knownDrugs` field no longer exists in the schema; the tool was written against the live schema by introspection.
2. ChEMBL REST. Parent molecule, `max_phase`, first approval year, mechanism of action with action type, looked up by `parent_molecule_chembl_id` (salt forms have no mechanism records of their own).
3. openFDA drug label API. Among the 25 most recent human prescription labels whose single generic name matches the ChEMBL name with salt words stripped, the tool keeps the label with a systemic route, a boxed warning and the fullest warnings text. Boxed warning, warnings, warnings and precautions and pediatric use are screened with six regular expressions: growth, malignancy or neoplasm, immunosuppression, nephrotoxicity or nephrocalcinosis, myelosuppression, retinal. The first matching snippet is kept as evidence.
4. Approval and ranking. A drug counts as approved only if ChEMBL `max_phase` is 4 and either a US label exists or Open Targets says APPROVAL. Ranking: approved, not a hazard-class drug (acts on a mitotic partner of the gene), not curated out, action direction matches, pediatric-use section present, fewest harm flags. Every row carries links to the Open Targets drug page, the ChEMBL report card and the DailyMed label by set ID.

## What it found for BUB1B

110 targets were queried: BUB1B, 33 consequence genes, 76 interaction partners. 148 unique molecules came back; 29 pass the three-way approval test; 14 of those are ranked as candidates, 5 are demoted, 10 are hazard-class.

BUB1B itself has no drug or clinical candidate at any stage. Sixteen of the 33 consequence genes have none either: CDKN2A, CGAS, TBK1, IRF3, SIRT2, UPF1, SMG1, SMG5, SMG6, SMG7, TFEB, ATP6V1A, PIK3C3, ULK1, HSP90B1, TRAP1. HSP90AA1 and HSP90AB1 have ten candidates each and none approved; pimitespib's Japanese approval is not carried by Open Targets. Of the 76 partners, 9 have any candidate and only TOP2A has approved drugs.

The ranked table, top to bottom: trilaciclib, abemaciclib, niacin, niacinamide, ribociclib, chloroquine, hydroxychloroquine, palbociclib, temsirolimus, everolimus, sirolimus, venetoclax, ataluren, gentamicin. Demoted: metformin and imiquimod (direction mismatch), pimecrolimus, tacrolimus and perhexiline (curated out). Hazard class: doxorubicin, etoposide, etoposide phosphate, valrubicin, daunorubicin, dexrazoxane, mitoxantrone, idarubicin, amsacrine, teniposide, all through TOP2A.

Compared with the manual route (potassium citrate, thiazide, metformin, hydroxychloroquine, dasatinib, sirolimus, everolimus, dexrazoxane, cyclophosphamide, growth hormone, mecasermin), the tool surfaced six approved drugs the manual route did not name: the four CDK4/6 inhibitors palbociclib, ribociclib, abemaciclib and trilaciclib, the BCL2 inhibitor venetoclax, and temsirolimus. It also produced label evidence that matters for this child. Palbociclib's pediatric-use section reports cataracts, lens degeneration, kidney tubule vacuolation and abnormal growing incisor teeth in juvenile rats, three findings that overlap the MVA phenotype. Dexrazoxane, on the manual list as a cardioprotectant, carries a malignancy flag from its warnings section (secondary malignancies) and sits in the hazard class because TOP2A is a 0.98-score partner of BUB1B. Everolimus and sirolimus each carry all four of immunosuppression, malignancy, myelosuppression and nephrotoxicity, and their pediatric sections say safety and effectiveness are not established.

The top hit is also the clearest warning about the tool. Trilaciclib ranks first because it is approved, has a pediatric section and zero flags. But in the Baker 2008 model p16 is the effector of senescence and its loss attenuates the phenotype; a CDK4/6 inhibitor mimics p16 and would be expected to push muscle and fat toward senescence, not away from it. The tool's direction check compares drug action against a protein (inhibitor of CDK4, as asked), not against the phenotype (oppose p16). A biologist has to set the wanted direction so that it encodes the phenotype, and for the CDK4/6 axis the honest entry is "activator", which no approved drug is. The ranking is therefore a shortlist for a human, not a recommendation.

Eight molecules that Open Targets marks APPROVAL were rejected because ChEMBL puts them at phase 2 or 3 and no US label exists: acadesine, navitoclax, oblimersen, ridaforolimus, zotarolimus, amrubicin, pazufloxacin, vosaroxin. Two of those (amrubicin, pazufloxacin) are marketed in Japan, so the cross-check also discards some true non-US approvals. Ataluren shows the other side: ChEMBL max_phase 4, EU conditional approval, no US label; the tool marks it approved with jurisdiction "verify manually".

## Limits

API coverage. Open Targets carries drugs only through their ChEMBL mechanism target. Rapalogs are filed under FKBP1A, not MTOR; metformin under mitochondrial complex I, not AMPK; the chloroquine class under TLR7 and TLR9. Without those three mapping choices in the config the run would have missed sirolimus, everolimus, metformin and hydroxychloroquine entirely. Conversely FKBP1A brings in tacrolimus and pimecrolimus, which are calcineurin inhibitors; they had to be curated out by name. Readthrough, NMD inhibition, autophagy and STING antagonism have no approved drug in the graph at all, so those mechanisms return zero regardless of how good the biology is. The partner-based hazard screen missed the best-documented hazard in the dossier, taxanes (Janssen 2009): TUBB is not a STRING partner of BUB1B at 0.9. Hazard detection by interaction graph is not a substitute for a curated aneugen list.

Approval status. Open Targets APPROVAL is unreliable in both directions; ChEMBL max_phase 4 covers any jurisdiction without saying which; openFDA covers the US only. The three-way rule is conservative for the US and blind to EMA and PMDA.

Label parsing. The flags are term screens. "Nephrotoxicity" fires on metformin and niacin because their labels say "use with caution in renal impairment", a dosing caution, not organ toxicity. Niacinamide has no single-ingredient prescription label, so the tool screened a prenatal multivitamin. Pediatric-use detection relies on the phrase "not established" and misclassifies labels that give age-banded data in other words. The label picker's preference for the fullest warnings text is deliberate for a harm screen but means the chosen label may be an older generic rather than the innovator's current one; the set ID is in every row so this can be checked.

Direction. ChEMBL action types are coarse. Metformin is demoted as "inhibitor when activator asked" because ChEMBL codes it as a complex I inhibitor even though AMPK activation is why it is on the list.

## Run time

Cold run on 5 September 2026: 350 seconds for 374 live HTTP calls, no failures, all three APIs up. openFDA dominates at roughly 1.5 seconds per label; Open Targets answered 110 targets in 12 batched calls in about 10 seconds. From cache the whole pipeline reruns in 0.2 seconds, so config changes (a new exclusion, a new direction) cost nothing. openFDA allows 240 requests per minute and 1,000 per day without a key, enough for about six genes of this size per day; a free key raises the limit.

## Transfer to another gene

Two things change and one does not. The gene symbol and the mechanism-to-gene mapping change; the code does not. For a gene with a single dominant mechanism the command line suffices:

```
python3.11 drugmap.py --gene TP53 --targets "MDM2 axis:MDM2,MDM4;p21:CDKN1A" --out /tmp/tp53
```

For a case like BUB1B, where the useful targets are consequences rather than the gene, the JSON config carries the biologist's decisions in a form that is reviewable: which genes stand for a mechanism, which direction is wanted, which hits are excluded and why, which drugs are seeded by name because the databases file them under an unrelated target. Those decisions are the scientific content; the tool only makes them explicit, applies them uniformly and attaches evidence links. The N-of-1 patients in the MVA Society share BUB1B and most of this config; a TRIP13 or CEP57 family would keep the consequence mechanisms and change the gene and the partner set. The partner query and the harm screen are gene-agnostic.

What does not transfer automatically is judgement about direction at the phenotype level, as the trilaciclib result shows, and knowledge of hazards that live in the literature rather than in the interaction graph. Both belong in the config, written down, so that the next person can see and argue with them.
