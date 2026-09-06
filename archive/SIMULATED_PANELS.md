# Simulated expert panels are not a source of evidence

A method note, written because this project got it wrong and then measured how wrong.

## What was done

Thirteen simulated specialist seats across two panels, briefed from five research dossiers, run over four rounds with cross-objections and a moderator. A clinical geneticist, a cell biologist, an oncologist, a pharmacologist, a nephrologist, an immunologist, and so on. Each produced ranked candidates, objections to the others, and a list headed **Excluded**.

## What they were good for

Two things, and both are real.

**Generating candidates.** The seats produced a candidate space no single line of reasoning would have reached, because each seat looked from a different discipline.

**Surfacing disagreement.** An earlier version of this project's synthesis claimed the second panel duplicated the first and recommended dropping it. Checking that claim refuted it: the two panels shared no specialty, and two of the report's four surviving outputs came from panel 2 alone, its nephrologist finding two renal causes that demand opposite prescriptions, and its pharmacokinetics seat computing the plasma concentration that removed the leading candidate. Disagreement between differently-briefed readers is productive.

## What they are not

**A source of evidence.** A seat's conclusion is a language model's assertion. It has the form of an expert judgement and none of the standing of one.

This is obvious when stated and easy to forget in practice, because the output looks like a specialist's opinion, arrives in a specialist's register, and is filed under a specialist's job title.

## The failure mode, measured

This project audited 577 claims against primary sources across five partitions. **184 did not hold.** That audit examined what the report *asserts*.

It never examined what the report *dropped*. The exclusions were made by simulated seats writing the word "excluded" followed by a reason, and those reasons entered the record and were never tested. Checking them afterwards, five did not survive:

| Excluded | Stated reason | What was wrong |
|---|---|---|
| Sirolimus | "without the paediatric formulation" | This project's own pharmacy file says sirolimus has a paediatric dosing base at this weight and costs a tenth as much. Both cross-model checks flagged the contradiction; nobody resolved it |
| HSP90 inhibitors | grouped under "not approved medicines" | This project's own drug-mapping output records that pimitespib is approved in Japan |
| Hydroxyurea | "raises micronucleated reticulocytes, inverting the readout I use to judge every other candidate" | That is a reason to change the endpoint, not to withhold a medicine from a child. It sat beside a genuine safety argument and the two were never separated |
| Colchicine, griseofulvin, vincas, taxanes | "approved aneugens" | Excluded by an inference the report itself labels a hypothesis, on which no study has shown these cells to be hypersensitive and the two available lines predict opposite outcomes |
| Growth hormone | "no response in the two patients tested" | The source reports one patient with a poor response |

**Two of those five were contradicted by files inside the same project.** The information needed to catch them was already on disk. Nobody looked, because an exclusion did not present itself as a claim.

## The rule that follows

**Treat every exclusion as a claim, and audit it exactly as you audit an assertion.**

An exclusion is the highest-leverage output of a review process, because it ends an investigation. An assertion that survives into the report will be read, questioned and possibly checked by someone else. An exclusion is invisible: the candidate is simply absent, and no reader can question a name they never see.

Three specific consequences.

1. **Separate the scope rule from the judgement.** "Not an approved medicine" is a scope rule and is checkable in a minute. "Would not work" is a judgement and needs evidence. Group A can be dispatched in a list; group B cannot.
2. **Separate the methodological convenience from the clinical reason.** Excluding something because it would spoil your measurement is a statement about your study design. Presented in the same sentence as a safety argument, it borrows credibility it has not earned.
3. **Do not let a hypothesis do the work of a finding.** Where a candidate is excluded by a mechanism argument the project elsewhere labels untested, say so at the point of exclusion, not only at the point of assertion.

## The wider point

The value of a simulated panel is that it is cheap enough to run many of, and diverse enough to disagree with itself. Both properties are lost the moment its output is treated as testimony rather than as generated text.

The finding that a simulated seat is not evidence is not a reason to stop using them. It is a reason to put the audit *after the narrowing* as well as after the writing, which is where this project put it only on the second attempt.

---

*Evidence for every claim in this note is in `archive/audit/EXCLUSION_AUDIT.md`, `archive/synthesis/VERIFY_headline_claim.md` and `archive/audit/AUDIT_SUMMARY.md`.*
