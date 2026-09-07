# AUDIT 03. Closing the SGO1 modifier candidate, bounding the phase gap with measured fragment lengths, and verifying allele-2's ClinVar record

**Run 03 of `PROMPT_relevant_additions.md`, 7 September 2026.** `AUDIT_02` ended by naming its item 3 for the
next run: the SGO1 missense that `R5` called "the only entry with a mechanistic story" and left as a hypothesis
"worth one sentence in a family study, nothing more," but never gave the read-level + in-silico + ClinVar closing
pass that `AUDIT_02` Entry 3 gave ANAPC2. This run takes that item, and while the primary data was open added two
more measurable, load-bearing claims: the fragment-length assertion under `R1`'s phase conclusion, and the ClinVar
statements about the second causal allele in `REPORT_track2.md:50` / `REPORT_track1.md:24`.

Before writing I read `R1` (phase), `R5` (modifiers), `R9` (ancestry/denominators, which already measured allele-2's
gnomAD frequency — **not re-opened here**), and both prior `AUDIT_NN` files. **Rule 3 credits:** the SGO1 variant
and its gnomAD frequency are `R5`'s; the phase-set absence is `R1`'s; allele-2's frequency and NFE-private status are
`R9`'s; the c.3006T>A ClinVar VUS citation is the report's. What is new below is (a) the read-level pileup and the
in-silico/ClinVar layer for SGO1 that `R5` did not reach; (b) the measured insert-size distribution that converts
`R1`'s order-of-magnitude assertion into a number; (c) direct verification of the report's three ClinVar claims at
the c.3006 base against ClinVar itself; and (d) RANBP2, which closes the last open cell of `R5`'s modifier table.

Tooling for reproduction: `python3.12` has `pysam 0.24.0`; no `bcftools`/`tabix` on `PATH`. The VCF uses contigs
`1..22,X,Y`; the reference FASTA and `work/bam/all.bam` use `chr1..`. **Egress correction (disconfirms `AUDIT_02`):
`AUDIT_02` stated egress "reaches only gnomAD and Ensembl"; NCBI E-utilities
(`eutils.ncbi.nlm.nih.gov`) is also reachable and was used for the ClinVar verification in Entry 3.** The Broad
SpliceAI host specifically still times out, so `AUDIT_02`'s SpliceAI conclusion is unaffected — but the general
"gnomAD and Ensembl only" characterisation was too narrow.

---

## Entry 1 — Closes an alternative explanation. The SGO1 modifier candidate is a benign-range rare missense, closed at every layer DNA allows.

`R5` screened the mitotic-checkpoint / cohesion / NMD network for a second gene that could modify severity and found
three rare coding variants outside *BUB1B*, of which **SGO1 p.Thr425Ala is the only one with a mechanistic story**:
shugoshin (SGO1) protects centromeric cohesion, and this is a chromosome-segregation disorder, so a hostile reviewer
asking "did you rule out a digenic cohesion modifier?" lands here. `R5` measured its frequency and the network's
depletion but explicitly stopped short of functional or in-silico assessment. This entry closes it as far as the
supplied DNA permits.

**VCF call, re-read verbatim** from `data/WGS_EX2312012_HGWCNDSX7.vcf.gz`:

> **chr3:20174258 T>C**, `GT 0/1`, `AD 19,21` (alt fraction 0.525), `DP 40`, `GQ 99`, `QUAL 544.77`, `MQ 60`,
> `QD 13.62`, `FS 9.80`, `SOR 0.11`, `MQRankSum 0.0`, `ReadPosRankSum −0.071`, `PASS`. `DP 40` matches `R5`.

**Population (confirms `R5`).** gnomAD v4.1: exomes **AC 4 / AN 1,459,042 / AF 2.74e-6 / 0 homozygotes**; genomes
**AC 2 / AN 151,916 / AF 1.32e-5 / 0 homozygotes**; rsID **rs1028681690**. All 4 exome and both genome carrier
alleles are **Non-Finnish European** — no homozygote anywhere in ~1.6 M sampled alleles.

**In-silico (new; `R5` did not run it).** Ensembl VEP, MANE Select **ENST00000412997 (NM_001199251.3)**:
missense **p.Thr425Ala**, **SIFT tolerated (0.23)**, **PolyPhen benign (0.005)**. Across every coding transcript that
annotates it (10 transcripts), SIFT is tolerated (0.20–0.23) and PolyPhen benign (0.001–0.005) without exception.
Most-severe consequence: missense_variant.

**ClinVar (new).** No clinical-significance record; the colocated variant rs1028681690 carries no clinical
significance and no phenotype/disease flag.

**Read-level pileup (new; `R5` took the variant from the coding VCF and a gnomAD range read, never from the reads).**
Piled up directly from `work/bam/all.bam`:

| | Reads | MAPQ min/med/max | Base-qual med | Strand +/− | Proper pairs | Duplicates | Soft-clipped | Secondary/suppl. |
|---|---|---|---|---|---|---|---|---|
| ALT (C) | **27** | **60 / 60 / 60** | 37 | 12 / 15 | 24 / 27 | 0 | 0 | 0 |
| REF (T) | 20 | 60 / 60 / 60 | 37 | 5 / 15 | 18 / 20 | 0 | 1 | 0 |

Alt fraction **0.574 (27/47)**, consistent with the caller's `AD 19,21` (0.525); no third base. The ±25 bp context
is `CAAGTAGATCACTTACTGGTAGGAG[T]TTTTGTTGGCTTAGAACCCTCCGTC` — **55% A+T, balanced (17 T, 12 G, 11 C, 11 A), not a
low-complexity tract**. Every one of the 27 alt reads maps uniquely (MAPQ 60), on both strands, none a duplicate,
none soft-clipped, none secondary/supplementary. **This is a genuine heterozygous call, not an artefact.**

**What this closes.** The alternative "an unassessed cohesion-machinery modifier is inflating severity" is now closed
at every layer DNA reaches: the variant is real (reads), rare (gnomAD, 0 hom), benign by two orthogonal predictors
(SIFT tolerated + PolyPhen benign, unanimous across transcripts), and carries no curated clinical flag — sitting in a
gene set `R5` measured to be **depleted**, not enriched, for rare coding variants. It remains a single heterozygous
missense in a recessive-associated gene with no second hit. `R5`'s "worth one sentence in a family study, nothing
more" stands, and is now fully evidenced rather than left as the one loose mechanistic thread. **The residual that DNA
cannot touch** is functional: a cohesion assay in the child's cells is the only thing that could promote or dismiss it
further, and nothing in `R5`'s enrichment result or these layers motivates running one.

## Entry 2 — Converts an assertion into a measurement, and bounds what cannot be known. The phase gap, in measured fragment lengths.

`R1` reached the correct load-bearing conclusion — the two causal *BUB1B* variants cannot be phased from these reads,
so trans is unproven and PM3 is unavailable — and measured the right primary fact: both variants (chr15:40209701,
chr15:40220612) carry **no `PGT`/`PID` phase set** in the VCF. But the *reason* `R1` gave is an assertion about the
library, not a measurement: "read-backed phasing … for this library means a few hundred base pairs. Ten kilobases is
**three orders of magnitude** beyond that." The fragment length is measurable from `work/bam/all.bam`, and the exact
gap a phase chain would have to cross is measurable from the VCF. Doing both turns an apology into a bounded result.

**The gap a phase chain must cross (measured from the VCF).** PASS heterozygous sites in chr15:40209000–40221500:

| Position | Change | Gap from previous het |
|---|---|---|
| 40209701 | T>G p.Leu737Ter (**causal allele 1**) | — |
| 40216470 | A>G (deep-intronic, the `AUDIT_02` variant) | **+6,769 bp** |
| 40220612 | T>G p.Asn1002Lys (**causal allele 2**) | **+4,142 bp** |
| 40221421 | G>C | +809 bp |

There is exactly **one** heterozygous site between the two causal variants (40216470). So to phase them by reads a
single fragment must span at least **6,769 bp** (allele 1 → intermediate het) or **4,142 bp** (intermediate het →
allele 2). There is no closer stepping stone.

**The fragment reach (measured from the BAM).** Template lengths of proper-pair, primary, non-duplicate fragments:

| Sample | n fragments | median TLEN | mean | p99 | p99.9 | max | ≥1,000 bp | ≥4,142 bp | ≥6,769 bp |
|---|---|---|---|---|---|---|---|---|---|
| BUB1B region chr15:40209000–40221500 | 2,137 | **421** | 431 | 764 | 797 | **798** | 0 | 0 | 0 |
| library sample chr1:20.0–20.5 Mb | 84,991 | 427 | 433 | 774 | 797 | **803** | 0 | 0 | 0 |

Across **87,128** measured fragments the longest is **803 bp**; **not one reaches 1,000 bp**. The smaller of the two
gaps a phase chain must cross (4,142 bp) is **≈5.2× the longest fragment observed** and ≈9.8× the median; the larger
(6,769 bp) is ≈8.4× the longest and ≈16× the median. Because insert size is fixed at library preparation, re-aligning
the same reads cannot manufacture longer fragments — **confirming `R1`'s corollary** that the 84 GB of raw FASTQ would
not answer this either.

**Disconfirming detail, recorded with equal prominence (rule 2).** `R1`'s magnitude is overstated. A median fragment
of 421 bp against the 10.9 kb variant separation is a factor of **≈26×, i.e. ≈1.4 orders of magnitude**, not "three";
against the largest single unbridgeable gap (6,769 bp) it is ≈16×, **≈1.2 orders of magnitude**. `R1`'s *conclusion*
(unphaseable from short reads) is untouched and now carries an exact number, but its "three orders of magnitude"
figure is wrong by about an order and a half and should read "≈1 order of magnitude beyond the longest fragment
measured (803 bp)."

**The bound, stated as a result.** Trans cannot be established from this WGS: no fragment in it spans even the nearer
4.1 kb link, by a measured factor of ≥5. The named remedies are unchanged — parental genotyping, or a long-read
amplicon across the 10.9 kb (both already gate item 1) — and the bound now says precisely why: a spanning read must be
>5× longer than the longest this library produced.

## Entry 3 — Closes an alternative explanation. The report's three ClinVar statements about allele 2 verify against ClinVar itself.

`REPORT_track2.md:50` rests part of allele-2's classification on the ClinVar situation at the c.3006 base:
"NM_001211.6(BUB1B):c.3006T>A (p.Asn1002Lys), **VCV004600147**, … uncertain significance, last evaluated
**19 September 2025**. The only other allele deposited at that base is the synonymous c.3006T>C, likely benign.
**No record exists for c.3006T>G**." The hostile-reviewer version is "you missed a ClinVar record for the child's
exact variant." These are `cited` claims; because NCBI E-utilities turned out reachable from this server, they were
verified directly rather than taken on trust.

**Nucleotide → consequence (Ensembl VEP, MANE ENST00000287598).** The report's three-allele description of the base
is correct: `c.3006T>G` and `c.3006T>A` both give **missense p.Asn1002Lys**; `c.3006T>C` gives **synonymous
p.Asn1002=**. VEP returns **no colocated variation record for the child's exact allele c.3006T>G**.

**ClinVar, queried per allele (new — direct verification):**

| Allele | ClinVar result | Verdict vs report |
|---|---|---|
| c.3006T>G (**the child's variant**, chr15:40220612 T>G) | **0 records** | confirms "No record exists for c.3006T>G" |
| c.3006T>A | **VCV004600147**, `NM_001211.6(BUB1B):c.3006T>A (p.Asn1002Lys)`, **Uncertain significance**, last evaluated **2025/09/19**, trait "Inborn genetic diseases" | confirms accession, class and date exactly |
| c.3006T>C | **VCV004842697**, `NM_001211.6(BUB1B):c.3006T>C (p.Asn1002=)`, **Likely benign** | confirms "likely benign"; adds the accession the report omitted |

**What this closes.** The alternative that a curated classification for the child's exact causal allele was missed is
closed decisively: ClinVar returns zero records for c.3006T>G. The report's reading — that allele 2 is a genuine VUS
by the "same protein change, different nucleotide" record, and that absence from ClinVar for the exact nucleotide is
absence of a submission, not evidence of benignity — is confirmed against the primary source, to the accession.

**Closing the last cell of `R5`'s modifier table (continuity).** `AUDIT_02` Entry 3 closed ANAPC2; Entry 1 above
closed SGO1; the third variant `R5` named, **RANBP2 chr2:108751880 C>T**, is closed here: gnomAD v4.1 exomes
**AC 9 / AN 1,459,684 / AF 6.17e-6 / 0 hom** (genomes absent), rs1255583041; VEP MANE **ENST00000283195
(NM_006267.5)** `c.1641C>T`, **synonymous**, ClinVar **likely_benign**. This matches `R5` exactly. **All three
non-*BUB1B* rare coding variants in `R5`'s checkpoint/cohesion/decay screen are now independently closed as
benign-range**, consistent with `R5`'s finding that the network is depleted rather than carrying a modifier.

---

## What this run found, against the prompt's own relevance test

- **Entry 1 (closes an alternative):** SGO1 p.Thr425Ala — the one modifier candidate with a cohesion-machinery
  mechanism — is a genuine heterozygous call (27 alt reads, all MAPQ 60, both strands, 0 duplicates, non-repetitive
  context), rare (gnomAD 4 exome / 2 genome alleles, 0 hom, NFE-private), benign by SIFT and PolyPhen unanimously
  across transcripts, and unflagged in ClinVar. Closed at every DNA-accessible layer; only a functional cohesion
  assay remains, and nothing motivates it.
- **Entry 2 (converts an assertion / bounds the unknown):** the two causal variants cannot be phased from this WGS —
  the nearer of the two gaps a read must span is 4,142 bp, and the longest of 87,128 measured fragments is 803 bp
  (median 421, none ≥1,000). `R1`'s conclusion holds and is now quantified; its "three orders of magnitude" is
  disconfirmed as ≈1.2–1.4 orders and corrected.
- **Entry 3 (closes an alternative):** the report's ClinVar statements about allele 2 verify to the accession
  (c.3006T>G: 0 records; c.3006T>A: VCV004600147 VUS 2025-09-19; c.3006T>C: VCV004842697 likely benign). RANBP2
  closes the last cell of `R5`'s modifier table.

**No load-bearing conclusion of the submission is overturned by these measurements.** Two disconfirming/method notes
are recorded with equal prominence: (a) `R1`'s "three orders of magnitude" overstates the phase gap by ~1.5 orders —
conclusion unchanged, figure wrong; (b) `AUDIT_02`'s "egress reaches only gnomAD and Ensembl" is too narrow — NCBI is
reachable, which is what made Entry 3's direct ClinVar verification possible (and does not change `AUDIT_02`'s
separate SpliceAI-host finding).

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | SGO1 VCF call | chr3:20174258 T>C, GT 0/1, AD 19,21, DP 40, GQ 99, QUAL 544.77, MQ 60, QD 13.62, FS 9.80, PASS | `pysam.VariantFile(VCF).fetch('3',20174257,20174258)` |
| 2 | SGO1 gnomAD v4.1 | exome AC 4 / AN 1,459,042 / AF 2.74e-6 / 0 hom (all NFE); genome AC 2 / AN 151,916 / AF 1.32e-5 / 0 hom (all NFE); rs1028681690 | gnomAD GraphQL `variant(variantId:"3-20174258-T-C")` |
| 3 | SGO1 consequence / in-silico / ClinVar | MANE ENST00000412997 (NM_001199251.3), missense p.Thr425Ala, SIFT tolerated 0.23, PolyPhen benign 0.005 (tolerated/benign across all 10 coding tx); no ClinVar significance | Ensembl REST `vep/human/region/3:20174258-20174258:1/C?canonical=1&mane=1` |
| 4 | SGO1 read-level pileup | ALT C = 27 reads, MAPQ 60/60/60, strand 12+/15−, 24/27 proper, 0 dup, 0 sclip, 0 sec/supp; REF T = 20; alt frac 0.574 (27/47); no third base | `pysam.AlignmentFile('work/bam/all.bam').pileup('chr3',20174257,20174258,truncate=True,min_base_quality=0,stepper='nofilter')` |
| 5 | SGO1 local composition ±25 bp | 55% A+T, balanced (17 T,12 G,11 C,11 A), not low-complexity | `Counter(FastaFile('work/ref/GRCh38.fa').fetch('chr3',20174232,20174283))` |
| 6 | PASS het sites chr15:40209000–40221500 | 4: 40209701 (causal), 40216470 (+6,769), 40220612 (causal, +4,142), 40221421 (+809) | `pysam.VariantFile(VCF).fetch('15',40209000,40221500)`, filter PASS het |
| 7 | fragment reach, BUB1B region | n=2,137; median TLEN 421, mean 431, p99 764, p99.9 797, max 798; 0 fragments ≥1,000 bp | `pysam` fetch chr15:40209000–40221500, proper-pair primary non-dup, `abs(template_length)` |
| 8 | fragment reach, library sample | n=84,991; median 427, mean 433, p99 774, p99.9 797, max 803; 0 ≥1,000, 0 ≥4,142, 0 ≥6,769 | same, chr1:20.0–20.5 Mb (cap 200k) |
| 9 | ratio gap : fragment | 4,142 bp = 5.2× max fragment (803) / 9.8× median; 6,769 bp = 8.4× / 16× | arithmetic on #6–#8 |
| 10 | BUB1B c.3006 nucleotide→consequence | T>G & T>A → missense p.Asn1002Lys; T>C → synonymous p.Asn1002=; no colocated record for T>G | Ensembl REST `vep/.../15:40220612-40220612:1/{G,A,C}` |
| 11 | ClinVar c.3006T>G | 0 records | E-utilities `esearch db=clinvar term="BUB1B[gene] AND c.3006T>G"` |
| 12 | ClinVar c.3006T>A | VCV004600147, Uncertain significance, last evaluated 2025/09/19, trait Inborn genetic diseases | E-utilities `esearch`+`esummary` id 4600147 |
| 13 | ClinVar c.3006T>C | VCV004842697, Likely benign, p.Asn1002= | E-utilities `esearch`+`esummary` id 4842697 |
| 14 | RANBP2 gnomAD / consequence / ClinVar | 2:108751880 C>T, exome AC 9 / AN 1,459,684 / AF 6.17e-6 / 0 hom (genome absent), rs1255583041; MANE ENST00000283195 (NM_006267.5) c.1641C>T synonymous; ClinVar likely_benign | gnomAD GraphQL + Ensembl REST VEP |
| 15 | NCBI E-utilities reachability | reachable (HTTP 200), correcting AUDIT_02's "gnomAD + Ensembl only" | `urllib` GET `eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi` |

All gnomAD queries via `POST https://gnomad.broadinstitute.org/api` (dataset `gnomad_r4`); annotation via
`https://rest.ensembl.org`; ClinVar via `https://eutils.ncbi.nlm.nih.gov/entrez/eutils`.

## Where the next run should start

1. **The pseudoexon score for chr15:40216470 remains the only open DNA-adjacent item inside the causal gene**
   (`AUDIT_02` item 1). `AUDIT_02` found the Broad SpliceAI host unreachable; this run found NCBI reachable, so a next
   run should re-test whether **any** SpliceAI route is reachable now (a different mirror, or the Illumina/Kishore
   precomputed SpliceAI scores distributed via a public bucket), and if so score `chr15-40216470-A-G` with the two
   causal alleles as positive controls. If still unreachable, the bound in `AUDIT_02` Entry 1 stands.
2. **The modifier table is now fully closed** (RANBP2/SGO1/ANAPC2 all benign-range). The natural next continuity
   target is outside the pre-assembled network: `R5`'s enrichment test assumed the 80+18-gene list is the right
   universe. A next run could ask whether any rare coding variant sits in a cohesion/SAC gene *not* on that list
   (e.g. the broader kinetochore/CPC set) — a bounded gene-set-completeness check against `work/coding_nodbsnp.gene.vcf.gz`.
3. **`AUDIT_01` item 3 (STR-aware comparator for the upstream regulatory scan) is still untouched** and remains the
   one methodological to-do for anyone reusing the regulatory scan as a template.
4. Tooling for whoever runs next: `python3.12` (pysam 0.24.0); VCF contigs `1..22`, BAM/FASTA `chr1..`; egress reaches
   gnomAD, Ensembl **and NCBI E-utilities** (Broad SpliceAI host times out); the library insert size is ~420 bp median,
   803 bp max — no read-backed phasing beyond ~800 bp is possible from this BAM.
