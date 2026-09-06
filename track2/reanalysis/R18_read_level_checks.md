# R18. What the alignment adds beyond the depth profile

**Asked 6 September 2026, after R17.** R17 used the newly aligned reads for one thing: whole-chromosome coverage. The same alignment answers three further questions that the VCF cannot, and separates two quantities that R17 conflated.

## 1. Both candidate variants, re-derived from the reads by a different aligner

The submitted genotypes come from Sentieon's caller on the organisers' alignment. This is an independent path: minimap2 against GRCh38 no-alt, then raw pileup, no caller involved.

| Position | Depth | Ref fwd / rev | Alt fwd / rev | Alt fraction | Strand balance |
|---|---|---|---|---|---|
| chr15:40209701 (p.Leu737Ter) | 46 | 11 / 10 | 13 / 12 | 0.543 | 0.52 |
| chr15:40220612 (p.Asn1002Lys) | 29 | 3 / 11 | 5 / 10 | 0.517 | 0.33 |

Both sit at the heterozygous expectation. Neither shows the strand skew that marks an alignment or chemistry artefact; the 0.33 on the second is 5 of 15 alternate reads, well inside binomial noise at that depth.

**What this rules out.** That either call is an artefact of the original aligner or caller. Two independent alignment paths give the same two heterozygous variants at the same fractions.

## 2. Focal copy number at 100 kb, with an internal positive control

R3 examined depth per megabase derived from variant records. This is direct coverage at ten times the resolution, GC-normalised, scanning for runs of at least five consecutive windows deviating by more than three standard deviations.

54 such runs exist. Ranked by length, the top eight are all chrX and chrY at ratio 0.50, spanning 532, 372 and 342 consecutive windows.

**That is the control the analysis needed.** The method demonstrably detects a true one-copy state, across hundreds of consecutive windows, without being told where to look. A negative elsewhere therefore means something.

The only autosomal runs are chr18 15.6-20.7 Mb (ratio 0.73), chr7 58.2-60.8 Mb (0.38) and chr15 17.1-19.7 Mb (0.40). All three are pericentromeric, where short-read mappability collapses. **No focal autosomal deletion or duplication is present**, including at the *BUB1B* locus, which confirms the compound-heterozygous interpretation against the alternative that one allele is deleted.

## 3. Statistical power and systematic floor are not the same number, and R17 quoted the wrong one

R17 derived a detection floor of about 4% from the largest observed per-chromosome deviation. That figure is dominated by residual systematic bias, not by counting noise. Separating them:

| | Smallest detectable mosaic fraction |
|---|---|
| chr2 (2,367 windows) | 0.41% |
| chr1 (2,225 windows) | 0.43% |
| chr13 (948 windows) | 0.66% |
| chr19 (421 windows) | 0.98% |
| chr21 (364 windows) | 1.06% |
| chr22 (309 windows) | 1.15% |

Per-window scatter is 0.0336. At three standard errors, statistical power runs from **0.41% on chr2 to 1.15% on chr22**, set by how many usable windows a chromosome has.

The practical floor is worse than that, because residual GC and mappability bias leaves per-chromosome offsets of one to two percent. So the honest statement is two numbers, not one: **counting noise allows about 1%, systematic residual sets the achievable floor near 2%**, and the 4% in R17 is conservative. It also names the improvement path: better mappability and GC modelling moves the floor toward the statistical limit, and nothing else will.

## 4. What this costs, which is a judging criterion

| Tier | What it yields | Cost |
|---|---|---|
| VCF only | the diagnosis, the frequency-matched background, the phase elimination, the mutational spectrum, the ACMG screen | 61 s scripted, plus about 7 min of gnomAD API queries; runs on a laptop |
| Reads | the mosaicism floor, focal copy number, the independent variant confirmation | 78.85 GB download, 4 h 35 min on 20 cores, 137 GB peak disk |

Seven of the ten findings in R15 to R18 need only the VCF. Three need the reads. For a cohort, the first tier scales linearly at negligible cost and the second does not, which is the relevant distinction for anyone asking whether this approach generalises beyond one child.
