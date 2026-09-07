# AUDIT 10. The ACMG secondary-findings screen reproduced end-to-end against live ClinVar, the two BUB1B allele counts re-fetched digit-for-digit from gnomAD v4.1 (with one ancestry-attribution overstatement corrected), and the RBM8A TAR-allele frequency behind the "NMD-normal" inference measured

**Run 10 of `PROMPT_relevant_additions.md`, 7 September 2026.** Continues `AUDIT_01`–`AUDIT_09`. Before writing I
re-read `AUDIT_09`'s "Where the next run should start", `R7`, `R9`, `R18`, and `SYNTHESIS_for_judging.md`, and confirmed
each target below was *named as measurable but not measured* by a prior file. This run takes **three load-bearing claims
that no prior run reduced to a fresh measurement** and measures them, each against a live source (the proband VCF, the
current NCBI ClinVar GRCh38 VCF read by remote tabix, and the gnomAD v4.1 public GraphQL API). **Measure before writing:**
every number below comes from the scripts named in the table, run this session.

**Rule 3 credits (what is *not* new here).** That the patient carries no reportable ACMG secondary finding, and that
the genome-wide P/LP set is 7 variants none of which sits in an ACMG SF gene, is `R7`'s (and `AUDIT_08` cross-checked it);
this run does not re-derive that genome-wide screen, it independently reproduces the *ACMG-gene* screen the report
actually submitted. That allele 2 is a gnomAD singleton and that both causal alleles are Non-Finnish-European–dominant is
`R9`'s; this run re-fetches the raw counts `R9` built on (which `R9` did not itself re-derive — it took them from the
Track-1 table and re-expressed them in the NFE denominator) and, doing so, finds one small overstatement in `R9`'s
ancestry sentence. The 288 bp phase span, the NMD geometry, and the three-gene callability are `AUDIT_09`'s and untouched.

The three targets, each a load-bearing sentence resting on assertion in this repository:

1. *"The 81 ACMG SF v3.2 genes contain **10,895 PASS variants**. None is ClinVar pathogenic or likely pathogenic. Nine
   carry conflicting classifications (**one homozygous, eight heterozygous**)."* (`REPORT_track1.md:46`) — the entire
   basis for submitting **no** `secondary` rows. The count and the 9-way split were asserted from a pipeline run
   (`pipeline/run.sh` steps, `acmg.clinvar.vcf.gz`) whose intermediate files are not in the repository; no audit had
   re-derived them, and `AUDIT_09` flagged the count as un-reproduced.
2. *"gnomAD v4.1 exomes **115/1,461,846** (7.9e-5), genomes **5/152,174**, 0 homozygotes"* (allele 1) and *"exomes
   **1/1,461,878** (6.8e-7), genomes absent, 0 homozygotes"* (allele 2) (`REPORT_track1.md:23–24`). `R9:9` calls the
   singleton status of allele 2 *"the single most load-bearing claim in the whole project."* Those exact counts were
   **cited from the report table, never re-fetched** in any `R`/`AUDIT` file.
3. *"The child carries rs139428292, the TAR-syndrome 5′UTR hypomorphic allele of RBM8A … in the heterozygous state. The
   rare-variant screen did not return it because at **2.6 percent** it is not rare … gnomAD v4.1 records **583
   homozygotes** for this allele with no reported decay phenotype"* (`REPORT_track2.md:38`). This is the population-
   frequency evidence on which the report's "NMD efficiency assumed normal" inference explicitly rests; the 2.6 % and the
   583 homozygotes were stated, not measured here.

---

## Entry 1 — Converts an assertion into a measurement. The ACMG SF v3.2 secondary-findings screen reproduces end-to-end against a *live* ClinVar pulled two days after the report's build: 10,895 PASS variants in the 81 genes, **0** pathogenic/likely-pathogenic, **9** conflicting split exactly 1 homozygous + 8 heterozygous, and the 9 genes match the submitted table one-for-one.

The load-bearing output of Track-1 section 5 is a **negative**: no ACMG SF secondary finding is reportable, so no
`secondary` row is submitted. That negative is only as good as (a) the gene set actually screened, (b) the completeness
of the variant set inside it, and (c) the ClinVar annotation applied. I reproduced all three from scratch.

**Gene spans (`work/track2/audit10_acmg_spans.py`).** The 81 ACMG SF v3.2 symbols in `pipeline/acmg_sf32_genes.txt` were
resolved to GRCh38 coordinates by a single batched Ensembl REST POST (`/lookup/symbol/homo_sapiens`), the server
reporting release **116** and assembly **GRCh38** — **all 81 located, none missing** (`work/track2/audit10_acmg.bed`).

**Variant count (`work/track2/audit10_acmg_count.py`, pysam over the proband VCF).**

| Quantity | Measured |
|---|---|
| ACMG SF genes resolved on Ensembl 116 | **81 / 81** |
| PASS variants overlapping the 81 gene spans | **10,895** — reproduces `REPORT_track1:46` **exactly** |
| all-filter records overlapping | 10,998 (103 non-PASS) |
| largest single gene | RYR2 (1,902), then KCNQ1 720, PRKAG2 692, TRDN 636, RBM20 451 |

**ClinVar annotation against the live database (`work/track2/audit10_acmg_clinvar.py`).** Rather than trust a cached
annotation, I opened the current NCBI ClinVar GRCh38 VCF *remotely* by tabix
(`https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz`, fetched 7 Sep 2026 — two days after the report's
5 Sep 2026 ClinVar), queried only the 81 ACMG regions, and required an **exact position+ref+alt match** to the patient's
PASS variants:

| ClinVar class among patient PASS variants in the 81 genes | Measured |
|---|---|
| **Pathogenic / Likely-pathogenic (non-conflicting)** | **0** — reproduces the reportable-secondary-finding negative |
| **Conflicting classifications** | **9** — split **1 homozygous + 8 heterozygous** (reproduces `REPORT_track1:46` exactly) |
| Benign / Likely-benign | 1,680 |
| Other (VUS / risk-factor / drug-response / etc.) | 135 |

The 9 conflicting variants, by gene and genotype: **PCSK9 1/1** (the single homozygote), and heterozygous **ATP7B, DSP,
HNF1A ×2, SDHD, TRDN, TTN ×2**. This set matches `figures/acmg_conflicting_only.tsv` **gene-for-gene and genotype-for-
genotype** (that file lists the same nine: ATP7B, DSP, HNF1A×2, PCSK9 1/1, SDHD, TRDN, TTN×2). So the submission's
"nine carry conflicting classifications (one homozygous, eight heterozygous)" is now an independently reproduced
measurement against live ClinVar, not a pipeline artefact taken on trust. **The negative holds:** zero ACMG SF genes carry
a P/LP variant in this child, so "no secondary rows submitted" is correct. Bound (rule 3): this is ClinVar-classification-
based, exactly as ACMG SF reporting requires; a novel truncating variant in an ACMG gene with *no* ClinVar record would be
invisible to this screen, which is a property of the reporting standard, not of this analysis.

## Entry 2 — Converts an assertion into a measurement, and corrects one overstatement. The two BUB1B allele counts re-fetch digit-for-digit from the gnomAD v4.1 API, confirming allele 2 is a genome-wide singleton; but the ancestry attribution in R9 ("all 117 copies are Non-Finnish European") is imprecise — 4 of allele 1's 115 exome copies sit in gnomAD's unassigned "remaining" bin, so it is 117 of **121** copies NFE, the other 4 unassigned. The rarity conclusion is unchanged.

`R9:9` names the singleton status of allele 2 the single most load-bearing claim in the project, yet the raw gnomAD
counts underneath it had only ever been *cited* (`REPORT_track1:23–24`), never re-fetched in an audit. I queried the
gnomAD v4.1 GraphQL API directly (`work/track2/audit10_gnomad.py`, 12-try backoff for the transient "Service overloaded"
responses):

| Variant | Field | `REPORT_track1` | gnomAD v4.1 API (this run) | Match |
|---|---|---|---|---|
| allele 1 p.Leu737Ter (15-40209701-T-G, rs759242053) | exome AC/AN | 115 / 1,461,846 (7.9e-5) | **115 / 1,461,846** (7.867e-5), hom **0** | exact |
| | genome AC/AN | 5 / 152,174, 0 hom | **5 / 152,174**, hom **0** | exact |
| allele 2 p.Asn1002Lys (15-40220612-T-G, no rsid) | exome AC/AN | 1 / 1,461,878 (6.8e-7) | **1 / 1,461,878** (6.841e-7), hom **0** | exact |
| | genome | absent | **null (absent)** | exact |
| allele 2 | NFE exome | 8.99e-07 (`REPORT_track2:50`) | AC 1 / AN 1,112,006 = **8.993e-7** | exact |

So **allele 2 is a single heterozygous copy in 1,461,878 sampled exome alleles and absent from 152k genomes** — the
singleton status is a reproduced measurement, and it is that single copy which sits in NFE (8.99e-7), exactly as
`REPORT_track2:50` states. The patient's own calls also match the report table to the read: allele 1 GT 0/1 AD 21,25 DP 46
GQ 99 PASS; allele 2 GT 0/1 AD 15,13 DP 28 GQ 99 PASS (`work/track2/audit10_gnomad.py` VCF read).

**The disconfirming refinement, recorded with rule-2 prominence.** `R9:62` states: *"All 117 observed copies of both
causal alleles … are Non-Finnish European. Neither allele has ever been seen in any other gnomAD population."* The gnomAD
per-population breakdown for allele 1 exome is **nfe = 111, remaining = 4** (the "remaining" group is gnomAD v4's residual
category for samples whose genetic ancestry did not cluster with a labelled group). `R9`'s table lists only the seven
*named* continental groups (afr/amr/asj/eas/fin/nfe/sas) and so summed 111 + 5 + 1 = **117, all NFE**; it dropped the
"remaining" bin. The complete accounting is:

| | exome | genome | total |
|---|---|---|---|
| allele 1 total copies | 115 | 5 | 120 |
| allele 2 total copies | 1 | 0 | 1 |
| **grand total copies** | | | **121** |
| of which NFE | 111 + 1 = 112 | 5 | **117** |
| of which "remaining" (unassigned) | 4 | 0 | **4** |

So the precise statement is **117 of 121 copies are NFE; the other 4 (all allele 1, all exome) are in gnomAD's unassigned
"remaining" group, none in afr/amr/asj/eas/fin/sas.** `R9`'s narrower claim — "never seen in any other *named* population"
— survives; its stronger claim "all 117 copies are NFE" slightly overstates, because it omitted the 4 unassigned copies
and undercounted the total by 4. **This does not touch any conclusion:** 4 residual-bin copies across 1.46 million alleles
leave allele 1 rare and NFE-dominant and leave allele 2 a singleton. It is recorded because rule 2 requires a measurement
that corrects a claim to be as prominent as one that confirms it, and because the number a reader would reproduce from
the API (121 copies, 4 unassigned) is not the number `R9` printed (117, all NFE).

## Entry 3 — Converts an assertion into a measurement. The RBM8A TAR-syndrome hypomorph is heterozygous in this child (PASS) and carries a gnomAD v4.1 exome frequency of 2.60 % with 583 homozygotes — the population evidence the report's "NMD-efficiency-normal" inference explicitly rests on, now measured rather than stated.

`REPORT_track2:38` builds two load-bearing steps on rs139428292: (i) it is *not* returned by the rare-variant screen
"because at 2.6 percent it is not rare", and (ii) NMD efficiency is "assumed normal … because gnomAD v4.1 records 583
homozygotes for this allele with no reported decay phenotype." Both rest on the frequency and the homozygote count, which
were asserted. Measured:

| Quantity | `REPORT_track2:38` | Measured (this run) | Source |
|---|---|---|---|
| patient genotype at chr1:145,927,447 C>T | heterozygous | **GT 0/1, AD 17,19, DP 36, GQ 99, PASS** | proband VCF (`work/track2/audit10_gnomad.py`) |
| rsID | rs139428292 | **rs139428292** | gnomAD API rsids |
| gnomAD v4.1 exome AF | "2.6 percent" | **2.602 % (AC 37,795 / AN 1,452,720)** | gnomAD API |
| gnomAD v4.1 exome homozygotes | 583 | **583** | gnomAD API |
| gnomAD v4.1 genome AF / hom (not quoted by report) | — | 1.844 % (2,808/152,246), 33 hom | gnomAD API |
| NFE exome AF (`R9` table gave 0.0302) | 0.0302 | **3.024 % (33,504/1,107,788)** | gnomAD API |

Both load-bearing numbers reproduce **exactly**: the 2.6 % that explains why the rare-variant filter (rare = below its
frequency threshold) skips this allele, and the **583 homozygotes** that are the sole stated basis for treating the
allele's effect on NMD as tolerated in the population. The report is careful to mark step (ii) as *"an inference from
population frequency, not a functional measurement, and is marked as such"* — this run does not upgrade that inference, it
verifies its input. The child is a **heterozygous carrier** (confirmed 0/1, PASS, balanced 17/19 read support), consistent
with the report's statement that no 1q21.1 deletion sits in trans (that trans-deletion check is `R7`'s and untouched here).

---

## What this run found, against the prompt's test

- **Entry 1 (converts an assertion):** the ACMG SF v3.2 secondary-findings screen reproduces end-to-end — **10,895** PASS
  variants across all **81** genes, **0** P/LP, **9** conflicting split exactly **1 homozygous + 8 heterozygous**, the nine
  genes matching `figures/acmg_conflicting_only.tsv` one-for-one — verified against a **live ClinVar pulled two days after
  the report's build**. The "no reportable secondary findings" negative is now an independent measurement.
- **Entry 2 (converts an assertion + one correction):** the two BUB1B allele counts re-fetch **digit-for-digit** from
  gnomAD v4.1 (allele 1 = 115/1,461,846 exome + 5/152,174 genome, 0 hom; allele 2 = 1/1,461,878 exome singleton, genomes
  absent, 0 hom), confirming allele 2's singleton status. **Disconfirming refinement:** allele 1's 115 exome copies are
  111 NFE + **4 "remaining"** (unassigned), so `R9`'s "all 117 copies are NFE" is precisely **117 of 121 NFE + 4
  unassigned**; the rarity/NFE-dominance conclusion is unchanged.
- **Entry 3 (converts an assertion):** the RBM8A TAR hypomorph rs139428292 is **heterozygous** in this child (0/1, PASS)
  and carries a gnomAD v4.1 exome frequency of **2.60 %** with **583 homozygotes**, exactly as the report states — the
  measured population evidence under the "NMD-efficiency-normal" inference and under "not rare, so the screen skips it."

**No load-bearing conclusion of the submission is overturned; three are converted from assertion to measurement, and one
subordinate ancestry sentence in `R9` is corrected.** The one disconfirming note, recorded with equal prominence (rule 2):
gnomAD's allele-1 exome breakdown carries 4 copies in the "remaining" (unassigned-ancestry) bin that `R9`'s seven-column
table dropped, so the correct copy accounting is 121 total / 117 NFE / 4 unassigned, not 117 all-NFE. Transferable points
(relevance test #4): (a) an ACMG SF screen's negative can be reproduced without a local ClinVar mirror by remote-tabix
querying the NCBI ClinVar VCF over the 81 gene regions only — cheap, and it dates the ClinVar build automatically; (b) a
frequency table lifted from a report should be re-fetched from the API before it is re-expressed in a new denominator,
because the API also returns the "remaining"/unassigned bin that a seven-population table silently drops; (c) an inference
flagged as "population-frequency, not functional" (here NMD normality) is still worth grounding by verifying the exact
homozygote count it names — 583 here, reproduced.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | ACMG SF v3.2 genes located on Ensembl 116 | **81 / 81**, GRCh38 | `work/track2/audit10_acmg_spans.py` (Ensembl REST POST) → `work/track2/audit10_acmg.bed` |
| 2 | PASS variants in the 81 ACMG spans | **10,895** (reproduces `REPORT_track1:46`) | `work/track2/audit10_acmg_count.py` (pysam) |
| 3 | patient PASS variants in ACMG genes that are ClinVar P/LP (non-conflicting) | **0** | `work/track2/audit10_acmg_clinvar.py` (remote tabix, live NCBI ClinVar, exact pos+ref+alt) |
| 4 | patient PASS variants in ACMG genes that are ClinVar Conflicting | **9** = 1 hom (PCSK9) + 8 het (ATP7B, DSP, HNF1A×2, SDHD, TRDN, TTN×2) | same — matches `figures/acmg_conflicting_only.tsv` |
| 5 | allele 1 gnomAD v4.1 exome / genome | **115/1,461,846 (7.867e-5), 0 hom; 5/152,174, 0 hom** | `work/track2/audit10_gnomad.py` (gnomAD GraphQL) |
| 6 | allele 2 gnomAD v4.1 exome / genome | **1/1,461,878 (6.841e-7) singleton, 0 hom; genome absent** | same |
| 7 | allele 1 exome ancestry breakdown | **nfe 111 + remaining 4** (= 115); genome nfe 5 | same |
| 8 | total causal-allele copies / NFE / unassigned | **121 / 117 / 4** (corrects `R9:62` "117 all NFE") | same |
| 9 | patient RBM8A rs139428292 genotype | **0/1, AD 17,19, DP 36, GQ 99, PASS** | same (proband VCF read) |
| 10 | RBM8A rs139428292 gnomAD v4.1 exome AF / homozygotes | **2.602 % (37,795/1,452,720) / 583 hom** (reproduces `REPORT_track2:38`) | same |
| 11 | patient allele 1 / allele 2 calls | **0/1 21,25 DP46; 0/1 15,13 DP28** (match `REPORT_track1:23–24`) | same |

All scripts are in `work/track2/audit10_*.py`. VCF = `data/WGS_EX2312012_HGWCNDSX7.vcf.gz`; ACMG list =
`pipeline/acmg_sf32_genes.txt`; ClinVar = live NCBI GRCh38 VCF over remote tabix (fetched 7 Sep 2026); gnomAD = v4.1 via
`https://gnomad.broadinstitute.org/api`; gene spans = Ensembl REST release 116. Tooling: `python3.12`, pysam 0.24.0.
**bcftools/mosdepth still not on PATH** (as `AUDIT_09` noted); pysam was used throughout. The gnomAD API returns transient
"Service overloaded" — the fetcher retries with backoff (12 tries) and every reported number came from a successful,
error-free response.

## Where the next run should start

1. **Report-editing items remain open** (still pure text edits, not measurement, carried from `AUDIT_08`/`AUDIT_09`): the
   `REPORT_track2:56` STR-wording, the 314/224/138 candidate-count altitudes, and the un-applied `AUDIT_06`/`AUDIT_07`
   corrections. A report-editing run should now **also**: (a) cite `AUDIT_09` for the 288 bp phase span (not `R1`); (b)
   correct `R9:62` to "117 of 121 copies NFE, 4 in gnomAD's unassigned 'remaining' bin" per Entry 2 here; (c) note the
   ACMG screen was independently reproduced against live ClinVar (Entry 1). These are edits, not new measurements.
2. **`R5`'s 97-gene / 18-gene cohesion-set modifier-enrichment row is still not re-derivable** (list absent from the
   repository — `AUDIT_04/05/06/08`). Bounded until the list surfaces.
3. **Remaining unmeasured load-bearing claims, in descending measurability:**
   - **The "18 remaining calls" in the three MVA genes** (`REPORT_track1:26`: besides the 2 reported, 18 intronic/UTR, "all
     common dbSNP except one deep-intronic BUB1B variant absent from gnomAD ~1 kb from the nearest exon"). Fully measurable
     from the VCF + gnomAD API (count and classify the non-coding calls in BUB1B/CEP57/TRIP13, confirm the deep-intronic
     one's gnomAD absence and exon distance). `AUDIT_02` covered the splice prediction for that one variant but the **count
     of 18 and the "all common except one" claim** were not enumerated. Good next target.
   - **The mosaic-aneuploidy detection floor** (`REPORT_track1:42`: 95th-percentile bin excess 0.032 on chr1–6, f≈0.14/bin,
     per-chromosome floor <0.10; vs `R6`'s "11.7 % per bin genome-wide"). The two floor figures (10 % vs 11.7 %) are not
     obviously the same number and deserve reconciliation; reproducible from `pipeline/mosaic_baf.py` + `f_math.py` on the
     VCF's het-SNV BAFs. Heaviest of the three but the most load-bearing (it is the MVA-defining negative for Track 1).
   - **The drugmap counts** (`REPORT_track2:100`: 110 targets, 148 molecules, 29 approved-passed) — reproducible only
     against live Open Targets/ChEMBL/openFDA, which drift; any re-run must report the query date. Lower priority.
   - **The Exomiser model-2 ranking** (`REPORT_track1:38`) remains **bounded by tooling** (37 GB bundle); attempt only if
     that bundle is fetchable.
4. Tooling unchanged from `AUDIT_09`: `python3.12` + pysam 0.24.0, samtools, minimap2 present; **no bcftools/mosdepth on
   PATH**; Ensembl REST pins release 116; egress wide (gnomAD r4 GraphQL, Ensembl REST, **NCBI ClinVar VCF is
   remote-tabix-able** — new this run, useful for whoever tackles item 3's non-coding enumeration). `work/track2/audit10_*.py`
   reproduce every number here; `work/track2/audit10_gnomad_out.json` holds the raw gnomAD responses.
