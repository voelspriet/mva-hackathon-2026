# AUDIT 12. The mosaic **depth channel** floor reproduced from the raw VCF (the channel `f_math.py` skipped and `AUDIT_11` left open), the 314-gene recessive filter's "dominated by polymorphic/multi-copy loci" characterisation taken to measurement, and the drugmap's 110/148/29 counts split into what reproduces from committed artifacts vs. what has drifted on the live API

**Run 12 of `PROMPT_relevant_additions.md`, 7 September 2026.** Continues `AUDIT_01`–`AUDIT_11`. Before writing I re-read
`AUDIT_11`'s "Where the next run should start" (its three named-measurable items become this run's three entries),
`AUDIT_08` (the 314-count reconciliation, so I do not re-derive it), `F_math §2`, `R6`, `R17`, and
`SYNTHESIS_for_judging.md`, and confirmed by grep that **no `R`/`AUDIT` file has reproduced the depth channel's
`f_depth`** (`grep -ln f_depth track2/reanalysis/R*.md` is empty). This run takes **three load-bearing claims** — the
exact three `AUDIT_11:221` queued as "remaining measurable" — from assertion to measurement. **Measure before writing:**
every number below was produced this session by the scripts named in the tables, all in `work/track2/audit12_*`.

**Rule 3 credits (what is *not* new here).** That the **BAF** channel of the mosaic scan reproduces (σ₀ 0.09456, per-chr
median excess 0.000, chr1-6 95th-pct 0.0324→f 0.1388) is `AUDIT_11`'s Entry 2; this run reproduces the **depth** channel,
which `AUDIT_11` explicitly left open (`AUDIT_11:228`, "This run reproduced the BAF channel; the depth channel needs …
`f_depth`") and which `f_math.py` prints a `[skipped]` for because `work/mosaic_robust.json` is uncommitted. That the
**314** count itself reproduces (and 189 of 314 enter on the ≥1-hom clause) is `AUDIT_08`'s Entry 2; this run does not
re-derive the count — it measures the **"dominated by polymorphic and multi-copy loci (MUC3A, LILRB1, PRSS2, HLA)"**
characterisation that `AUDIT_08` did not test. That the drugmap surfaced six approved drugs (palbociclib, ribociclib,
abemaciclib, trilaciclib, venetoclax, temsirolimus) with trilaciclib's direction-check limitation is the report's and is
untouched as a conclusion; this run measures whether its three **counts** (110 targets / 148 molecules / 29 passed)
reproduce, and finds a drift `AUDIT_11:224` predicted.

The three targets, each a load-bearing sentence resting on assertion:

1. *"depth channel: observed autosomal `f_depth` range … min −0.047 max +0.044 … sd 0.025 … 95% floor ~ 5.0%"*
   (`F_math §2` / `pipeline/track2_math/f_math.py`, the block that prints `[skipped]` when `mosaic_robust.json` is absent).
2. *"the list is **dominated by polymorphic and multi-copy loci (MUC3A, LILRB1, PRSS2, HLA)**, which is what a filter
   without population frequencies produces"* (`REPORT_track1.md:28`) — the justification for why 313 of the 314 recessive-
   compatible genes are not candidates and why a frequency-aware re-ranking (Exomiser model 2) is needed.
3. *"For *BUB1B* it queried **110 targets** (gene, 33 consequence genes, 76 interaction partners at STRING/IntAct 0.9 or
   above), returned **148 molecules** and passed **29** through a three-way approval test"* (`REPORT_track2.md:100`).

---

## Entry 1 — Converts an assertion into a measurement (closes a channel left `[skipped]`). The mosaic **depth channel** reproduces from the raw VCF to printed precision: per-autosome `f_depth` runs **−0.047 (chr4) to +0.044 (chr19)**, sample SD **0.0254**, two-sided 96% floor 1.96·SD = **0.0498 ≈ 5.0%** — matching `F_math §2`'s "−0.047 to +0.044, SD 0.025, floor near 5%". The one structural note: the spread is **GC-driven**, not copy-number — the only positive `f_depth` autosomes are the four GC-rich small chromosomes (16, 17, 19, 22), so the "5% floor" is a technical-noise floor, and the genome shows nothing above it.

`F_math §2` states the depth-channel detection floor, the second of the two independent channels (BAF + depth) behind the
Track-1 "no mosaic aneuploidy" negative. But `f_math.py` cannot compute it: its input `work/mosaic_robust.json` is derived
from the patient VCF and **is not committed** (`ls work/mosaic_robust.json` → absent), so the script prints
`[skipped: … not found]` and the depth numbers in `F_math.md` had never been reproduced by any audit. I regenerated
`mosaic_robust.json` by feeding the VCF through the **original** `pipeline/mosaic_robust.py` unchanged — reproducing
`run.sh:36`'s `bcftools query -i 'FILTER="PASS" && TYPE="snp"' -f '%CHROM\t%POS\t[%GT\t%AD\t%DP]\n' | mosaic_robust.py`
with a pysam feeder (`bcftools` absent), emitting the identical five-column stream (`work/track2/audit12_feed_mosaic.py`
→ `pipeline/mosaic_robust.py`). This is the same PASS-biallelic-SNV filter `AUDIT_11` validated to an exact σ₀ match, so
the feeder is not a new definition.

| Quantity (`F_math §2` / `f_math.py` depth block) | Report value | Measured this run | Match |
|---|---|---|---|
| min autosomal `f_depth` | −0.047 | **−0.047** (chr4, depth ratio 0.9766) | exact |
| max autosomal `f_depth` | +0.044 | **+0.044** (chr19, depth ratio 1.0219) | exact |
| sample SD of `f_depth` over 22 autosomes | 0.025 | **0.0254** | exact (to rounding) |
| two-sided 96% floor 1.96·SD | "~5.0%" | **0.0498 = 5.0%** | exact |

`f_depth` is `2·(median-bin-depth-ratio − 1)` per chromosome (a trisomy present in fraction *f* of cells raises mean copy
number to 2+*f*, i.e. depth ratio 1+*f*/2). The full per-chromosome table is in `work/track2/audit12_mosaic_full.txt`; the
regenerated JSON is `work/track2/audit12_mosaic_robust.json`.

**The structural observation, recorded (relevance test #1 — closes an alternative reading of "5% floor").** The 22
`f_depth` values are not centred on zero-with-symmetric-noise: their mean is **−0.0114**, and the only four autosomes with
**positive** `f_depth` are **chr16 (+0.027), chr17 (+0.033), chr19 (+0.044), chr22 (+0.039)** — the four most GC-rich
small chromosomes, the same set `AUDIT_11` flagged carrying the high BAF-channel depth ratios. So the ±0.05 spread that
sets the "5% floor" is **GC-composition bias in per-bin coverage, not residual mosaic copy-number**: the floor is a
*technical* limit of depth-based dosage on this library, and the true biological signal is flat (BAF median excess 0.000
on every autosome, `AUDIT_11`). This makes the depth channel the **weaker** of the two — its floor (~5%) is set by GC
noise, while the BAF channel's per-bin genome-wide floor is 11.7% but rests on allele balance, which has no GC bias. The
negative holds on both, but for different reasons, and the depth "5%" should not be read as "we could see 5% mosaicism":
it is "bin-to-bin GC noise is ±5%, and no chromosome exceeds it."

## Entry 2 — Converts an assertion into a measurement (confirms it, to the rank). The 314-gene recessive-compatible list is **dominated by polymorphic/multi-copy loci exactly as claimed**: the three named single genes are literally the **top three by heterozygous-variant count** — MUC3A (#1, 48 het), LILRB1 (#2, 44 het), PRSS2 (#3, 39 het) — HLA fills **7** entries (HLA-DRB1 at #14 the highest), **92 of the 314 (29.3%)** belong to named polymorphic/immunogenetic/multi-copy families, and **23 of the top 30** by het count do. *BUB1B*, the true diagnosis, ranks **#103 with 2 het** — buried below ~100 artefact-driven loci, which is precisely the report's argument for a frequency-aware re-ranking.

`REPORT_track1:28` characterises the 314 list qualitatively; `AUDIT_08` reproduced the *count* but not the
characterisation. I fed `work/coding_nodbsnp.gene.vcf.gz` through the **original** `pipeline/recessive_scan.py` unchanged,
reproducing `run.sh:32`'s `bcftools query -i 'GQ>=50 && FMT/DP>=10' -f '%INFO/GENE\t[%GT]\t%CHROM:%POS:%REF:%ALT\n'` with
a pysam feeder (`work/track2/audit12_feed_recessive.py` → `pipeline/recessive_scan.py`). Output = **314 genes** (reproducing
`AUDIT_08`/`REPORT_track1:28` exactly), sorted by the script's own key (−het, −hom, gene).

**The four named loci, located in the actual ranking (`work/track2/audit12_recessive.txt`):**

| Named locus | rank in list | het | hom |
|---|---|---|---|
| **MUC3A** | **1** | 48 | 0 |
| **LILRB1** | **2** | 44 | 4 |
| **PRSS2** | **3** | 39 | 0 |
| HLA-DRB1 | 14 | 13 | 1 |
| HLA-DQB2 / -DQA1 / -DQA2 / -DRB5 / -A / -B | 25 / 29 / 49 / 53 / 58 / 59 | — | — |

The three single genes the report names are **exactly ranks 1, 2, 3**, and HLA appears **7 times**. Quantifying the whole
list by known polymorphic / segmental-duplication / immunogenetic gene families (`work/track2/audit12_families.py`):

| Family | genes in the 314 | examples |
|---|---|---|
| TRBV/TRAV/TRGV (TCR variable) | 28 | TRBV3-1, TRBV7-6, TRBV6-5 |
| IG[HKL]V/D/J (Ig variable) | 20 | IGLV5-48, IGHV4-4, IGHV3-48 |
| LILR (leukocyte Ig receptors) | 9 | LILRB1, LILRA2, LILRB2 |
| HLA | 7 | HLA-DRB1, HLA-DQB2, HLA-A |
| MUC (mucins) | 7 | MUC3A, MUC6, MUC2 |
| TAS2R (taste receptors) | 5 | TAS2R31, TAS2R46, TAS2R30 |
| OR (olfactory receptors) | 4 | OR8U1, OR10G2, OR6J1 |
| PRSS (trypsinogens) | 4 | PRSS2, PRSS1, PRSS3 |
| ZNF (zinc-finger clusters) | 4 | ZNF717, ZNF285, ZNF91 |
| KRT/KRTAP (keratins) | 3 | KRTAP10-4, KRTAP10-5 |
| KIR (killer Ig receptors) | 1 | KIR3DL3 |
| **total in these families** | **92 of 314 = 29.3%** | |

**23 of the top 30** by het count fall in these families; the seven that do not (KCNJ18, SERPINA1, GSTT4, ASMTL, SLC25A5,
PRAMEF18, FCGBP) are themselves each known polymorphic or paralog-prone loci, though I count only what the symbol pattern
proves — 23/30. The load-bearing point is confirmed: **the top of the recessive list is dominated by immunogenetic and
multi-copy gene families**, and *BUB1B* is not near the top — it ranks **#103** (2 het), so a filter without population
frequencies genuinely does not surface it. This is the measured justification for planning Exomiser model 2.

## Entry 3 — Bounds what cannot be known / records a disconfirming drift (relevance test #3). Two of the drugmap's three counts reproduce **exactly from committed artifacts** — **148 molecules** (rows in `E_drugmap_output.csv`), **29 approved-passed** (29 `approved=yes`), and **33 consequence genes** (distinct HGNC symbols in `targets_bub1b.json`) — and all six "missed" approved drugs are present, max-phase 4, with trilaciclib ranked #1 exactly as the report's stated limitation predicts. But the third input count, **76 interaction partners at ≥0.9, does not reproduce against live Open Targets today (2026-09-07): it now returns 97 distinct partners** (raw 113 rows), so "110 targets" = 1 + 33 + 76 was a **point-in-time** figure and is 1 + 33 + 97 = 131 today. The load-bearing conclusion is unaffected; the *count* is not reproducible without a pinned Open Targets release.

`REPORT_track2:100`'s three numbers rest on two different kinds of source. I separated them:

**(a) Reproducible from committed files (no network):**

| Count | Report | Measured this run | Source |
|---|---|---|---|
| consequence genes | 33 | **33** distinct HGNC symbols across 8 mechanisms | `pipeline/track2_drugmap/targets_bub1b.json` |
| molecules returned | 148 | **148** data rows | `archive/creative/E_drugmap_output.csv` |
| passed 3-way approval | 29 | **29** rows with `approved=yes` (119 `no`) | same |
| six drugs the manual route missed | palbo/ribo/abema/trilaci/veneto/temsiro | **all 6 present, `approved=yes`, max_phase 4.0**; trilaciclib **rank 1**, abemaciclib 2, ribociclib 5, palbociclib 8, temsirolimus 9, venetoclax 12 | same |

The gene + 33 consequence = 34; 34 + 76 partners = 110, so the report's arithmetic is internally consistent, and the
`approved=yes` set, the ranking, and trilaciclib-as-top-hit (the report's own named limitation) all reproduce from the
committed CSV byte-for-byte.

**(b) Live-API count that has drifted (relevance test #3 — the disconfirming result, recorded with full prominence):**

I queried Open Targets Platform GraphQL live today (`work/track2/audit12_ot_partners.py`, resolving BUB1B →
`ENSG00000156970`, then the **identical** `OT_INTERACTIONS` query and `ot_interactions` dedup logic drugmap.py uses,
`scoreThreshold:0.9`):

| Quantity | Report (`REPORT_track2:100`) | Measured 2026-09-07 | Verdict |
|---|---|---|---|
| interaction partners at STRING/IntAct ≥ 0.9 | **76** | **97** distinct partners (raw `count` = 113 rows) | **drifted +21** |
| implied total target set | 110 | **1 + 33 + 97 = 131** | not reproducible |

So the "110 targets" figure is **not reproducible** — Open Targets has added interaction evidence for BUB1B since the run,
and the partner count moved from 76 to 97 at the same 0.9 threshold. This is exactly the drift `AUDIT_11:224` anticipated
("must report the query date and expect the counts to move"). **The bound, stated cleanly:** of the three drugmap counts,
**two (148 molecules, 29 approved) are frozen in a committed artifact and reproduce exactly; one (the input target-set
size) is a live-database quantity and should be reported as "N partners at ≥0.9 as of [date], Open Targets release [x]",
never as a fixed 110.** The conclusion the count supports — an automated tool surfaced six approved CDK4/6-, BCL2- and
mTOR-axis drugs a manual search missed, with a known direction-check flaw putting trilaciclib on top — stands on the
committed CSV and is untouched by the drift.

---

## What this run found, against the prompt's test

- **Entry 1 (converts an assertion; closes a `[skipped]` channel):** the mosaic **depth channel** reproduces from the raw
  VCF via the original `mosaic_robust.py` — `f_depth` **−0.047 to +0.044**, SD **0.0254**, floor 1.96·SD = **5.0%**,
  matching `F_math §2` to printed precision. **Structural note:** the spread is GC-driven (only GC-rich chr16/17/19/22 go
  positive; mean `f_depth` −0.011), so the "5% floor" is a *technical* noise floor, not a biological sensitivity — the
  depth channel is the weaker of the two, and the negative rests mainly on the (GC-immune) BAF channel.
- **Entry 2 (converts an assertion; confirms to the rank):** the 314-gene recessive list is dominated by the named loci
  exactly — **MUC3A / LILRB1 / PRSS2 are ranks 1 / 2 / 3**, HLA appears 7×, **92 of 314 (29.3%)** are named polymorphic/
  multi-copy/immunogenetic families, **23 of top 30** are, and **BUB1B ranks #103** (2 het). The characterisation is true
  and the case for frequency-aware re-ranking is measured, not asserted.
- **Entry 3 (bounds; disconfirming drift):** drugmap's **148 molecules and 29 approved reproduce exactly** from the
  committed CSV, **33 consequence genes** from the committed config, and the six "missed" drugs are all present/approved
  with trilaciclib #1 — but the **76 interaction-partner count has drifted to 97** on live Open Targets today, so
  **"110 targets" is a point-in-time figure (131 today), not a reproducible count.**

**No load-bearing conclusion of the submission is overturned.** Two channels of the mosaic negative are now both
independently reproduced (BAF by `AUDIT_11`, depth here); the recessive-list characterisation is confirmed to the rank;
the drug-tool conclusion stands on committed artifacts. One supporting number — the drugmap's "110 targets" — is shown to
be **non-reproducible by construction** (a live-API count), and its current value recorded with the query date.
Transferable points (relevance test #4): (a) a two-channel dosage negative should say **which channel sets the floor** —
here the depth floor is GC-noise-limited (~5%) and weaker than it looks, while the allele-balance channel is the real
constraint; (b) when a filter's output is characterised as "dominated by X-type loci," that is checkable by ranking the
list and family-tagging the top — here the top 3 were exactly the named genes; (c) a pipeline that mixes **frozen output
files** with **live-API inputs** should tag each reported number as one or the other, because only the frozen ones
reproduce — here 148/29 reproduce forever and 110 does not.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | mosaic depth channel, per-autosome `f_depth` range | **−0.047 (chr4) to +0.044 (chr19)** | `work/track2/audit12_feed_mosaic.py \| pipeline/mosaic_robust.py` |
| 2 | SD of `f_depth` over 22 autosomes | **0.0254** | same (JSON → `python3.12` stdev) |
| 3 | two-sided 96% depth floor 1.96·SD | **0.0498 = 5.0%** | same |
| 4 | sign structure of `f_depth` | mean **−0.0114**; only chr16/17/19/22 positive (GC-rich) | `work/track2/audit12_mosaic_robust.json` |
| 5 | recessive-compatible gene count (reproduces `AUDIT_08`) | **314** | `work/track2/audit12_feed_recessive.py \| pipeline/recessive_scan.py` |
| 6 | rank of MUC3A / LILRB1 / PRSS2 in the list | **1 / 2 / 3** (48 / 44 / 39 het) | `work/track2/audit12_recessive.txt` |
| 7 | HLA entries in the list | **7** (highest HLA-DRB1 #14) | same |
| 8 | genes in named polymorphic/multi-copy families | **92 of 314 = 29.3%**; 23 of top 30 | `work/track2/audit12_families.py` |
| 9 | rank of BUB1B | **#103**, 2 het 0 hom | `work/track2/audit12_recessive.txt` |
| 10 | drugmap consequence genes (config) | **33** distinct HGNC across 8 mechanisms | `pipeline/track2_drugmap/targets_bub1b.json` |
| 11 | drugmap molecules / approved (cached CSV) | **148 rows / 29 `approved=yes`** | `archive/creative/E_drugmap_output.csv` |
| 12 | six "missed" drugs status | all present, approved, max_phase 4; trilaciclib **rank 1** | same |
| 13 | BUB1B interaction partners at ≥0.9, **live OT 2026-09-07** | **97** distinct (raw 113); report said 76 → **drift** | `work/track2/audit12_ot_partners.py` (Open Targets GraphQL) |
| 14 | implied total target set today | **1 + 33 + 97 = 131** vs report 110 | derived from #10, #13 |

All new scripts and outputs are under `work/track2/audit12_*`. VCF = `data/WGS_EX2312012_HGWCNDSX7.vcf.gz` (contigs
unprefixed); gene VCF = `work/coding_nodbsnp.gene.vcf.gz`; drugmap cache = `archive/creative/E_drugmap_output.csv`;
Open Targets = live Platform GraphQL v4 (`api.platform.opentargets.org`, queried 7 Sep 2026). Tooling: `python3.12` +
pysam 0.24.0; **bcftools/mosdepth/tabix still absent** (both original scripts run unchanged behind pysam feeders that
reproduce the exact `bcftools query` streams).

## Where the next run should start

1. **Report-editing items remain open** (pure text edits, carried from `AUDIT_08`–`AUDIT_11`, plus three from this run,
   all edits not new measurements):
   - `REPORT_track2:100` "110 targets … 76 interaction partners" → add a **query date and Open Targets release**; the
     partner count is a live-API quantity (97 on 2026-09-07, was 76), not a fixed number. 148/29 are reproducible and can
     stay as stated.
   - `F_math §2` depth block prints `[skipped]` when `work/mosaic_robust.json` is absent → the file can be regenerated
     with `work/track2/audit12_feed_mosaic.py | pipeline/mosaic_robust.py`; consider committing the ~small JSON so the
     appendix reproduces offline, or noting the depth floor is GC-noise-limited (Entry 1).
   - the still-open `REPORT_track1:26` dbSNP/ClinVar wording (`AUDIT_11`), `REPORT_track2:56` STR-wording, the
     314/224/138 altitudes, the un-applied `AUDIT_06`/`AUDIT_07` corrections, the 288 bp phase-span citation
     (→`AUDIT_09`), and the `R9:62` "117 of 121 NFE" correction (`AUDIT_10`).
2. **Still bounded / not measurable here** (unchanged): `R5`'s 97-gene/18-gene cohesion-set modifier-enrichment row (list
   absent from the repo); the Exomiser model-2 ranking (`REPORT_track1:38`, 37 GB bundle).
3. **Remaining measurable load-bearing claims, in descending measurability:**
   - **The full drugmap re-run** (`REPORT_track2:100`: "in 350 seconds", 148 molecules end-to-end). This run reproduced
     the counts from the *cached CSV* and re-queried only the partner set; a full `drugmap.py --config targets_bub1b.json`
     re-run against all three live APIs (OT + ChEMBL + openFDA) would test whether the **whole table** still builds and how
     far 148/29 themselves drift — but it hits rate limits and the 76→97 partner drift guarantees the molecule set differs,
     so this is a *characterise-the-drift* exercise, not a reproduction. Medium effort.
   - **The `REPORT_track1:38` Exomiser model-2 statement** — still gated on the 37 GB bundle; not measurable here unless
     the bundle is fetched.
   - **`REPORT_track2` harm-screen / referee-adjudication counts** (`SUBMISSION_track2` §13, "three referee reports … a
     third verification pass") — these are process claims about this project's own documents; individual contested points
     could be spot-checked against the primary sources cited, but most are editorial, not measurements.
4. Tooling unchanged: `python3.12` + pysam 0.24.0, samtools, minimap2 present; **no bcftools/mosdepth/tabix on PATH**
   (original `mosaic_robust.py` and `recessive_scan.py` both run unchanged behind pysam feeders); Open Targets GraphQL,
   ChEMBL REST and openFDA all reachable (HTTP 200 on 2026-09-07); gnomAD r4 GraphQL and NCBI ClinVar remote-tabix
   reachable. `work/track2/audit12_*` reproduce every number here.
