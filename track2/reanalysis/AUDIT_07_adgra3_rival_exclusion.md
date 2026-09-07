# AUDIT 07. The other gene the unbiased funnel keeps: ADGRA3 excluded by measurement, not by assertion

**Run 07 of `PROMPT_relevant_additions.md`, 7 September 2026.** Continues `AUDIT_01`–`AUDIT_06`. Before writing I
re-read `R15`, `R21` and `SYNTHESIS_for_judging.md`; the 224→8→2 funnel and its two survivors (*ADGRA3*, *BUB1B*)
are established there and reproduced to the gene in `AUDIT_06`. This run does **not** re-open the funnel. It
attacks the one sentence the funnel leaves standing.

## The claim audited, and why it is load-bearing

The submission's strongest rigor claim is that an unbiased filter — frequency plus call quality, **no phenotype,
no gene panel, no disease knowledge** — reduces 224 candidate genes to two, and one of them is the diagnosis
(`SYNTHESIS:11`, `R15`, `R21`). The other is *ADGRA3*. About it the submission says:

> "*ADGRA3* is an adhesion G protein-coupled receptor with no established link to this phenotype, and it is named
> here because it is the only gene besides the diagnosis that survives two independent measured filters. It is a
> candidate for exclusion, not a rival diagnosis." (`R21:45`; repeated verbatim in intent at `SYNTHESIS:58`)

**Relevance test: this entry does #1 (closes an alternative explanation) and #2 (converts an assertion into a
measurement).** The exclusion of *ADGRA3* is currently `assumed`: "no established link to this phenotype" cites no
measurement, and R21's only *ADGRA3* numbers are call-quality (coverage 0.96, allele balance 0.44). That is the
single most obvious hostile-reviewer objection to the whole unbiased-funnel framing, in the reviewer's words:

> *"Your own phenotype-free filter outputs two genes on equal footing. You picked BUB1B because you already knew
> the answer. On the evidence your filter actually used, what makes ADGRA3 the reject and BUB1B the diagnosis?"*

The honest answer is that the funnel **cannot** tell them apart — and that is not a flaw, it is the point of the
funnel. The filter is deliberately blind to protein consequence and pathogenicity so it cannot be accused of
circularity. Both genes survive *because* that axis is held out. The exclusion of *ADGRA3* therefore has to be
re-imported from the held-out axis — and until this run, that re-import was asserted. Here it is measured.

---

## Entry 1 — *ADGRA3* legitimately survives the funnel. Confirmed, not disputed.

Both *ADGRA3* variants are clean, rare heterozygous calls, exactly as R21/`AUDIT_06` report. Re-measured from the
primary VCF and live gnomAD r4:

| | chr4:22388312 G>A | chr4:22420767 T>A |
|---|---|---|
| VCF genotype | `0/1`, AD 14,13, DP 27, GQ 99, PASS | `0/1`, AD 25,17, DP 42, GQ 99, PASS |
| gnomAD exome AF | 7.94e-5 | 1.65e-5 |
| gnomAD genome AF | 2.63e-5 | 3.29e-5 |
| max AF < 1e-4 (funnel bar)? | yes | yes |

So the funnel is right to keep *ADGRA3*: two rare, high-quality het calls in one gene. Nothing here overturns the
224→2 reduction. The dispute is entirely about what happens **after** the funnel, on the axis the funnel excludes.

## Entry 2 — On protein consequence, the two genes are not on equal footing. This is the exclusion.

The funnel never looks at *what the variants do to the protein*. When you do — the very step that would make the
funnel circular if it were inside it — *ADGRA3* and *BUB1B* separate cleanly and the separation is not close.

| | allele 1 | allele 2 |
|---|---|---|
| **ADGRA3** | missense **p.Ala1120Val** — REVEL **0.100**, PolyPhen **0.244**, SIFT **0.900 (tolerated)**, CADD 19.8; ClinVar **Uncertain significance** (multi-submitter, no conflicts) | **3′UTR variant** — *not protein-coding*; CADD **0.006**, phyloP **−0.928**, no missense/LoF consequence in any transcript; **not in ClinVar** |
| **BUB1B** | **stop_gained p.Leu737Ter** — CADD 38.0; ClinVar **Pathogenic/Likely pathogenic** (multi-submitter, no conflicts) | missense **p.Asn1002Lys** — REVEL 0.472, PolyPhen **0.997**, SIFT **0.00 (deleterious)**, CADD 26.4 |

The decisive fact is structural, not probabilistic: **a recessive/biallelic disease model needs two damaging
alleles, and *ADGRA3* does not have two.** One of its two hits is a **3′UTR variant** — it changes no amino acid,
scores CADD 0.006 at a base with negative phyloP, and carries no splice or coding consequence in any transcript.
The coding hit is a single missense that three orthogonal predictors call benign/tolerated (REVEL 0.10, PolyPhen
0.24, SIFT 0.90) and ClinVar records as a VUS. *BUB1B*, by contrast, is a nonsense allele that ClinVar already
classifies **Pathogenic/Likely pathogenic** trans to a missense that every predictor calls damaging (SIFT 0,
PolyPhen 0.997). **The exclusion of *ADGRA3* is therefore not "no phenotype link" — it is "no damaging biallelic
genotype exists to link."**

**Disconfirming detail, recorded with equal prominence.** *ADGRA3* allele 1 sits at a base with phyloP **8.80** —
highly conserved. A hostile reviewer can say the benign predictions may be wrong at so conserved a position. Two
things answer this without hand-waving: (a) REVEL (0.10) already integrates conservation and still calls it benign;
(b) it does not matter, because allele 2 is a 3′UTR variant, so **even if allele 1 were fully damaging there is no
second damaging allele to complete a biallelic hit.** The conserved-base caveat is real and is stated; it does not
reopen the rival hypothesis.

## Entry 3 — The disease-association claim, converted from assertion to a ClinVar count.

"No established link to this phenotype" (`R21:45`) is checkable. Measured across every ClinVar submission for each
gene (via the gnomAD gene endpoint, strict Pathogenic/Likely-pathogenic classes only, "Conflicting" excluded):

| Gene | OMIM gene id | ClinVar variants submitted | strictly Pathogenic / Likely-pathogenic |
|---|---|---|---|
| **ADGRA3** | 612303 | 1,120 | **0** |
| **BUB1B** | 602860 | 2,353 | **81** |

Not one of 1,120 submitted *ADGRA3* variants reaches pathogenic; *BUB1B* has 81, and an established recessive
disease (mosaic variegated aneuploidy 1, the diagnosis). R21's asserted "no established link" is now a measured
0-of-1,120. (Scope limit, stated: 0 P/LP in ClinVar is absence of *reported* pathogenicity, not proof the gene can
never cause disease; combined with Entry 2 — no damaging biallelic genotype in this child — it is sufficient to
exclude *ADGRA3* **as this child's diagnosis**, which is the only claim being made.)

## Entry 4 — Bounds what cannot be known. Phase is the one thing that can't decide ADGRA3, and that is why Entry 2 is required.

The genome-wide phase eliminator (`R15`, `R18`) removed 79 of 151 genes by proving both variants sit on one
haplotype. It could not touch *ADGRA3*: both variants are **unphased** (no `PGT`/`PID` in the VCF) and lie
**32,455 bp apart** — far beyond read-backed phasing range at this insert size. So trans vs cis is genuinely
undecided for *ADGRA3*, exactly as `R15` recorded ("no shared phase set → undecided"). This is the reason the
exclusion *must* rest on the consequence/pathogenicity axis of Entries 2–3: for *ADGRA3*, phase — the tool that
disposed of most competitors — is unavailable, and only the measurement of what the alleles do remains.

## Entry 5 — Disconfirming: the axis I expected to separate them (gene constraint) does not.

I predicted loss-of-function constraint would distinguish a real recessive-disease gene from an adhesion-GPCR.
Measured, it does **not**:

| Gene | pLI | LOEUF (oe_lof_upper) | mis_z |
|---|---|---|---|
| ADGRA3 | 7.05e-5 | 0.584 | 1.40 |
| BUB1B | 5.52e-17 | 0.747 | 1.30 |

Both are **loss-of-function tolerant** (pLI ≈ 0, LOEUF > 0.5), and *BUB1B* is if anything the *less* constrained of
the two. Recorded prominently because it is the opposite of what I set out to show, and because the reason is
instructive: pLI/LOEUF measure selection against **heterozygous** LoF, and *BUB1B* disease is **recessive** — het
LoF is tolerated in the population by design, so low pLI is expected and constraint is uninformative for
separating recessive candidates. Anyone reusing this exclusion should not reach for pLI/LOEUF here; the load is
carried by variant-level consequence, in-silico pathogenicity and ClinVar, not by gene constraint.

---

## What this run found, against the prompt's test

The submission's assertion that *ADGRA3* is "a candidate for exclusion, not a rival diagnosis" is **correct, and
now measured rather than assumed.** The unbiased funnel legitimately keeps both genes (Entry 1) because it is
consequence-blind by design; the exclusion of *ADGRA3* is re-imported cleanly from the held-out axis: its two
alleles are a benign-predicted missense VUS and a **3′UTR variant** — not a damaging biallelic genotype (Entry 2) —
in a gene with **0 of 1,120** ClinVar pathogenic submissions (Entry 3), and it is precisely the one funnel survivor
that phase could not eliminate (Entry 4). Two disconfirming results are recorded with equal prominence: gene
constraint does **not** separate the two genes (Entry 5), and *ADGRA3* allele 1 sits at a highly conserved base
(phyloP 8.80) whose benign predictions a reviewer may distrust — neither reopens the rival hypothesis, because the
biallelic-damage model fails on allele 2 regardless.

**No load-bearing conclusion of the submission is overturned; one asserted exclusion is converted into a
measurement and the strongest reviewer objection to the funnel framing is answered before it is raised.** The
transferable point (relevance test #4): an unbiased frequency+quality funnel is *supposed* to output more than the
diagnosis, and the honest way to close it is to state which held-out axis (here: protein consequence + ClinVar, not
gene constraint, not phase) does the final separation — and to show it, not assert it.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | ADGRA3 var1 VCF genotype | 4:22388312 G>A `0/1` AD 14,13 DP 27 GQ 99 PASS, PGT/PID none | `work/track2/audit07_adgra3.py` (pysam `fetch`) |
| 2 | ADGRA3 var2 VCF genotype | 4:22420767 T>A `0/1` AD 25,17 DP 42 GQ 99 PASS, PGT/PID none | same |
| 3 | ADGRA3 inter-variant distance | 32,455 bp, both unphased → trans/cis undecided | same (`22420767−22388312`) |
| 4 | ADGRA3 var1 gnomAD AF | exome 7.94e-5, genome 2.63e-5 (both < 1e-4 funnel bar) | gnomAD r4 `variant(variantId:"4-22388312-G-A")` |
| 5 | ADGRA3 var2 gnomAD AF | exome 1.65e-5, genome 3.29e-5 | gnomAD r4 `variant(variantId:"4-22420767-T-A")` |
| 6 | ADGRA3 var1 consequence + in-silico | **missense p.Ala1120Val**; REVEL 0.100, PolyPhen 0.244, SIFT 0.900, CADD 19.8, phyloP 8.80; ClinVar **VUS** | gnomAD `transcript_consequences`/`in_silico_predictors`/`clinvar_variant` |
| 7 | ADGRA3 var2 consequence + in-silico | **3′UTR variant** (non-coding); CADD 0.006, phyloP −0.928; not in ClinVar | same |
| 8 | BUB1B var1 consequence | **stop_gained p.Leu737Ter**; CADD 38.0; ClinVar **Pathogenic/Likely pathogenic** | gnomAD `variant("15-40209701-T-G")` |
| 9 | BUB1B var2 consequence + in-silico | **missense p.Asn1002Lys**; REVEL 0.472, PolyPhen 0.997, SIFT 0.00, CADD 26.4 | gnomAD `variant("15-40220612-T-G")` |
| 10 | ADGRA3 gene constraint | pLI 7.05e-5, LOEUF 0.584, mis_z 1.40 | gnomAD `gene(gene_symbol:"ADGRA3").gnomad_constraint` |
| 11 | BUB1B gene constraint | pLI 5.52e-17, LOEUF 0.747, mis_z 1.30 (**less** constrained than ADGRA3) | gnomAD `gene(gene_symbol:"BUB1B").gnomad_constraint` |
| 12 | ADGRA3 ClinVar disease burden | **0** strict P/LP of **1,120** submitted variants | gnomAD `gene.clinvar_variants`, strict P/LP filter |
| 13 | BUB1B ClinVar disease burden | **81** strict P/LP of **2,353** submitted variants | same |

All gnomAD queries via `POST https://gnomad.broadinstitute.org/api`, dataset `gnomad_r4` / reference GRCh38.
Every number above is reproduced in one pass by `work/track2/audit07_adgra3.py` (pysam 0.24.0 on `python3.12`).

## Where the next run should start

1. **This run closes the ADGRA3 rival-diagnosis objection with measurement; the reports should now cite it rather
   than assert it.** A run permitted to edit reports (this run only measured) should replace R21:45's "no
   established link to this phenotype … candidate for exclusion" with the measured chain: *ADGRA3*'s two funnel
   survivors are a benign-predicted missense VUS (REVEL 0.10) and a 3′UTR variant (not coding), i.e. no damaging
   biallelic genotype, in a gene with 0/1,120 ClinVar P/LP — and note explicitly that the funnel keeps it because
   the funnel is consequence-blind by design. `SYNTHESIS:58` should point to this file.
2. **The two disconfirmations from `AUDIT_06` (the "224 rare" wording at `SYNTHESIS:67` and the R15 1e-5-survivor
   line) are still un-applied text corrections** — same status as when `AUDIT_06` left them; they need a
   report-editing run, not a new measurement.
3. **`R5`'s 97-gene modifier-enrichment row remains non-reproducible** (the 18-gene cohesion list is in no file
   present — `AUDIT_04`/`AUDIT_05`/`AUDIT_06`). It stays bounded until the list surfaces.
4. **`AUDIT_01` item 3 (STR-aware comparator for the upstream regulatory scan) is still the one untouched
   methodological to-do** across all seven runs.
5. Tooling: `python3.12` (pysam 0.24.0); no `bcftools` on PATH; gnomAD r4 GraphQL reachable by POST but slow enough
   that a 4-retry loop can exceed a 2-minute shell timeout — run heavy gnomAD scripts with a longer timeout.
   `work/track2/audit07_adgra3.py` reproduces every number in this file.
