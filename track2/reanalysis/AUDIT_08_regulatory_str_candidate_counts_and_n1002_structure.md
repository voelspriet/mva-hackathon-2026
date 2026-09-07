# AUDIT 08. The upstream regulatory scan re-done locus-aware, the 314/224/138 candidate counts reconciled, and N1002's exposure measured rather than proxied

**Run 08 of `PROMPT_relevant_additions.md`, 7 September 2026.** Continues `AUDIT_01`–`AUDIT_07`. Before writing I
re-read `R15`, `R21`, `R7`, `SYNTHESIS_for_judging.md`, `archive/creative/D_compute.md` §4, and all seven prior
`AUDIT_NN` files. **Rule 3 credits:** the upstream 60 kb scan (85 variants, 57 het, 2 below 1%) is `Q17`/`R7`'s and
its exact-ID "3 absent STR" caveat is `AUDIT_01` Entry 4's; the candidate-space counts (224, 138, 8→2) are
`R15`/`R21`/`AUDIT_06`'s; the AlphaFold N1002 geometry is `creative D §4`'s; the seven-hit genome-wide ClinVar
screen and the *LZTR1* finding are `R7`'s. This run takes three assertions that no prior run measured and measures
them. **Measure before writing:** every number below comes from the scripts named in the table, run this session.

The three targets, each a load-bearing sentence resting on assertion:

1. *"There is no candidate regulatory allele upstream of *BUB1B* in this child … none is absent from gnomAD."*
   (`REPORT_track2.md:56`) — the closure of the Ochiai-2014 regulatory-allele class. `AUDIT_01` item 3, the one
   methodological to-do untouched across all seven prior runs, asked for an **STR/locus-aware** comparator here.
2. *"Genome-wide, **314 genes** pass the crude recessive-compatible filter."* (`REPORT_track1.md:28`) — a candidate
   count that sits beside **224** (`SYNTHESIS:11`/methods) and **138** (`R15`/`AUDIT_06`) with no statement of how
   the three relate.
3. *"N1002 is predicted partially exposed, **9.14 A** from T1008."* (`REPORT_track2.md:50`, from `creative D §4`) —
   the structural premise for treating allele 2 as a surface/phospho allele rather than a folding-core destabiliser,
   which `creative D` itself flags is a **neighbour-count proxy, not a computed SASA**.

---

## Entry 1 — Closes an alternative explanation, and converts an assertion into a measurement (with a disconfirming method result). The upstream regulatory closure holds under a locus-aware comparator; the "none absent" figure does not survive at the exact-allele level, and exact-ID matching fails in two distinct ways.

The strongest reviewer objection to "the genome was fully searched for a second *BUB1B* allele" is Ochiai 2014
(PMID 24344301): a proven-causal **single-base substitution** 44 kb upstream of the TSS that no coding filter
finds. `Q17`/`R7`/`AUDIT_01` answered it by counting the 60 kb upstream window; `AUDIT_01` Entry 4 then found the
"0 absent from gnomAD" figure is an artefact of position-level matching and that allele-exact matching gives "3
absent, all STR-length polymorphisms." It recommended an STR-aware comparator and nobody built one. This is it.

**Re-derived from the primary VCF** (`work/track2/audit08_regulatory.py`, pysam, contig `15`, window
chr15:40,101,023–40,161,023; the Ochiai position is TSS−44 kb = chr15:40,117,023):

| Quantity | Measured | vs prior |
|---|---|---|
| PASS records in window | **85** | reproduces `Q17`/`AUDIT_01` exactly |
| heterozygous records | **57** | exact |
| ALT alleles (multiallelic sites split) | **90** — 66 SNV, 24 indel/MNV | new decomposition |
| rare (<1%) present in gnomAD | **2**: 40,114,056 A>G (SNV) AF **0.00212**, 2,967 bp distal of the 44 kb point; 40,144,423 AAAG-repeat AF **0.00259**, 27,400 bp away | reproduces `Q17`'s 0.0021 / 0.0026 |

**The locus-aware resolution of "absent."** A naive per-variant `variant()` lookup returned **9** ALT alleles
"absent from gnomAD." Two failure modes, both measured by re-querying each with generous retries and a gnomAD
**region** query at the exact position (`work/track2/audit08_reg_recheck.py`):

- **6 of the 9 are not absent at all — they are common**, and the first-pass null was a per-variant query
  artefact. Re-queried: 40,107,934 C>A **AF 1.00**, 40,136,709 A>C **AF 0.999** (segdup), 40,142,445 A>G AF 0.571,
  40,140,837 G>T AF 0.538, 40,119,937 G>GA AF 0.965 (lcr), 40,157,240 G>A AF 0.062. Five are SNVs; several are
  **reference-minor sites** where the ALT is near-fixed. None is a rare candidate.
- **3 are truly absent as the exact allele — and all 3 are STR-length polymorphisms at loci gnomAD shows are
  common.** 40,106,517 (AC-repeat), 40,120,606 (TATC-repeat), 40,143,237 (AT-repeat) — the identical three
  `AUDIT_01` named. The region query converts `AUDIT_01`'s assertion ("their other allele *is* common in gnomAD")
  into a count: gnomAD carries **79, 14 and 42** distinct variants **at the exact position** of these three loci
  respectively (different repeat lengths). They are absent only as a specific repeat length, not as functional
  candidates.

**The Ochiai class, isolated and measured.** Ochiai's allele is a single-base substitution, so the class that
matters is the 66 SNVs. After proper resolution **0 of 66 upstream SNVs is absent or novel**; the rarest is
40,114,056 A>G at **AF 0.00212** (2,967 bp from the 44 kb point), and the nearest SNV to the 44 kb position itself,
40,116,528 C>T, is **common at AF 0.460** (495 bp away). **There is no rare or novel single-base substitution
anywhere in the 60 kb upstream window.** The regulatory-allele alternative is closed by measurement, not assertion.

**Disconfirming detail, recorded with equal prominence (rule 2).** `REPORT_track2.md:56`'s literal wording — "none
is absent from gnomAD" — is **false at the exact-allele level**: three alleles are absent as written. It is true in
substance: those three are STR-length variants at demonstrably common loci and none is a coding/regulatory
candidate. The honest statement is `AUDIT_01`'s: *"3 alleles are absent only as exact STR-length representations at
loci that are common in gnomAD; 0 single-base substitutions are absent or rare-and-novel."* This run adds a second
lesson `AUDIT_01` did not reach: **a per-variant gnomAD lookup also produces false absences on common
reference-minor SNVs** (here 5, up to AF 1.00). Anyone reusing this scan needs the region/locus query for both
reasons — STR representation and per-variant nulls — not exact-ID matching. The load-bearing conclusion is
unchanged; the method behind the "0 absent" number is what needed fixing.

## Entry 2 — Converts an assertion into a measurement, and closes a numeric ambiguity. The submission's three candidate-space counts — 314, 224, 138 — are one file under three stated filters, and all three reproduce exactly.

`REPORT_track1.md:28` reports **314** genes passing the "crude recessive-compatible filter"; `SYNTHESIS:11` and the
methods form use **224**; `R15`/`AUDIT_06` use **138** (compound-het het grouping). Three numbers, no stated
relation — the kind of gap a hostile reviewer reads as inconsistency. `REPORT_track1.md:12` defines the model-1
filter verbatim: *"PASS variants overlapping any Ensembl CDS, not flagged as dbSNP by the caller, GQ ≥ 50, DP ≥ 10,
grouped per gene; genes with two or more heterozygous or one homozygous variant."* Applied to
`work/coding_nodbsnp.gene.vcf.gz` (the "coding, non-dbSNP" set; 1,694 rows, 704 genes, 29 duplicate rows;
`work/track2/audit08_gene_counts.py`):

| Submission number | Filter that produces it | Measured | Match |
|---|---|---|---|
| **314** (`REPORT_track1:28`) | GQ≥50, DP≥10; **≥2 het OR ≥1 hom**; raw rows | **314** | exact |
| **224** (`SYNTHESIS:11`, methods, OBS) | unfiltered; **≥2 any zygosity**; raw rows | **224** | exact |
| **138** (`R15`, `AUDIT_06`) | **≥2 het**; distinct variants (dedup) | **138** | exact |

*BUB1B* is in the recessive-compatible set with exactly its two het variants, under every definition. The three
numbers are **not inconsistent** — they are the same file read at three altitudes. Two measured points worth
carrying:

- **The 314 is dominated by the single-homozygous clause.** Within the 314: 189 genes carry ≥1 homozygous
  non-dbSNP coding variant (overwhelmingly reference-minor / common homozygous sites) and 151 carry ≥2 het (raw),
  with 26 satisfying both — so **163 of the 314 enter on the ≥1-hom clause alone**, genes the compound-het rule
  would never list. The compound-heterozygote field proper is the 138 (deduped) that `R15` funnels. So
  `REPORT_track1:28`'s own characterisation ("dominated by polymorphic and multi-copy loci") is quantitatively
  right: most of the 314 is not a compound-het candidate at all.
- **Dedup changes the het count by 13** (raw 151 → distinct 138), because 29 rows in the file are duplicate
  chr:pos:ref:alt (multiallelic splits / multi-gene annotations). `R15`'s 138 is the deduped count;
  `AUDIT_06`'s 218 for "≥2 any zygosity" is the distinct-variant analogue of the raw 224 (my dedup gives 209; the
  residual is AF-map-merge convention). The lesson for reuse: **state whether the count is raw-row or
  distinct-variant** — the two differ by ~6–13 genes and the submission uses both without saying which.

## Entry 3 — Converts an assertion (a proxy) into a measurement. N1002's "partial exposure" and its 9.14 Å distance to T1008 reproduce exactly, and the exposure is now a computed SASA rather than a neighbour count.

`REPORT_track2.md:50` states N1002 is "partially exposed, 9.14 A from T1008," sourced to `creative D §4`, which
adds pLDDT 91.1, 16 CB neighbours within 10 Å (a proxy for exposure), and 10.35 Å to L1012 — and states plainly
that burial "is a proxy for solvent accessibility, **not a computed SASA**." This entry reproduces the geometry
independently from the model and replaces the proxy with a real Shrake–Rupley SASA
(`work/track2/audit08_structure.py`, Biopython on AF-O60566-F1 v6):

| Quantity | `creative D §4` | Reproduced | Match |
|---|---|---|---|
| residue identities 1002 / 1008 / 1012 | Asn / Thr / Leu | **ASN / THR / LEU** | exact (confirms p.Asn1002Lys, T1008 phosphosite, L1012) |
| pLDDT at 1002 | 91.1 | **91.1** | exact |
| min heavy-atom N1002→T1008 | 9.14 Å | **9.14 Å** | exact |
| min heavy-atom N1002→L1012 | 10.35 Å | **10.35 Å** | exact |
| CB neighbours ≤10 Å: 1002 / 1012 | 16 / 26 | **16 / 26** | exact |

**The improvement — computed relative solvent accessibility (RSA = SASA / Tien-2013 max ASA):**

| Residue | SASA (Å²) | RSA | reading |
|---|---|---|---|
| **ASN1002** | 31.5 | **0.162** | **partially exposed** |
| THR1008 | 10.1 | 0.059 | buried |
| **LEU1012** | 0.0 | **0.000** | **fully buried** |

The computed SASA **confirms** the report's proxy-based call: N1002 is partially exposed (RSA 0.16) while L1012 —
the reference MVA destabilising allele — is fully buried (RSA 0.00). The mechanistic separation the report draws
between N1002K and L1012P ("unlikely to act by the same mechanism," so the mouse L1002P/human-L1012P data should
not transfer) now rests on a measured accessibility, not a neighbour count. **Two caveats, stated because they
bound the reading (rule 3):** (i) whole-chain pLDDT is 63.6 with long low-confidence stretches, so global SASA on
this monomer is soft — but residue 1002's own pLDDT is 91.1 and its neighbourhood is confident, so its local RSA is
trustworthy; (ii) T1008 computes as **buried** (RSA 0.06) in the apo monomer, and phosphosites are commonly exposed
only on activation/partner binding, so the 9.14 Å distance is a static-monomer geometry, not evidence of a
functional N1002–T1008 contact. Neither caveat touches the load-bearing point (N1002 partially exposed, L1012
buried); both should travel with any reuse.

## Adjunct (building on `R7`, not new). The secondary-findings negative confirmed by the stronger genome-wide route.

`REPORT_track1.md:45` reports no ClinVar P/LP variant among the 81 ACMG SF v3.2 genes. `R7`'s genome-wide ClinVar
screen (no gene list) found the child's **complete** set of unconflicted P/LP hits: **7 genes** (RBM8A, FLG,
GNRHR, PRSS1, HK1, BUB1B, LZTR1). Intersecting those 7 with the pipeline's 81-gene ACMG SF list
(`pipeline/acmg_sf32_genes.txt`) gives **0 overlap**, so the ACMG-SF secondary-findings negative holds under a
screen that is genome-wide rather than panel-bounded — a strictly stronger statement than the report's own.
`R7` already characterised the one P/LP hit outside the panel (*LZTR1*, a dominant tumour-predisposition gene) and
declined to carry it into any recommendation; nothing here changes that, and the point is only that the negative is
independently confirmed by the broader method.

---

## What this run found, against the prompt's test

- **Entry 1 (closes an alternative + converts an assertion; disconfirming method result):** the "no upstream
  regulatory allele" closure **holds** under a locus-aware comparator — 0 of 66 upstream SNVs (the Ochiai class) is
  rare-and-novel, the rarest is AF 0.0021 nearly 3 kb from the 44 kb point, and the only 3 truly-absent alleles are
  STR-length polymorphisms at loci carrying 79/14/42 gnomAD variants each. But `REPORT_track2:56`'s literal "none
  absent" is false at the exact-allele level, and the audit shows **exact-ID matching fails in two ways** (STR
  representation *and* false nulls on common reference-minor SNVs), which is the STR-aware comparator `AUDIT_01`
  asked for across seven runs, now built and run.
- **Entry 2 (converts an assertion; closes a numeric ambiguity):** the submission's three candidate counts —
  **314, 224, 138** — all reproduce **exactly** from one file under three stated filters, so they are not
  inconsistent; and 189 of the 314 enter via the single-homozygous clause, confirming most of the 314 is not a
  compound-het candidate.
- **Entry 3 (converts a proxy into a measurement):** N1002's geometry reproduces to the digit (9.14 Å, pLDDT 91.1,
  16/26 neighbours), and its "partial exposure" is now a **computed SASA** (RSA 0.162 vs L1012's 0.000), so the
  N1002K≠L1012P mechanistic separation rests on measured accessibility.

**No load-bearing conclusion of the submission is overturned.** The regulatory closure, the candidate funnel and
the allele-2 structural interpretation all survive measurement. Two disconfirming method results are recorded with
equal prominence: the upstream "none absent" figure is a matching artefact (true in substance, false as written),
and the candidate-count "inconsistency" dissolves once each number's filter is stated. The transferable points
(relevance test #4): (a) an upstream/non-coding rarity screen must compare **locus-aware**, not by exact variant
ID, or it will both miss common STR loci and invent absences at reference-minor SNVs; (b) any candidate-space count
must declare its filter altitude and raw-vs-distinct convention; (c) a solvent-accessibility claim from an
AlphaFold monomer is cheap to compute properly and should be, not proxied by neighbour count.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | upstream window PASS / het records | **85 / 57** (reproduces Q17/AUDIT_01) | `work/track2/audit08_regulatory.py` (pysam, chr15:40,101,023–40,161,023) |
| 2 | ALT alleles by class | 90 total: **66 SNV, 24 indel/MNV** | same |
| 3 | rare (<1%) present in gnomAD | **2**: 40,114,056 A>G AF 0.00212; 40,144,423 AAAG-rep AF 0.00259 | same + gnomAD `variant()` r4 |
| 4 | exact-ID "absent" (first pass) → resolved | 9 → **3 truly absent, all STR** (40,106,517 / 40,120,606 / 40,143,237); other 6 present & common (AF 0.062–1.00) | `work/track2/audit08_reg_recheck.py` (gnomAD `variant()`, 8 retries) |
| 5 | STR loci polymorphism at exact pos | gnomAD variants at the 3 absent positions: **79 / 14 / 42** | `audit08_regulatory.py` gnomAD `region()` |
| 6 | Ochiai class (SNV) rare/absent | **0 of 66** absent; rarest SNV AF 0.00212; nearest SNV to 44 kb pos (40,116,528 C>T) AF **0.460**, 495 bp | `audit08_regulatory.py` |
| 7 | 314-gene recessive filter | **314** = GQ≥50,DP≥10; ≥2 het OR ≥1 hom; raw (reproduces REPORT_track1:28) | `work/track2/audit08_gene_counts.py` |
| 8 | 224 / 138 candidate counts | **224** = unfiltered ≥2 any-zyg (raw); **138** = ≥2 het (distinct) — both exact | same |
| 9 | 314 decomposition | 189 carry ≥1 hom, 151 carry ≥2 het (raw), 26 both → **163 hom-only**; *BUB1B* present (2 het) | same |
| 10 | AF-O60566 v6 residues / pLDDT | 1002 ASN / 1008 THR / 1012 LEU; pLDDT(1002)=**91.1** | `work/track2/audit08_structure.py` (Biopython) |
| 11 | N1002 min heavy-atom distances | →T1008 **9.14 Å**, →L1012 **10.35 Å**; CB neighbours ≤10 Å 16 / 26 (all reproduce creative D §4) | same |
| 12 | **computed** SASA (Shrake–Rupley) | ASN1002 RSA **0.162** (partially exposed); THR1008 0.059; LEU1012 **0.000** (buried) | same |
| 13 | ACMG SF genome-wide confirmation | **0 of 7** genome-wide P/LP hit genes in the 81 ACMG SF genes | inline (clinvar_gw hits ∩ acmg_sf32_genes.txt) |

All gnomAD queries via `POST https://gnomad.broadinstitute.org/api`, dataset `gnomad_r4`, reference GRCh38.
AlphaFold model AF-O60566-F1 v6 from EBI. Tooling: `python3.12`, pysam 0.24.0, Biopython (pip-installed this run).

## Where the next run should start

1. **`AUDIT_01` item 3 is now discharged** — the upstream scan has a locus-aware comparator, and the finding is
   that the closure holds while the "none absent" wording needs the two-line correction in Entry 1's disconfirming
   paragraph. A report-editing run (this one only measured) should replace `REPORT_track2:56`'s "none is absent
   from gnomAD" with "3 alleles absent only as STR-length representations at loci common in gnomAD; 0 single-base
   substitutions absent or rare-and-novel."
2. **The candidate-count reconciliation (Entry 2) should be folded into the text once, not left as three bare
   numbers.** A report-editing run can state at each site which filter produces 314 vs 224 vs 138; the mapping in
   Entry 2 is sufficient to do it without recomputing.
3. **The un-applied text corrections from `AUDIT_06`/`AUDIT_07` remain** (the "224 rare" wording at
   `SYNTHESIS:67`, the `R15` 1e-5-survivor line, and the `R21:45` ADGRA3 exclusion) — all need a report-editing
   run, not new measurement.
4. **`R5`'s 97-gene modifier-enrichment row is still not re-derivable** (the 18-gene cohesion list is in no file
   present — `AUDIT_04`/`05`/`06`). It stays bounded until the list surfaces.
5. Tooling for whoever runs next: `python3.12` (pysam 0.24.0, Biopython now installed); egress wide (gnomAD r4,
   AlphaFold/EBI, PyPI); gnomAD per-variant `variant()` lookups can return transient nulls — use the `region()`
   endpoint or ≥8 retries for any absence claim (Entry 1). `work/track2/audit08_*.py` reproduce every number here.
