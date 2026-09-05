# Prompt A: source audit

## Purpose

Every factual claim in this project's deliverables is checked against the primary source it cites. The output is a per-claim verdict, not an opinion on the work.

## Scope

Deliverables, in priority order:
1. REPORT_track2.md
2. REPORT_track1.md
3. track2/gate/G1, G2, G3
4. track2/research/00 to 04
5. track2/creative/A to J
6. track2/panel/round4_grand_moderator.md and the eight final_*.md
7. track2/verify/V1, V2, V3

Working files in panel/ and panel2/ rounds 1 and 2 are out of scope except where a deliverable inherits a claim from them.

## Unit of audit

A claim is any sentence that asserts a fact about the world and carries or implies a source: a number, a date, a study result, a regulatory status, a dose, a gene or protein fact, a database record, an attribution of a position to a named paper.

Claims already adjudicated in V1, V2 or V3 are re-checked, not assumed. Two of those adjudications reversed a referee, and one reversed an earlier verification pass.

## Method

For each claim:
1. Record it verbatim with its file and line.
2. Identify the source it cites, or record that it cites none.
3. Retrieve the primary source. Full text where reachable; state the access level reached: full text, PMC, publisher abstract, supplementary file, database record, label, or unreachable.
4. Quote the passage that supports or contradicts the claim, verbatim.
5. Assign one verdict: SUPPORTED, OVERSTATED, CONTRADICTED, MISATTRIBUTED, UNVERIFIABLE, or NO SOURCE CITED.
6. Where the verdict is not SUPPORTED, write the sentence that should replace the claim.

Numbers are recomputed rather than read across. Where a claim rests on a figure, the figure number is verified. Where a claim rests on a supplementary file, the supplementary file is opened.

## Specific checks

These claims have changed at least once during the project and are re-derived from source:
- The concentrations at which metformin acted in Tang 2011, and in which cell types, for how long.
- Which figure of Suijkerbuijk 2010 contains the LAP-731X rescue, and what the allele IVS16-2A>G actually is.
- The RMS 2005 survival figures, their intervals, the primary endpoint and its p value.
- Mouse to human residue correspondence in BubR1, and which mouse genotype carries which human variant.
- Which paper reports the ECG J-point finding, in which genotype and sex.
- The residual BubR1 percentages attributed to mouse genotypes, and which paper first reported each.
- The doxycycline titration doses in Suijkerbuijk 2010 Figure 4D and the replicate count.
- ClinVar and gnomAD records for both variants, retrieved live.
- The regulatory status of ataluren and of the dasatinib oral suspension, per jurisdiction.
- Every PMID in every deliverable resolves to the paper it is cited as.

## Partitioning

The audit is split by source domain so that each auditor reads a coherent literature: (a) BubR1 molecular and mouse biology, (b) aneuploidy, senescence and immune surveillance, (c) clinical oncology, surveillance and rhabdomyosarcoma, (d) nephrology, endocrinology, nutrition, (e) pharmacology, regulatory status, formulations, (f) genetics, variant interpretation, databases, NMD, (g) statistics, power, and the quantitative appendix. Each partition is audited independently by a reader who does not see the others' work.

## Output

Per partition, a file at track2/audit/AUDIT_<partition>.md containing:
- A table: claim (verbatim), file and line, source cited, access level reached, verdict, correcting sentence.
- A list of claims that cite no source.
- A list of sources cited more than once whose PMID or DOI does not match the work described.
- A count: claims audited, and the verdict distribution.

Then one consolidated file, track2/audit/AUDIT_SUMMARY.md, listing every non-SUPPORTED verdict in one table, ordered by how much argumentative weight the claim carries, with the correcting sentence for each.

## Constraints

No claim is marked SUPPORTED on the basis of a secondary source, a review, or another file in this project. Where the primary source cannot be reached, the verdict is UNVERIFIABLE and the attempted routes are listed. No number is estimated. No em or en dashes. No adjectives of praise or alarm.
