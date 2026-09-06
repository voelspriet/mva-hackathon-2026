# What today's work is worth against the four judging criteria

The panel judges on **scientific rigor, potential impact, innovation and scalability** (challenge FAQ), and for Track 1 also on depth of understanding in the methods write-up. This note sorts everything produced on 6 September against those four, states the strength of each item, and names what should not be claimed.

**The headline, stated before the detail: nothing here changes the answer.** The diagnosis was *BUB1B* compound heterozygous at the start of the day and it still is. Every item below strengthens, bounds, or falsifies part of the reasoning around it. A submission that presents any of this as a new discovery will be caught.

---

## Scientific rigor

**Strong. The candidate space, measured rather than asserted.** The compound-heterozygote pattern is not rare on its own: 224 genes in this genome carry two coding variants absent from the common catalogue. Applying the candidate's own frequency threshold (gnomAD < 1e-4 on both) leaves 8. Adding four call-quality measurements (coverage ratio, allele balance, genotype quality, inter-variant distance) leaves **2**: *ADGRA3* and *BUB1B*. Neither filter uses the phenotype, a gene panel or any disease knowledge. `R15`, `R21`

**Strong. A heuristic of ours, falsified by measurement.** Genes were first labelled artefact-prone by name prefix. Tested against measurement on 164 genes, that label disagreed 79 times, and 78 of those were false clearances: genes marked "worth examining" that four measurements dispose of. A heuristic that fails safe is tolerable; this one failed open. Reporting it is worth more than hiding it. `R21`

**Strong. A negative with an internal positive control.** The focal copy-number scan at 100 kb finds no autosomal deletion or duplication, including at *BUB1B*, which closes the hemizygous alternative to the compound heterozygote. The scan's longest hits are chrX and chrY at ratio 0.50 across hundreds of consecutive windows, so the method demonstrably detects a true one-copy state. A negative without such a control is worthless. `R18`

**Solid. The two candidate variants re-derived independently.** A second aligner (minimap2) and a raw pileup, no caller involved: alt fractions 0.543 and 0.517, strand balance 0.52 and 0.33. Neither call is an artefact of the original pipeline. `R18`

**Solid. Statistical power separated from systematic floor.** Counting noise permits 0.41% (chr2) to 1.15% (chr22); residual GC and mappability bias sets the achievable floor near 2%. This also corrects a figure of our own: `R17` quoted 4% from the largest observed deviation, which conflated the two. `R18`

**Modest. A control that found nothing.** The mutational spectrum is ordinary: Ti/Tv 2.01, C>T 34.1%, CpG C>T 12.2%, no excess of C>A. It removes one alternative explanation for everything built on these calls. Worth one sentence, not a section. `R16`

**Rigor is also visible in the corrections.** Three are recorded in place rather than quietly fixed: the 4% floor (`R17` → `R18`), the coherence test that promoted heterochromatin at ratios of 3 to 7 (`R19`), and a coverage rule that flagged high but not absent coverage (`R21`).

---

## Potential impact

**Strong, and the most transferable item produced today.** Bulk sequencing is structurally blind to this disease. Mosaic **variegated** aneuploidy puts different chromosomes in different cells, so if a fifth of cells were aneuploid for a randomly different chromosome, the per-chromosome affected fraction is about 1%, below any bulk floor including the improved one. This is why karyotyping remains the diagnostic standard and why WGS cannot replace it here. It saves the next team a wasted week. `R17`

**Strong. The detection floor lowered with a measurement behind it.** From the 10% stated in the report to about 2%, by GC-bin normalisation of read depth. Chromosomes that looked elevated rank by GC content, and correcting removes it. `R17`, `R18`

**Solid, and it demonstrates the screen works.** A blind enumeration surfaced a genuine copy-number difference at chr5:69.6-71.1 Mb; `SMNCopyNumberCaller` resolved it within the hour as *SMN1* copy number 2, *SMN2* copy number 0, not SMA and not a carrier. Three copies where four is typical explains the measured 0.73-0.77 exactly. The finding is benign, and the chain is the point. `R19`, `R20`

---

## Innovation

**Strong. Read-backed phase used as an eliminator, not a check.** `PGT`/`PID` are in every GATK VCF and are conventionally used to check one candidate. Applied across the whole candidate list they become a filter: 79 of 151 genes eliminated with proof because both variants sit on one haplotype and the other allele is intact, including *KIR3DL3*, the only other gene meeting the strictest frequency threshold. Seconds of compute, no new data. `R15`, `R18`

**Solid. The enumeration protocol itself.** 2,013 candidate observations produced by rule across thirteen classes, with the phenotype document excluded and the known candidate genes given no special treatment, each line carrying class, locus, measurement, comparator and status. The value is coverage and auditability, not insight: it is a written record of what was looked at, including everything that was nothing. `OBSERVATIONS_2000.md`, `PROMPT_2000_observations.md`

**Modest. GC-bin normalisation of window depth.** Standard technique, applied here to a floor that had not been measured this way.

---

## Scalability

**Solid, and directly answerable with numbers.** Seven of the ten substantive findings need only the supplied VCF: 61 seconds scripted plus about seven minutes of gnomAD API queries, on a laptop. Three need the raw reads: 78.85 GB downloaded, 4 h 35 min alignment on 20 cores, 137 GB peak disk, 51x median coverage. For a cohort the first tier scales linearly at negligible cost and the second does not. `R18`

**The 224 to 2 reduction is the scalable part.** Both filters are linear in genome size, need no training, no panel and no phenotype, and run in minutes. That is a statement about the method rather than about this child.

---

## What must not be claimed

- **The 2,013 observations are not findings.** They are a screening layer, 1,372 unexamined by design. Any sentence implying two thousand results is false and checkable.
- **ADGRA3 is not a rival diagnosis.** It is the only other gene surviving two measured filters, which makes it a candidate for explicit exclusion, nothing more.
- **The SMN result is negative.** Two copies of *SMN1* is normal.
- **Nothing here says how other practitioners work.** Every count describes this analysis. The claim that a background count or a genome-wide phase filter is unusual in the field has no evidence behind it and was withdrawn.
- **The mutational spectrum found nothing.** Presenting a null control as a result is padding.

---

## The three sentences to put in the methods form

> The compound-heterozygous pattern is not rare in isolation: 224 genes in this genome carry two rare coding variants. Applying the candidate's own frequency threshold leaves 8, and adding four call-quality measurements leaves 2, of which *BUB1B* is one; neither filter uses the phenotype or a gene panel.

> Read-backed phase (`PGT`/`PID`) was applied genome-wide as an eliminator rather than as a check on the candidate, removing 79 of 151 genes with proof that both variants lie on one haplotype.

> Coverage from the supplied raw reads, GC-normalised in 100 kb windows, lowers the mosaic-aneuploidy detection floor from about 10% to about 2% of cells; nothing is present above it, and the method is in any case structurally blind to variegated aneuploidy, which is why karyotyping remains the standard for this condition.
