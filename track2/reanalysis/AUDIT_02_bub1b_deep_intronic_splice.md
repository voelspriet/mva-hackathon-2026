# AUDIT 02. The deep-intronic *BUB1B* variant — how far a splice call goes without the model, and a read-level reality check

**Run 02 of `PROMPT_relevant_additions.md`, 7 September 2026.** `AUDIT_01` ended by naming three places for the
next run to start; this run takes the first two. Item 1: the deep-intronic *BUB1B* variant that Track 1 recorded
with "no splice prediction run" and R12 recorded as "not assessable for a splicing effect here." Item 2: the
ANAPC2 variant AUDIT_01 called "uncharacterised."

Before writing I read `R12` (which found this variant), `R5` (which had already characterised ANAPC2), `R1` and
`R18` (phase and read-level checks), and `SYNTHESIS_for_judging.md`. **Rule 3 applies twice below:** the variant
itself and its absence from gnomAD are R12's, not new here, and ANAPC2's identity and frequency are R5's. What is
new is (a) the deterministic part of the splice assessment R12 declared unassessable, done and bounded against the
authoritative Ensembl MANE annotation; (b) a read-level pileup of the variant, which R18 never ran for this site;
and (c) closing ANAPC2 with the in-silico and ClinVar layer R5 did not reach.

Tooling for reproduction: `python3.12` has `pysam 0.24.0`; no `bcftools`/`tabix`/`spliceai` on `PATH`. The VCF
uses contigs `1..22,X,Y`; the reference FASTA and `work/bam/all.bam` use `chr15`. Egress is firewalled to the
gnomAD and Ensembl APIs only — see Entry 1 for the test that establishes SpliceAI cannot be reached.

The variant, re-read verbatim from `data/WGS_EX2312012_HGWCNDSX7.vcf.gz`:

> **chr15:40216470 A>G**, `GT 0/1`, `AD 28,18`, `DP 46`, `GQ 99`, `QUAL 383.77`, `MQ 60`, `QD 8.34`, `FS 4.376`,
> `SOR 1.042`, `MQRankSum 0.0`, `ReadPosRankSum −0.079`, `PASS`. Every field matches R12 to the digit.

---

## Entry 1 — Bounds what cannot be known, and converts "not assessable" into a measured part plus a named residual.

R12 wrote that this variant "is not assessable for a splicing effect here, because a cryptic-splice or
branch-point prediction needs the model P1 says this project does not hold." That sentence bundles two different
things: the part of a splice assessment that follows deterministically from sequence and annotation, and the part
that genuinely needs a trained model. They can be separated, and the first part can be done now.

**Authoritative geometry (this is new — R12 used "local exon structure" of unstated provenance; AUDIT_01 flagged
that).** Ensembl MANE Select transcript for *BUB1B* is **ENST00000287598** (BUB1B-201, canonical, + strand, 23
exons). The variant falls in **intron 20**, between exon 20 (ends 40213474) and exon 21 (starts 40217496):

| Landmark | Position | Distance from variant |
|---|---|---|
| 5′ splice site (donor), exon-20 end | 40213474 | **2,996 bp downstream** of the donor |
| 3′ splice site (acceptor AG), last two intron bases 40217494–40217495 | 40217495 | **1,025 bp upstream** of the acceptor AG (1,026 bp to the exon-21 first base) |
| intron 20 total length | 40213475–40217495 | 4,021 bp |

The intron's own dinucleotides read `GT…AG` directly from the reference FASTA, so the annotation matches the
sequence. R12's "1,025 bp before the next exon" and its exon-end 40213474 both reproduce; its downstream exon
start (40217495) was off by one against MANE (40217496).

**Deterministic motif result (measured from the reference, not a model).** A canonical (U2) splice site is created
only by producing the invariant dinucleotide at the junction — `GT` for a new donor, `AG` for a new acceptor;
>98.7% of human introns are GT–AG. The reference context is `…CAC A CAC…`; the A>G makes it `…CAC G CAC…`:

- the two dinucleotides touching the site go from `CA`/`AC` (REF) to `CG`/`GC` (ALT);
- **no acceptor `AG` is created** (the base 5′ of the variant is C, giving `CG`, not `AG`);
- **no donor `GT` is created** (the variant G is followed by C, giving `GC`; the +2..+7 context is `GCTTTA`,
  nothing like the `GYRAGT` donor consensus, so not even a plausible minor GC-AG donor);
- the change **removes an adenine**, and a branch-point requires an A, so it cannot create a branch point;
- position rules out both splice sites' regulatory windows: the branch point and polypyrimidine tract of a 3′
  acceptor sit ≤~40 bp upstream of the AG, and this variant is **1,025 bp** upstream — ~25× too far; it is
  **2,996 bp** from the donor, far outside the ~6-base donor consensus.

**So the assessable component is negative:** this variant does not create, destroy, or sit within any canonical
splice signal of intron 20.

**The residual that genuinely needs the model, stated precisely.** What a deterministic scan cannot rule out is
*deep-intronic pseudoexon activation* — a cryptic donor and cryptic acceptor elsewhere in the intron being
strengthened into use by an intronic splicing regulatory element. Detecting that is exactly what SpliceAI is
trained for, and it is the part no single-dinucleotide rule captures. **I tested whether the model could be run
here and it cannot:** the Broad SpliceAI lookup API resolves by DNS (`spliceailookup-api.broadinstitute.org` →
34.71.77.14) but every connection times out at 90 s, consistent with egress being open only to the gnomAD and
Ensembl hosts; and no offline splice package (`spliceai`, `maxentpy`) is installed, with no weights present to run
one. This confirms P1/R12's statement that the project does not hold the model, and adds that it also cannot be
fetched from this server.

**What this changes.** R12's "not assessable" becomes: *the canonical-signal component is assessable and negative;
only the model-scored pseudoexon component remains, and it needs either SpliceAI (one variant, seconds of compute
on a machine with egress or the weights) or the RNA assay the report already proposes (report §4 item 2), which
would settle it directly rather than predict it.* That is a bounded gap with a named, cheap remedy, not an open
one.

## Entry 2 — Closes an alternative explanation: the variant is real, verified at the read level, not just from FORMAT fields.

R12 asserted "It is real" from `GQ 99` and site-level `MQ 60`. But this site is a **low-complexity CA/AT tract**
(reference ±25 bp is 73% A+T, `…AAACAAAAC ACACACATGCACAC A CTTTACATATATATAT…`, a single G in the 50 reference
bases around it), and site-level `MQ` is averaged over all reads — in such a context the *alt* reads specifically
could be the mismapped ones. R18 checked the two causal alleles at the read level but never this variant. Piled up
directly from `work/bam/all.bam`:

| | Reads | MAPQ min/med/max | Base-qual med | Strand +/− | Proper pairs | Duplicates | Soft-clipped | Secondary/suppl. |
|---|---|---|---|---|---|---|---|---|
| ALT (G) | **20** | **60 / 60 / 60** | 37 | 13 / 7 | 20 / 20 | 0 | 1 | 0 |
| REF (A) | 30 | 29 / 60 / 60 | 37 | 13 / 17 | 30 / 30 | 0 | 4 | 0 |

Alt fraction **0.400** (20/50), matching the caller's `AD 28,18` (0.391). **Every one of the 20 alt-supporting
reads maps uniquely (MAPQ 60), on both strands, all properly paired, none a duplicate, one soft-clipped, none
secondary or supplementary.** Despite the low-complexity context the alt allele is not a mismapping artefact. The
alternative explanation — that this is a low-complexity false positive — is closed, and R12's "it is real" now
rests on the reads rather than on the caller's summary. This is a **confirming** result.

## Entry 3 — Converts an assertion into a measurement (continuity): ANAPC2 was already characterised in R5; here it is closed.

AUDIT_01 item 2 called the ANAPC2 variant "uncharacterised." That was an oversight in AUDIT_01: **`R5` had
already measured it** — `chr9:137185989 C>T, missense p.Gly297Asp, 0/1, DP 53, gnomAD genomes AC 25 / AN 152,312 /
AF 1.6e-4` — and noted the 80-gene checkpoint/decay network carries one rare coding variant where its coding
length predicts nine, i.e. depleted, not enriched. Per rule 3 that is R5's, not new. Re-verified here and extended
with the layer R5 did not reach:

| Property | Measured now | Source |
|---|---|---|
| VCF call | `C>T`, `GT 0/1`, `AD 22,31`, `DP 53`, `GQ 99`, `QUAL 939.8`, `PASS` | VCF, confirms R5 |
| gnomAD v4.1 | genome AC 25, AN 152,312, **AF 1.64e-4, 0 homozygotes**; **not in the exome dataset** | gnomAD API, confirms R5's AF |
| consequence | missense, **p.Gly297Asp** (G/D at codon 297), rs760949720 | Ensembl VEP |
| in-silico (new) | **SIFT tolerated_low_confidence 0.27**; PolyPhen not computed for the scored transcript | Ensembl VEP |
| ClinVar (new) | **no ClinVar record** returned for the locus or rsID (colocated variant is rs760949720 with no clinical significance) | Ensembl VEP colocated_variants |
| population detail (new) | AF highest in South-Asian 8.3e-4 and (small-sample) Middle-Eastern 1.0e-2; East-Asian 0 | gnomAD via VEP frequencies |

**This closes the alternative that ANAPC2 is a digenic modifier.** It is present in gnomAD at 1.6e-4 — it fails the
project's own "absent from dbSNP / absent from gnomAD" bar for a candidate second hit; it has 25 heterozygous
carriers and 0 homozygotes; SIFT calls it tolerated; and no curated source flags it pathogenic. It is a
benign-range rare missense, consistent with R5's read that the checkpoint network is depleted rather than carrying
a modifier. The one correction to record is procedural: **AUDIT_01 should have cited R5 for this variant** rather
than listing it as uncharacterised.

---

## What this run found, against the prompt's own relevance test

- **Entry 1 (bounds the unknown / converts an assertion):** the deep-intronic *BUB1B* variant creates no canonical
  splice signal and lies outside both splice sites' regulatory windows — the deterministic part of the assessment
  R12 declared unassessable is negative. Only pseudoexon activation remains, it needs SpliceAI or the RNA assay,
  and the model is confirmed unreachable from this server. The gap is now bounded with a named remedy.
- **Entry 2 (closes an alternative):** a read-level pileup confirms the variant is a genuine heterozygous call —
  20 alt reads, all MAPQ 60, both strands, all properly paired — not a low-complexity artefact. R18 never checked
  this site; now it is checked.
- **Entry 3 (continuity, closes an alternative):** ANAPC2 p.Gly297Asp is a benign-range rare missense (gnomAD AF
  1.6e-4, 0 hom, SIFT tolerated, no ClinVar), already found by R5; AUDIT_01's "uncharacterised" is corrected.

**No load-bearing conclusion of the submission is overturned by these measurements.** The submission does not
build on the deep-intronic variant (R12: "recorded, not built on"), and this run supports that stance: the variant
is real but shows no deterministic splice signal, so treating it as an inference pending an RNA assay is the
correct call. The one disconfirming note is small and procedural (AUDIT_01 miscredited ANAPC2 as unmeasured; R5
had measured it). The value added is that Track 1's "no splice prediction run" and R12's "not assessable" are now
resolved as far as DNA and sequence permit, with the residual precisely delimited.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | VCF record at chr15:40216470 | A>G, GT 0/1, AD 28,18, DP 46, GQ 99, QUAL 383.77, MQ 60, QD 8.34, FS 4.376, PASS | `pysam.VariantFile(VCF).fetch('15',40216469,40216470)` |
| 2 | *BUB1B* MANE transcript | ENST00000287598, canonical, + strand, 23 exons | Ensembl REST `lookup/id/ENST00000287598?expand=1` |
| 3 | flanking exons of variant | intron 20; exon 20 ends 40213474, exon 21 starts 40217496 | same lookup, sort exons by coord |
| 4 | distance to 5′ donor / 3′ acceptor | 2,996 bp from donor; 1,025 bp to acceptor AG (1,026 bp to exon-21 start) | arithmetic on #3 |
| 5 | intron 20 length | 4,021 bp | 40217495 − 40213475 + 1 |
| 6 | intron dinucleotides (sanity) | 5′ GT, 3′ AG | `FastaFile(REF).fetch('chr15', donor, donor+2)` and acceptor −3..−1 |
| 7 | ref→alt local motif | `…CAC A CAC…` → `…CAC G CAC…`; touching dinucs CA/AC → CG/GC; no AG, no GT created | `FastaFile(REF).fetch('chr15',40216439,40216500)`, substitute index |
| 8 | local composition ±25 bp | 73% A+T, single G in 50 ref bases (low complexity) | `Counter(FastaFile.fetch('chr15',40216444,40216495))` |
| 9 | SpliceAI API reachability | DNS 34.71.77.14, connection times out at 90 s (egress blocked) | `urllib` GET `spliceailookup-api.broadinstitute.org/spliceai/?hg=38&variant=chr15-40216470-A-G` |
| 10 | gnomAD v4.1 status of variant | not found (absent), confirming R12 | gnomAD API `variant(variantId:"15-40216470-A-G")` |
| 11 | read-level pileup at variant | ALT G = 20 reads all MAPQ 60, both strands, 20/20 proper, 0 dup; REF A = 30; alt frac 0.400 | `pysam.AlignmentFile('work/bam/all.bam').pileup('chr15',40216469,40216470,truncate=True)` |
| 12 | ANAPC2 VCF call | chr9:137185989 C>T, GT 0/1, AD 22,31, DP 53, GQ 99, QUAL 939.8, PASS | `pysam.VariantFile(VCF).fetch('9',137185988,137185989)` |
| 13 | ANAPC2 gnomAD v4.1 | genome AC 25, AN 152,312, AF 1.64e-4, 0 hom; exome null | gnomAD API `variant(variantId:"9-137185989-C-T")` |
| 14 | ANAPC2 consequence / in-silico | missense p.Gly297Asp; SIFT tolerated_low_confidence 0.27; no ClinVar record; rs760949720 | Ensembl REST `vep/human/region/9:137185989-137185989:1/T` |

All gnomAD queries via `POST https://gnomad.broadinstitute.org/api` (dataset `gnomad_r4`); all annotation via
`https://rest.ensembl.org` (GRCh38, Ensembl 116-era MANE Select).

## Where the next run should start

1. **The pseudoexon question is now the only open piece inside the causal gene, and it has a cheap remedy.**
   Everything deterministic about chr15:40216470 is done; only a trained-model or RNA readout remains. The next run
   that has egress or the SpliceAI weights should score this single variant (`chr15-40216470-A-G`, and for
   completeness the two causal alleles as positive controls) and record the delta scores. Until then the gap is
   bounded, not open. No further DNA-only work will move it.

2. **AUDIT_01 item 3 (STR-aware comparator for the upstream regulatory scan) is still untouched.** If a future run
   rebuilds the regulatory scan as a transferable template, it needs allele-exact, STR-aware matching rather than
   position-level or exact-variant-ID matching; AUDIT_01 Entry 4 showed exact-ID matching mislabels three common
   STR-length alleles as "absent from gnomAD."

3. **The other two rare coding variants R5 named — SGO1 p.Thr425Ala and the synonymous call — were not
   re-examined here.** ANAPC2 is now closed; SGO1 (a cohesion/checkpoint gene, directly relevant to an aneuploidy
   phenotype) is characterised in R5 but has not had the in-silico + ClinVar + independent-gnomAD closing pass that
   Entry 3 gave ANAPC2. That is the natural next continuity item.

4. Tooling for whoever runs next: `python3.12` (pysam 0.24.0); reference FASTA and `work/bam/all.bam` use `chr15`,
   the VCF uses `15`; egress reaches only gnomAD and Ensembl (SpliceAI/Broad and general hosts time out); Ensembl
   MANE Select for *BUB1B* is ENST00000287598.
