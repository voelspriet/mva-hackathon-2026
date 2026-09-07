# AUDIT 06. The "224 genes carry two rare coding variants" candidate space, and R15's strictest-threshold survivors — both re-derived on measured gnomAD frequency

**Run 06 of `PROMPT_relevant_additions.md`, 7 September 2026.** `AUDIT_05` ended by naming (item 2) the one hunt
its own finding opened but did not run: *the common-variant contamination is a property of
`work/coding_nodbsnp.gene.vcf.gz` itself, so any **other** analysis that counts entries in that file without a
frequency filter inherits the caveat — sweep for a positive claim that does.* `AUDIT_05` checked two such analyses
and declared them safe: `AUDIT_01`'s NMD/EJC screen (a negative, which contamination cannot fabricate) and — the
sentence this run tests — **"`R15`'s compound-het funnel is safe (it re-applied AF<1e-4 downstream)."** This run
takes that sweep to the one place the contamination is load-bearing: the headline candidate-space claim that goes
into the methods form.

Before writing I re-read `R14`, `R15`, `R21`, `OBSERVATIONS_2000.md`, `SYNTHESIS_for_judging.md` and all five prior
`AUDIT_NN` files. **Rule 3 credits:** the 82%-common measurement of the input file is `AUDIT_05`'s; the compound-het
funnel (224→8→2), the eight genes at AF<1e-4 and the "state your rarity criterion" principle are `R15`/`R21`'s; the
call-quality filter that leaves two genes is `R21`'s. What is new below is (a) the "224 genes carry two *rare* coding
variants" claim re-derived on measured gnomAD AF, which shows the genuinely-rare candidate space is **~19, not 224**;
and (b) a disconfirmation `AUDIT_05` did not reach — `R15`'s strictest-threshold row (AF<1e-5) does **not** survive
re-derivation: the two genes it names (*BUB1B*, *KIR3DL3*) are not the two that meet it.

The load-bearing sentence, verbatim, the one destined for the submission's methods form
(`SYNTHESIS_for_judging.md:67`):

> "The compound-heterozygous pattern is not rare in isolation: **224 genes in this genome carry two rare coding
> variants**. Applying the candidate's own frequency threshold leaves 8, and adding four call-quality measurements
> leaves 2, of which *BUB1B* is one."

And `R15:19`, the strictest-threshold claim:

> "At AF < 1e-5 only two survive: **BUB1B and KIR3DL3**."

**Method consistency (stated first so every number is auditable).** Rarity is `AF = max(exome_af, genome_af)` on
gnomAD v4.1 — the identical rule the project's own `pipeline/alien/fetch_gnomad_af.py` uses — read from
`work/gnomad_af.json` (850 variants) + `work/track2/gnomad_missing_af.json` (826, the file `AUDIT_05` built);
absent-from-gnomAD counts as rare. Coverage is **complete**: all 1,676 distinct gene+variant records in
`work/coding_nodbsnp.gene.vcf.gz` map to a measured AF (`af-unmapped = 0`). One reproducible script does the whole
derivation: `work/track2/audit06_rare_recount.py`. Tooling: `python3.12` (pysam 0.24.0); VCF contigs `1..22,X`.

---

## Entry 1 — Converts an assertion into a measurement (disconfirming). Of the ~224 genes said to "carry two rare coding variants," only 19 carry two variants that are actually rare; the rest are pairs that include common variants.

The "224" is `OBSERVATIONS_2000.md`'s `gene-burden` class: *"Genen met 2 of meer coderende varianten buiten de
gangbare catalogus"* — genes with ≥2 coding variants **absent from the common catalogue**, i.e. the same
dbSNP-absence proxy `AUDIT_05` measured to be **81.6% common**. `SYNTHESIS_for_judging.md:11` states this honestly
("two coding variants **absent from the common catalogue**"); the methods-form sentence at line 67 restates it as
"two **rare** coding variants." That one word is the whole of this entry, and it is measurable.

**Reproduction of the candidate space from files in hand.** Grouping `work/coding_nodbsnp.gene.vcf.gz` by
`INFO/GENE`:

| Grouping | This run (from `coding_nodbsnp`) | Prior number |
|---|---|---|
| genes with ≥2 non-dbSNP coding variants, any zygosity | **218** | `R21`/OBS report **224** (from `R11`'s snpEff no-rsID set, which is not present as a file in `work/`; the ~6-gene gap is a proxy-definition difference — snpEff-no-rsID vs `INFO/DB=0` — not material below) |
| genes with ≥2 **heterozygous** non-dbSNP coding variants | **138** | `R15`'s raw grouping = **138** — reproduces exactly |

**The measurement — every gene, reclassified on measured gnomAD AF (not on dbSNP absence).** Number of genes that
carry **≥2 variants that are genuinely rare** at each threshold (any zygosity):

| "rare" = both variants below | genes with ≥2 such | fraction of the 218 |
|---|---|---|
| AF < 50% | 137 | 63% |
| AF < 10% | 59 | 27% |
| **AF < 1% (any clinical rare bar)** | **19** | **8.7%** |
| AF < 0.1% | 11 | 5.0% |
| AF < 1e-4 (the candidate's own threshold) | 8 | 3.7% |
| AF < 1e-5 | 2 | 0.9% |

So of the ~218–224 genes that "carry two coding variants absent from the common catalogue," **only 19 carry two
variants that are rare by any ordinary bar (AF<1%)**, and only 8 at the candidate's own 1e-4. The other ~91% are
genes paired on **common** variants — e.g. *AADACL3*, one of `R14`'s surviving "missense pairs," whose two
non-dbSNP coding variants sit at gnomAD max-AF **0.169 and 0.171** (and a third at 0.326). They are absent from the
caller's dbSNP build but are ordinary population polymorphisms.

**What this changes, and what it does not.** The funnel *arithmetic* survives — applying "both variants < 1e-4"
gives **8** genes (reproduces `R15`/`R21` exactly, same eight: *ADAMTS1, ADGRA3, BUB1B, KIR3DL3, MUC4, RBM39,
SERPINA1, VPS41*), and `R21`'s call-quality filter leaves **2** (*ADGRA3, BUB1B*). The diagnosis and the final
two-gene result are untouched. But the **rhetorical setup is not measurement-honest**: the sentence sells the
method by the size of the field it clears ("the pattern is not rare — 224 genes have it — and we cut to 2"), and
the true genuinely-rare compound-het field is **~19, not 224**. The honest statement is either `SYNTHESIS:11`'s own
careful wording ("224 genes carry two coding variants *absent from the common catalogue*; 19 carry two that are
rare in gnomAD; the candidate's <1e-4 threshold on both leaves 8; call quality leaves 2"), or drop "224" from the
rarity sentence entirely. This is exactly the `AUDIT_05` contamination biting the one downstream claim `AUDIT_05`
assumed was safe: safe at the *final count*, not at the *headline*.

## Entry 2 — Closes/corrects a sub-claim (disconfirming). R15's "at AF<1e-5 only BUB1B and KIR3DL3 survive" is not reproducible and contradicts the 7.9e-5 figure R15 itself reports; the two genes that actually meet it are both artifacts.

`R15`'s Change-1 funnel thresholds on **both** of a gene's variants ("Threshold on both variants", `R15:9`). Its
bottom row states that at AF<1e-5 the two survivors are *BUB1B* and *KIR3DL3*, and Change 2 leans on it:
*"The elimination of KIR3DL3 is the substantive one: it was the only other gene meeting the strictest threshold"*
(`R15:36`; echoed in `SYNTHESIS:39`). Re-derived under `R15`'s own rule on measured AF, the row does not hold.

**The measured 1e-5 survivors (genes with ≥2 het variants each AF<1e-5):**

| Gene | its het variants (chr:pos:ref:alt → max-AF) | ≥2 below 1e-5? |
|---|---|---|
| **BUB1B** | 15:40209701 T>G → **7.87e-5**; 15:40220612 T>G → 6.84e-7 | **No** — only 1 of 2 |
| **KIR3DL3** | 19:54726088 G>A → **7.32e-5**; 19:54726091 A>C → 6.84e-7 | **No** — only 1 of 2 |
| **SERPINA1** | 19 het variants in a 164 bp cluster; 6 of them <1e-5 (incl. 3 gnomAD-absent) | Yes |
| **VPS41** | 7:38726051 C>T → absent; 7:38726056 AG>A → absent (5 bp apart) | Yes |

`R15` reports the candidate's alleles as **"gnomAD AF 7.9e-5 and 6.8e-7"** — so it *knew* one *BUB1B* allele is
7.9e-5, which is above 1e-5. Under `R15`'s stated "both variants below" rule, *BUB1B* therefore meets 1e-4 (both
below) but **cannot** meet 1e-5, and neither can *KIR3DL3* (its second het allele is 7.32e-5). The 1e-5 row naming
*BUB1B* and *KIR3DL3* is internally inconsistent with `R15`'s own numbers. No interpretation reproduces
`{BUB1B, KIR3DL3}` at 1e-5: as a subset of the eight 1e-4 survivors, the genes with two het alleles below 1e-5 are
**SERPINA1 and VPS41**; as a "gene has at least one allele <1e-5" rule, more than two qualify. The exact-two answer
is `{SERPINA1, VPS41}`.

**And the two that do meet it are precisely the artifacts the call-quality filter exists to remove** (measured from
`data/WGS_EX2312012_HGWCNDSX7.vcf.gz`):

- **SERPINA1** — 28 PASS variants in chr14:94379443–94379607, a **164 bp span with minimum inter-variant distance
  1 bp**: a dense misalignment/indel pile-up, the textbook target of `R14`/`R21`'s "variants <1 kb apart" rule.
- **VPS41** — its two ultra-rare variants are **5 bp apart and both carry `PGT 0|1`, `PID 38726051_C_T`**: phased in
  *cis* on one haplotype — a single event, not a compound heterozygote (this is the phase-elimination `R15` Change 2
  already recorded, here shown to also be a <1 kb cluster).

**What this changes, and what it does not.** It does not touch the diagnosis, the eight-gene 1e-4 result, or the
final two genes — all of which reproduce. Three specific `R15` statements are corrected: (i) *BUB1B* does **not**
survive to 1e-5 — its rarer-threshold allele is 7.9e-5, so its correct strictest passing bar is the 1e-4 `R15`
itself calls "the candidate's own threshold"; claiming 1e-5 overstates the candidate's rarity. (ii) *KIR3DL3* is
**not** "the only other gene meeting the strictest threshold" — at 1e-5 the genes meeting it are SERPINA1 and VPS41,
and *KIR3DL3* is one of the *seven* others at 1e-4, so the phrase is wrong under either reading of "strictest."
(iii) The phase elimination of *KIR3DL3* remains valid and useful, but its billing as removing "the only gene left
at the strictest threshold" is not.

**The constructive transfer (this is why the correction is worth writing, not just a nit).** The genes that pass a
*pure frequency* filter at the strictest level are **both artifacts** — a cis-phased 5 bp pair and a 164 bp indel
cluster — and **zero** real candidates survive frequency-alone at 1e-5. That is a sharper version of `R21`'s own
lesson than `R21` stated: it is not merely that "frequency plus call quality" beats a name-prefix label; it is that
**at the tightest frequency bar, frequency alone selects only artifacts**, so the call-quality/clustering filter is
not an optional refinement but the thing doing the work at that end of the funnel. A team reusing this funnel on
another patient should apply the clustering/phase filter *before* reading off the strictest-frequency survivors, or
it will mistake a misalignment pile-up for the rarest candidate in the genome.

---

## What this run found, against the prompt's own relevance test

- **Entry 1 (converts an assertion into a measurement — disconfirming):** the methods-form claim "224 genes carry
  two **rare** coding variants" is not measurement-honest. Of the 218 genes with ≥2 non-dbSNP coding variants
  (≈`R21`'s 224), only **19** carry two variants rare at AF<1% and **8** at the candidate's 1e-4; the rest are pairs
  including common variants (e.g. *AADACL3* at AF 0.17/0.17). The funnel arithmetic (→8→2) and the diagnosis are
  untouched; the word "rare" applied to the 224 candidate space is the error. This is `AUDIT_05`'s 82%-common
  finding landing on the one downstream claim `AUDIT_05` had assumed safe.
- **Entry 2 (closes/corrects a sub-claim — disconfirming):** `R15`'s "at AF<1e-5 only *BUB1B* and *KIR3DL3* survive"
  is not reproducible and contradicts `R15`'s own 7.9e-5 allele figure. Under `R15`'s stated rule the two genes with
  two het alleles below 1e-5 are **SERPINA1 and VPS41**, both artifacts (a 164 bp indel cluster; a 5 bp cis-phased
  pair). *BUB1B* and *KIR3DL3* each have only one het allele below 1e-5. The 1e-4 result and the final two genes
  reproduce; only the strictest-threshold row and the "only other gene at the strictest threshold" billing are wrong.

**No load-bearing conclusion of the submission is overturned.** *BUB1B* is the diagnosis; the 224→8→2 reduction
lands on *ADGRA3* + *BUB1B* exactly as reported; every one of `R15`'s 18/10/8 funnel counts reproduced to the gene.
**Two disconfirming results are recorded with equal prominence (rule 2):** the "224 rare" candidate space is really
~19 rare, and `R15`'s 1e-5 survivors are SERPINA1/VPS41 (artifacts), not BUB1B/KIR3DL3. The transferable
contribution is that at the tightest frequency bar the funnel needs its clustering/phase filter applied *first*,
because frequency alone there selects only artifacts.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | AF coverage of the input file | 1,676 distinct gene+variant records, **0 unmapped** to measured AF | `work/track2/audit06_rare_recount.py` (merges `work/gnomad_af.json` + `work/track2/gnomad_missing_af.json`) |
| 2 | genes with ≥2 non-dbSNP coding variants (any zyg) | **218** (`R21`/OBS report 224 from the snpEff no-rsID set, not present as a file) | same, group `INFO/GENE`, count ≥2 |
| 3 | genes with ≥2 **het** non-dbSNP coding variants | **138** — reproduces `R15`'s raw grouping exactly | same, het-only |
| 4 | genes with ≥2 genuinely rare variants, any zyg | <1% : **19**; <1e-3 : 11; <1e-4 : 8; <1e-5 : 2 (of 218) | same, `is_rare(max-AF, thr)` on both |
| 5 | het compound-het funnel on measured AF | <1e-2 : **18**; <1e-3 : **10**; <1e-4 : **8**; <1e-5 : **2** | same; matches `R15`'s 18/10/8 and its eight gene names |
| 6 | the eight at AF<1e-4 | ADAMTS1, ADGRA3, BUB1B, KIR3DL3, MUC4, RBM39, SERPINA1, VPS41 | same — identical to `R15:17` |
| 7 | example common "224 candidate" | *AADACL3* two non-dbSNP coding variants at max-AF **0.169, 0.171** (third 0.326) | `work/gnomad_af.json` keys `1:12719558:C:T`, `1:12719616:C:T` |
| 8 | BUB1B causal allele AFs | 15:40209701 T>G **7.866765719508074e-05**; 15:40220612 T>G **6.840516103258959e-07** | `work/gnomad_af.json['15:40209701:T:G'/'15:40220612:T:G']` |
| 9 | KIR3DL3 het allele AFs | 19:54726088 G>A **7.32e-5**; 19:54726091 A>C 6.84e-7 (rest of gene hom-common) | `audit06_rare_recount.py` per-gene dump |
| 10 | **the actual AF<1e-5 survivors (two het alleles each)** | **SERPINA1, VPS41** — NOT BUB1B/KIR3DL3 | `audit06_rare_recount.py` block [C], threshold 1e-5 |
| 11 | BUB1B / KIR3DL3 count below 1e-5 | each: 2 het variants, **1** below 1e-5 | `audit06_rare_recount.py` block [D] |
| 12 | SERPINA1 cluster | 28 PASS variants in chr14:94379443–94379607, **164 bp span, min inter-variant distance 1 bp** | pysam `fetch('14',94379440,94379610)`, PASS positions |
| 13 | VPS41 phase | both variants (5 bp apart) `PGT 0|1`, `PID 38726051_C_T` → in *cis* | pysam `fetch('7',38726040,38726070)`, read PGT/PID |

gnomAD frequencies via `work/gnomad_af.json` (project fetch) and `work/track2/gnomad_missing_af.json` (`AUDIT_05`
fetch), both `POST https://gnomad.broadinstitute.org/api` dataset `gnomad_r4`, `af=max(exome,genome)`. All grouping
and re-derivation in `work/track2/audit06_rare_recount.py`.

## Where the next run should start

1. **The two disconfirmations here are corrections to submission text, not to the analysis, and they are cheap to
   apply.** (a) In the methods-form sentence (`SYNTHESIS_for_judging.md:67`) replace "224 genes carry two **rare**
   coding variants" with the honest chain: 224 (≈218) carry two non-dbSNP coding variants, **19** carry two that are
   rare (AF<1%), the candidate's 1e-4 threshold on both leaves 8, call quality leaves 2. (b) In `R15:19,36` and
   `SYNTHESIS:39`, drop or fix "at AF<1e-5 only BUB1B and KIR3DL3 survive / KIR3DL3 the only other gene at the
   strictest threshold": the measured 1e-5 pair is SERPINA1+VPS41, both artifacts, and *BUB1B*'s correct strictest
   passing bar is 1e-4. A next run that is allowed to edit the reports (this run only measured) should make these two
   edits; the measurements and line references above are sufficient to do it without re-computing.
2. **The 97-gene enrichment row (`R5`) is still not re-derivable** — `AUDIT_04`/`AUDIT_05` established the 18-gene
   cohesion list is in no file present, and this run confirms it is not recoverable from `pipeline/track2_compute/`
   (only the 80-gene `genes_network.txt` is there). It stays bounded as `AUDIT_05` left it unless the list surfaces.
3. **`AUDIT_01` item 3 (STR-aware comparator for the upstream regulatory scan) remains the one untouched
   methodological to-do** across all six runs — the single item nobody has taken.
4. Tooling for whoever runs next: `python3.12` (pysam 0.24.0); egress wide (gnomAD, Ensembl, NCBI, PyPI, GCS); a
   complete measured max-AF for all 1,676 coding non-dbSNP variants now exists across `work/gnomad_af.json` +
   `work/track2/gnomad_missing_af.json`, and `work/track2/audit06_rare_recount.py` reproduces every number in this
   file in one pass.
