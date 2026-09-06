# What was excluded, on whose say-so, and whether the reason holds

## Why this file exists

Every check this project ran examined what the report **asserts**. The five audit partitions took 577 claims and tested each against a primary source. None of them looked at what the report **dropped**.

That is a hole, because the candidates were excluded by simulated panel seats, and **a simulated specialist's opinion is not evidence**. Where a seat wrote "excluded" and gave a reason, the reason entered the record and was never checked. Where the reason was wrong, the candidate stayed out.

This file checks the exclusions. **Five do not survive.**

---

## Correctly out of scope, and not audited further

The challenge asks for market-approved medicines. These were excluded as not approved, which is a scope rule rather than a judgement: navitoclax, fisetin, quercetin, resveratrol, AICAR, nicotinamide mononucleotide, nicotinamide riboside, and KIF18A and Mps1 inhibitors. That is correct.

---

## Exclusions that do not survive

### 1. Sirolimus, excluded on a claim contradicted inside this project

**Stated reason** (`panel/round1_geneticist.md`): "Sirolimus: same mechanism as everolimus without the paediatric formulation."

**The project's own pharmacy file says the opposite** (`creative/I_pharmacist.md`): "Sirolimus solution over everolimus. Both giveable liquids; sirolimus has a paediatric dosing base at this weight and costs a tenth as much."

Both cross-model passes flagged this contradiction. It was never resolved, and sirolimus remained excluded on the false half.

**Status: the stated reason is wrong.** Whether sirolimus should be excluded on other grounds, the rapalog arguments in section 7, is a separate question that this exclusion never engaged with.

### 2. HSP90 inhibitors, excluded as unapproved when one is approved

**Stated reason** (`panel/round1_cellbiologist.md`, `panel/round1_family.md`): grouped with "not approved medicines".

**The project's own drug-mapping output says** (`creative/E_drugmap_output.md`): "Pimitespib is approved in Japan only."

Approved in one jurisdiction is approved. The class was excluded by a scope rule that does not apply to it.

**Status: the stated reason is wrong.** The report does still carry pimitespib in a section 7 row, so it was not entirely lost, but it was removed from candidate consideration on a false premise rather than assessed.

### 3. Hydroxyurea, excluded because it interferes with the measurement

**Stated reason**, in three separate seats: it "raises micronucleated reticulocytes, inverting the readout I use to judge every other candidate", and "adding a micronucleus inducer to a constitutional CIN disorder is unjustifiable."

The second clause is a safety argument. The first is not: **it excludes a drug because it would spoil the chosen endpoint.** That is a reason to pick a different endpoint, not a reason to withhold a medicine from a child.

**Status: one of the two stated reasons is methodological convenience dressed as a clinical judgement.** The safety argument may well stand on its own; it was never separated from the other and never tested.

### 4. Colchicine, griseofulvin, vinca alkaloids and taxanes outside oncology, excluded on a hypothesis

**Stated reason**: "approved aneugens", citing the mechanism.

**The report itself now labels that reasoning a hypothesis for follow-up**, and states that no study has shown MVA or *BUB1B* patient cells to be hypersensitive to any spindle agent, and that the two available laboratory lines predict opposite outcomes.

**Status: the exclusion is not wrong, but it is not evidence-based either.** These are candidates ruled out by the same untested inference that section 5 flags as untested. That is defensible as caution and indefensible as a finding, and the distinction was not made when they were dropped.

### 5. Growth hormone, excluded on a factual claim that was wrong

**Stated reason**: "no efficacy in MVA2", elsewhere given as no response in two MVA2 patients tested.

**Corrected during the research loop**: the source reports one MVA2 patient treated from age 6 with "only poor response", and states generally that MVA2 patients probably do not benefit. Not two patients with no response.

**Status: the exclusion probably stands**, since there is still no efficacy evidence and mecasermin carries a labelled contraindication with a malignancy history. But it was made on a misread source, and the report only corrected the sentence, not the decision that rested on it.

---

## Exclusions that survive checking

| Excluded | Stated reason | Holds |
|---|---|---|
| Mecasermin | Labelled contraindication with a history of malignancy | Yes, a label is checkable and was checked |
| Acetazolamide, topiramate | Carbonic anhydrase inhibition promotes stones, documented for topiramate in children with resolution on withdrawal | Yes for topiramate, inferred for acetazolamide, and the report says so |
| High-dose intermittent vitamin D | Association with later nephrocalcinosis | Weak and labelled weak: a ten-patient series the authors call suggestive |
| Aspirin, statins | No link to the biology; statin myopathy against low muscle mass | An absence claim, but a reasonable one, and nothing has since contradicted it |

---

## What this changes

**Nothing in the report's positive recommendations.** No excluded candidate is being reinstated here, because reinstating one would need the work that was skipped the first time, not a note.

**It changes what the report can claim about its own method.** Section 3 describes a process in which candidates were generated and then narrowed. The narrowing was not audited, and five of the exclusions rest on a reason that is wrong, methodological, or explicitly hypothetical. The report should say so rather than let a reader assume the exclusions were held to the same standard as the assertions.

**And it names the real limitation of simulated panels.** They are useful for generating candidates and for surfacing disagreement, which is what the verification pass found panel 2 genuinely contributed. They are not a source of evidence, and when a seat writes "excluded" with a reason, that reason needs checking exactly like any other claim. In this project it was not.
