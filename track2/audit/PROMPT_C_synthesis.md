# Prompt C: synthesis of the whole project, and what to do next

## Purpose

The project is now large enough that no single file states what it knows. This pass reads everything that was produced, states what the work established, states what it failed to establish, and proposes the next actions in the order that a reader with limited time should take them. It produces no new claims about the world. Every statement in the output traces to a file already in the repository or to a primary source retrieved during this pass.

## What was produced, and what reads it

1. Two reports: `REPORT_track1.md`, `REPORT_track2.md`.
2. Five research dossiers, ten divergent lenses, three gate files.
3. Thirteen expert seats across two panels, four rounds, plus a final objection round.
4. Three verification passes and three independent referee reports.
5. Five audit partitions covering 577 claims against primary sources.
6. Two cross-model passes on a de-identified corpus, four neutral prompts each.
7. A pipeline that runs Track 1 end to end, a drug-mapping tool, and a quantitative appendix with its script.

## The task

### Part 1: what the project established

State, in order of how much would have to be retracted if it were wrong, what this project now holds to be true. For each:

- The claim, in one sentence.
- The evidence tier: measured in this project, measured in a primary source, inferred, or assumed.
- Which files carry it, and which stage it survived. A claim that survived the audit is not the same as one no auditor read.
- What would falsify it.

### Part 2: what the project failed to establish

Separate three kinds of failure, because they call for different responses.

- **Answered in the negative.** A question was asked and the answer is no. Metformin and dasatinib belong here.
- **Unreachable.** The evidence exists but could not be retrieved. List every UNVERIFIABLE verdict from the audit and every paywalled source, with the routes already tried, so that the next reader does not repeat them.
- **Never asked.** Questions the structure of the work made invisible. This is the part the panels are worst at, because every seat was briefed from the same dossiers.

### Part 3: the review process, judged on its own output

The project ran six review layers: two panels, an objection round, three verification passes, three referees, five audit partitions, and two cross-model passes. For each layer:

- What it caught that no earlier layer had.
- What it missed that a later layer caught.
- Its cost in time and tokens, where recorded.

Then answer the question the sequence poses: which layers earned their place, which were redundant, and what a second project should run instead. Report the answer even where it is unflattering to a layer that was expensive.

### Part 4: next steps

Propose the actions that remain, each with:

- The action, stated so it can be executed without further interpretation.
- What it changes: a claim, a recommendation, a number, or a submission artefact.
- Its cost, in the units that bind: elapsed time, money, tokens, or a decision the user must make.
- Its dependency, if it must follow another action.
- Whether it can be executed here, or requires the user, or requires someone outside this project.

Order them by what they change per unit of cost. Separate the actions that must happen before the hackathon submission from the actions that are research in their own right.

## Method

- Read the files rather than the summaries of the files. Where a summary and its source disagree, the source governs, and the disagreement is reported.
- Where a number is stated, recompute it from its inputs.
- Where a claim is attributed to a stage of the process, verify that the stage's own file contains it.
- Nothing is proposed that requires contact with the family, the organisers, or any third party.

## Output

`track2/synthesis/SYNTHESIS.md`, with Parts 1 to 4 as its sections, and `track2/synthesis/NEXT.md` carrying only the ordered action list, so that it can be worked through and ticked off.

## Constraints

Claims are labelled by tier. Inference is labelled inference. A dead end is reported as a dead end, with what was checked. No em or en dashes. No adjectives of praise or alarm. No recommendation is made about this child's care in this file; care recommendations live in `REPORT_track2.md` and are not restated here.
