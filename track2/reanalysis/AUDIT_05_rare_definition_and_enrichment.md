# AUDIT 05. What "rare" actually means in the coding non-dbSNP file, the modifier-enrichment p-value re-derived on that measurement, and an orthogonal (AlphaMissense) closure of SMC4

**Run 05 of `PROMPT_relevant_additions.md`, 7 September 2026.** `AUDIT_04` ended by naming three open items:
(2) settle **SMC4 p.Asp256Asn** with an orthogonal predictor — it named **AlphaMissense**, and the repo already holds
the streaming recipe `pipeline/track2_compute/get_alphamissense_bub1b.sh`; and (3) **re-derive `R5`'s enrichment
p-values on a gnomAD-rarity-filtered input**, because `AUDIT_04` had spot-checked three entries
(CENPV 0.46, H2BW1 0.36, FANCD2 0.35) and shown the input file `work/coding_nodbsnp.gene.vcf.gz` — which supplies
**both** the numerator and the density of `R5`'s test — is not a "rare variant" file. This run takes both, and closes
item 3 by measuring the rarity of **every** variant in that file rather than a handful.

Before writing I read `R5` (the enrichment), `R12` (the deep-intronic variant), `R14`/`R15` (the compound-het funnel
and its explicit rare-definition caveat), and all four prior `AUDIT_NN` files. **Rule 3 credits:** the modifier screen,
its enrichment table (80-gene P=0.0012; 97-gene P=0.021) and its three named hits are `R5`'s; SMC4 p.Asp256Asn as an
ontology-surfaced, ultra-rare, in-silico-damaging candidate is `AUDIT_04`'s; the principle that "any claim of the form
'only N genes look like this' should state its criterion" is **`R15`'s**, established there for the compound-het
shortlist. What is new below is (a) that principle carried into the one analysis that never applied it — `R5`'s
enrichment — with the p-value recomputed on measured rarity; (b) the rarity of all 1,676 variants in the input file,
which converts `AUDIT_04`'s three-variant spot-check into a complete count; and (c) a third, orthogonal pathogenicity
score for SMC4.

**Method consistency (stated first so the numbers are auditable).** Rarity is classified by
`AF = max(exome_af, genome_af)` on gnomAD **v4.1** (`gnomad_r4`), which is **exactly** the rule the project's own
`pipeline/alien/fetch_gnomad_af.py` uses to build `work/gnomad_af.json`. That pre-fetched file covers 850 of the 1,676
variants (the compound-het candidates `R15` queried); the remaining **826** were fetched this run with the identical
batched query (`work/track2/fetch_missing.py`, 20 variants/request, `gnomad_r4`, 0 fetch failures) and cached in
`work/track2/gnomad_missing_af.json`. Absent-from-gnomAD is treated as rare. Tooling: `python3.12` (pysam 0.24.0); VCF
contigs `1..22,X`; egress is wide (AUDIT_04) — the AlphaMissense bulk TSV streams from `storage.googleapis.com`.

---

## Entry 2 (taken first because it is the disconfirming one). Converts an assertion into a measurement. `R5`'s "the network is depleted, P=0.0012" does not survive a real rarity filter: the input file is 82% common variants, and once they are removed the network carries about as many rare coding variants as chance predicts.

`R5`'s test is a Poisson comparison: `expected = density × coding_bases`, with the density taken from the same file of
"1,694 rare coding variants." For the 80-gene mitotic-checkpoint/decay network (296,459 coding bases) it reports
**expected 9.0, observed 1, P(X≤1) = 0.0012**, and concludes "the network carries **fewer** rare coding variants than
its coding footprint predicts … the opposite of a modifier signal … what constraint on essential mitotic genes
predicts." The load-bearing assumption is in the word **rare**: both the density (9.0) and the observed count (1) are
counts of variants *absent from the caller's dbSNP build*, which is not the same as rare in the population.

**R5's arithmetic reproduces exactly**, so the recomputation is like-for-like:
`P(X≤1 | Poisson(9.0)) = e⁻⁹·(1+9) = 0.00123` ✓ (matches R5's 0.0012).

**The measurement — every variant in the file, not three.** `AUDIT_04` named CENPV/H2BW1/FANCD2 as common. Across all
**1,676** distinct alt-records in `work/coding_nodbsnp.gene.vcf.gz`:

| Population status (`max(exome,genome)` AF, gnomAD v4.1) | count | % of file |
|---|---|---|
| **AF ≥ 1% (common by any clinical bar)** | **1,368** | **81.6%** |
| of which AF ≥ 10% | 1,207 | 72.0% |
| of which **AF ≥ 50% (the ALT is the *major* allele)** | **531** | **31.7%** |
| absent from gnomAD entirely | 17 | 1.0% |
| rare: absent **or** AF < 1% | 308 | 18.4% |
| rare: absent **or** AF < 0.1% | 221 | 13.2% |
| rare: absent **or** AF < 0.01% | 176 | 10.5% |

So the file `R5` treated as 1,694 rare variants is **~82% common**, and nearly a third of it is sites where the
reference genome simply carries the minor allele. "Absent from the caller's dbSNP build" turns out to select common
population variants at least as often as rare ones. (`AUDIT_01` had already noted the converse — the file *misses*
catalogued rare variants; this is the complete count of the other direction.)

**The 80-gene network holds exactly one variant in this file** — ANAPC2 chr9:137185989 C>T, `max` AF **1.64e-4**
(genome; absent from exomes) — which reproduces `R5`'s observed = 1 and is, correctly, one of the genuinely rare
entries. So the contamination is entirely in the **density/expected** side of `R5`'s test, not the observed side.

**Re-derivation.** Holding `R5`'s density model and coding-base denominators fixed and scaling the expected by the
measured rare fraction `f = N_rare/N_all` (this is exact: `rare_density × B₈₀ = f × all_density × B₈₀ = f × 9.0`):

| Definition of "rare" | rare fraction f | expected in 80-net (f × 9.0) | observed rare | **P(X ≤ obs)** |
|---|---|---|---|---|
| `R5` (all non-dbSNP counted as rare) | 1.000 | 9.00 | 1 | **0.0012** — significant depletion |
| AF < 1% or absent | 0.184 | 1.65 | 1 | **0.51** — not significant |
| AF < 0.1% or absent | 0.132 | 1.19 | 1 | **0.67** — not significant |
| AF < 0.01% or absent | 0.105 | 0.95 | 0 (ANAPC2 at 1.64e-4 excluded) | **0.39** — not significant |

**What this changes, and what it does not.** `R5`'s *conclusion* — no enrichment, therefore no modifier signal — is
**not overturned**: under every threshold the network still carries no *excess* of rare coding variants (observed ≈
expected, never above), and `AUDIT_02`/`AUDIT_03` independently closed the three named variants as benign-range. But
`R5`'s specific statistical claim — a **significant depletion** at P=0.0012, read as evidence of "constraint on
essential mitotic genes" — **does not survive measurement.** The significance came entirely from an expected value
(9.0) inflated by ~1,368 common variants; on genuinely rare variants the network's single hit sits squarely inside
chance (expected ≈ 1.2–1.7, P ≈ 0.4–0.7), so there is no measurable depletion and no constraint signal to point to.
The honest statement is "the mitotic-checkpoint network shows no enrichment **and no significant depletion** for rare
coding variants," not "the network is depleted, P=0.0012." This is the `R15` principle — state the rare criterion,
because the answer depends on it — applied to the one analysis that had not applied it.

I did not recompute the **97-gene** row: `AUDIT_04` established the 18-gene cohesion addition is not enumerated in any
file present, so that universe cannot be reproduced. The same inflation applies to it in principle (its expected 11.9
is built from the identical density), but I will not put a number on a set I cannot rebuild from files in hand.

## Entry 1. Converts an assertion into an orthogonal measurement (and transfers). SMC4 p.Asp256Asn scores AlphaMissense 0.594 "likely pathogenic" — a third, independent predictor agreeing with SIFT and PolyPhen, on a residue AlphaMissense calls intolerant to any substitution.

`AUDIT_04` surfaced **SMC4 p.Asp256Asn** (chr3:160411998 G>A) — ultra-rare (gnomAD exome AF 1.37e-6, 0 hom), a clean
heterozygous PASS call, in a core chromosome-segregation gene (condensin ATPase) — and called it "in-silico damaging"
on **SIFT deleterious (0) + PolyPhen probably_damaging (1)**. Those two predictors are correlated (both largely
conservation-driven), so `AUDIT_04` explicitly left an orthogonal score (AlphaMissense) as the way to settle it. Run
this run by streaming the public AlphaMissense hg38 bulk table for the SMC4 region (same recipe as the repo's BUB1B
script, no patient coordinate disclosed — a whole-region pull):

| Substitution at chr3:160411998 (codon 256) | protein | AlphaMissense | class |
|---|---|---|---|
| **G>A (the child's variant)** | **D256N** | **0.5937** | **likely_pathogenic** |
| G>C | D256H | 0.9454 | likely_pathogenic |
| G>T | D256Y | 0.8554 | likely_pathogenic |

(transcript ENST00000344722.5, UniProt Q9NTJ3; protein change D256N is identical to `AUDIT_04`'s MANE p.Asp256Asn.)

**Reading it honestly.** AlphaMissense **agrees** with SIFT and PolyPhen — a third, methodologically independent
predictor calling the child's allele damaging — and all three possible substitutions at Asp256 score pathogenic
(0.59–0.95), so the residue is intolerant. But 0.5937 sits only just above AlphaMissense's likely-pathogenic threshold
(0.564): this is a **modest-confidence** pathogenic call, not a strong one, and it is a *prediction*, not a functional
result. So `AUDIT_04`'s status for SMC4 is confirmed and slightly firmed — three orthogonal predictors now concur — but
its **placement is unchanged**: a single damaging-predicted heterozygote, **no second hit** in the gene (so no recessive
model), **no established SMC4 Mendelian segregation disease**, and no ClinVar assertion. It does not touch the *BUB1B*
compound-het diagnosis. It remains "one sentence in a family study," now with three predictors behind that sentence
instead of two, and the only thing that could raise it further is parental genotyping.

---

## What this run found, against the prompt's own relevance test

- **Entry 2 (converts an assertion into a measurement — disconfirming):** the input file behind `R5`'s enrichment test
  is **81.6% common variants** (1,368 of 1,676 at AF ≥ 1%; 531 are the major allele). Recomputing `R5`'s Poisson test
  on the genuinely rare subset collapses its **P=0.0012 "significant depletion" to P ≈ 0.39–0.67 (not significant)**:
  the depletion was an artefact of counting common variants as rare. `R5`'s *no-modifier / no-enrichment* conclusion
  survives (observed never exceeds expected); its *significant-depletion-from-constraint* claim does not.
- **Entry 1 (converts an assertion into an orthogonal measurement):** SMC4 p.Asp256Asn scores **AlphaMissense 0.594
  likely_pathogenic**, a third independent predictor agreeing with SIFT+PolyPhen (modest confidence; residue intolerant
  to all substitutions). `AUDIT_04`'s loose end is closed at the in-silico layer; its placement ("one sentence in a
  family study") is unchanged.

**No load-bearing conclusion of the submission is overturned.** The diagnosis is untouched; `R5`'s modifier answer
(no enrichment) stands; SMC4 remains an incidental single het. **The disconfirming result recorded with equal
prominence (rule 2)** is that `R5`'s headline statistic — the 0.0012 depletion, presented as evidence of purifying
constraint — is not reproducible once "rare" is measured rather than proxied by dbSNP absence. The transferable
contribution is the same as `R15`'s lesson made concrete: an enrichment/depletion test built on "absent from a dbSNP
build" as the rarity proxy will manufacture significance from common variants; the density and the observed count must
be filtered on measured population frequency, and here that turns a significant depletion into no signal.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | distinct alt-records in coding_nodbsnp | 1,676 (1,705 alt-records; R5's "1,694" is the VCF-record count) | pysam scan of `work/coding_nodbsnp.gene.vcf.gz` |
| 2 | gnomAD AF for the 826 not pre-fetched | fetched, 0 failures; cached `work/track2/gnomad_missing_af.json` | `python3.12 work/track2/fetch_missing.py` (batched `gnomad_r4`, 20/req, max(exome,genome)) |
| 3 | AF method match to project pipeline | `af = max(exome_af, genome_af)` — identical to `pipeline/alien/fetch_gnomad_af.py` | read of that script |
| 4 | common fraction of the file (AF ≥ 1%) | **1,368 / 1,676 = 81.6%** | classify all 1,676 by max-AF ≥ 0.01 |
| 5 | major-allele fraction (AF ≥ 0.5) | **531 / 1,676 = 31.7%** | classify by max-AF ≥ 0.5 |
| 6 | absent from gnomAD | 17 / 1,676 | max-AF is None |
| 7 | rare fraction (absent or AF<1% / <0.1% / <0.01%) | 308 (18.4%) / 221 (13.2%) / 176 (10.5%) | classify by threshold |
| 8 | coding_nodbsnp variants in the 80-gene network | 1 — ANAPC2 chr9:137185989 C>T, AF 1.64e-4 | intersect `INFO/GENE` with `pipeline/track2_compute/genes_network.txt` (80 genes) |
| 9 | R5 Poisson reproduction | P(X≤1 \| λ=9.0) = 0.00123 = R5's 0.0012 | `sum(e^-9·9^i/i!, i=0..1)` |
| 10 | re-derived 80-net enrichment, rare<1% | expected 1.65, obs 1, **P=0.51** | scale expected = 0.184 × 9.0; Poisson P(X≤1) |
| 11 | re-derived, rare<0.1% | expected 1.19, obs 1, **P=0.67** | scale 0.132 × 9.0 |
| 12 | re-derived, rare<0.01% | expected 0.95, obs 0, **P=0.39** | scale 0.105 × 9.0 (ANAPC2 1.64e-4 excluded) |
| 13 | SMC4 p.Asp256Asn AlphaMissense | chr3:160411998 G>A → **D256N 0.5937 likely_pathogenic** (D256H 0.945, D256Y 0.855) | stream `AlphaMissense_hg38.tsv.gz`, region chr3:160400000–160420000 → `work/track2/alphamissense_SMC4.tsv` |

gnomAD via `POST https://gnomad.broadinstitute.org/api` (`gnomad_r4`); AlphaMissense via
`https://storage.googleapis.com/dm_alphamissense/AlphaMissense_hg38.tsv.gz`. Artefacts in `work/track2/`
(`gnomad_missing_af.json`, `fetch_missing.py`, `alphamissense_SMC4.tsv`).

## Where the next run should start

1. **The `R5` enrichment is now measured, and the correction is bounded to the 80-gene set.** The 97-gene row cannot be
   re-derived without the 18-gene cohesion list, which `AUDIT_04` established is in no file present. If a next run can
   recover or reconstruct that list (e.g. from `R5`'s working scripts under `pipeline/track2_compute/` if any survive),
   the identical density-scaling would put a number on the 97-gene P=0.021 too; the direction (its expected 11.9 is
   built from the same 82%-common density, so it will also lose significance) is already implied but not measured.
2. **The common-variant contamination is a property of `work/coding_nodbsnp.gene.vcf.gz` itself**, so any *other*
   analysis that used that file as a "rare coding" input inherits the caveat. `AUDIT_01`'s NMD/EJC second-hit screen is
   safe (its result was an **absence**, which common-variant contamination cannot fabricate) and `R15`'s compound-het
   funnel is safe (it re-applied AF<1e-4 downstream). A next run could sweep for any *positive* claim elsewhere that
   counts entries in this file without a frequency filter — that is where the 82% would bite.
3. **SMC4 is closed at every in-silico layer** (SIFT, PolyPhen, AlphaMissense all damaging; ultra-rare; single het). The
   only thing that could move it is parental genotyping (is it de novo or inherited, and is there a second allele in
   trans that a coding-only screen missed) — wet-lab, not DNA-in-hand.
4. **`AUDIT_01` item 3 (STR-aware comparator for the upstream regulatory scan) remains the one untouched methodological
   to-do** across all five runs.
5. Tooling for whoever runs next: `python3.12` (pysam 0.24.0); egress wide (PyPI, GitHub, GCS/AlphaMissense, gnomAD,
   Ensembl, NCBI); complete max-AF for all 1,676 coding non-dbSNP variants now exists across
   `work/gnomad_af.json` (850) + `work/track2/gnomad_missing_af.json` (826).
