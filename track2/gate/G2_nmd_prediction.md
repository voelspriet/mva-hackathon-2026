# G2 — Predicted nonsense-mediated decay efficiency of BUB1B c.2210T>G p.(Leu737Ter)

**Variant.** *BUB1B*, ENST00000287598.11 / NM_001211.6 / MANE Select, `NC_000015.10:g.40209701T>G`,
`c.2210T>G`, `p.(Leu737Ter)`, rs759242053, ClinVar VCV000533901.

**Bottom line.** Every line of evidence available points the same way, and for once the tool and the
hand calculation agree without needing to be reconciled.

| Source | Value | Meaning |
|---|---|---|
| **NMDetective-A** | **0.60** | **[computed]** — inside the published "efficiently triggers NMD" bin (>0.52). ~71st percentile of all human coding positions. |
| **NMDetective-B** | **0.65** | **[computed]** — the model's **maximum** leaf value. All four escape tests negative. |
| Hand-applied rules | **10 of 10 predict decay** | [computed] — no published rule rescues this PTC. |
| Measured on this allele | **nothing** | No NMD measurement exists for c.2210T>G in any cell, ever. |

Everything below is labelled **[computed]** (derived in this session from primary files), **[cited]**
(taken from a named publication or database, quoted or numerically transcribed), or **[inferred]**.

---

## 0. Three corrections to the brief, before anything else

These matter because two of them change what can be concluded.

1. **PMID 31768072 is not the NMDetective paper.** It is Van den Eynden et al., "Lack of detectable
   neoantigen depletion signals in the untreated cancer genome," *Nat Genet* 2019;51:1741. The
   correct citation is **Lindeboom RGH, Vermeulen M, Lehner B, Supek F.** "The impact of
   nonsense-mediated mRNA decay on genetic disease, gene editing and cancer immunotherapy."
   *Nat Genet* 2019;51:1645-1651. doi:10.1038/s41588-019-0517-5. **PMID 31659324**, PMC6858879. [cited]
2. **NMDetective-A and -B do not differ in training data.** Both are trained on the same NMD-efficacy
   estimates from matched tumour exome/transcriptome data. The difference is **model class**:
   A is a Random Forest regression, B is a conditional-inference decision tree. The
   aneuploidy/allelic-imbalance framing in the brief is not supported. [cited]
3. **The Suijkerbuijk "731X" allele is new in Suijkerbuijk 2010, not from Hanks 2004.** Its
   Supplemental Table 1 footnote marks 1156C>T (386X), R727C, IVS16-2A>G (731X) and Y155C with an
   asterisk and states "All mutations except those marked with * have been described (Hanks et al.,
   2004)." Do not cite Hanks for 386X or 731X. [cited]

Minor: the brief's Cummings pext PMID (32461652) is Collins et al. gnomAD-SV; Cummings is **32461655**.
Rivas 2015 is **25954003**, not 25954002 (that is Melé et al.). "Teran 2021" is *AJHG* 2021;108:1401,
**PMID 34216550**, not *Nat Commun* and not PMID 34556770. [cited]

---

## 1. The models

### 1.1 Lindeboom, Supek & Lehner 2016 — the rule set

**Lindeboom RGH, Supek F, Lehner B.** "The rules and impact of nonsense-mediated mRNA decay in human
cancers." *Nat Genet* 2016;48:1112-1118. doi:10.1038/ng.3664. **PMID 27618451**, PMC5045715. [cited]

Built on 2,840 high-confidence nonsense mutations with NMD-efficiency estimates, in 1,900 genes from
1,271 patients, using matched tumour exome and transcriptome data. Their regression explained **74%**
of the variance in NMD efficiency from eight features. Reported rules and effect sizes, transcribed: [cited]

| Rule | Reported effect |
|---|---|
| 50 nt EJC boundary | "a sharp decrease towards a complete NMD insensitivity over the 50 nt boundary upstream of the last exon" — **2.2% vs 84.7%** NMD efficiency, p = 5.3e-5 |
| Last exon | PTC ≥50 nt upstream of last junction **84.7%**; PTC in last exon **1.7%** |
| Start-proximal | "PTCs located in the first 100 coding nts are rarely targeted for NMD, followed by a gradual increase up to 200 nt from the start codon" — **35% vs 93%** |
| Long exon | "reduced NMD efficiency when PTCs are located in exceptionally long exons" — **61% vs 98%**, p < 4.8e-9, for exons **>400 nt** |
| Downstream in-frame AUG | **1.9% vs 57%** |
| Distance to normal stop | **99% vs 67%** (top 20% longest PTC-to-normal-stop distances) |
| mRNA half-life | half-life <1 h: **74% vs 1.2%** |
| 3'UTR intron | penultimate-exon PTC with a 3'UTR intron: **7% vs 81%** |

Two notes. The paper states **50 nt**, not "50-55 nt"; the 55 comes from the older EJC literature.
And there is **no distinct "first-exon rule"** in this paper — what it reports is that *intronless*
transcripts escape ("as expected from their lack of deposited EJCs"), and the start-proximal effect
is expressed in nucleotides from the AUG, not in exon index. [cited]

### 1.2 Lindeboom et al. 2019 — NMDetective-A and -B

**Features.** [cited]

- **NMDetective-A** (Random Forest regression): `on_last_exon`, `in_last_50nt_of_penultimate_exon`,
  `rna_halflife`, `distance_to_coding_start`, `exon_length`, `distance_to_downstream_EJC`,
  `distance_to_wildtype_stopcodon`, plus variant allele fraction. Explains **71%** of variance.
- **NMDetective-B** ("fully transparent about the series of tests it performs in a decision tree"),
  four nested tests, explains **68%** of variance:
  1. PTC in the last exon
  2. PTC in the last 50 nt of the penultimate exon
  3. PTC **<150 nt** from the start codon
  4. PTC in a **long exon (>407 nt)**

Note the threshold drift between the two papers: start-proximal is **150 nt** in 2019 (100/200 nt in
2016), and the long-exon cut is the fitted **407 nt** (prose "~400 nt"). [cited]

**Scale and direction — high means strong NMD.** Verbatim: *"Full NMD efficacy would correspond to a
score of 1 (50% decrease in mRNA level due to a heterozygous PTC) and completely inefficient NMD a
score of 0 (no change in mRNA level)."* [cited]

**Published interpretation bins.** *"51% of all possible PTCs in the human genome are predicted to
efficiently trigger NMD (NMDetective-A score >0.52)"* and *"22% of PTCs are predicted not to trigger
NMD (NMDetective-A score <0.25)."* The intermediate 0.25-0.52 band (~27%) is the arithmetic
remainder, not a labelled bin. [cited]

### 1.3 Availability — the score tables are public, and I fetched them

Distribution is **figshare, not GitHub**. Record `https://figshare.com/articles/dataset/NMDetective/7803398`,
DOI `10.6084/m9.figshare.7803398.v1`, GPL-3.0+, author Rik G.H. Lindeboom. The **original source code
was never published** (no code-availability statement in the paper; `github.com/fsupeklab` and
`github.com/supeklab` both 404). What is published is the **precomputed per-nucleotide score track**,
which is what this task needs. [cited]

Downloaded in this session **[computed]**:

| File | figshare id | size on disk |
|---|---|---|
| `hg38_NMDetectiveA_Lindeboom_et_al.v2.gtf.gz` | 17357381 | 54,146,561 B |
| `hg38_NMDetectiveB_Lindeboom_et_al.v2.gtf.gz` | 17357378 | 28,301,643 B |

Format, verified by decompression: GTF over **UCSC knownGene**. `transcript` and `exon` lines carry no
score; each **`CDS`** line carries an `nmd_score` attribute holding one comma-separated value **per
nucleotide** of that CDS block, in transcript order. So it is a genuine per-position score for every
possible PTC position. The integration friction is that it is keyed to UCSC `uc…` accessions, not
Ensembl — handled below.

Not distributed inside dbNSFP, ANNOVAR or gnomAD. The Ensembl **VEP `NMD.pm` plugin** exists and cites
Lindeboom 2016, but it is **not NMDetective**: it emits a binary escape flag with no score, and still
uses the 2016 **100 nt** start-proximal figure. [cited]

### 1.4 Other predictors, for completeness [cited]

- **NMDEscPredictor** — Coban-Akdemir Z, et al. *AJHG* 2018;103:171-187. **PMID 30032986** (the brief's
  30049473 is an unrelated nephrology paper). Rule-based binary escape/no-escape plus a gene-level
  "NMD escape intolerance score".
- **aenmd** — Klonowski J, Liang Q, Coban-Akdemir Z, Lo C, Kostka D. *Bioinformatics*
  2023;39(9):btad556. PMID 37688563. R package, five rules with named defaults (`d_pen = 50`,
  `d_css = 150`, exon >407 bp, last exon, single-exon transcript) — it adopts the 2019 NMDetective-B
  thresholds but returns **rule flags, not an efficacy score**. Its stated edge is handling
  frameshifts and inserted sequence. `github.com/kostkalab/aenmd`.
- **NMDetective-AI** — Veiner M, Toledano I, Palou-Márquez G, Lehner B, Supek F, bioRxiv 2026
  (Europe PMC PPR1218124). Successor from the same lab, genomic language model plus large-scale
  mutational scanning, trained on ~14,000 somatic PTCs. `github.com/Vejni/NMDetectiveAI`. Not used
  here: preprint, not peer-reviewed, and no precomputed track.
- Third-party reimplementation of B: `github.com/oaxiom/NMDetective_B`.

---

## 1.5 THE COMPUTED SCORE

I did not run the original code — it does not exist publicly. I read the authors' own precomputed
per-nucleotide track at the exact genomic position. That is the published model's output for this
variant, not a reimplementation.

### Transcript matching

Two UCSC transcripts carry a CDS block over chr15:40,209,701: **`uc001zkx.5`** and `uc059hpm.1`.
`uc001zkx.5` has **23 CDS blocks that match ENST00000287598 base-for-base** (40161221-40161255,
40165053-40165196, … 40220564-40220756; the last block is 3 nt shorter only because UCSC excludes the
stop codon from the CDS). It is the same transcript under a different accession. **[computed]**

### The values

```
chr15  NMDetectiveA  CDS  40209635  40209775  +   uc001zkx.5  exon_number 17
chr15  NMDetectiveB  CDS  40209635  40209775  +   uc001zkx.5  exon_number 17
```

| Genomic position | Codon | NMDetective-A | NMDetective-B |
|---|---|---|---|
| 40,209,700 (c.2209) | 737, base 1 | 0.60 | 0.65 |
| **40,209,701 (c.2210)** | **737, base 2 — the variant** | **0.60** | **0.65** |
| 40,209,702 (c.2211) | 737, base 3 | 0.61 | 0.65 |

Both transcripts give identical values. Across exon 17, NMDetective-A ranges 0.60-0.62 and
NMDetective-B is a flat 0.65. **[computed]**

### Interpretation scale

- **NMDetective-A = 0.60.** The published bin for "efficiently triggers NMD" is **>0.52**, covering 51%
  of all human PTCs. **0.60 is inside that bin.** [cited threshold, computed score]
- **NMDetective-B = 0.65.** By empirical tabulation of the track, B emits exactly **five** discrete
  leaf values — 0, 0.12, 0.20, 0.41, 0.65 — because it is a four-test decision tree. **0.65 is the
  maximum**, the leaf reached when all four escape tests are negative. There is no higher NMD call
  this model can make. **[computed]**

### Where 0.60 sits genome-wide **[computed]**

I sampled 58,198,057 scored coding nucleotide positions from the hg38 NMDetective-A track:

| Percentile | Score |
|---|---|
| p10 | 0.12 |
| p25 | 0.30 |
| **p50** | **0.54** |
| p75 | 0.61 |
| p90 | 0.63 |

**0.60 sits at the ~71st percentile.** My sample reproduces the paper's published bins almost exactly
— **52.4%** of positions score >0.52 (paper: 51%) and **19.8%** score <0.25 (paper: 22%) — which is
the check that I am reading the file correctly.

### Independent validation that the track behaves as documented **[computed]**

Profiling NMDetective-B across the whole *BUB1B* CDS reproduces the four decision-tree rules exactly:

- **Exon 23 (last exon): 0.00** across all 193 nt — the last-exon rule.
- **Exon 22 (penultimate):** flips 0.65 → 0.20 at chr15:40,218,513, which is **exactly 50 nt** from the
  exon's 3' end — the penultimate-50 nt rule, to the base.
- **Exons 1-2 (start-proximal):** 0.12 until chr15:40,165,166, which is **149 nt** from the CDS start —
  the 150 nt rule, to the base.
- **Exons 3-21, including exon 17: a flat 0.65** — no escape rule fires.

The model is not being extrapolated or approximated. It is being read at the correct base, and it is
returning its strongest decay call.

### Why NMDetective-A is 0.60 rather than 1.0

A reads 0.60, not 1.0, because it is a Random Forest **regression** over noisy tumour data, and its
values are compressed toward the training mean: the gene-wide *BUB1B* NMDetective-A mean is 0.553 and
the observed maximum anywhere in my 58 M-position sample is 1.42, so the nominal 0-1 scale is not
respected at either end. **Do not read 0.60 as "60% of transcript degraded."** The percentile and the
published bin are the safe readings; the raw number is not a fraction. **[computed + inferred]**

---

## 2. The rules, applied by hand

All geometry below is **[computed]** in this session from the Ensembl 116 GFF3
(`work/ref/Homo_sapiens.GRCh38.116.chr.gff3.gz`, records for `ENST00000287598`) and the GRCh38 chr15
FASTA (`work/ref/Homo_sapiens.GRCh38.dna.chromosome.15.fa.gz`). Nothing here is taken from a
database consequence annotation.

### 2.0 The transcript, rebuilt from primary reference files

- 23 exons, transcript length **3,669 nt**.
- CDS **tx 153..3305 = 3,153 nt = 1,050 codons + stop**; the rebuilt CDS begins `ATG` and ends `TGA`,
  matching NM_001211.6.
- chr15:40,209,701 T>G falls in exon rank 17 (chr15:40,209,635-40,209,775).
- Transcript position **2,362** = **c.2210**, the **middle base of codon 737**.
- Wild-type codon 737 read off the genome = **TTA (Leu)**; with c.2210T>G = **TGA**. p.Leu737Ter
  confirmed from sequence, not assumed.
- Stop context: **-1 = G, UGA, +4 = A**; local mRNA c.2207-2215 = `GGAGTGAAGT`. This independently
  reproduces the context in `creative/A_allele_expression_segregation.md`.
- ClinVar confirmed locally from `work/ref/clinvar.vcf.gz`: `15 40209701 533901 T G`,
  `CLNSIG=Pathogenic/Likely_pathogenic`, `MC=SO:0001587|nonsense`, `RS=759242053`.

### 2.1 Full exon table of ENST00000287598.11 **[computed]**

| rank | tx start-end | length (nt) | CDS range | codons | >407 nt? |
|---|---|---|---|---|---|
| 1 | 1-187 | 187 | c.1-35 | 1-12 | no |
| 2 | 188-331 | 144 | c.36-179 | 12-60 | no |
| 3 | 332-391 | 60 | c.180-239 | 60-80 | no |
| 4 | 392-536 | 145 | c.240-384 | 80-129 | no |
| 5 | 537-733 | 197 | c.385-581 | 129-194 | no |
| 6 | 734-903 | 170 | c.582-751 | 194-251 | no |
| 7 | 904-1118 | 215 | c.752-966 | 251-323 | no |
| 8 | 1119-1210 | 92 | c.967-1058 | 323-353 | no |
| 9 | 1211-1440 | 230 | c.1059-1288 | 353-430 | no |
| 10 | 1441-1553 | 113 | c.1289-1401 | 430-468 | no |
| 11 | 1554-1669 | 116 | c.1402-1517 | 468-506 | no |
| 12 | 1670-1719 | 50 | c.1518-1567 | 506-523 | no |
| 13 | 1720-1780 | 61 | c.1568-1628 | 523-543 | no |
| 14 | 1781-1886 | 106 | c.1629-1734 | 543-579 | no |
| 15 | 1887-2161 | 275 | c.1735-2009 | 579-670 | no |
| 16 | 2162-2295 | 134 | c.2010-2143 | 670-715 | no |
| **17** | **2296-2436** | **141** | **c.2144-2284** | **715-762** | **no** |
| 18 | 2437-2537 | 101 | c.2285-2385 | 762-796 | no |
| 19 | 2538-2687 | 150 | c.2386-2535 | 796-846 | no |
| 20 | 2688-2830 | 143 | c.2536-2678 | 846-893 | no |
| 21 | 2831-3002 | 172 | c.2679-2850 | 894-951 | no |
| 22 | 3003-3109 | 107 | c.2851-2957 | 951-986 | no |
| 23 | 3110-3669 | 560 | c.2958-3153 | 987-1051 | **YES** |

**The only exon in the entire transcript longer than 407 nt is the last one.** That single fact
disposes of the long-exon escape rule for every internal PTC in *BUB1B*, this one included.

### 2.2 Rule-by-rule verdict

| Rule | Threshold as published | This variant **[computed]** | Predicts |
|---|---|---|---|
| **50 nt rule** (Nagy & Maquat 1998; 50 nt in Lindeboom 2016) | PTC >50 nt upstream of the last exon-exon junction triggers NMD | Last junction at tx **3,109** (exon 22/23). PTC occupies tx 2,361-2,363. Distance from the **last base** of the PTC = **746 nt**; from the first base = **748 nt**. (The brief's 747 is the same figure under a one-base-different convention.) All three are **~15x** the threshold. | **DECAY** |
| **Nearest downstream junction** | The rule needs only one EJC >50 nt downstream | Nearest downstream junction is the exon 17/18 boundary at tx **2,436**, i.e. **73 nt** downstream of the PTC's last base. Even the closest EJC clears the window. | **DECAY** |
| **Number of downstream EJCs** | More downstream junctions → more efficient decay | **6** downstream junctions (17/18, 18/19, 19/20, 20/21, 21/22, 22/23). | **DECAY** |
| **Last-exon rule** | PTC in the final exon escapes | PTC in exon **17 of 23**; last exon is tx 3,110-3,669. Not applicable. | **DECAY** |
| **Penultimate-exon 50 nt rule** | PTC in the last 50 nt of the penultimate exon escapes | Penultimate exon = 22, tx 3,003-3,109; its last 50 nt = tx 3,060-3,109. PTC at tx 2,361 is **699 nt upstream of that window**. | **DECAY** |
| **Long-exon rule** (>400 nt in 2016 prose, **407 nt** fitted in 2019) | Exon length >407 nt | Exon 17 is **141 nt**, below the median internal exon of this transcript. | **DECAY** |
| **Start-proximal rule** (<150 nt from AUG escapes) | <150 nt | PTC starts at c.2209, i.e. **2,208 nt** downstream of the A of the AUG. **~15x** beyond the window. | **DECAY** |
| **First-exon / intronless rule** | Intronless transcripts escape (no EJCs deposited) | Transcript has 22 introns; PTC is in exon 17. | **DECAY** |
| **Distance-from-start effect** | NMD efficiency rises with distance from the start codon, then plateaus (35% → 93% by 200 nt) | PTC is at **70.1% of the CDS** (c.2209 of 3,153) and **codon 737 of 1,050 (70.2%)**. Deep in the plateau. | **DECAY** |
| **Distance to normal stop** | Longer PTC-to-normal-stop distance → more NMD (99% vs 67%) | **942 nt** from the PTC to the native stop. | **DECAY** |
| **Downstream in-frame AUG / reinitiation** | A close downstream in-frame AUG in good Kozak context permits reinitiation and attenuates NMD (1.9% vs 57%) | There **is** an in-frame ATG at **codon 750**, only **39 nt** downstream (also codons 872, 1019). But its Kozak is `AGACCA-ATG-C`: **-3 = C (pyrimidine, weak)** and **+4 = C (weak)** — both critical positions suboptimal. Decisively, reinitiation requires a **short** upstream ORF (conventionally <30 codons) for the 40S to retain initiation factors; here the upstream ORF is **736 codons**. | **DECAY**; reinitiation effectively excluded |
| **3'UTR intron rule** | A 3'UTR intron rescues a penultimate-exon PTC | The 3'UTR (tx 3,306-3,669, **364 nt**) is entirely within the final exon; there is **no 3'UTR intron**. Rule cannot fire, and would not apply to an exon-17 PTC anyway. | not applicable |

**Result: every applicable rule — 11 of 11 — predicts decay, and none is a marginal call.** The
smallest margin anywhere in the table is the 73 nt to the nearest EJC, still comfortably above 50 nt.
This is a textbook-canonical NMD substrate.

### 2.3 Internal control: the native stop codon **[computed]**

The normal stop (c.3151-3153, tx 3,303-3,305) sits **196 nt into the 560 nt final exon** with **zero**
downstream junctions and a 364 nt 3'UTR. It escapes NMD, as it must — and NMDetective-B independently
scores **0.00** across that exon. The geometry calculation and the track agree on the control.

### 2.4 What is lost if the transcript survives **[computed]**

Codon 737 of 1,050 removes **314 C-terminal residues**: the entire UniProt-annotated kinase domain
(766-1050) plus the linker up to it. Retained: TPR, GLEBS, KEN boxes, ABBA motifs, and the **KARD
(665-682)**, the PP2A-B56 recruitment module. The truncate would be ~82 kDa.

---

## 3. Empirical data: has NMD ever been measured for a *BUB1B* PTC?

**Yes, twice, and both measurements are weak. Neither is on this allele.**

### 3.1 Suijkerbuijk et al., *Cancer Res* 2010;70:4891. PMID 20516114, PMC2887387 [cited]

**Cell lines** (Results §1 + Supplemental Table 1). Four patient lines had cells available:

| Genotype | Cell type |
|---|---|
| absent / I909T | lymphoblastoid |
| 386X / R727C | lymphoblastoid |
| 753X / R814H | fibroblast |
| 731X / Y155C | fibroblast |

Plus parental heterozygote lines **386X/WT** and **731X/WT** and unrelated healthy controls.
(194X/[L844F+Q921H in cis], 483X/R550Q and 753X/L1012P had **no patient cells**.)

**What was measured, and how. Northern blot — not qPCR, not RT-PCR.** Supplementary Methods: total
RNA (RNeasy), 15 µg on 0.8% agarose, GeneScreen membrane, radiolabelled cDNA probes (a 720 bp *BUB1B*
CDS fragment, bp 1-720; α-tubulin bp 1-650), PhosphorImager/Storm 820 quantification. **Fig. 3A**,
BUBR1/tubulin band intensity relative to healthy control, described as "representative of 2
experiments" — **n = 2, no error bars, no statistics.**

**The values, verbatim:**

- Substitution alleles I909T, R727C, Y155C: mRNA "was unaffected". No number given.
- **386X: "In patient cells, mRNA from the 386X allele could not be detected."** Undetectable, not
  quantified.
- **731X: "although the relevant parental controls are missing, the 2-fold reduction in mRNA levels
  of 731X/WT relative to healthy controls suggested that transcripts from the 731X allele were also
  absent (Fig. 3A)."** So the only number for 731X is a **~2-fold reduction in a heterozygous line
  versus unrelated wild-type controls**, from which absence of the mutant allele's transcript is
  *inferred* by the authors, not measured allele-specifically. Note the authors' own internal
  tension: for 386X they say the parental control exists; for 731X they say it is missing.
- 194X, 483X, 753X: "It is, however, unclear what the status of 194X, 483X or 753X is in patient
  cells." No transcript data.

**Protein (Fig. 2A).** "**None** of the truncated proteins, 386X, 731X and 753X, could be detected in
lysates of MVA patient cell lines or in parental controls." The legend states the antibody (rabbit
anti-BUBR1 A300-386A, Bethyl) "can recognize truncated proteins if overexpressed in HeLa", so this is
**not** an epitope-loss artefact. Full-length substitution mutants were down **2-6 fold**; parental
heterozygotes intermediate.

**NMD bypass (Fig. 2D + Fig. S1).** LAP-tagged constructs transfected into HeLa and U2OS: "most
truncations, except LAP-194X and LAP-753X, showed expression levels comparable to or higher than
wild-type BUBR1", and explicitly **"both 386X and 731X are expressed when NMD is circumvented by
plasmid-driven expression in HeLa or U2OS cells."** This is the closest existing evidence that
*BUB1B* truncating transcripts are NMD substrates: the protein is absent from patient cells but
appears when the transcript is supplied from a plasmid.

### 3.2 What the alleles actually are, at nucleotide level [cited, from Supplemental Table 1]

This is where the brief's caution is correct and then some — **only one of the three truncating
alleles is a true nonsense allele.**

| Label | Nucleotide | Protein | Class |
|---|---|---|---|
| **386X** | **1156C>T** | **p.Gln386Ter** | **true nonsense**, coding exon 9 |
| 731X | IVS16-2A>G (modern: c.2144-2A>G, g.40209633A>G) | p.Ser714fsTer731 | **splice acceptor → frameshift** |
| 753X | "2211-2insGTTA" (printed malformed; reconstructs as c.2211_2212insGTTA) | p.Ser738fsTer753 | **frameshift insertion** |
| 194X | 580C>T | p.X194 | nonsense (Hanks 2004) |
| 483X | IVS10-1G>T, Δexon11 | p.Gln467fsTer483 | splice → frameshift |
| "absent" | unknown | "no transcript" | — |

Table 1's WT windows cross-check as standard NM_001211.6 numbering: the 731X window places **R727**
exactly where R727C sits, and the 753X window places **L737** exactly where c.2210T>G sits.

**Is 731X informative for a true nonsense allele? The brief is right to flag it, but the answer is
more useful than a flat no.**

*Against:* it is not a nonsense allele. The transcript is aberrantly spliced before it is terminated,
so the mutant mRNA's own exon structure — and therefore its EJC deposition, the very thing NMD reads —
is not the reference structure. Worse, **the splice product is undemonstrated.** The paper reports
only the predicted consequence and never shows the aberrant transcript. On ENST00000287598, coding
exon 17 is c.2144-2284 = **141 nt, divisible by 3**, so plain exon-17 skipping would be **in frame**
(a 47-residue deletion), not a frameshift. Producing p.Ser714fs therefore requires a cryptic acceptor
or intron retention that nobody has shown. **[computed exon length + cited]**

*For:* if the predicted product is right, the 731X stop lands at **codon 731 — inside exon 17, the
same exon as p.Leu737Ter, 18 nt upstream of it**, with the same 6 downstream junctions. I read
NMDetective at that base: **A = 0.61, B = 0.65**, against **0.60 / 0.65** for our variant. As an NMD
substrate the two are near-identical twins. **[computed]**

*Net:* 731X is a good **positional** analogue and a poor **mechanistic** one. **386X (c.1156C>T,
p.Gln386Ter) is the allele to lean on** — a genuine nonsense codon whose mRNA was undetectable in
patient cells and whose protein reappeared on NMD bypass. It is the real precedent, and the brief
under-weights it.

### 3.3 Hanks et al., *Nat Genet* 2004;36:1159. PMID 15475955 [cited]

Paywalled, not in PMC; **not verified directly.** Five MVA families with "truncating and missense
mutations of *BUB1B*". **No mRNA or NMD measurement is described in the abstract**, and Suijkerbuijk
2010 attributes the prior NMD *suggestion* to Matsuura 2006, not to Hanks — indirect evidence that
Hanks did no transcript work. **[inferred, not verified.]** Its alleles, via the Suijkerbuijk
supplementary footnote: 580C>T (X194), IVS10-1G>T/Δexon11 (Q467fsX483), 2211-2insGTTA (S738fsX753),
plus L844F+Q921H in cis, R550Q, R814H, L1012P, I909T.

**Hanks 2004 contributes nothing to the NMD question.**

### 3.4 Matsuura et al., *Am J Med Genet A* 2006;140:358. PMID 16411201 [cited]

Paywalled, no PMC; abstract only. Seven Japanese PCS families. Verbatim: *"Transcripts derived from
the patients with the 1833delT mutation and the splice site mutation were significantly reduced,
probably due to nonsense-mediated mRNA decay."* Method: RT-PCR plus Western. **No quantitative value
is verifiable** — "significantly reduced" by how much is not in the abstract, and the full text was
not obtainable. Second alleles showed "a modest decrease".

### 3.5 The honest summary of section 3

- **NMD has never been measured for c.2210T>G in any cell, in any paper.**
- The entire empirical base for *BUB1B* PTC decay is **two datasets**: Suijkerbuijk 2010 Fig. 3A
  (Northern, n = 2, semi-quantitative, no allele-specific readout) and Matsuura 2006 (RT-PCR,
  abstract-level only). Neither is allele-specific; neither has statistics.
- The strongest single piece of evidence is not the mRNA blot at all. It is the **protein
  disappearance/reappearance pair**: truncated BubR1 absent from patient lysates (Fig. 2A) but
  expressed from a plasmid (Fig. 2D, S1). That is a clean NMD signature, and it holds for 386X, a
  genuine nonsense allele.
- Bounded negative: an open-access search found no third *BUB1B* PTC transcript measurement, but
  coverage was not exhaustive.

---

## 4. Large-scale evidence

### 4.1 gnomAD v4 constraint for *BUB1B* [cited, gnomAD GraphQL API]

Gene ENSG00000156970; canonical **and** MANE Select transcript **ENST00000287598** — the constraint
applies to exactly the transcript in question.

| Metric | Value |
|---|---|
| **pLI** | **5.52e-17** (effectively 0) |
| o/e LoF | 0.624 |
| o/e LoF 90% CI | 0.525 - 0.747 |
| **LOEUF** | **0.747** |
| Observed LoF | **86** |
| Expected LoF | 137.74 |
| LoF z | 3.74 |
| o/e missense | 0.914 (0.870-0.960); obs 1130 / exp 1236.9 |
| missense z | 1.297 |
| o/e synonymous | 1.005 (obs 420 / exp 417.9); syn z -0.061 |

*(gnomAD v2.1.1 for contrast: pLI 7.0e-10, o/e LoF 0.420 (0.309-0.580), obs 27 / exp 64.2.)*

**What this implies.** pLI ≈ 0 means the data give essentially **no support for haploinsufficiency**;
86 LoF variants are actually observed in the population. LOEUF 0.747 is a mild depletion — non-neutral
(LoF z 3.74, upper CI below 1) but far above the LOEUF <0.35 decile that flags haploinsufficient
dominant-disease genes. Missense constraint is essentially absent (z 1.30). The synonymous calibration
is clean (o/e 1.005, z -0.06), so the LoF depletion is not a model artefact.

This is **the expected signature of a recessive disease gene**: heterozygous carriers are healthy and
circulate at appreciable frequency, so purifying selection acts only weakly on the heterozygote. It is
fully consistent with 115 healthy heterozygotes for this allele. **It resolves the "115 carriers"
worry at the level of the gene, not at the level of the variant.**

**Critical caveat.** LOEUF and pLI say **nothing whatsoever about whether an individual PTC escapes
NMD.** They are selection metrics over carriers, not molecular measurements. Do not use them either
way in this argument.

### 4.2 gnomAD v4, the variant itself, 15-40209701-T-G [cited]

| | AC | AN | AF | Hom |
|---|---|---|---|---|
| Exomes | **115** | 1,461,846 | **7.867e-5** | **0** |
| Genomes | 5 | 152,174 | 3.286e-5 | 0 |

Variant-level `flags`: **empty** — no low-complexity, no segdup, no discrepant-frequency flag.
**FILTER = PASS** in both exomes and genomes. **LOFTEE: high-confidence (HC)** on both annotated
transcripts, with **no `lof_filter` and no `lof_flags`** (ENST00000287598 c.2210T>G p.Leu737Ter
stop_gained HC; ENST00000412359 c.2252T>G p.Leu751Ter HC).

**Essentially European-specific.** Exomes: nfe 111/1,111,986 (AF 9.98e-5); all of afr, amr, asj, eas,
fin, mid, sas have **AC = 0**. Genomes: nfe 5/68,028, all others 0.

**Zero homozygotes carries no statistical weight on its own**: expected homozygotes ≈ AN × AF² ≈ 0.009.
Their absence is what chance predicts. **[computed from the cited AC/AN]**

Note the tension worth stating plainly: Invitae's ClinVar comment calls the population frequency at
this position "unreliable, as metrics indicate poor data quality", but **gnomAD v4 shows PASS with no
flags and LOFTEE HC**. The frequency looks real.

### 4.3 pext — available, high, and the wrong tool for this question [cited]

**Cummings BB, et al.** "Transcript expression-aware annotation improves rare variant interpretation."
*Nature* 2020;581:452-458. **PMID 32461655**, PMC7334198. pext = the isoform-expression-weighted
fraction of a gene's total expression coming from transcripts in which a given base is coding,
computed per base from GTEx isoform quantifications (11,706 samples). Headline: expression-based
filtering removed **22.8%** of falsely annotated pLoF variants in haploinsufficient disease genes
while removing **<4%** of high-confidence pathogenic variants.

**Value here.** gnomAD's pext regions for *BUB1B* align to CDS exon boundaries, and coding **exon 17 =
chr15:40,209,635-40,209,775** — the exon containing our base — has **mean pext = 0.784** (GRCh38).
On GRCh37 the containing region has mean pext = 0.852. No pext flags on the gene.

**What that does and does not tell us.** It tells us the exon is **constitutively included**: ~78-85%
of *BUB1B* transcriptional output contains this base, so p.Leu737Ter is **not** the "pLoF in a poorly
expressed exon" false positive pext was built to catch, and the Cummings filter would **retain** it.
It tells us **nothing about NMD.** pext measures which isoforms are transcribed, from **reference-allele**
expression in GTEx individuals who overwhelmingly do not carry this variant. It has no allele-specific
component and no read-out of transcript degradation. Using high pext to argue the mutant transcript
survives — or that it is destroyed — is a category error. **[inferred]**

### 4.4 The one large-scale dataset that genuinely bears on this: allele-specific expression of PTCs

This is the honest counterweight to sections 1 and 2, and it is the reason the decision table below
is not a formality.

**Rivas MA, et al.** "Effect of predicted protein-truncating genetic variants on the human
transcriptome." *Science* 2015;348:666-669. **PMID 25954003**, PMC4537935. 1,814 PTVs, 635
individuals, GTEx + Geuvadis, Bayesian ASE classification. [cited]

- Rare nonsense SNVs **predicted to trigger** NMD by the 50 bp rule show ASE in **69.5%** of cases
  (n = 287); predicted **escapees** in **31.9%** (n = 158); synonymous baseline **7.9%** (n = 25,233).
  All P < 0.001. Fig. 2A.
- **Among rare nonsense variants predicted to trigger NMD, 30.5% showed no ASE in any tissue.**
  48.3% moderate ASE across all tissues, 3.3% strong across all, **17.9% heterogeneous across
  tissues**, 8.1% single-tissue. Fig. 2D-F.
- Their model beats the bare 50 bp rule: AUC **80.8%** (95% CI 77.3-84.4) vs **72.9%** (69.3-76.5).
- **No dosage compensation:** heterozygous PTV carriers do not up-regulate the intact allele
  (P = 2.90e-9 across 53 strong-ASE nonsense PTVs). *Directly relevant: the p.Asn1002Lys allele will
  not be up-regulated to compensate.*

**Teran NA, et al.** "Nonsense-mediated decay is highly stable across individuals and tissues."
*AJHG* 2021;108:1401-1408. **PMID 34216550**, PMC8387471. GTEx v8, 2,320 rare PTVs, 809 individuals,
49 tissues, 40,402 variant-tissue-subject observations. [cited]

- Empirically, **52%** of predicted-target observations showed allelic imbalance vs **20%** of
  predicted escapees. **Roughly half of predicted NMD targets show no measurable imbalance.**
- **"Unpredicted allelic balance":** of the 2,320 PTVs, **23.4% (543)** showed it at least once, and
  **7.5% (173)** showed it in **>90% of observations**. That 7.5% is the cleanest estimate of
  consistent, reproducible NMD escape among variants the rules say should be degraded.
- **Tissue variance is small.** Adding tissue did not improve the model; adding individual made it
  worse. Within 50 nt-rule targets, tissue predicted NMD poorly (best AUC 0.56). Median cross-tissue
  correlation of allelic ratio within an individual: 0.508 for PTVs (0.552 for predicted targets),
  vs 0.131 synonymous.
- **Practically useful:** **fibroblasts predict other tissues' NMD category with balanced accuracy
  0.767** (vs 0.728 for their genomic model); whole blood 0.745. **A patient fibroblast line is an
  empirically validated surrogate for measuring NMD of this allele** — which matters, because the
  731X/Y155C MVA line is a fibroblast line and fibroblasts are the obvious biopsy.
- Also predictive beyond position: allele frequency (**ultra-rare and singleton PTVs show *more*
  imbalance**, and the effect does not plateau). Our variant at AF 7.9e-5 is rare, which pushes
  marginally *toward* efficient decay.

**The number to carry forward:** the prediction here is as strong as the models can make it, but the
base rate of escape among confidently predicted NMD targets is **not negligible — somewhere between
7.5% (consistent escape, Teran) and 30.5% (no ASE in any tissue, Rivas)**, depending on how escape is
defined. That is the residual uncertainty on a 0.60/0.65 call, and it is empirical, not hand-waving.

---

## 5. What each answer would mean

| | **A. NMD efficient** (predicted; all rules and both models agree) | **B. NMD partial** (allele-specific expression 20-50% of WT) | **C. NMD inefficient / escape** (the 7.5-30% tail) |
|---|---|---|---|
| **What the allele contributes** | Nothing. An effective null. The child's entire BubR1 pool comes from the p.Asn1002Lys allele, and per Rivas that allele will **not** be up-regulated to compensate. | A minority of transcript survives and may be translated to a 736-residue product. | A ~82 kDa kinase-domain-less BubR1 is present at appreciable level. |
| **Dosage model** | **Firm.** MVA1 in this child is a quantitative-insufficiency disease with one hypomorphic missense allele carrying the whole load. Matsuura 2006's ">50% decrease in BubR1 is involved in the syndrome" applies directly. | Model holds, but the denominator changes and the truncate may add or subtract function. | The dosage framing is **wrong for this allele**. The question becomes what the truncate *does*, not how much protein there is. |
| **Readthrough (ataluren, aminoglycosides)** | **The substrate is being destroyed before the drug can act.** Readthrough needs a ribosome to reach the PTC on an intact mRNA. If NMD removes the message, a readthrough agent has nothing to read through. **NMD inhibition becomes the mandatory upstream step**, not an optional adjunct. | A real substrate pool exists. **Amlexanox** — which inhibits NMD via UPF1 phosphorylation *and* promotes readthrough — becomes the single most rational candidate. | Readthrough is directly testable alone. But note the codon context is only mid-favourable: UGA is the leakiest stop, yet **-1 = G is the weakest -1 class** (Floquet 2012) and **+4 = A** ranks below C. |
| **NMD inhibition (cardiac glycosides, amlexanox, SMG1 brakes)** | Becomes the **enabling step for everything else**, and a standalone hypothesis: stabilise the transcript, get a truncate, see whether the truncate helps. | Already partly achieved; marginal gain from a drug is smaller. | Pointless as a lever. The transcript is already there. |
| **Therapeutic object** | An allele that makes no protein. Either restore the transcript, or forget this allele and work on the *missense* allele's stability (chaperone arm) and on downstream aneuploidy. | Ambiguous. Measure the truncate before choosing. | A protein that exists and may be partly functional — or a **dominant negative** on MCC assembly. |
| **First experiment** | **Allele-specific ddPCR at c.2210 in patient fibroblasts**, ± cycloheximide or UPF1 knockdown. A c.2210G fraction rising from near 0 toward 0.5 on NMD block is the direct proof. Teran 2021 validates fibroblasts as the surrogate tissue (balanced accuracy 0.767). | Same assay; quantify the plateau. | Immunoblot for a ~82 kDa band with an epitope-mapped N-terminal antibody (A300-386A detects truncates, per Suijkerbuijk Fig. 2A legend). |

### 5.1 The Suijkerbuijk counterfactual, and its boundaries

Branch C is not automatically bad news, and that is worth stating precisely. **Suijkerbuijk 2010
Fig. 5A-5C** [cited]: RNAi-insensitive **LAP-tagged** BubR1 truncations co-transfected with *BUB1B*
shRNA (the transient-replacement scheme of Fig. 4A).

- **5A** — U2OS, flow cytometry, MPM-2 positivity of the 4N population after 16 h nocodazole
  (checkpoint). LAP-731X **restored the nocodazole response**.
- **5B** — U2OS + H2B-EYFP, live imaging of unperturbed mitosis. LAP-731X **restored proper
  chromosome segregation**.
- **5C** — **HeLa**, 90 min MG132, chromosome alignment (left) and cold-stable microtubules (right).
  Verbatim: *"LAP-731X has no kinase domain yet is fully capable of supporting the microtubule
  attachment function of BUBR1."*
- Contrasts in the same figure: LAP-386X restored nothing and never reached kinetochores (5D);
  LAP-483X restored the checkpoint (5A, 5B) and localised (5D) but could **not** rescue alignment (5C).

Supported by **Suijkerbuijk 2012** (*Dev Cell* 22:1321, PMID 22698286): human BUBR1 catalysis is
dispensable; removing the kinase domain did not affect error-free segregation.

**The boundaries, stated plainly, because this is the most over-extrapolated result in the file:**

1. **HeLa and U2OS replacement assays.** Endogenous BubR1 knocked down, construct supplied ectopically
   from a plasmid at experimenter-set, non-physiological level. A cell-line complementation
   experiment, not a model of the disease.
2. **No organism was made.** No mouse, fly or organoid carries a kinase-domain-less BubR1 as its only
   allele. The whole-animal phenotypes of BubR1 insufficiency (Baker 2004 onward: aneuploidy,
   senescence, progeroid pathology, dwarfism, infertility) were never tested against this construct.
3. **No construct terminating at 737 was ever tested.** The tested truncation was LAP-731X, described
   by the authors as containing "only 715 amino acids of BUBR1 sequence" — i.e. BubR1 1-714 plus a
   **frameshift-derived 16-residue tail** to a stop at 731. A construct stopping cleanly at 736 is a
   *different molecule*: 736 native residues, no foreign tail. The 6-codon difference is probably
   immaterial; the foreign tail may not be. Neither has been shown.
4. **The 731X patient allele and the LAP-731X plasmid are two different objects that share a name.**
   The patient allele is a splice variant whose actual transcript was never demonstrated. The
   plasmid is a defined ORF. Do not let the shared label carry an inference across.
5. **Expression level was set by the experimenter.** A truncate that rescues when supplied at or above
   wild-type level says nothing about a truncate present at whatever fraction survives NMD.
6. **Nothing in that work tests dominant-negative behaviour** — the specific risk of deliberately
   stabilising a truncated MCC component in a checkpoint-weak child.

### 5.2 Confidence, itemised

| Claim | Confidence | Basis |
|---|---|---|
| The geometry predicts efficient NMD | **High** | [computed] 11/11 rules; NMDetective-A 0.60 (>0.52 bin, p71); NMDetective-B 0.65 (maximum leaf) |
| NMD is in fact efficient on c.2210T>G in this child's cells | **Untested** | No measurement exists. Empirical escape base rate among predicted targets is 7.5-30.5% [cited: Teran 2021, Rivas 2015] |
| *BUB1B* truncating transcripts are NMD substrates as a class | **Moderate** | [cited] Suijkerbuijk 2010: 386X mRNA undetectable, protein absent from patient lysates but expressed on plasmid bypass. n = 2 Northern, no allele-specific assay |
| The allele is disease-causing in a patient sense | **Weakest link, and independent of the NMD question** | ClinVar 2-star but reasoning from mechanism; no published MVA patient carries it; 115 gnomAD heterozygotes, LOFTEE HC, PASS, no flags |
| A truncate would be functional if it existed | **Low** | [cited] HeLa/U2OS overexpression rescue only; no organism; no 737 construct; dominant-negative untested |

---

## Files and reproducibility

- Score tracks: `hg38_NMDetectiveA_Lindeboom_et_al.v2.gtf.gz` (figshare file 17357381) and
  `hg38_NMDetectiveB_...` (17357378), from DOI 10.6084/m9.figshare.7803398.v1.
- Read at `chr15:40,209,701`, CDS block `40209635-40209775`, transcript `uc001zkx.5`
  (= ENST00000287598 by exact CDS-block identity), `exon_number 17`.
- Geometry recomputed from `work/ref/Homo_sapiens.GRCh38.116.chr.gff3.gz` and
  `work/ref/Homo_sapiens.GRCh38.dna.chromosome.15.fa.gz`.
- ClinVar confirmed from `work/ref/clinvar.vcf.gz`.
- Track behaviour validated against its own documented rules: NMDetective-B flips at exactly 50 nt
  from the penultimate exon's 3' end and at 149 nt from the CDS start, and is 0.00 across the last exon.
