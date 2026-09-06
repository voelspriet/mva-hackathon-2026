# R11. A genome-wide loss-of-function scan that does not depend on ClinVar

**Asked 6 September 2026.** This exists to close a blind spot R7 named in its own text.

R7 screened the whole genome against the whole of ClinVar and stated its ceiling plainly: *BUB1B* allele 2 does not appear there, and should not, because it has no ClinVar record. **A ClinVar screen can only find what ClinVar already knows.** This scan asks the complementary question, with no gene list and no dependence on prior curation: **where in this genome is a protein truncated?**

## Method

All 388,842 coding intervals in the local Ensembl annotation, plus 8 bp of flank so canonical splice sites are covered. PASS variants only. Consequence from snpEff GRCh38.86. Rarity proxied first by absence of an rsID, which is the same proxy the project's earlier rare-variant work used, then by gnomAD v4.1 for anything that survived.

| | |
|---|---|
| PASS variants in coding sequence genome-wide | **33,416** |
| Carrying a HIGH-impact consequence | **1,054** |
| Of those, with no rsID | **178** |

Consequence classes among the 1,054: 360 frameshift, 326 structural interaction, 139 stop gained, 73 splice acceptor, 57 stop lost, 54 splice donor, 37 start lost, 8 protein-protein contact.

**Positive control: the scan returns *BUB1B* chr15:40209701, p.Leu737\*, as a no-rsID stop-gained heterozygote.** It found the causal allele without being told the gene, so the pipeline works.

## What 178 candidates actually are

Two systematic artefact classes account for most of them, and both are measurable rather than assumed.

**Class 1: clustered calls, 107 of 178 in 39 genes.** A gene carrying more than one no-rsID frameshift is almost never a gene with more than one frameshift. It is a misaligned indel cluster or a collapsed paralogue. The worst offenders are unambiguous:

| Gene | Such variants | Why |
|---|---|---|
| *FCGBP* | 8 | Eight frameshifts inside 84 bp |
| *OR8U1* | 6 | Olfactory receptor family, segmental duplication |
| *SERPINA1*, *LILRB1* | 5 each | Paralogue families |
| *HLA-B*, *HLA-A*, *HLA-DRB1*, *HLA-DRB5*, *HLA-DQA1* | 3 to 4 each | The most polymorphic locus in the genome, read against one reference haplotype |
| *MUC3A* | 4 | Tandem repeat |
| *PRSS1*, *PRSS2* | 3 each | **The same region R7 discarded and `ANOMALIES.md` D5 already flagged for mismapping.** Independent confirmation from a scan that knew nothing about it |
| *AGAP3*, *AIM1L*, *CELA1* | 3 each | Adjacent frameshifts within tens of base pairs |

**Class 2: transcript-choice artefacts, 38 of the 71 singletons.** snpEff reports the most severe consequence across all transcripts. A variant can therefore be labelled HIGH on the strength of one minor isoform while every other transcript sees an intron. Thirty-eight of the singletons are called intronic or untranslated by at least one other transcript, which puts them at risk of exactly this.

That leaves about 33 for individual assessment. Two were worth chasing.

## *FANCD2*, and why Exomiser ranked it third

*FANCD2* chr3:10046723, a splice-donor deletion, heterozygous, no rsID. This mattered more than most, because Fanconi anaemia is a chromosome-instability and cancer-predisposition syndrome and therefore a genuine differential for this child's diagnosis, and because **the project's own Exomiser run ranked *FANCD2* third genome-wide** (`track2/research/04_exomiser_model2.md`) and nobody followed it up.

**It is an artefact, on four independent grounds.**

1. **Population frequency refutes it.** In gnomAD the same AG>A allele sits at **AF 0.321 with zero homozygotes**, where Hardy-Weinberg predicts roughly 50,700. gnomAD fails the site on both AS_VQSR and InbreedingCoeff.
2. **Mapping quality is degraded**, MQ 46.25 against 60 for a clean call.
3. **Depth is inflated.** The surrounding 15 kb carries **106 PASS calls at mean depth 75.2** against a genome median of 44.
4. **Heterozygosity is impossible.** Of those 106 calls, **97 are heterozygous, 92 percent.** A real 15 kb stretch of a diploid genome does not look like that. Two loci are being read as one, which is what *FANCD2*'s pseudogenes *FANCD2P1* and *FANCD2P2* do.

The contrast with a clean region is stark: around the *ARID1B* candidate below, the same measurement gives 4 PASS calls at mean depth 45.8.

**So Exomiser's third-ranked gene was a mismapping artefact.** Together with R7's finding that its fourth-ranked gene, *LZTR1*, was real but too low-penetrance to act on, **both of the project's unexamined Exomiser leads are now resolved, and neither changes anything.**

## *ARID1B*, and the transcript trap

*ARID1B* chr6:157186528 C>T looked like the best candidate in the whole scan. A stop-gained, p.Gln703\*, heterozygous, and the call is excellent: AD 26,33, depth 59, GQ 99, QUAL 919.77, **MQ 60**, QD 15.59, in a region of normal depth. gnomAD has it at AF 9.41e-06, genuinely rare. ClinVar has never seen it. *ARID1B* haploinsufficiency causes Coffin-Siris syndrome and is one of the commonest causes of intellectual disability.

**It is not a loss-of-function variant, and the full annotation says so.**

| Transcript | Consequence |
|---|---|
| ENST00000319584, 12 exons | stop gained, p.Gln703\*, **in the final exon, 12 of 12** |
| ENST00000346085, 19 exons | **intron variant, c.3550+2093C>T** |
| ENST00000350026, 18 exons | **intron variant, c.3511+2093C>T** |
| ENST00000636930, ENST00000635849, ENST00000637904 | **intron variant** |

In every full-length transcript the variant sits **2,093 nucleotides inside an intron**. It is a stop codon only in a short 12-exon isoform, and even there it lands in the terminal exon, where the 50 nucleotide rule this project computes elsewhere predicts escape from decay. There is no *ARID1B* haploinsufficiency here, and no Coffin-Siris question to raise.

**What this shows:** a HIGH-impact label is a statement about the most severe transcript, not about the gene. Taking it at face value would have put a nonsense variant in a major intellectual-disability gene into this report. The check that prevented it was reading the whole annotation instead of the first field.

## Result

**No novel loss-of-function variant of consequence exists in this genome's coding sequence.** Every candidate resolves into one of five classes:

| Class | Example |
|---|---|
| Collapsed paralogue or repeat | *FANCD2*, *HLA*, *PRSS1/2*, *FCGBP*, *CYP21A2*, *CYP2D7* |
| Common polymorphism where GRCh38 carries the minor allele | *FMO2* p.Gln472\*, *GPR33* p.Arg140\*, *G6PD* |
| Known common functional allele | *CYP3A5*\*3 splice acceptor |
| Transcript-choice annotation artefact | *ARID1B* |
| **The causal allele** | ***BUB1B* p.Leu737\*** |

R7's blind spot is therefore closed. A scan that owed nothing to ClinVar found the same answer: **one truncating variant of consequence in this genome, and it is the one already known.**

## What R11 changes

| | |
|---|---|
| New findings | **None** |
| R7's stated ceiling | Closed. The complementary scan was run and agrees |
| Unfollowed Exomiser leads resolved | **Both.** Rank 3 *FANCD2* is an artefact, rank 4 *LZTR1* was settled in R7 |
| Artefact signatures quantified | Two: clustering, 107 of 178, and transcript conflict, 38 of 71 singletons |
| Confirmation of an earlier call | *PRSS1*, discarded in R7 and flagged in D5, is independently flagged here |
| Recommendations added | **None** |
