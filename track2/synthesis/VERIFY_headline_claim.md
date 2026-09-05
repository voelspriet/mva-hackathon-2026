# Adversarial verification of the project's headline methodological claim

The claim in `SYNTHESIS.md` Part 3 was going to be the thing shown to judges. It was decomposed into four falsifiable parts and each was attacked rather than confirmed. **Three of the four did not survive in the form they were written.** What survives is narrower, and in one respect more interesting than the original.

---

## The robust version, rewritten so every sentence survived

**In this project, the errors were introduced at the summarising step, not at the research step, and the cheapest reviewers were the ones who caught them.**

Section 8 of the report, which recounts the project's own power calculation, carries **7 contradicted claims in 21 audited**, a 33 percent contradiction density. The rest of the report runs at 5 percent and the mathematics appendix it summarises runs at 4 percent. That is a genuine outlier and the largest concentration of flat contradictions anywhere in the corpus.

The same pattern holds for two of the three errors the referees caught. The correspondence between the mouse residue and the human one was stated correctly in the project's first research dossier, which reads "BubR1^L1002P (modelling human L1012P)". The electrocardiogram finding was likewise placed correctly in that dossier, in the row for the SIRT2 transgene on the hypomorph, citing North 2014. **In both cases the dossier was right and the report lost it.** The referees did not supply missing knowledge; they found where the summary had corrupted its own sources.

Only one of the three was a fact nobody in the project held. The correct RMS 2005 survival figures, 86.5 against 73.7 percent, appear **nowhere** in any panel file, creative file or research dossier; the wrong figures appear in ten files, originating in the dossier and propagating. Two referees found it independently. That one is a genuine external catch.

**The referees were cheap and effective because they were the only readers not briefed from the project's own dossiers.** That is the transferable point, and it is about briefing, not about expertise or headcount.

---

## Killed

### Claim 3, that panel 2 duplicated panel 1: REFUTED

This was wrong, and it was wrong in a way that matters, because it was the basis for the recommendation to drop the second panel.

The two panels shared **no specialty at all**. Panel 1: cell biologist, family representative, geneticist, oncologist, pharmacologist. Panel 2: CIN biologist, endocrinologist, second family representative, immunologist, laboratory geneticist, nephrologist, PK pharmacologist, predisposition oncologist.

The integrating moderator record names team 2's distinct contributions 23 times against 26 for team 1, and **two of the report's headline outputs came from panel 2**:

- "Team 2's nephrologist showed two causes demanding opposite prescriptions: nephrocalcinosis of prematurity vs ifosfamide tubulopathy" — this is the renal work-up, one of the four surviving recommendations.
- "Team 2's PK seat computed plasma at 7..." — this is the metformin exposure arithmetic, which is what removed metformin from the ranked list.

A panel that produced the renal work-up and killed the leading candidate did not duplicate anything. **The recommendation to drop the second panel is withdrawn.**

### Claim 2 in its general form, that errors cluster in the report rather than the work: REFUTED as stated

Two independent reasons.

**Selection.** `PROMPT_A_source_audit.md` scopes the audit to deliverables in priority order and states that "working files in panel/ and panel2/ rounds 1 and 2 are out of scope". Panel rounds contributed 9 and 2 audited claims against the report's 181. A comparison of raw error counts between the report and the working files is therefore an artefact of what was audited.

**Rates.** Where families were audited comparably, the report is not an outlier at all.

| File family | Claims | Non-supported | Rate |
|---|---|---|---|
| REPORT_track2 | 181 | 72 | 40% |
| Research dossiers | 75 | 28 | 37% |
| Creative lenses | 136 | 43 | 32% |
| Gate files | 113 | 14 | 12% |

Forty percent against thirty-seven is not a cluster. The claim only holds for the specific section-8-versus-appendix pair, where the gap is 33 percent contradicted against 4 percent.

### The sub-claim that the appendix "recomputes exactly": REFUTED

`creative/F_math.md` carries **17 non-supported claims of 60 audited**, including four misattributions, one of them a PMID pointing at a brain-tumour polymorphism study, and an internal inconsistency between a table header reading 11.2 percent and the 11.7 percent derived four lines above it. Its arithmetic is largely sound; the document is not clean, and saying it was overstated the contrast.

---

## Caveated

**Claim 1 survives only in narrowed form.** Three referees with no access to working files found three consequential errors. But only one, the RMS 2005 survival figures, was a fact absent from the whole project. The other two were present and correct in the project's own first dossier and were corrupted in the report. The correct statement is that the referees caught two summarisation failures and one propagated factual error, which is a different and more useful finding than "they knew things thirteen specialists did not".

---

## Open

**Claim 4, that nobody has published comparable measurements: UNVERIFIABLE.** It was asserted with no search behind it. Searches across PubMed and OpenAlex for published error-rate measurements on multi-agent or LLM-assisted review pipelines returned nothing comparable, but the queries returned little of any kind, the field moves faster than either index, and most such work appears at machine-learning conferences that neither covers well. Per the rule that absence of a refuting hit is not proof, this is recorded as not established rather than as true. **What would settle it:** a search of the ACL, NeurIPS and ICML proceedings and of arXiv cs.CL for the last eighteen months. Until then the claim of novelty should not be made to a judge.

---

## What this episode demonstrates

The audit checked 577 claims against primary sources and did not catch any of this, because none of it is a claim about the world. Every failure above is a claim about **this project's own process**, and the audit had no instrument pointed there. That is the same gap named in Part 2 of the synthesis: verification catches wrong facts and never catches wrong framing. The headline claim was itself an instance of the thing it described.
