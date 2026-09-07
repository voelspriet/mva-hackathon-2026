# AUDIT 01. The allele-1 / NMD-normal assumption chain, re-derived from primary data

**Run 01 of `PROMPT_relevant_additions.md`, 7 September 2026.** No prior `AUDIT_NN` file existed, so this
begins at step 1. Before writing anything I read `R15`–`R21` and `SYNTHESIS_for_judging.md`; the compound-het
candidate space (224→2), the mosaicism floor, the SMN resolution and the gene-label test are already done there
and are not re-opened here.

This run takes a single load-bearing sentence in `REPORT_track2.md` §2 and audits the chain of facts under it:

> "NMD efficiency is still assumed normal ... That step is an inference from population frequency, not a
> functional measurement, and is marked as such." (`REPORT_track2.md:38`)

That inference is what lets the report say "for allele 1 the therapeutic object is the transcript, not the
fold" (`REPORT_track2.md:48`). If NMD were *not* efficient in this child, the mutant p.Leu737Ter transcript
would survive, a truncated protein could be made, and the whole allele-1 argument — and every NMD-inhibitor and
readthrough hypothesis it gates — would change. The report rests the NMD-normal call on five sub-facts, four of
which are measurable from data in hand. It attributes them to summary files (`creative D §6`, `Q17`) rather than
to the primary VCF. **Measure before writing:** every number below was recomputed from
`data/WGS_EX2312012_HGWCNDSX7.vcf.gz` and the live gnomAD v4.1 API, not read from those summaries.

Tooling note for reproduction: `bcftools` is not on `PATH` on this server; `python3` is 3.10 without pysam.
Use `python3.12`, which has `pysam 0.24.0`. The VCF uses contig names `1..22,X,Y` (no `chr`);
`work/depth.regions.bed.gz` uses `chr1..`.

---

## Entry 1 — Converts an assertion into a measurement. The RBM8A carrier claim is exactly right.

`REPORT_track2.md:38` states the child "carries rs139428292, the TAR-syndrome 5' UTR hypomorphic allele of
*RBM8A* ... in the heterozygous state," that "at 2.6 percent it is not rare," and that "gnomAD v4.1 records 583
homozygotes for this allele." `creative D §6` adds the HGVS `c.-21G>A`.

Resolved rs139428292 through the gnomAD gene endpoint (the rsID alone is ambiguous — it maps to three alleles at
one position). The TAR allele is **chr1:145927447 C>T**, a 5′UTR variant of *RBM8A*.

| Claim in report | Measured | Verdict |
|---|---|---|
| carried, heterozygous | VCF: `GT 0/1`, `AD 17,19` (alt balance 0.528), `DP 36`, `GQ 99`, `PASS` | **confirmed** |
| "2.6 percent" | gnomAD v4.1 exome AF **0.02602** (genome AF 0.01844) | **confirmed** |
| "583 homozygotes" | gnomAD v4.1 exome homozygote_count **583** (genome 33) | **confirmed** |

Every part holds. This is a clean, high-quality heterozygous call, and the two population numbers are exact.

## Entry 2 — Closes an alternative explanation. No 1q21.1 deletion sits in trans, so the allele is a benign carrier state.

A heterozygous *RBM8A* 5′UTR hypomorph causes disease (TAR syndrome) **only** in trans with a 1q21.1 deletion.
If a deletion were present the allele would stop being a silent carrier state and would compromise the EJC.
`creative D §6` asserts "no 1q21.1 deletion in trans" from a 100 kb dosage screen (its numbers: depth 0.80–1.19,
retained heterozygosity 0.53–0.98). Re-measured directly:

- Depth across chr1:145.0–146.2 Mb (12 windows, `work/depth.regions.bed.gz`) runs **49.50–73.92**, i.e.
  **0.97×–1.45×** the autosomal median window depth of **50.85×**. No window is depressed; nothing resembling a
  hemizygous loss. (The 1.45× window at 145.3–145.4 Mb reflects the segmental-duplication content of 1q21.1, the
  opposite of a deletion.)
- Heterozygosity is retained across chr1:145.3–146.0 Mb: **350 PASS het** vs 62 hom-alt, het fraction **0.85**. A
  hemizygous deletion would collapse heterozygosity toward zero; 350 het calls confirm two copies.

**No 1q21.1 deletion in trans.** The RBM8A allele is a benign heterozygous carrier state, exactly as the report
treats it. Alternative closed.

## Entry 3 — Converts an assertion into a measurement. No rare coding second-hit anywhere in the NMD/EJC machinery.

`creative D §6` and `REPORT_track2.md:38` state that "no rare coding variant falls in any of the 14 NMD genes or
7 EJC genes screened" and that "Only one rare non-dbSNP coding variant fell in the entire 80-gene network ...
(ANAPC2 missense, heterozygous)." This is the load-bearing negative: if the NMD apparatus itself carried a
disrupting variant, the NMD-normal inference would be unsafe regardless of the RBM8A carrier allele.

Independently screened `work/coding_nodbsnp.gene.vcf.gz` (1,694 gene-annotated coding variants absent from the
caller's dbSNP build, 704 distinct genes) against a broad canonical NMD + EJC + APC/C gene set:

- NMD factors screened (UPF1, UPF2, UPF3A, UPF3B, SMG1, SMG5, SMG6, SMG7, SMG8, SMG9, ETF1, GSPT1, GSPT2, DHX34,
  NBAS, MOV10): **zero** rare coding variants.
- EJC genes screened (EIF4A3, MAGOH, MAGOHB, RBM8A, CASC3, RNPS1, ACIN1, PNN, SAP18, SRRM1, ALYREF): **zero**.
- APC/C: the **only** hit is **ANAPC2 chr9:137185989 C>T, heterozygous, DP 53** — the exact variant the
  report names.

Confirmed. Nothing in the NMD or EJC machinery modifies the prediction. Scope limit, stated plainly: this file
holds only coding variants *absent from dbSNP*, so a rare-but-catalogued coding variant would not appear here;
`creative D §6` covered that separately via gnomAD frequency on the 80-gene network, which is not re-run here.

## Entry 4 — Closes an alternative explanation (reproduction of Q17/R7, not a new finding). No regulatory allele upstream of *BUB1B*.

The strongest reviewer objection to "the genome has been fully searched for a second BUB1B allele" is Ochiai 2014
(PMID 24344301): a proven-causal single-base substitution **44 kb upstream** of the *BUB1B* TSS that no coding
filter would find. `Q17_regulatory_allele.md` already answered this (85 PASS variants in the 60 kb upstream
window, 57 het, 0 absent from gnomAD, 2 below 1%). Per rule 3 this is **not new** — but it rested on a byte-range
read summarised in one file, so I re-derived it independently from the VCF + gnomAD GraphQL.

gnomAD gives *BUB1B* at chr15:40,161,023–40,221,123 (+ strand), within 40 bp of Q17's TSS. Window scanned:
chr15:40,101,023–40,161,023.

| Q17 number | Reproduced here | Match |
|---|---|---|
| 85 PASS variants | **85** | exact |
| 57 heterozygous | **57** (= 52 strict `0/1` + 5 multiallelic `1/2`) | exact |
| 2 variants < 1% | **2**: 15:40,114,056 A>G AF **0.00212**; 15:40,144,423 AAAG-repeat AF **0.00259** | exact (Q17: 0.0021, 0.0026) |
| nearest call to the 44 kb position is "456 bp away and homozygous" | nearest PASS variant to 40,116,984 is 40,116,528, **456 bp**, `GT 1/1` | exact |

The load-bearing conclusion holds on independent re-measurement: **no candidate regulatory allele upstream of
*BUB1B* in this child.** The two rare variants are 3.0 kb and 27.4 kb from the Ochiai position and neither is a
single-base substitution of that class.

**Disconfirming detail, recorded with equal prominence (it is a method caveat, not an overturned conclusion).**
Q17 reports "0 absent from gnomAD." Querying by *exact* left-aligned variant ID, I find **3 alleles absent**:
15:40,106,517 `AAC>AAC(AC)8`, 15:40,120,606 `TTATC>TTATC(TATC)2`, 15:40,143,237 an AT-repeat expansion. All three
are the ALT2 of multiallelic **short-tandem-repeat** sites whose other allele *is* common in gnomAD; they are
absent only because gnomAD represents repeat-length alleles differently, not because they are rare functional
candidates. None is near the 44 kb position. So Q17's *conclusion* is unaffected, but its "0 absent" figure is an
artefact of position-level matching; under allele-exact matching the honest count is "3 absent, all common-locus
STR-length polymorphisms." The distinction matters only for anyone reusing the scan as a template: an STR-aware
comparison, not exact-ID matching, is what the method needs.

## Entry 5 — Bounds what cannot be known. The one link that stays an inference, and its named remedy.

Actual NMD efficiency in this child's cells cannot be measured from DNA. Entries 1–4 remove every measurable way
the NMD-normal inference could be wrong (a compromising RBM8A genotype, a deletion in trans, a coding second-hit
in the machinery, a regulatory second allele) — but they cannot *measure* decay of the mutant transcript. The
report already flags this correctly. What would close it: the long-amplicon RT-PCR with a cycloheximide arm and
parental genotyping (report §4 item 2 / §9 question 1), on RNA that does not exist in this repository. This audit
confirms the gap is real, correctly bounded, and correctly attributed to the one step that needs living cells.

## Anchor — the headline genotype matches the Track 1 table exactly.

So the chain above is anchored to a verified diagnosis rather than an assumed one:

| Variant | Track 1 table | VCF (measured) |
|---|---|---|
| chr15:40209701 T>G p.Leu737Ter | `0/1, 21/25` | `GT 0/1`, `AD 21,25`, `DP 46`, `GQ 99`, `PASS` — exact |
| chr15:40220612 T>G p.Asn1002Lys | `0/1, 15/13` | `GT 0/1`, `AD 15,13`, `DP 28`, `GQ 99`, `PASS` — exact |

Both re-derived from reads by minimap2 in `R18` (alt fractions 0.543, 0.517); here confirmed against the
caller's own AD fields.

---

## What this run found, stated against the prompt's own test

The allele-1 / NMD-normal assumption chain is **soundly built on measurable facts**. Four of its five load-bearing
sub-claims are confirmed by independent re-derivation from the primary VCF and the live gnomAD API; the fifth
(NMD efficiency itself) is genuinely unmeasurable from DNA and is correctly flagged as an inference by the
authors. I found **no load-bearing conclusion that measurement overturns**. The single disconfirmation is a
method detail (Entry 4: "0 absent" is really "3 absent STR-length alleles" under allele-exact matching), which
does not change the conclusion but should travel with the scan if it is reused.

This is a verification-heavy run by design: the reports attribute these numbers to internal summary files, and the
value added is that they now reproduce, to the digit, from the supplied data by someone holding only that data.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | rs139428292 position/allele | chr1:145927447 C>T (RBM8A 5′UTR) | gnomAD GraphQL `gene(gene_symbol:"RBM8A")` variants, filter rsids |
| 2 | child's genotype at rs139428292 | GT 0/1, AD 17,19, DP 36, GQ 99, PASS | `pysam.VariantFile(VCF).fetch('1',145927446,145927448)` |
| 3 | gnomAD AF / hom for that allele | exome AF 0.02602, hom 583; genome AF 0.01844, hom 33 | gnomAD GraphQL `variant(variantId:"1-145927447-C-T")` |
| 4 | 1q21.1 depth 145.0–146.2 Mb | 49.50–73.92× (0.97–1.45× of 50.85 median) | `zcat work/depth.regions.bed.gz \| awk -F'\t' '$1=="chr1" && $2>=145000000 && $3<=146200000'` |
| 5 | 1q21.1 het density 145.3–146.0 Mb | 350 het / 62 hom-alt, het frac 0.85 | pysam fetch('1',145300000,146000000), count PASS GT |
| 6 | NMD/EJC coding second-hit screen | 0 NMD, 0 EJC; only ANAPC2 (chr9:137185989 C>T het) | pysam scan of `work/coding_nodbsnp.gene.vcf.gz`, GENE ∈ NMD∪EJC∪APCC |
| 7 | *BUB1B* gene coords/strand | chr15:40,161,023–40,221,123, + | gnomAD GraphQL `gene(gene_symbol:"BUB1B")` |
| 8 | upstream 60 kb PASS variants / het | 85 / 57 (52 `0/1` + 5 `1/2`) | pysam fetch('15',40101023,40161023), count PASS GT |
| 9 | upstream rare (<1%) variants | 2: 40,114,056 A>G 0.00212; 40,144,423 AAAG-rep 0.00259 | pysam window + gnomAD GraphQL batch `variant()` per ALT |
| 10 | upstream alleles absent from gnomAD (exact-ID) | 3, all multiallelic STR ALT2 alleles | same as #9, af=None |
| 11 | nearest PASS variant to 44 kb position | 40,116,528, 456 bp, GT 1/1 | pysam fetch('15',40116984±5000), min|pos−40116984| |
| 12 | median DP, all PASS autosomal variants | 43.0 (n=4,539,994) | pysam full scan, autosomes, PASS, `statistics.median(DP)` |
| 13 | median DP, PASS autosomal SNVs DP[20,120] | 44.0 (n=3,587,560) | same scan, SNV filter + 20≤DP≤120 |

All gnomAD queries via `POST https://gnomad.broadinstitute.org/api` (dataset `gnomad_r4`).

## Where the next run should start

1. **The deep-intronic *BUB1B* variant is the one unmeasured item left inside the causal gene.** Track 1
   (`REPORT_track1.md:26`) records "one deep-intronic BUB1B variant absent from gnomAD (about 1 kb from the
   nearest exon, **no splice prediction run**)." That is an explicit, load-bearing gap: a second *cis*-acting
   allele class in the causal gene that was found and set aside without evaluation. Next run should (a) locate it
   exactly in the VCF within chr15:40,161,023–40,221,123, (b) measure its true distance to the nearest exon
   (needs the Ensembl 116 GFF3 — **not present under `work/ref/`, only `GRCh38.fa`; it must be fetched or the exon
   boundaries pulled from the Ensembl REST API**), and (c) if any splice tool is installable offline, run it;
   otherwise bound the gap and name SpliceAI/parental RNA as the remedy.

2. **The ANAPC2 variant surfaced in Entry 3 is uncharacterised here.** It is the only rare coding hit in the
   whole SAC/APC/C/NMD network. This run only confirmed its existence and zygosity (chr9:137185989 C>T, het,
   DP 53). Its gnomAD frequency, ClinVar status and predicted consequence were not measured. APC/C is downstream
   of the same checkpoint *BUB1B* sits in, so whether this is benign is worth one measured paragraph — likely
   benign, but currently assumed.

3. **STR representation caveat for any reuse of the upstream scan** (Entry 4): the "0 absent from gnomAD" figure
   is position-level; allele-exact matching gives 3 absent STR alleles. If a future run rebuilds the regulatory
   scan as a transferable template, it should use an STR-aware comparator, not exact variant-ID matching.

4. Tooling for whoever runs next: `python3.12` (pysam 0.24.0), no `bcftools`/`tabix` on `PATH`; gnomAD API
   reachable by POST; `work/coding_nodbsnp.gene.vcf.gz` is the fastest route to "rare coding variant in gene X?".
