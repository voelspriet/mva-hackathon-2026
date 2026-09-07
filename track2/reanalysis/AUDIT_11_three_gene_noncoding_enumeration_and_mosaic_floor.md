# AUDIT 11. The "18 remaining calls" in the three MVA genes enumerated and characterised against gnomAD and live ClinVar (with the "all common dbSNP except one" description corrected), and the MVA-defining mosaic-aneuploidy negative reproduced from the VCF end-to-end — both the empirical BAF scan and the theoretical detection floor, reconciling the report's "10%" with F_math/R6's "11.7%"

**Run 11 of `PROMPT_relevant_additions.md`, 7 September 2026.** Continues `AUDIT_01`–`AUDIT_10`. Before writing I re-read
`AUDIT_10`'s "Where the next run should start", `R6`, `R12`, `R13`, `R18`, `SYNTHESIS_for_judging.md`, `F_math.md §2` and
`pipeline/mosaic_robust.py`/`f_math.py`, and confirmed each target below was **named as measurable-but-not-measured** by a
prior file. This run takes **three load-bearing claims** off `AUDIT_10`'s queue (item 3, bullets 1 and 2) and measures
them. **Measure before writing:** every number below was produced this session by the scripts named in the tables.

**Rule 3 credits (what is *not* new here).** That all 5,955 CDS bases of *BUB1B/CEP57/TRIP13* are covered ≥22× so "no
other **coding** variant" is a real negative is `AUDIT_09`'s; this run does not re-derive coverage, it enumerates the
actual calls. That the deep-intronic *BUB1B* variant chr15:40216470 is the one novel variant in *BUB1B*, absent from
gnomAD, ~1,025 bp from the next exon, and makes no canonical splice signal is `R12`'s (body scan) and `AUDIT_02`'s (splice
geometry); this run **extends that single-gene scan to the full three-gene set** and is the first to (a) count all 20
calls / 18 non-coding across *BUB1B*+*CEP57*+*TRIP13*, (b) test the report's "all common dbSNP except one" against gnomAD
for *every* non-coding call, and (c) find that the description fails for **two uncatalogued *TRIP13* calls** `R12` never
looked at. The 11.7 % per-bin floor and the 56 segmental outlier bins are `R6`'s/`F_math §2`'s; this run **reproduces the
underlying scan and the floor arithmetic from scratch** (no prior `R`/`AUDIT` file re-derived σ₀, the 2.2 M het count, or
the 0.032 / f≈0.14 empirical floor from the VCF — they were stated in the report and cited by `R6`).

The three targets, each a load-bearing sentence resting on assertion in this repository:

1. *"No other coding or ClinVar-flagged variant exists in the three genes; the **remaining 18 calls** are intronic or UTR
   and, except one deep-intronic BUB1B variant absent from gnomAD (about 1 kb from the nearest exon…), **all are common
   dbSNP polymorphisms**."* (`REPORT_track1.md:26`) — the completeness statement behind "*BUB1B* is the only one of the
   three MVA genes carrying a candidate", and behind excluding *TRIP13* (MVA2) and *CEP57* (MVA2-like).
2. *"no whole-chromosome mosaic aneuploidy above **roughly 10 %** of cells … per-chromosome median BAF excess is 0.000 …
   depth ratios lie between 0.977 and 1.022 … 95th percentile of bin-level excess on chromosomes 1-6 is **0.032**,
   corresponding to **f about 0.14** per bin"* (`REPORT_track1.md:42`) — the MVA-defining negative for Track 1.
3. The apparent tension `AUDIT_10` flagged between the report's **"roughly 10 %"** floor and `F_math §2`/`R6`'s
   **"11.7 % per bin"** floor: are they the same number or two different ones?

---

## Entry 1 — Converts an assertion into a measurement, and corrects the description on two counts. The three MVA genes hold exactly **20 PASS calls: 2 coding (the reported pair) + 18 non-coding**, reproducing "the remaining 18". But the report's "all [others] are common dbSNP polymorphisms except one" is imprecise: **all 18 are intronic, none UTR**; **three** non-coding calls carry no dbSNP rsid (not one) — the *BUB1B* deep-intronic variant **plus two uncatalogued *TRIP13* calls** present in gnomAD at ~0.5 %; and **5 of 18** have gnomAD max-AF below 1 %, so "common" overstates. The load-bearing negative (only one coding gene, only one P/LP) holds.

**Enumeration (`work/track2/audit11_enumerate.py`, pysam over the proband VCF; full transcript footprints from Ensembl 116
via `work/track2/audit11_gene_struct.py`).** Gene bodies used (canonical transcripts, UTRs included): *BUB1B*
chr15:40161069-40221123 (ENST00000287598, 23 exons), *CEP57* chr11:95790498-95832693 (ENST00000325542, 11 exons),
*TRIP13* chr5:892884-918120 (ENST00000166345, 13 exons). Each PASS call classified CDS / UTR / intron against the exon
list and the CDS BED (`work/track2/mva_cds.chr.bed`):

| Gene | PASS calls | CDS | UTR | intron |
|---|---|---|---|---|
| BUB1B | 13 | 2 | 0 | 11 |
| CEP57 | 4 | 0 | 0 | 4 |
| TRIP13 | 3 | 0 | 0 | 3 |
| **total** | **20** | **2** | **0** | **18** |

So **"the remaining 18 calls" reproduces exactly** (20 − 2 reported coding = 18), and the two CDS calls are precisely the
reported causal pair (chr15:40209701 0/1 AD 21,25; chr15:40220612 0/1 AD 15,13). The load-bearing half of the sentence —
**no *other* coding variant in the three genes** — holds: BUB1B is the only gene with a coding call and both its coding
calls are the submitted pair.

**gnomAD v4.1 for all 18 non-coding calls (`work/track2/audit11_gnomad.py`, GraphQL, 12-try backoff).**

| Category | count | variants |
|---|---|---|
| **absent from gnomAD** | **1** | chr15:40216470-A-G (BUB1B, the deep-intronic novel variant) |
| present, max-AF ≥ 1 % ("common") | 12 | — |
| present, max-AF < 1 % (**not** common) | 5 | see below |

The **one absent** call is exactly the *BUB1B* deep-intronic variant the report names, at **1,026 bp from the nearest
exon** (`work/track2/audit11_exondist.py`; consistent with `R12`/`AUDIT_02`'s 1,025 bp to the acceptor). That half of the
report's clause is confirmed to the base.

**The disconfirming refinement, recorded with rule-2 prominence.** The report says every *other* non-coding call is a
"common dbSNP polymorphism". Measured, two things fail:

- **Three non-coding calls, not one, carry no dbSNP rsid in this VCF** (`id=None`): the *BUB1B* deep-intronic one **and two
  *TRIP13* calls the report never singled out** —

  | Call | gene | region | dbSNP id | gnomAD | max-AF | VCF GT/DP | raw BAM depth (MAPQ 60) |
  |---|---|---|---|---|---|---|---|
  | chr5:893128 A>C | TRIP13 | intron 1, 38 bp from exon | **none** | exome 0.522 %, genome 0.130 % | 0.52 % | 0/1, DP 7 | 12 |
  | chr5:893132 G>C | TRIP13 | intron 1, 42 bp from exon | **none** | exome 0.503 %, genome 0.127 % | 0/1, DP 7 | 10 |

  Both are genuine recurrent variants (present in gnomAD, same alleles), but they are **neither "common" (~0.5 %) nor
  catalogued in this VCF's dbSNP build** — the very `coding_nodbsnp` phenomenon this repo tracks, here in a non-coding 5′
  region. They sit 4 bp apart on a coverage cliff at the *TRIP13* transcript start (raw depth falls 26→12→5 across
  893120-893137, some reads soft-clipped; `work/track2/audit11` BAM pileup), which is why the caller emitted DP 7. They
  are ~40 bp from the exon-1 splice site, **not** deep intronic, and 0.5 % population variants, so nothing pathogenic —
  but they are two counter-examples to "all are common dbSNP polymorphisms except one."

- **Five of the 18** have gnomAD max-AF **below 1 %** (`work/track2/audit11_gnomad_out.json`): rs185599777 (0.213 %,
  genome-only), rs117154762 (0.834 %), rs142950691 (0.834 %), and the two *TRIP13* calls above (0.52 % / 0.50 %). "Common"
  is therefore imprecise for roughly a quarter of the non-coding calls; the accurate statement is "**12 of 18 common
  (≥1 %), 5 rare-but-present, 1 absent from gnomAD.**"

**ClinVar sweep over the three gene spans against live NCBI ClinVar (`work/track2/audit11_clinvar.py`, remote tabix, exact
pos+ref+alt, fetched 7 Sep 2026 — 3,676 ClinVar records in the three spans).** Of the patient's 20 calls, exactly two have
an exact ClinVar record: chr15:40209701 (the reported allele 1) = **Pathogenic/Likely-pathogenic**, and **chr15:40192892
rs185599777** (an **intron** call, gnomAD genome 0.213 %) = **Uncertain_significance**. So:

- **Only one P/LP variant exists in the three genes, and it is the reported allele 1.** The reportable-finding negative
  holds. Allele 2 (chr15:40220612 T>G) has **no exact ClinVar record**, consistent with the report's own note that
  "c.3006T>G itself [is] unsubmitted."
- **Second precision note (rule 2):** the report's phrase "no other … **ClinVar-flagged** variant" is literally imprecise
  — one *other* call (intronic rs185599777) *does* carry a ClinVar record. But it is a VUS on a 0.2 % intronic SNV, not
  P/LP, so it is not reportable and changes nothing. (`R12:65` had already flagged rs185599777 as present and "too far to
  matter"; `R12` called it "too common", which at 0.21 % it is not — it is rare and genome-only. Minor, recorded for the
  record.)

**Net:** the load-bearing completeness claim — *BUB1B* is the only one of the three MVA genes with a coding candidate, and
the reported pair is the only P/LP in any of them — is **confirmed by direct enumeration**. Its supporting description
("18 intronic/UTR, all common dbSNP except one deep-intronic absent from gnomAD") is corrected: 18 all-intronic; **three**
uncatalogued (not one); five below 1 % (so not all "common"); and one non-coding intronic VUS in ClinVar.

## Entry 2 — Converts an assertion into a measurement (independent reproduction). The MVA-defining mosaic-aneuploidy negative reproduces from the proband VCF end-to-end: σ₀ = 0.09456, **2,224,820** autosomal het sites, per-chromosome median BAF excess **0.000** on every autosome, depth ratios **0.9766–1.0219** with the highs on GC-rich chr16/17/19/22, and the chromosome-1-6 95th-percentile bin excess **0.0324 → f = 0.1388** — every figure in `REPORT_track1:42` reproduced to its printed precision.

`REPORT_track1:42` is the Track-1 negative that rules out the *mosaic aneuploidy* the syndrome is named for. Its numbers
came from `pipeline/mosaic_robust.py`, whose input (`mosaic_robust.json`) is not committed, so no audit had re-run the
scan. I re-implemented it faithfully in pysam (`work/track2/audit11_mosaic.py`; `bcftools` absent, so the
`bcftools query | mosaic_robust.py` pipe was replaced by a direct VCF stream with identical filters: PASS biallelic SNV,
DP 20-120, 5 Mb bins, keep bins with ≥500 hets and depth ratio 0.93-1.07, chromosome = median over kept bins):

| Quantity | `REPORT_track1:42` / `F_math §2` | Measured this run | Match |
|---|---|---|---|
| baseline sd of (AB−0.5), σ₀ | 0.09456 | **0.09456** | exact |
| autosomal heterozygous PASS SNVs used | "2.2 million" | **2,224,820** | exact |
| per-chromosome median BAF excess | 0.000 on every autosome | **0.0000 on all 22 autosomes** | exact |
| autosomal depth-ratio range | 0.977 – 1.022 | **0.9766 – 1.0219** | exact (to rounding) |
| chromosomes carrying the high depth ratios | GC-rich 16, 17, 19, 22 | **16 (1.0137), 17 (1.0167), 19 (1.0219), 22 (1.0194)** | exact |
| 95th-percentile bin excess, chr 1-6 | 0.032 | **0.0324** (n = 239 bins) | exact |
| implied f at that excess | "about 0.14" | **0.1388** = 4·0.0324/(1−2·0.0324) | exact |

The negative is therefore not a pipeline artefact taken on trust: **independently recomputed from the raw VCF, no
autosome shows any median BAF excess, and the noisiest 5 % of chr1-6 bins reach only f≈0.14**, i.e. the scan cannot see a
whole-chromosome trisomy present in fewer than ~14 % of cells at a single bin — and sees none. `R6`'s finding that 56
individual bins exceed the segmental threshold but every one implies f>1 (heterochromatin/acrocentric/centromere/MHC
mapping artefacts) is unchanged and untouched here.

## Entry 3 — Bounds what cannot be known, with the number attached, and reconciles a two-figure discrepancy. The report's "roughly 10 %" floor and `F_math §2`/`R6`'s "11.7 % per bin" floor are **the same number**: the per-bin genome-wide-Bonferroni detection floor, which reproduces from `f_math.py` as **11.66 %**. "Roughly 10 %" is that figure to one significant figure; the per-chromosome floors (4.24 % large autosomes, 6.84 % chr21) are both below 10 %, exactly as the report also states.

`AUDIT_10` flagged that "10 % vs 11.7 % are not obviously the same number and deserve reconciliation." I ran `f_math.py`'s
Problem-2 block (`nice -n 15 python3.12 pipeline/track2_math/f_math.py`), which computes the floor from σ₀, N and the
z-threshold:

| Test level | N / bins | f_min (this run) | where the report uses it |
|---|---|---|---|
| single 5 Mb bin, one-sided 95 % | N = 3,900 | **7.58 %** | — |
| **single bin, Bonferroni over 563 bins** | N = 3,900 | **11.66 %** | = `F_math`/`R6` "11.7 %"; = report "roughly 10 %" |
| chr1, median of 45 bins, Bonf over 23 chr | 45 bins | **4.24 %** | report: "per chromosome the floor is below 0.10" |
| chr21, median of 7 bins, Bonf over 23 chr | 7 bins | **6.84 %** | report: "per chromosome the floor is below 0.10" |

So there is **no discrepancy**: the report's single genome-level number "roughly 10 %" is the **per-bin, genome-wide-
corrected** floor (11.66 %, which `F_math` and `R6` print to two figures as 11.7 %), and the report's separate clause
"per chromosome the floor is below 0.10" is the **per-chromosome** floor, which the same script gives as 4.24 %/6.84 % —
both genuinely below 10 %. The two report sentences are two different (and both reproduced) floors, not one number stated
inconsistently. **The bound, stated cleanly:** on this data the mosaic scan is blind to a whole-chromosome trisomy below
≈11.7 % of cells *within any single 5 Mb bin* under genome-wide correction, and below ≈4.2 % (large autosomes) to ≈6.8 %
(chr21) *when the whole chromosome is aggregated*; the observed genome shows nothing above its own noise on either scale.

---

## What this run found, against the prompt's test

- **Entry 1 (converts an assertion + two corrections):** the three MVA genes hold **20 PASS calls — 2 coding (the reported
  pair) + 18 non-coding**, reproducing "the remaining 18". The load-bearing negative (only *BUB1B* carries a coding call;
  only one P/LP in the three genes, the reported allele 1) is **confirmed by direct enumeration + live ClinVar**.
  **Disconfirming refinements:** (a) all 18 non-coding are intronic, **zero UTR**; (b) **three** carry no dbSNP rsid, not
  one — the *BUB1B* deep-intronic variant **plus two uncatalogued *TRIP13* calls** (chr5:893128, chr5:893132) present in
  gnomAD at ~0.5 % on a coverage cliff, which the report's "all common dbSNP except one" omits; (c) **5 of 18** are below
  1 % gnomAD AF, so "common" overstates; (d) one non-coding intronic call (rs185599777) carries a ClinVar **VUS**, so "no
  other ClinVar-flagged variant" is literally imprecise though not reportable.
- **Entry 2 (converts an assertion, independent reproduction):** the MVA-defining mosaic negative reproduces from the raw
  VCF to printed precision — σ₀ **0.09456**, **2,224,820** hets, per-chromosome median excess **0.000**, depth ratios
  **0.9766–1.0219** (highs on GC-rich 16/17/19/22), chr1-6 95th-pct excess **0.0324 → f 0.1388**.
- **Entry 3 (bounds + reconciles):** the report's "roughly 10 %" and `F_math`/`R6`'s "11.7 %" are the **same** per-bin
  Bonferroni floor, reproduced as **11.66 %**; the per-chromosome floors are **4.24 %/6.84 %**, both <10 %, matching the
  report's second clause. No inconsistency; two distinct, both-reproduced floors.

**No load-bearing conclusion of the submission is overturned.** Three assertions are converted to measurement; one
supporting description in `REPORT_track1:26` is corrected on two counts (three uncatalogued calls not one; "common"
overstated; one intronic ClinVar VUS). Transferable points (relevance test #4): (a) a "N common-dbSNP calls" completeness
statement should be checked against gnomAD **per call**, because a caller's dbSNP build silently drops real 0.5 %
recurrent variants (two here) that then read as "novel"; (b) a mosaic-aneuploidy negative can be reproduced without
`bcftools` by streaming the VCF with pysam under identical bin/DP filters, and its detection floor recovered from the
bin-to-bin BAF-excess spread alone, using the genome as its own negative control; (c) when a report rounds a floor to one
significant figure ("~10 %") and an appendix prints two ("11.7 %"), verify they are the *same* quantity before treating
them as a discrepancy — here they were.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | full transcript footprints, Ensembl 116 | BUB1B chr15:40161069-40221123 (23 ex), CEP57 chr11:95790498-95832693 (11 ex), TRIP13 chr5:892884-918120 (13 ex) | `work/track2/audit11_gene_struct.py` (Ensembl REST) |
| 2 | PASS calls in the three gene bodies | **20 total = 2 CDS + 18 non-coding**; 18 all intronic, 0 UTR | `work/track2/audit11_enumerate.py` (pysam) |
| 3 | the 2 CDS calls | exactly the reported pair (40209701 0/1 21,25; 40220612 0/1 15,13) | same |
| 4 | non-coding calls absent from gnomAD v4.1 | **1** = chr15:40216470-A-G (BUB1B), 1,026 bp from nearest exon | `work/track2/audit11_gnomad.py`, `audit11_exondist.py` |
| 5 | non-coding calls with **no dbSNP rsid** in VCF | **3** = 40216470 (BUB1B) + **893128, 893132 (TRIP13)** | `work/track2/audit11_enumerate.py` |
| 6 | TRIP13 893128 / 893132 gnomAD AF | exome 0.522 % / 0.503 %, genome 0.130 % / 0.127 %; present, uncatalogued here | `work/track2/audit11_gnomad_out.json` |
| 7 | TRIP13 893128 raw BAM depth / MAPQ | 12 (VCF DP 7), MAPQ 60, coverage cliff at TRIP13 5′ end | `samtools depth/view chr5:893120-893140` |
| 8 | non-coding calls with gnomAD max-AF < 1 % | **5 of 18** (rs185599777 0.213 %, rs117154762 0.834 %, rs142950691 0.834 %, 893128 0.522 %, 893132 0.503 %) | `work/track2/audit11_gnomad.py` |
| 9 | ClinVar records among the 20 calls (live NCBI, exact match) | **1 P/LP** (40209701 = reported allele 1) + **1 VUS** (intronic rs185599777); allele 2 not in ClinVar | `work/track2/audit11_clinvar.py` (remote tabix) |
| 10 | mosaic σ₀ / autosomal het sites | **0.09456 / 2,224,820** | `work/track2/audit11_mosaic.py` (pysam) |
| 11 | per-chromosome median BAF excess | **0.000 on all 22 autosomes** | same |
| 12 | autosomal depth-ratio range | **0.9766 – 1.0219**, highs chr16/17/19/22 | same |
| 13 | chr1-6 95th-pct bin excess / implied f | **0.0324 / 0.1388** (n = 239 bins) | same |
| 14 | detection floor, single bin Bonferroni/563 | **11.66 %** (= report "~10 %" = F_math/R6 "11.7 %") | `pipeline/track2_math/f_math.py` |
| 15 | detection floor, per chromosome (Bonf/23) | **4.24 %** (chr1) / **6.84 %** (chr21), both <10 % | same |

All new scripts are in `work/track2/audit11_*.py`; raw outputs in `work/track2/audit11_gnomad_out.json`,
`audit11_mosaic_out.json`, `audit11_variants.json`, `audit11_gene_struct.json`. VCF =
`data/WGS_EX2312012_HGWCNDSX7.vcf.gz` (contigs unprefixed); BAM = `work/bam/all.bam` (contigs `chr`-prefixed); ClinVar =
live NCBI GRCh38 VCF over remote tabix (fetched 7 Sep 2026); gnomAD = v4.1 GraphQL; gene structure = Ensembl REST release
116. Tooling: `python3.12` + pysam 0.24.0, samtools present; **bcftools/mosdepth/tabix still not on PATH** (mosaic scan
therefore re-implemented in pysam).

## Where the next run should start

1. **Report-editing items remain open** (pure text edits, carried from `AUDIT_08`–`AUDIT_10`), now with three additions
   from this run, all edits not new measurements:
   - `REPORT_track1:26` "all are common dbSNP polymorphisms" → the accurate count is **12 of 18 common (≥1 %), 5 rare-but-
     present, 1 absent**; **three** non-coding calls lack a dbSNP rsid (BUB1B 40216470 + TRIP13 893128/893132), not one;
     and "no other ClinVar-flagged variant" should read "no other **P/LP** ClinVar variant" (one intronic VUS exists).
   - the still-open `REPORT_track2:56` STR-wording, the 314/224/138 candidate-count altitudes, the un-applied
     `AUDIT_06`/`AUDIT_07` corrections, the 288 bp phase-span citation (→`AUDIT_09` not `R1`), and the `R9:62` "117 of 121
     NFE" correction from `AUDIT_10`.
2. **Still bounded / not measurable here** (unchanged): `R5`'s 97-gene/18-gene cohesion-set modifier-enrichment row (list
   absent from the repo); the Exomiser model-2 ranking (`REPORT_track1:38`, 37 GB bundle).
3. **Remaining measurable load-bearing claims, in descending measurability:**
   - **The drugmap counts** (`REPORT_track2:100`: 110 targets, 148 molecules, 29 approved-passed for *BUB1B*) — reproducible
     only against live Open Targets GraphQL / ChEMBL REST / openFDA, which drift; any re-run **must report the query date**
     and expect the counts to move. `pipeline/track2_drugmap/drugmap.py` is the script. Medium effort, medium confidence it
     will still reproduce.
   - **The depth-channel mosaic floor** (`F_math §2`: "observed autosomal f_depth runs −0.047 to +0.044, SD 0.025, floor
     near 5 %"). This run reproduced the **BAF** channel; the **depth** channel needs `work/mosaic_robust.json`'s per-bin
     `f_depth` (or a re-run producing it). My `audit11_mosaic.py` already computes per-chromosome depth ratios (0.9766-
     1.0219); extending it to emit per-bin `f_depth` and its SD would close the depth channel too. Low-medium effort.
   - **The `REPORT_track1:28` "314 genes pass the crude recessive-compatible filter"** count and its "dominated by
     polymorphic/multi-copy loci (MUC3A, LILRB1, PRSS2, HLA)" characterisation — partially touched by `AUDIT_06`/`AUDIT_08`
     (candidate-space rarity) but the **314 count itself** and the named-locus domination were not re-enumerated from the
     VCF. Measurable.
4. Tooling unchanged: `python3.12` + pysam 0.24.0, samtools, minimap2 present; **no bcftools/mosdepth/tabix on PATH**;
   Ensembl REST pins release 116; gnomAD r4 GraphQL and NCBI ClinVar remote-tabix both reachable. `work/track2/audit11_*`
   reproduce every number here.
