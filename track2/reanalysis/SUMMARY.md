# Re-analysis of the primary data: what was asked, what was found, what is left

Run under `track2/audit/PROMPT_B_reanalysis.md`, after the audit round and both cross-model passes. Every angle below was computed from data already in hand. No patient data left this machine; gnomAD was read as a static public file by byte range, never queried with a patient coordinate.

## Computed, with the answer

Ordered by what the answer changes.

| # | Question | Answer | Changes |
|---|---|---|---|
| R5 | Is there a modifier in the checkpoint, cohesion or decay machinery? | **No.** Two rare missense variants outside *BUB1B* (SGO1 p.Thr425Ala, ANAPC2 p.Gly297Asp) and one synonymous likely-benign. The 80-gene network carries 1 rare coding variant where its coding length predicts 9. It is depleted, not enriched. | Converts the report's assumption that no rare variant exists in the decay machinery into a computation. Closes the digenic hypothesis. |
| R6 | Are the bins the mosaicism scan discarded, and the outliers it recorded but never read, informative? | **No, and the method has a hole.** 56 bins exceed the threshold; all imply cell fractions above 1.0, which is impossible, and all sit in heterochromatin, acrocentric arms, centromeres or the MHC. | The 11.7 percent per-bin detection floor is a genome average that does not hold in these regions. The method needs a mappability filter. The negative result is unaffected. |
| R1 | Can phase be read out of the existing VCF? | **No.** Neither variant carries a phase set, and at 10.9 kb apart no short-read library can join them. The raw reads would not answer it either. | Confirms the gate's first item cannot be shortcut. Removes the raw-read download as a route to phase. |
| R2 | Runs of homozygosity, consanguinity, uniparental disomy? | **None.** Zero runs at any threshold tried. Chromosome 15 is unremarkable around *BUB1B*. | Excludes isodisomy and consanguinity. Heterodisomy remains untestable without parents. |
| R3 | Copy number from depth? | **Nothing but mapping artefact.** Every outlier window is a centromere or an acrocentric short arm. | Excludes a deletion spanning *BUB1B*, at megabase resolution only. |
| R4 | The mitochondrial genome? | **Thirteen variants, all at or near homoplasmy.** Highest minor fraction 2.1 percent, in the control region. Coverage 1,700 to 5,200 reads. | Removes a second explanation for the growth and muscle phenotype, and the drug contraindications that would follow it. |

**The pattern across all six is negative.** That is the useful part. Six routes by which the Track 1 answer could have been wrong or incomplete are now closed by computation rather than by not having looked.

## Proposed, not computed

| # | Question | Data | Why it was not done here |
|---|---|---|---|
| P1 | Deep intronic and regulatory variants near *BUB1B* | In hand | Needs a splice and regulatory prediction model this project does not hold offline |
| P2 | Structural variant signatures visible in a germline VCF | In hand | The VCF carries no split-read or discordant-pair evidence; a caller on the reads is the right instrument |
| P3 | Overlay of a segmental duplication and mappability track on the R6 outlier bins | Obtainable, free | The track is not held offline |
| P4 | Haplogroup assignment and a curated pathogenicity check on the 13 mitochondrial variants | Obtainable, free | Needs MITOMAP or equivalent |
| P5 | What the 84 GB of raw reads would answer that the VCF cannot | Gated, not downloaded | Only two things: exon-level copy number, and coverage in the regions where no variant was called. Neither changes a recommendation, and neither answers phase. |
| P6 | Methods published since 2024 in single-cell and long-read aneuploidy detection | Public | This is a literature question, not a data question, and belongs in the research loop |

## What this does not do

It does not change any recommendation in `REPORT_track2.md`. Six negatives and one methodological hole are the whole of it. The one place the report should be touched is the mosaicism detection floor, which is now known to be a genome-average figure that fails in low-mappability regions, and that qualification belongs beside the figure.
