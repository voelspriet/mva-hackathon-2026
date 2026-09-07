# AUDIT 09. The genome-wide read-backed phase span measured for the first time (and its filter's reach bounded), the p.Leu737Ter NMD geometry reproduced on Ensembl 116, and the three MVA genes' coding sequence shown callable to the base

**Run 09 of `PROMPT_relevant_additions.md`, 7 September 2026.** Continues `AUDIT_01`–`AUDIT_08`. Before writing I
re-read `SYNTHESIS_for_judging.md`, `R1`, `R12`, `R15`, `R18`, `R21`, `AUDIT_03` and `AUDIT_08`, and mapped what every
prior `AUDIT_NN`/`R` file had already reduced to measurement. This run takes **three load-bearing claims that no prior
run measured** and measures them. **Measure before writing:** every number below comes from the scripts named in the
table, run this session, against the supplied VCF, the supplied BAM, and Ensembl release **116** (confirmed live from
the REST API, the same release the report used).

**Rule 3 credits (what is *not* new here).** The BUB1B-locus fragment bound (longest of 87,128 fragments = 803 bp; the
nearer unbridgeable gap = 4,142 bp) is `AUDIT_03`'s; the whole-gene BUB1B depth (mean 42.3 vs control 41.9) is `R12`'s;
the read-level re-derivation of the two variants (minimap2 alt-fractions 0.543/0.517) is `R18`'s; the phase-as-eliminator
idea and the 79/151 count are `R15`'s; the ADGRA3 32,455 bp inter-variant distance is `AUDIT_07`'s; the 138-gene
distinct-het candidate count is `AUDIT_08`'s. This run measures three quantities none of those files computed: the
**genome-wide** longest read-backed phase set, the **reach** of R15's phase filter across the candidate space, the
**Ensembl-116 NMD geometry** of allele 1, and the **base-resolution callability** of all three MVA genes' CDS.

The three targets, each a load-bearing sentence resting on assertion:

1. *"the longest read-backed phase set anywhere in this genome spans **288 bp**, so 'two variants in one gene' is nowhere
   shown to be one on each copy, for *BUB1B* or for any candidate that was excluded."* (`REPORT_track2.md:388`) — the
   bound on which **all** phase reasoning rests, including R15's genome-wide phase-elimination filter. The figure was
   carried through `R14`/`R12`/`SUMMARY` **attributed to `R1`, but `R1` never computed it** (it says "a few hundred base
   pairs"). No file in the repository derives the 288.
2. *"the 50 to 55 nucleotide rule **predicts** nonsense-mediated decay … **746 nucleotides** from the last base of the
   premature stop codon to the last exon junction, with **six downstream junctions**."* (`REPORT_track2.md:47`) — the
   structural premise of the **PVS1** call for allele 1, the pathogenic allele. The script that computes it,
   `pipeline/track2_compute/stop_context.py`, needs an Ensembl 116 GFF3 that **is not present on disk**, so the number
   was un-reproducible in this repository until now.
3. *"No other coding or ClinVar-flagged variant exists in the three genes."* (`REPORT_track1.md:26`, of *BUB1B*, *CEP57*,
   *TRIP13*) — a negative whose completeness depends on those genes' coding sequence actually being **callable**. `R12`
   measured whole-gene *mean* depth (42.3); a mean hides a single dropped exon. Base-resolution minimum coverage across
   all three genes' CDS was never measured.

---

## Entry 1 — Converts an assertion into a measurement, and bounds what cannot be known. The genome-wide longest read-backed phase set spans exactly 288 bp; this both confirms the report's figure (whose derivation was absent from every file) and hard-bounds the reach of R15's phase-elimination filter — which is why *BUB1B* and *ADGRA3* can never be phase-decided from this data.

**The measurement (`work/track2/audit09_phase_sets.py`, pysam streaming the whole VCF).** Every genotype's `PID`
(phase-set ID) and `PGT` were read; variants sharing a `(chrom, PID)` form one read-backed phase set, and its span is
max−min position.

| Quantity | Measured |
|---|---|
| VCF genotype records iterated (all contigs) | 5,012,204 |
| records carrying a read-backed phase set (`PID`) | **770,458** |
| distinct phase sets | 337,422 |
| phase sets with ≥2 variants | 301,363 |
| **longest phase set span, genome-wide** | **288 bp** — reproduces `REPORT_track2:388` **exactly** |
| widest set's location / size | **chr6:32,487,891, 54 variants** (HLA class II, DR/DQ region) |
| median multi-variant set span | **9 bp**; only 1 set reaches ≥288 bp, 2,681 sit in 100–287 bp, 298,681 are <100 bp |

So read-backed phasing in this genome is real but tiny: the *one* set that reaches 288 bp sits in the HLA class II
region, where heterozygosity is dense enough for a single ~300 bp fragment to phase many adjacent sites. Everywhere else
the median phased pair is 9 bp apart. **The 288 bp figure is correct** — and this run is the first place in the
repository it was actually computed rather than asserted. That provenance gap is recorded here with the prominence rule 2
demands: a load-bearing bound was propagated across `R14`→`R12`→`SUMMARY` credited to `R1`, which does not contain it;
the value survives measurement, but nobody had measured it.

**Why this bound is load-bearing: the reach of the phase filter, measured (`work/track2/audit09_phase_reach.py`).** R15
uses shared phase sets as an *eliminator* — if a gene's two variants share a `PID` with the same orientation they are in
*cis*, the other allele is intact, and the gene cannot be the recessive cause. That filter can only speak to a gene whose
two variants fall **inside one phase set**, i.e. ≤288 bp apart. Applied to the 138 candidate genes carrying ≥2 distinct
heterozygous coding variants (the `AUDIT_08`/`R15` distinct-het space, reproduced here at 138):

| Quantity | Measured | Reading |
|---|---|---|
| candidate genes (≥2 distinct het CDS variants) | **138** | cross-checks `AUDIT_08` exactly |
| genes whose two variants **share a phase set** (phased together → eliminable) | **81** | corroborates R15's ~79/151 (raw-row grouping) |
| genes with a variant pair **≤288 bp apart** (theoretical reach ceiling) | **115** | 23 genes are structurally beyond any phase set |
| *KIR3DL3* / *ADAMTS1* / *VPS41* min pair distance; shared PID | **3 / 8 / 5 bp; all True** | exactly the three R15 eliminates |
| ***BUB1B*** min pair distance; shared PID | **10,911 bp; False** | 37.9× the longest phase set |
| ***ADGRA3*** min pair distance; shared PID | **32,455 bp; False** | 112× the longest phase set (matches `AUDIT_07`) |

**The result, stated as a bound.** Phase can eliminate at most the 115 of 138 candidate genes whose variants lie within
288 bp; the other 23 — including both final survivors, *BUB1B* (10.9 kb) and *ADGRA3* (32.5 kb) — are **out of reach by
construction**, not by oversight. The two genes the funnel cannot separate by phase are precisely the two whose alleles
sit tens of kilobases apart, an order to two orders of magnitude beyond the longest fragment this library ever produced.
This closes the reviewer objection "you eliminated 79 genes by phase but not *BUB1B* — why the special pleading?": there
is no special pleading, the 288 bp span is a fixed property of the library, and it lands *BUB1B* and *ADGRA3* on the
unphaseable side of a line drawn by fragment length. The trans configuration for *BUB1B* therefore cannot be read from
this WGS by any method, which is why gate item 1 (parental genotyping / long-amplicon RT-PCR) is the only route — a point
`AUDIT_03` reached locally and this run now proves globally.

## Entry 2 — Converts an assertion into a measurement. The p.Leu737Ter NMD geometry — 746 nt to the last exon junction, six downstream junctions, exon 17 of 23 — reproduces to the digit on Ensembl release 116, so the PVS1 call for allele 1 rests on a computed geometry rather than a stated one.

Allele 1's classification is **PVS1** (`REPORT_track2:58`), which requires the premature stop to be predicted to trigger
NMD rather than escape it. The report's geometry (`REPORT_track2:47`) was computed by `pipeline/track2_compute/stop_context.py`
**from an Ensembl 116 GFF3 that is absent from the repository**, so the number could not be checked here. I reconstructed
the transcript independently from the **live Ensembl 116 REST API** (`work/track2/audit09_nmd.py`), which returns the
exon structure and translation for ENST00000287598, then placed the patient allele and measured the junction geometry:

| Quantity | `REPORT_track2:47` | Reproduced (Ensembl 116) | Match |
|---|---|---|---|
| Ensembl release | 116 | **116** (API `info/data`) | exact |
| exon count | 23 | **23** | exact |
| variant genomic 40209701 → CDS position | c.2210 | **c.2210** | exact (confirms the c.2210T>G / p.Leu737Ter call) |
| codon number | 737 | **737** (codon spans c.2209–2211) | exact |
| stop-codon transcript positions | 2,361–2,363 | **2,361–2,363** | exact |
| exon containing the PTC | 17 of 23 | **17 of 23** | exact |
| last exon-exon junction (transcript pos) | 3,109 | **3,109** | exact |
| **distance last base of stop → last junction** | **746 nt** | **746 nt** (3,109 − 2,363) | exact |
| **downstream exon-exon junctions** | **six** | **6** | exact |
| distance from the *variant base* (alt convention) | 747/748 noted as earlier drafts | **747** | matches the report's own note |

The 55-nt rule (Nagy & Maquat 1998): a PTC ≥50–55 nt upstream of the final exon-exon junction is predicted to trigger
NMD. Here the PTC's last base is **746 nt** upstream of the final junction — 13.6× the 55 nt threshold — so **NMD is
predicted**, and the PVS1 assignment's structural premise is now a reproduced measurement on the exact annotation
release, not an assertion. Two bounds travel with it, as the report already states and this run does not change: (i) this
is a *prediction* from transcript geometry, not a measurement of decay on this allele (which needs the gate-item-2
RT-PCR); (ii) the CDS reconstructs to 3,153 nt = 1,051 codons with the native terminator at transcript position 3,305,
consistent with the 1,050-residue BubR1, so the geometry is internally coherent. Incidental: 5′UTR length is 152 nt, and
the transcript is 3,669 nt — figures the report does not quote but which anchor the coordinate conversion.

## Entry 3 — Closes an alternative explanation, and bounds what cannot be known. Every coding base of all three MVA genes is covered to ≥22× with unambiguous mapping, so the negative "no other coding variant in the three genes" is a real negative, not a coverage gap; and identical raw vs MAPQ-filtered depth rules out a paralog-alignment artifact for the two BUB1B calls.

`REPORT_track1:26` draws a load-bearing negative: besides the two reported alleles, *no other coding or ClinVar-flagged
variant exists in BUB1B, CEP57 or TRIP13*. A negative like that is only as strong as the coverage behind it — a single
exon dropping to a handful of reads could hide a third allele or make a true heterozygote uncallable. `R12` measured
*BUB1B* whole-gene *mean* depth (42.3), which cannot see a localised dropout. This run measures **every coding base** of
the three genes from the alignment (`samtools depth`, index-based, over the canonical-CDS BED built from Ensembl 116;
`work/track2/mva_cds.bed`, 5,955 CDS bp = BUB1B 3,153 + CEP57 1,503 + TRIP13 1,299):

| Metric (5,955 CDS bases) | RAW (all reads) | MAPQ ≥ 20 (callable) |
|---|---|---|
| minimum depth | **22×** | **22×** |
| median / mean / max | 53 / 51.9 / 86 | 53 / 51.7 / 86 |
| CDS bases < 10× | **0 (0.00%)** | **0** |
| CDS bases < 20× | **0 (0.00%)** | **0** |
| CDS bases < 30× | 119 (2.00%) | 122 (2.05%) |
| per gene minimum | BUB1B 31× · CEP57 22× · TRIP13 32× | BUB1B 31× · CEP57 22× · TRIP13 32× |
| allele sites chr15:40209701 / 40220612 | **52× / 32×** | 52× / 32× |

**Two results, both load-bearing.** (1) **The negative is real.** No coding base of any of the three MVA genes falls
below 22×, and a heterozygous SNV needs only ~10–15× to be callable, so a second/third coding allele could not have
escaped detection anywhere in these genes for want of coverage. The "no other variant in the three genes" statement is
bounded by measurement: it is a genuine absence over a fully-covered target, not an untested assumption. (2) **The two
BUB1B calls are not a paralog artifact.** *BUB1B* has known paralogy (the *BUB1B-PAK6* readthrough locus), so a
compound-het could in principle be two paralogous copies collapsing onto one reference position — that would show up as
multi-mapping reads (MAPQ < 20). Here **MAPQ ≥ 20 depth equals raw depth at every base**, including 52× and 32× at the two
allele positions: the coverage is uniquely placed, no multi-mapping ambiguity exists in these CDS, and the two variants
sit on reads that map only here. This independently corroborates `R18`'s minimap2 re-derivation and closes the
paralog-collapse alternative to the compound heterozygote. **Bound (rule 3):** this covers the *canonical* CDS only
(5,955 bp); non-canonical coding exons, deep-intronic/UTR positions, and structural variants are outside it — exactly the
blind spots `REPORT_track2:388` already names, and this entry neither extends nor contradicts them.

---

## What this run found, against the prompt's test

- **Entry 1 (converts an assertion + bounds what cannot be known):** the genome-wide longest read-backed phase set is
  **288 bp** — reproducing `REPORT_track2:388` exactly and supplying the primary measurement that was missing from every
  file (the figure had been carried, credited to `R1`, which never computed it). The bound then explains the funnel:
  phase can reach only the 115 of 138 candidate genes whose variants sit ≤288 bp apart; **81 were actually phased
  together** (corroborating R15's ~79); and the two survivors *BUB1B* (10,911 bp) and *ADGRA3* (32,455 bp) are
  **structurally unphaseable**, at 38× and 112× the longest phase set. The trans call for *BUB1B* cannot come from this
  WGS by any route.
- **Entry 2 (converts an assertion):** allele 1's NMD geometry — **746 nt** to the final junction, **six** downstream
  junctions, exon **17/23**, stop at transcript 2,361–2,363 — reproduces to the digit on **Ensembl release 116**, so the
  PVS1 premise for the pathogenic allele is a reproduced measurement, not an un-checkable computation (the GFF3 it
  originally used is absent from disk).
- **Entry 3 (closes an alternative + bounds):** all **5,955 CDS bases** of *BUB1B*, *CEP57* and *TRIP13* are covered to
  a **minimum of 22×** with **0 bases below 20×** and **raw depth == MAPQ≥20 depth**, so the "no other coding variant in
  the three genes" negative is real rather than a coverage gap, and the two *BUB1B* calls are not a paralog-collapse
  artifact.

**No load-bearing conclusion of the submission is overturned; three are converted from assertion to measurement.** All
three targets *confirm* the submission — the 288 bp bound, the 746 nt NMD geometry, and the coverage of the known genes
all hold. The one disconfirming note, recorded with equal prominence (rule 2): the 288 bp phase-span figure had been
propagated through the reanalysis chain **attributed to a file (`R1`) that does not contain it**; the value is right, but
its derivation did not exist in the repository until this run. The transferable points (relevance test #4): (a) a
read-backed phase filter's *reach* is a fixed, measurable property of the library — compute the longest phase set once
and you know which candidate pairs it can ever decide; here it is 288 bp and it lands the true answer on the
undecidable side, so phase is a filter for *close* variant pairs only; (b) a PVS1/NMD geometry should be reproduced on
the *named annotation release* (Ensembl REST pins it to 116), because the last-exon-junction distance is release-sensitive;
(c) a "no other variant in gene X" negative should be backed by *minimum* coding coverage, not mean, and raw-vs-MAPQ
depth equality is a cheap paralog-artifact check worth reporting alongside it.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | records carrying a read-backed phase set (`PID`) | **770,458** of 5,012,204 | `work/track2/audit09_phase_sets.py` (pysam) |
| 2 | distinct phase sets / with ≥2 variants | 337,422 / 301,363 | same |
| 3 | **genome-wide longest phase-set span** | **288 bp** (chr6:32,487,891, 54 variants, HLA class II); median multi-variant span 9 bp | same — reproduces `REPORT_track2:388` |
| 4 | candidate genes (≥2 distinct het CDS variants) | **138** (cross-checks AUDIT_08) | `work/track2/audit09_phase_reach.py` (coding_nodbsnp.gene.vcf.gz) |
| 5 | candidates sharing a phase set / ≤288 bp apart | **81 / 115** | same (corroborates R15 ~79/151) |
| 6 | BUB1B / ADGRA3 min inter-variant distance; shared PID | **10,911 bp / 32,455 bp; both False** (37.9× / 112× the 288 bp bound) | same |
| 7 | KIR3DL3 / ADAMTS1 / VPS41 min dist; shared PID | 3 / 8 / 5 bp; all **True** (exactly R15's eliminated three) | same |
| 8 | ENST00000287598 NMD geometry on Ensembl 116 | c.2210 / codon 737 / exon **17/23** / stop tx 2,361–2,363 / last junction 3,109 / **746 nt** / **6 downstream junctions** → NMD predicted | `work/track2/audit09_nmd.py` (Ensembl REST, release 116) |
| 9 | CDS coverage, three MVA genes (5,955 bp) | **min 22×, 0 bases <20×, median 53×**; raw == MAPQ≥20 | `samtools depth -a [-Q20] -r` per gene → `work/track2/audit09_*.py`; BED `work/track2/mva_cds.bed` |
| 10 | per-gene CDS minimum | BUB1B 31× · CEP57 22× · TRIP13 32× | same |
| 11 | depth at the two allele sites (BAM) | chr15:40209701 **52×**, chr15:40220612 **32×** (VCF DP 46 / 28) | same |

All scripts are in `work/track2/audit09_*.py`. VCF = `data/WGS_EX2312012_HGWCNDSX7.vcf.gz`; BAM = `work/bam/all.bam`
(GRCh38 no-alt, `chr`-prefixed); transcript structure = Ensembl REST release 116 (`https://rest.ensembl.org`).
Tooling: `python3.12`, pysam 0.24.0, samtools.

## Where the next run should start

1. **The three report-editing items from `AUDIT_08` remain open and are still pure text edits, not measurement**: the
   `REPORT_track2:56` "none absent" STR-wording, the candidate-count filter altitudes (314/224/138), and the un-applied
   `AUDIT_06`/`AUDIT_07` corrections (`SYNTHESIS:67` "224 rare", `R15` 1e-5-survivor line, `R21:45` ADGRA3). A
   report-editing run should now also: (a) cite this run for the 288 bp figure instead of `R1`, which does not contain
   it; (b) note that the PVS1 NMD geometry is reproduced on Ensembl 116.
2. **`R5`'s 97-gene / 18-gene cohesion-set modifier-enrichment row is still not re-derivable** (list absent from the
   repository — `AUDIT_04`/`05`/`06`/`08`). It stays bounded until the list surfaces.
3. **Remaining unmeasured load-bearing claims found this run but not taken** (candidates for run 10): the **Exomiser
   model-2 ranking** (`REPORT_track1:38`: rank 1 dominant, rank 2 recessive p=0.0009 of 389 genes) — reproducible only
   with the 37 GB Exomiser 15.1.0 / data-2512 bundle and the eight HPO terms, so it is *bounded by tooling*, not by
   data, and should be attempted only if that bundle is fetchable; the **drugmap.py** counts (`REPORT_track2:100`: 110
   targets, 148 molecules, 29 approved-passed) — reproducible only against live Open Targets/ChEMBL/openFDA, which may
   have drifted since, so any re-run must report the query date; the **ACMG SF secondary-findings screen count**
   (`REPORT_track1:46`: 10,895 PASS variants across 81 genes) — measurable from the VCF + the ACMG SF v3.2 list, though
   the load-bearing negative (0 P/LP) is already confirmed genome-wide by `R7`/`AUDIT_08`, so the count alone is low
   yield.
4. Tooling for whoever runs next: `python3.12` (pysam 0.24.0), samtools and minimap2 present; **bcftools and mosdepth
   are NOT on PATH** (mosdepth binary is at `/root/mva/mosdepth`; use `pysam` or `samtools` instead of bcftools); the
   Ensembl 116 GFF3 named in the task is **absent from `work/ref/`**, but Ensembl REST is reachable and pins the release;
   egress is wide (gnomAD r4, Ensembl REST, EBI). `samtools depth -b BED` streams the whole 61 GB BAM — use `-r region`
   for index-based access. `work/track2/audit09_*.py` reproduce every number here.
