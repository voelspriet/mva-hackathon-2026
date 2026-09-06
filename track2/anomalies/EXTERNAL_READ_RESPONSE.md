# Response to the external read

`track2/audit/PROMPT_E_external_read.md` was run on Fable 5.1 against a de-identified package of the supplied phenotype, the anomaly measurements, the primary-data re-analysis and the synthesis. Output at `vertex/out/promptE__anthropic.md`.

**It found more errors in this project's own material in one pass than the two cross-model passes found all day**, because it was pointed at the derived files rather than at claims about the literature. Everything below was checkable from data in hand, and was checked.

---

## Checks run in response, and what they returned

### 1. Contamination is excluded, so the allele-balance bounds need no contamination term

**Asked because** the read pointed out that 57 percent of the low allele-balance tail sits outside the fifteen artefact bins and was never quantified, so contamination was not excluded by the regional argument alone.

**Measurement.** The standard single-sample estimate: reference-supporting reads at homozygous-alternate autosomal single-nucleotide sites at depth 30 or more, 1,304,728 sites.

| Statistic | Value | Interpretation |
|---|---|---|
| Mean reference-read fraction | 0.0005 | a clean sample sits near 0.000 to 0.005 |
| Median | 0.0000 | |
| Sites above 0.02 | 1.29 percent | |

**Recomputed on PASS calls only**: 1,295,341 sites, mean reference-read fraction 0.0005, median 0.0000. Unchanged. This is the one anomaly measurement that filtering does not move at all.

**Contamination is excluded.** The low-allele-balance tail is not foreign DNA, and no contamination term is needed in the mosaicism floor or in the appendix's allele-depth model.

### 2. The sex is 46,XY, which was asserted without the X measurement

**Asked because** the read noted that Y at half autosomal depth is consistent with both 46,XY and 47,XXY, and that X was never reported.

**Measurement.** Non-pseudoautosomal X, PASS calls: **103,068 calls, median depth 21 against an autosomal 43**, with **1.3 percent heterozygous**. An earlier unfiltered pass gave 107,895 calls at median 20 with 2.5 percent heterozygous; filtering makes the reading cleaner. Two X chromosomes would give a ratio near 1.0 and heterozygosity near 50 percent.

**One X and one Y.** The claim now rests on a measurement rather than on the Y alone.

### 3. The runs-of-homozygosity result was produced by an insensitive method

**Asked because** the read observed that zero runs at any threshold is itself an unusual result for a human genome, and that the thresholds were not stated.

**The criticism is correct.** The original scan used the *ratio* of heterozygous to total calls per megabase, which is not how homozygosity is detected. Re-run with absolute heterozygous single-nucleotide density per 100 kb against a genome median of 95 per window, taking runs below 10 percent of that median:

| Run | Span |
|---|---|
| chr12:32.8 to 34.6 Mb | 1.8 Mb, pericentromeric |
| chr8:111.1 to 112.6 Mb | 1.5 Mb |
| chr7:124.9 to 126.1 Mb | 1.2 Mb |
| chr4:72.8 to 73.9 Mb | 1.1 Mb |
| chr12:110.4 to 111.5 Mb | 1.1 Mb |

Five runs, 6.7 Mb in total, longest 1.8 Mb. **The conclusion is unchanged and now rests on a method that works.** Six point seven megabases of short runs is ordinary for an outbred genome; consanguinity at first-cousin level produces runs above 10 Mb and totals above 50 Mb. **None is on chromosome 15**, so isodisomy at the *BUB1B* locus remains excluded.

### 4. The stated blind spot is wrong, and both recurrent microdeletions are excluded

**Asked because** the read pointed out that the recurrent deletion intervals are flanked by low-copy repeats but their interiors are largely unique and mappable, so the claim that a deletion there "would be invisible to every scan run in this project" might be false.

**It is false.** Measuring the unique interiors rather than the flanking repeats:

| Interval | Calls | Median depth | Heterozygosity |
|---|---|---|---|
| 22q11.2 interior, chr22:19.0 to 21.4 Mb | 4,487 | 42 | 72.4 percent |
| 15q11-q13 interior, chr15:22.8 to 28.3 Mb | 10,478 | 43 | 66.5 percent |

Autosomal median depth is 42. A heterozygous deletion would give roughly half that with heterozygosity near zero. **Both intervals are normal, so the two commonest recurrent microdeletions in the genome are positively excluded** rather than being a blind spot. The blind spot is confined to the repeat blocks themselves.

### 5. All 33 no-call gaps are now classified, not 20 of 33

The thirteen smaller gaps run 150 to 203 kb. Five are on the X chromosome, where a male carries one copy and lower call density is expected; the remainder are pericentromeric or acrocentric, at chr16:33 to 34.5 Mb and chr21:8 to 9.5 Mb. None sits in autosomal unique sequence.

---

## Errors in this project's files that the read identified and that are confirmed

| Where | The error | Status |
|---|---|---|
| `ANOMALIES.md` D8 | "A deletion there would be invisible to every scan run in this project" | **Wrong.** Corrected; see check 4 |
| `ANOMALIES.md` D3 | "roughly 155,000 that fail ... dominated by MQ40 at 177,522" | A single filter cannot exceed the total failing. The two counts have different denominators: 155,000 over primary contigs, 177,522 filter applications over the whole file including non-primary contigs and multi-filter records. Corrected |
| `ANOMALIES.md` D2 | "Four of the eight ... exactly the growth and perinatal cluster" | On the table's own evidence the count is five or six, and recurrent miscarriage is family history rather than growth or perinatal. Corrected |
| `ANOMALIES.md` D2 | "the earliest measurable manifestation of the syndrome, preceding the tumour and the renal finding" | Contradicts the literal reading of "present since birth" that D1 deliberately keeps open, and the parental losses precede the birth entirely. Corrected |
| `reanalysis/SUMMARY.md` R2 | "Zero runs at any threshold tried" | Method was insensitive; see check 3. Corrected |
| `reanalysis/SUMMARY.md` R5 | "two rare missense variants" against "the 80-gene network carries 1 rare coding variant" | Different gene sets: the 80-gene network contains only one of them. Corrected |
| `SYNTHESIS.md` Part 2c | "None of this has been run. The prompt exists; the work does not." | Stale. It was written before the re-analysis and never updated. Corrected |
| `SYNTHESIS.md` Part 3 | "Six layers ran in sequence" above a table of eight rows | Corrected |
| `SYNTHESIS.md` Part 1 item 1 | "causal genotype ... independently confirmed" | Agreement with a scorer confirms the pair is the expected answer, not that it is causal; for a recessive condition causality requires trans, which item 2 states is unproven. Corrected |

## Identified, not yet resolved

- **The positive control mixes mechanisms.** Paralogous mismapping at the T-cell receptor and immunoglobulin loci produces the same allele-balance skew as somatic recombination, without any somatic process. Distinguishing them needs the depth profile across those loci, which is in hand and not yet read.
- **The mitochondrial detection claim is stronger than the measurement.** A germline diploid caller records minor fractions only at sites it called, so a heteroplasmy at 5 to 20 percent might produce no record at all. Blood heteroplasmy can also be low where muscle is high, and nuclear-encoded mitochondrial genes were not examined.
- **The birth weight centile names no chart and no sex.** Now that the sex is measured, a z-score against a named preterm reference is obtainable.
- **The 78,917 calls on non-primary contigs remain unexamined.**

## Note on the method

The read was run on the model that refused this project's corpus twice earlier today. It did not refuse this package. The package differs in being derived measurements and summaries rather than a dossier of individualised therapeutic reasoning, which is consistent with the pattern recorded in `vertex/REFUSAL_EXPERIMENT.md`. The first attempt returned 2,642 characters and stopped at the output limit; raising the limit to 40,000 tokens produced a complete answer of 34,735 characters.
