# Every claim about the hackathon data, checked against the hackathon data

## Why this is separate from the source audit

The five audit partitions checked 577 claims against the **literature**. They did not check the claims this project makes about **the data it was given**: variant coordinates, genotypes, allele depths, variant counts, frequencies, and everything derived from the VCF and the phenotype document.

Those are the claims a judge can check fastest, because the data is in their hands too. This file checks them one file at a time. It is built up over repeated passes and records the check even where the claim was right.

**Method.** Each claim is recomputed from `data/WGS_EX2312012_HGWCNDSX7.vcf.gz` or from the supplied phenotype document, or retrieved from gnomAD v4.1 by indexed byte range. The recomputation is stated so it can be repeated.

---

## `REPORT_track1.md` — 11 claims, 10 exact, 1 correct but underspecified

| Claim | Recomputed | Verdict |
|---|---|---|
| "4.74 M PASS variants" | `bcftools view -H -i 'FILTER="PASS"'` gives **4,740,790** | **Exact** |
| "autosomal depth 44x" | Over PASS single-nucleotide variants at depth 20 to 120, autosomes, which is what `mosaic_baf.py` computes: **median 44**. Over all PASS autosomal variants including indels: median 43, mean 43.2 | **Correct for the pipeline's definition, which the sentence does not give.** Corrected to say which |
| Allele 1 `chr15:40209701 T>G`, genotype 0/1, allele depths 21/25 | Queried directly: `0/1`, `AD=21,25`, `DP=46`, `GQ=99` | **Exact** |
| Allele 2 `chr15:40220612 T>G`, genotype 0/1, allele depths 15/13 | Queried directly: `0/1`, `AD=15,13`, `DP=28`, `GQ=99` | **Exact** |
| Allele 1 gnomAD exomes 115/1,461,846, AF 7.9e-5 | Byte-range read of the public sites file: `AC=115 AN=1461846 AF=7.87e-05 nhomalt=0` | **Exact** |
| Allele 1 gnomAD genomes 5/152,174 | `AC=5 AN=152174 AF=3.29e-05 nhomalt=0` | **Exact** |
| Allele 2 gnomAD exomes 1/1,461,878, AF 6.8e-7 | `AC=1 AN=1461878 AF=6.84e-07 nhomalt=0` | **Exact** |
| "The variants are 10.9 kb apart" | 40,220,612 minus 40,209,701 = **10,911 bp** | **Exact** |
| "no read-backed phase (PGT/PID) is present on either" | Both records carry `.` in PGT and PID. Genome-wide, the longest phase set spans 288 bp | **Exact, and stronger than stated** |
| "314 genes pass the crude recessive-compatible filter" | `work/recessive_compatible_genes.txt` holds **314** lines | **Exact** |
| "The 81 ACMG SF v3.2 genes contain 10,895 PASS variants" | Gene list holds **81** symbols; `work/acmg.vcf.gz` holds **10,895** PASS records | **Exact, both halves** |

**Nothing in Track 1 is wrong.** The single imprecision is a depth figure that is right under the definition its own pipeline uses and ambiguous as written, which is the same failure mode the audit found elsewhere: a number correct at source and underspecified in the summary.

---


---

## `REPORT_track2.md` — data claims, first pass

| Claim | Recomputed | Verdict |
|---|---|---|
| "No rare variant in the NMD machinery or EJC core exists in this genome" | All 14 nonsense-mediated decay genes and all 7 exon junction complex genes are present in the scanned 80-gene set, and the rare coding variant file contains **zero** variants in any of them | **Exact.** The claim was previously an assumption carried from a working file; it is now checked directly |
| "Every PASS variant in the 60 kb upstream of *BUB1B*, 88 of them and 53 heterozygous" | On PASS calls only: **85 variants, 57 heterozygous**. The earlier figures were taken without the PASS filter and included three failing records | **Wrong, corrected.** The conclusion is unchanged: none absent from gnomAD genomes, the same two below one percent at AF 0.0021 and 0.0026 |
| Allele 1 "115 gnomAD v4 heterozygotes at AF 7.87e-5" | `AC=115 AN=1461846 AF=7.87e-05` by byte-range read | **Exact** |
| Allele 2 "gnomAD 1 of 1,461,878" | `AC=1 AN=1461878 AF=6.84e-07` | **Exact** |

**Note on the error found.** It was in text written the same day, by the same process that is auditing it, and it arose the same way as several of the errors this project found in its own earlier work: a query run without a filter that the surrounding argument assumed. The correct figures were one command away and nobody ran it.


---

## `track2/anomalies/` — a systematic filter fault, six measurements, no conclusion changed

The anomaly analysis was computed from a query that did not restrict to `FILTER="PASS"`. That swept in roughly 155,000 failing records, and those failures are concentrated in exactly the low-mappability regions the analysis reasons about, so the fault is not random with respect to the argument. Every measurement recomputed on PASS calls.

| Measurement | Unfiltered, as published | PASS only | Conclusion |
|---|---|---|---|
| Allele balance below 0.25 | 4.34 percent | **2.86 percent** | Unchanged, but the asymmetry is smaller: ratio 4.9 against the 7.0 reported |
| Allele balance above 0.75 | 0.62 percent | **0.58 percent** | Unchanged |
| Calls below 0.20 | 85,649 | **43,584** | **Half of the low tail was failing calls** |
| Share of that tail in the 15 busiest bins | 43 percent | **34 percent** | Still regional, less concentrated |
| Contamination, reference reads at homozygous-alternate sites | mean 0.0005, median 0.0000 | **mean 0.0005, median 0.0000** | Identical. The only measurement filtering does not move |
| Non-PAR X depth and heterozygosity | 20, 2.5 percent | **21, 1.3 percent** | 46,XY, and cleaner after filtering |
| No-call gaps of 150 kb or more | 33 gaps, 59.7 Mb | **78 gaps, 71.7 Mb** | More gaps, because removing failing calls opens gaps precisely where only failing calls existed. The six largest are the same heterochromatic blocks |
| Immune-locus depth against flanks | 45, 45, 46 against 43, 43, 42 | **46, 44, 46 against 43, 44, 43** | Unchanged. Depth is not reduced, so the withdrawal of the positive control stands on filtered data too |

**No conclusion changes. Several numbers do, one by a factor of two.** The pattern is worth naming: an unfiltered query does not bias a measurement randomly when the excluded records cluster in the regions under discussion. Here it inflated exactly the signal the entry was explaining away, which would have made the artefact argument look stronger than the data supports.


---

## `track2/reanalysis/` — the same filter fault, three more numbers, no conclusion changed

| Measurement | As published | PASS only | Conclusion |
|---|---|---|---|
| Runs of homozygosity | 5 runs, 6.7 Mb | **9 runs, 10.9 Mb**, longest 1.8 Mb, none on chromosome 15 | Unchanged. Ordinary for an outbred genome; first-cousin consanguinity gives runs above 10 Mb and totals above 50 Mb |
| Depth windows below 0.7x / above 1.4x | 50 / 14 | **11 / 19** | Unchanged. Most apparent low-depth windows were failing calls, which is what filtering should remove |
| Mitochondrial variants | 13 | **11 PASS of 13 called**. The two that fail, at 4769 and 8860, are near-universal differences from the reference | Unchanged. Highest minor fraction is 2.1 percent at 16093, confirmed on PASS calls |
| Phase, R1 | no phase set on either variant | Confirmed on PASS; longest phase set genome-wide is 288 bp | Unchanged |
| Modifier scan, R5 | 1 rare coding variant in the 80-gene network | Already PASS-filtered at source: `run.sh` builds that file with `FILTER="PASS" && INFO/DB=0` | **No fault. The only re-analysis measurement that was filtered correctly the first time** |

**Running total across the anomaly and re-analysis work: nine numbers corrected, no conclusion changed.** Every fault has the same cause and the same shape.


---

## `track2/creative/F_math.md` — five inputs exact, one range wrong

| Claim | Recomputed | Verdict |
|---|---|---|
| Baseline standard deviation `sigma0 = 0.09456` | Pipeline output: **0.09456** | **Exact** |
| "observed autosomal median depth of 44x" | Pipeline output: **44** | **Exact** |
| Binomial standard deviation at that depth, 0.0754 | sqrt(0.25/44) = **0.0754** | **Exact** |
| Overdispersion factor 1.574 | Measured variance over binomial variance = **1.574** | **Exact** |
| "Bonferroni over 563 bins" | Autosomal 5 Mb bins with 500 or more heterozygous sites: **563**; 536 also pass the depth-ratio filter | **Exact** |
| Median heterozygous sites per bin, about 3,900 | **3,865** | **Exact to the rounding used** |
| "autosomal 5 Mb bins hold 3,500 to 4,760 heterozygous sites" | Interquartile range is 3,318 to 4,523. **The true range is 542 to 15,129** | **Wrong. A central range presented as the full range** |

**Why the range matters.** The detection threshold scales as N to the power minus one quarter, so the sparsest bin carries a floor **1.64 times** the quoted one and the densest **0.71 times** it. Quoting a narrow range hid that the published per-bin floor is a floor at the median bin rather than a floor everywhere. This is the same weakness the anomaly analysis found from the other direction, reached independently, and the appendix now states it.


---

## Gate files and external database records

### The decay prediction, recomputed from the Ensembl exon structure

The most load-bearing prediction in the report is that allele 1 triggers nonsense-mediated decay, which rests entirely on where the stop sits relative to the last exon junction. Recomputed from `ENST00000287598` in the local Ensembl 116 annotation:

| Claim | Recomputed | Verdict |
|---|---|---|
| 23 exons | **23** | **Exact** |
| Premature stop codon at transcript positions 2,361 to 2,363 | Variant at genomic 40,209,701 maps to transcript **2,362**, the middle base of the codon, so the codon spans **2,361 to 2,363** | **Exact** |
| Last exon junction at transcript 3,109 | Junctions end at **2,830, 3,002, 3,109** | **Exact** |
| Six downstream junctions | **6** | **Exact** |
| "747 nucleotides upstream of the last exon junction" | From the **last base** of the stop: 3,109 − 2,363 = **746**. From the first base: **748**. From the variant base itself: 747 | **Underspecified, corrected.** The rule is stated from the last base of the stop, so the figure is 746. GPT-5's cross-model pass flagged this ambiguity and it is now resolved |

**The prediction itself is unaffected and is comfortably clear of the threshold.** The 50 to 55 nucleotide rule needs the stop more than about 55 nucleotides upstream of the last junction; it is 746.

### ClinVar, retrieved live

| Claim | Record | Verdict |
|---|---|---|
| Allele 1 is Pathogenic or Likely pathogenic, 2 submitters, no conflicts, MVA syndrome 1 | `CLNSIG=Pathogenic/Likely_pathogenic`, `CLNREVSTAT=criteria_provided,_multiple_submitters,_no_conflicts`, two submission accessions, `CLNDN` includes `Mosaic_variegated_aneuploidy_syndrome_1` | **Exact on every element** |
| c.3006T>G, this child's allele 2, is not in ClinVar | No record at that allele | **Exact** |
| The same protein change by a different nucleotide, c.3006T>A, is a VUS, VCV004600147 | `40220612 T>A`, variation ID **4600147**, `CLNSIG=Uncertain_significance`, single submitter | **Exact** |
| "The only other allele deposited at that base is the synonymous c.3006T>C, likely benign" | `40220612 T>C`, `CLNSIG=Likely_benign` | **Exact** |

**All four ClinVar claims verify.** Combined with the three gnomAD frequencies checked earlier by byte-range read, every external database record the two reports rely on has now been retrieved and matched.

---

---

## Final sweep: the remaining files

| File | Data claims | Verdict |
|---|---|---|
| `FAMILY_CARD.md` | **None.** The page carries no counts, frequencies or measurements at all | **Nothing to check, by design.** A page handed to a clinician makes no numerical claim it would have to defend |
| `SIMULATED_PANELS.md` | 13 simulated seats; 577 claims audited; 185 not supported | **All three exact.** Thirteen round-one seat files exist. The five partitions state 110, 57, 71, 110 and 229 audited, summing to **577**, and 28, 22, 31, 54 and 50 non-supported, summing to **185** |
| `README.md` | Repeats figures checked elsewhere | **No unchecked claim** |
| `track2/gate/G1` expression table | Re-derived live from the GEO series matrix: **65.8, 108.0 and 93.8 percent** | **Matches** the corrected values of 65.7, 108.0 and 93.8; the first differs by 0.1 only in whether the ratio is taken of means or means of ratios |
| `track2/gate/G1` cost table | Rows sum to **$16,170** | Table now states the exact sum rather than a rounded $16,200 |

---

## Result

**Every claim in this repository that asserts something about the supplied data, or about a database record that can be retrieved, has been recomputed or re-retrieved.**

| | |
|---|---|
| Numbers corrected | **13** |
| Conclusions changed | **0** |
| External database records checked | ClinVar, four claims, all exact; gnomAD, three frequencies, all exact; GEO, three ratios, all matching |

**The single recurring fault was a query run without `FILTER="PASS"`.** It produced nine of the thirteen corrections. It matters more than an ordinary slip because the excluded records are not randomly distributed: they concentrate in the low-mappability regions the analyses were reasoning about, so the error inflated exactly the signals those analyses were explaining away.

**The two most load-bearing claims both survive intact.** The Track 1 answer, where ten of eleven claims were exact to the digit and the eleventh was underspecified rather than wrong. And the nonsense-mediated decay prediction, whose transcript arithmetic recomputes exactly from the Ensembl exon structure, and which clears its threshold by more than an order of magnitude.

---

## Nothing further outstanding in this category

What is not covered here is the literature, which the five audit partitions covered separately, and the exclusions, which `EXCLUSION_AUDIT.md` covers.
