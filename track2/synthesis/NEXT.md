# NEXT: the remaining actions, ordered by what they change per unit of cost

Produced under `track2/audit/PROMPT_C_synthesis.md`. Reasoning is in `SYNTHESIS.md`. Each action states what it changes, what it costs, what it depends on, and who can do it.

---

## A. Before the hackathon submission

| # | Action | Changes | Cost | Depends on | Who |
|---|---|---|---|---|---|
| A1 | Upload the pitch video to YouTube, unlisted, with `video/mva_track2_pitch.vtt` as the subtitle track | The submission's video field | 10 minutes | Nothing | **The user.** Cannot be done from here. |
| A2 | Submit Track 2 on the Space: display name, GitHub URL, video link, `REPORT_track2.md`, and the note in `SUBMISSION_track2.md` | The submission itself | 10 minutes | A1 | **The user.** Three uploads are allowed and only the latest is read, so there is no cost to watching the video first. |
| A3 | Attach `submissions/henkvaness_track2_methods.xlsx` to the repository rather than resubmitting it through the form, per discussion #10 | Compliance with the organisers' own instruction | Done, verify only | Nothing | Executable here |
| A4 | Re-read `SUBMISSION_track2.md`'s judge note against the corrected report, since the audit round is now a stronger selling point than the referee round it describes | What the panel reads first | 20 minutes | Nothing | Executable here |
| A5 | Decide whether the repository goes public at close carrying the working files uncorrected | Whether the audit's own evidence survives, against the risk that a reader quotes an uncorrected working file as if it were the report | A decision, not time | Nothing | **The user.** The recommendation is to keep them, with the status column in `AUDIT_SUMMARY.md` as the guard. |

## B. Research that changes a claim in the report

Ordered by what each would change per unit of effort.

| # | Action | Changes | Cost | Depends on | Who |
|---|---|---|---|---|---|
| B1 | Run `track2/audit/PROMPT_B_reanalysis.md` against the primary data: phasing from PGT and PID, runs of homozygosity, mitochondrial genome, depth-derived copy number, absent-coverage regions, uniparental disomy and copy-neutral loss of heterozygosity, segmental mosaicism, the discarded bins, X and Y | Potentially the mosaicism bound, the modifier question, and whether phase is partially readable from the VCF itself without a trio | Hours of compute on data already in hand; no money | Nothing. The data, the prompt and the pipeline all exist. | **Executable here. This is the largest unclaimed result in the project.** |
| B2 | Test whether phase is readable from the existing WGS: the two variants are 10.9 kb apart, which is beyond a short read but not beyond read-backed phasing across intervening heterozygous sites | The single most consequential open claim in Track 1 | Hours | B1 overlaps it | Executable here |
| B3 | Re-source the Orphanet 75 percent cancer-risk figure, or delete the second decision-threshold row | A published threshold that currently rests on a figure this report could not retrieve | 1 hour, or one library request | Nothing | Executable here for the search; the user for institutional access |
| B4 | Reduce the dependence on Suijkerbuijk 2010 by finding a second source for each of the 28 claims that cite it, or by marking each as single-sourced in the report | The robustness of the whole mechanism section against one paper being wrong | 3 to 4 hours | Nothing | Executable here |
| B5 | Retrieve the six publisher-gated sources listed in `SYNTHESIS.md` section 2b | Six UNVERIFIABLE verdicts become supported or contradicted | Under an hour with institutional access; unreachable without it | Nothing | **The user**, or anyone with a subscription |
| B6 | Cost the surveillance additions in burden rather than money: visits, sedation for imaging, false-positive rate, and what a family actually carries | A recommendation currently justified on the ground that it is free | 2 to 3 hours | Nothing | Executable here |
| B7 | Get the report in front of one real clinical geneticist or paediatric oncologist | The only thing thirteen simulated seats cannot supply | A decision and an introduction | A5, since it means showing the document to someone outside | **The user.** The report itself says it should not be posted publicly without the family's agreement, and that constraint governs here too. |

## C. Reusable output, worth doing regardless of the submission

| # | Action | Changes | Cost | Who |
|---|---|---|---|---|
| C1 | Package the four cross-model prompts and `run_passes.py` as a standalone tool, since the numeric recomputation pass is the cheapest useful check in the whole project and transfers to any document | Nothing in this report; everything in the next one | 2 hours | Executable here |
| C2 | Write up the review-layer comparison in Part 3 as a method note: which of six layers caught what, and why the referees beat the panels | The methodological claim the project can actually defend | 2 hours | Executable here |
| C3 | Add a single-source counter to the audit tooling, so that reliance on one paper surfaces at the start of a project rather than at the end | Future projects | 1 hour | Executable here |

---

## The one-line recommendation

**B1 first.** It is the only remaining action that can change a factual claim using data already in hand, at no cost beyond compute, and it is the one the project has been deferring since the audit round began.
