# V3 — Referee challenges settled against primary sources

Date of check: 2026-09-05. Every quote below was pulled from the primary record
(PMC full text, NCBI eutils, ClinVar API), not from a review or a secondary summary.

Evidence levels used:
- **L1 primary/verbatim** — quoted from the paper's own full text or from the NCBI/ClinVar API.
- **L2 primary/abstract only** — quoted from the publisher-deposited abstract; body text not reachable.
- **L3 secondary** — only reachable via a third party. Flagged explicitly.

---

## Summary table

| # | Claim as it stands | Referee's challenge | Verdict | Correcting sentence to use |
|---|---|---|---|---|
| 1a | LAP-731X rescue shown in Fig 5A–5C | Referee: it is Fig 4A–4C; Fig 5 is R550Q and Y155C | **Referee WRONG. Earlier pass CORRECT.** L1 | "LAP-731X restored mitotic checkpoint activity, chromosome segregation and chromosome alignment in BUBR1-depleted cells (Suijkerbuijk et al., Cancer Res 2010, Fig. 5A–5C); Figure 4 covers the low-abundance mutants (LAP-194X, LAP-753X and the five kinase-domain substitutions), not 731X." |
| 1b | 731X expressed at "1.44 times wild type" | Referee: not in the paper | **BOTH PARTLY RIGHT — 1.44 is real but it is from the 2012 Dev Cell paper (Fig 3D), not from Cancer Res 2010. The 2010 paper gives 2.05 (U2OS) and 3.70 (HeLa).** L1 | "LAP-731X is expressed at 1.44 times wild-type BUBR1 in U2OS cells (Suijkerbuijk et al., Dev Cell 2012, Figure 3D); the 2010 study independently reported 2.05-fold (U2OS) and 3.70-fold (HeLa) (Cancer Res 2010, Figure 2D)." Cite the 2012 paper for 1.44, never the 2010 one. |
| 1c | 731X mRNA only ~2-fold reduced, so if the transcript escaped decay the protein would accumulate | Referee: this argues against the inference | **Referee CORRECT.** The paper reads the 2-fold drop as evidence the mutant transcript is *absent*, not partially present. L1 | "The ~2-fold reduction in BUB1B mRNA in 731X/WT cells is what the authors interpret as complete loss of the 731X transcript (the wild-type allele alone accounting for the residual half), and they attribute the absence of truncated protein to nonsense-mediated decay rather than to protein instability." |
| 1d | 731X encodes 730 aa | Paper says 715 aa | **Both are wrong. The allele is the splice mutation IVS16-2A>G, protein S714fsX731: 714 native BUBR1 residues + 16 frameshift residues, 730 total, stop at 731. The 2010 paper's own supplement contradicts its "715".** L1 | "The 731X allele (IVS16-2A>G, p.Ser714fsTer731) retains 714 amino acids of BUBR1 sequence followed by 16 frameshift-derived residues before a stop at codon 731, giving a 730-residue product of ~81 kDa." |
| 2 | 5-yr OS 85.0% vs 72.4% | Referees: 86.5% vs 73.7% | **Referees CORRECT; manuscript WRONG.** L1 | "5-year overall survival was 86.5% (95% CI 80.2–90.9) with maintenance chemotherapy versus 73.7% (65.8–80.1) without (HR 0.52 [95% CI 0.32–0.86]; p=0.0097); the primary endpoint was disease-free survival, 77.6% (70.6–83.2) versus 69.8% (62.2–76.2), HR 0.68 (0.45–1.02), p=0.061." |
| 3 | BubR1-H/L1002P models a human p.Asn1002Lys variant | Mouse 1002 = human 1012, so no | **Referee CORRECT.** L1 | "Mouse BubR1 residue 1002 corresponds to human residue 1012, so the BubR1-L1002P mouse models the human BUBR1 L1012P substitution and is not a model of a human p.Asn1002Lys variant." |
| 4 | ECG J-point defect attributed to Sieben 2020 BubR1-H/L1002P | Referee: it is North 2014, male BubR1-H/H | **Referee CORRECT.** L1 | "J-point depression was reported in male 3-month-old BubR1-H/H mice (North et al., EMBO J 2014, Fig 5E–5G); Sieben et al. 2020 report no electrocardiography at all, only reduced cardiac stress tolerance on isoproterenol challenge." |
| 5 | ClinVar VCV004600147, Ambry, uncertain significance, Sep 2025 | — | **CONFIRMED.** No record exists for c.3006T>G. L1 | "BUB1B NM_001211.6:c.3006T>A (p.Asn1002Lys) is in ClinVar as VCV004600147, submitted by Ambry Genetics (SCV007198955), classified uncertain significance, last evaluated 19 September 2025; no ClinVar record exists for c.3006T>G." |
| 6 | Welch 2007 and Floquet 2012 support "UGA is the leakiest stop codon and the best readthrough substrate" | — | **HALF-SUPPORTED. Both support the UGA>UAG>UAA readthrough ranking; neither supports "best readthrough substrate" in the drug-response sense, and neither uses the word "leaky".** L1 | "UGA supports the highest readthrough of the three nonsense codons (Floquet et al. 2012, UGA>UAG>UAA for basal and gentamicin-induced readthrough; Welch et al. 2007, same ranking for PTC124-induced readthrough). Responsiveness to a readthrough drug, however, was independent of stop-codon identity, with nucleotide context (−1 U, +4 C) the determinant." |

---

## 1. Suijkerbuijk SJE et al., Cancer Res 2010;70:4891–900 (PMID 20516114, PMC2887387)

### 1(a) Which figure shows the LAP-731X rescue? — **Figure 5A–5C. The earlier pass was right; the referee is wrong.**

The referee's premise ("Figure 5 covers R550Q and Y155C") is only half true. Figure 5 covers *all* the mutants
that do not affect protein stability, which is R550Q and Y155C **plus** the truncations 386X, 483X and 731X.

Results text, verbatim:

> "Surprisingly, the kinase domain did not contribute to chromosome alignment; since LAP-731X has no kinase
> domain yet is fully capable of supporting the microtubule attachment function of BUBR1 ( Fig. 5C ).
> Furthermore, LAP-731X restored the response to nocodazole as well as proper chromosome segregation in
> unperturbed mitosis ( Fig. 5A and 5B )"

Section heading and lead sentence, verbatim:

> "Stable MVA mutants cause direct functional BUBR1 defects and reveal novel aspects of BUBR1's roles in mitosis
> We next examined functionality of the MVA mutations in BUBR1 that have no significant effect on BUBR1 protein
> levels. Again, all mutants were assayed on the capability to rescue mitotic checkpoint defects and chromosome
> misalignment in cells depleted of endogenous BUBR1 (as in Fig. 4A-4C )."

That last clause is almost certainly the source of the referee's confusion: "as in Fig. 4A-4C" refers to the
**assay design**, not to where the 731X data appear.

**Figure 4 legend, verbatim (title + panels):**

> "Fig. 4. Low BUBR1 levels is the primary cause of BUBR1 dysfunction by MVA Mutations in the kinase domain.
>
> (A) Flow cytometric analysis of MPM-2 positivity of U2OS cells transfected with control (Mock) or BUBR1 shRNA
> in combination with control or RNAi insensitive LAP-BUBR1 cDNA, treated with nocodazole for 16 hours. Boxes
> indicate percentage of cells positive for MPM-2. Graph represents the fraction of MPM-2 positive cells of 4N
> population relative to the LAP-BUBR1 WT control (average of at least 3 experiments, ± s.e.m.). (B) Analysis of
> chromosome segregation by live imaging of U2OS expressing H2B-EYFP and transfected as in 4A. Graph indicates
> the fraction of cells with chromosome mis-segregations relative to BUBR1 depleted cells (average of 3
> experiments, a total of at least 238 cells, ± s.e.m.). (C) HeLa cells, transfected as in 4A, were treated with
> MG132 for 90 minutes and analyzed for chromosome alignment. Graph indicates the fraction of cells with
> misaligned chromosomes relative to BUBR1 depleted cells (average of 3 experiments, at least 90 cells counted
> per experiment, ± s.e.m.). (D, upper) Flow cytometric analysis of MPM-2 positivity of U2OS cells transfected
> control (Mock) or BUBR1 shRNA in combination with control or RNAi insensitive LAP-BUBR1 cDNA, substitution
> mutants were overexpressed to levels comparable to wild-type, and treated with nocodazole for 16 hours. Graph
> represents the percentage of MPM-2 positive cells of 4N population. Immunoblot shows the expression of
> wild-type and mutant LAP-BUBR1 in lysates from the same experiment (1 representative experiment). (D, middle)
> Analysis of chromosome segregation by live imaging of U2OS expressing H2B-EYFP and transfected as in 4A. Graph
> indicates the percentage of cells with chromosome mis-segregations (average of 3 experiments, a total of at
> least 270 cells, ± s.e.m.). Immunoblot shows the expression of wild-type and mutant LAP-BUBR1 in lysates from a
> representative experiment. (D, lower) Analysis of chromosome segregation by live imaging of HeLa cells
> expressing inducible BUBR1 shRNA and H2B-EYFP treated with 0, 1 or 1000 ng/ml doxycycline. Graph indicates the
> percentage of cells with chromosome mis-segregations (average of 3 experiments, a total of at least 350 cells,
> ± s.e.m.). Quantitative immunoblot shows the expression of BUBR1 and Tubulin in lysates from a representative
> experiment, band intensity of BUBR1/Tubulin relative to untreated control is indicated (average of 3 experiments)"

Which mutants Figure 4 actually tests, verbatim from the Results:

> "Checkpoint function was restored by expression of wild-type, shRNA-insensitive LAP-BUBR1, but the truncated
> proteins LAP-194X and LAP-753X as well as the five kinase-domain-localized substitution mutants were unable to
> sustain a mitotic delay in response to spindle depolymerization and caused severe chromosome missegregations
> ( Fig. 4B )."

731X is not among them.

**Figure 5 legend, verbatim (title + panels):**

> "Fig. 5. The MVA-associated BUBR1 mutants that do not affect protein stability directly compromise BUBR1
> function.
>
> (A) Flow cytometric analysis of MPM-2 positivity of U2OS cells transfected as in 4A, treated with nocodazole
> for 16 hours. Graph represents the fraction of MPM-2 positive cells of 4N population relative to the LAP-BUBR1
> WT control (average of at least 3 experiments, ± s.e.m.). (B) Analysis of chromosome segregation by live
> imaging of U2OS expressing H2B-EYFP and transfected as in 4A. Graph indicates the fraction of cells with
> chromosome mis-segregations relative to BUBR1 depleted cells (average of 3 experiments, a total of at least 268
> cells, ± s.e.m.). (C) HeLa cells, transfected as in 4A, were treated with MG132 for 90 minutes and analyzed for
> chromosome alignment (left) or cold-stable microtubules (right). Graph indicates the fraction of cells with
> misaligned chromosomes relative to BUBR1 depleted cells (average of 3 experiments, at least 100 cells counted
> per experiment, ± s.e.m.). Insets show representative unattached kinetochore pairs, scale bar is 5μm. (D) HeLa
> cells transfected as in 4A, treated with nocodazole and MG132 for 30 minutes, immunostained for LAP-BUBR1 and
> centromeres (ACA), scale bar is 5μm."

Note that the legends are generic (they do not name the mutants), so the mutant-to-figure mapping has to be read
off the Results text — which is exactly what is quoted above, and it says Fig. 5.

**Independent confirmation from the figure images themselves.** I downloaded the deposited figure files from PMC
(`ukmss-30245-f0004.jpg` and `ukmss-30245-f0005.jpg`) and read the x-axis labels directly. This removes any doubt:

- **Figure 4A** x-axis, left to right: `Mock` | `Mock` | `WT` | `194X` | `753X` | `R727C` | `R814H` | `L844F` |
  `I909T` | `L1012P`. **731X is not on it.** (Panel B carries the same series; panel D is the WT/I909T/L1012P
  overexpression experiment.)
- **Figure 5A, 5B and 5C** x-axis, left to right, identical in all three panels:
  `Mock` | `Mock` | `WT` | `386X` | `483X` | **`731X`** | `Y155C` | `R550Q`. Panel 5D shows kinetochore
  localisation for `WT`, `386X`, `483X`, **`731X`**, `Y155C`, `R550Q`.

So Figure 5 is not "R550Q and Y155C" as the referee states — it carries six constructs, three of them truncations,
and 731X is one of them, in every one of panels A, B, C and D.

**Verdict 1(a): Figure 5A–5C. Evidence level L1 (text + figure image).** Keep the original claim. The referee should be told that
Figure 5 is not restricted to R550Q and Y155C: it also carries 386X, 483X and 731X, and that Figure 4's mutant
panel is 194X, 753X and the five kinase-domain substitutions.

### 1(b) Is "1.44 times wild type" in the paper? — **Not in the 2010 paper. It is in the 2012 paper.**

A full-text search of PMC2887387 (title through references, including all figure legends) for the strings
"1.44" and "1,44" returns zero hits. The only statement about truncation expression levels is qualitative:

> "However most truncations, except LAP-194X and LAP-753X, showed expression levels comparable to or higher than
> wild-type BUBR1 in U2OS and HeLa cells ( Fig. 2D and S1 )."

But the paper **does** quantify it — the numbers are printed on the blot in Figure 2D, not in the running text, so
a text search alone would have missed them. Figure 2D legend, verbatim:

> "(D) Quantitative immunoblot of lysates of HeLa and U2OS cells transfected with wild-type or mutant LAP-BUBR1
> together with pBabe-Puro and selected for transfection by puromycin. **Band intensity of BUBR1/Tubulin relative
> to wild-type is indicated** (average of at least 3 experiments, bands were aligned for visualization purposes,
> full blot is presented in supplemental Figures (S1A))."

Reading the values off the deposited figure file (`ukmss-30245-f0002.jpg`, panel D, "Relative Intensity
BUBR1/Tubulin" row):

| Construct | WT | 194X | 386X | 483X | **731X** | 753X | Y155C | R550Q | R727C | R814H | L844F | I909T | L1012P |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **U2OS** | 1.00 | 0.20 | 2.05 | 3.55 | **2.05** | 0.12 | 1.06 | 0.96 | 0.19 | 0.06 | 0.08 | 0.12 | 0.13 |
| **HeLa** | 1.00 | 1.50 | 5.29 | 3.24 | **3.70** | 0.27 | 0.97 | 0.87 | 0.06 | 0.11 | 0.10 | 0.17 | 0.18 |

**LAP-731X is quantified at 2.05× wild-type in U2OS and 3.70× wild-type in HeLa. Not 1.44× in either cell line,
and 1.44 is not any value anywhere in that panel.** The 1.44 figure is **not in Suijkerbuijk 2010** —
but it is not invented either. **It is in Suijkerbuijk 2012, Dev Cell, Figure 3D.** See Appendix A.

Evidence level L1 (deposited full text searched for "1.44"/"1,44": zero hits; figure panel read from the
deposited image file). One honest caveat: the PMC figure file is 418×601 px and I read the digits from an
upscaled crop. The digits are unambiguous at that magnification, but if the exact 2.05 / 3.70 values are going to
be quoted in the manuscript, confirm them against the publisher PDF.

**So the correct handling is to move the citation, not delete the number.** Anyone who wrote "1.44 times wild
type" and cited Cancer Res 2010 attached the right value to the wrong paper.

### 1(c) The decisive point — does the 2-fold mRNA reduction argue AGAINST "if the transcript escaped decay the protein would accumulate and function"?

Both statements, verbatim, from the same paragraph:

> "None of the truncated proteins, 386X, 731X and 753X, could be detected in lysates of MVA patient cell lines or
> in parental controls ( Fig. 2A )."

> "In patient cells, mRNA from the 386X allele could not be detected and although the relevant parental controls
> are missing, the 2-fold reduction in mRNA levels of 731X/WT relative to healthy controls suggested that
> transcripts from the 731X allele were also absent ( Fig. 3A )."

The underlying numbers, read off the deposited Figure 3A image (`ukmss-30245-f0003.jpg`, "Relative band intensity
of BUBR1/Tubulin" row, fibroblast panel):

| Genotype | WT/WT | WT/WT | **731X/WT** | 731X/Y155C | 753X/R814H |
|---|---|---|---|---|---|
| BUBR1 mRNA relative to healthy control | 1.00 | 0.85 | **0.51** | 0.56 | 0.73 |

**The framing in the challenge misreads the paper.** The paper does not say "731X mRNA is reduced only about
2-fold, therefore some transcript survives." It says the opposite: a 2-fold reduction in a *heterozygous*
731X/WT cell is precisely what you expect if the mutant allele contributes **nothing** and the residual signal is
the wild-type allele alone. The authors state this explicitly — the 2-fold drop "suggested that transcripts from
the 731X allele were also absent." 0.51 is not "only about 2-fold reduced" in the sense the challenge implies;
0.51 is one allele's worth.

What the paper concludes about why the truncated proteins are absent in patients, verbatim:

> "These findings suggested that the premature STOP codons decreased transcript stability and thereby contributed
> to reducing BUBR1 levels. This was in agreement with a previous suggestion that expression of truncated BUBR1
> proteins may be prevented by nonsense-mediated mRNA decay (NMD, see for review ( 28 )) ( 3 ), and supported by
> the finding that both 386X and 731X are expressed when NMD is circumvented by plasmid-driven expression in HeLa
> or U2OS cells."

And the paper's own summary of the mechanism:

> "This indicates that truncations also affected BUBR1 protein levels, although not necessarily by decreased
> protein stability. […] however BUBR1 abundance of truncation mutants is mainly affected on mRNA level."

**So the paper actually SUPPORTS, not contradicts, the inference "if the transcript escaped decay the protein
would accumulate and function"** — that is literally the experiment they ran (plasmid-driven expression bypasses
NMD; 731X protein then appears, and rescues checkpoint, alignment and segregation, Fig. 5A–5C). What the
challenge gets wrong is the *premise*, not the conclusion: it is not the case that "mRNA is only 2-fold reduced
yet protein is absent" is a paradox. In a heterozygote, 2-fold reduced total mRNA = mutant transcript gone. There
is no surviving 731X transcript in patient cells to be reconciled with the absent protein.

Two caveats that a referee is entitled to press, and that should go into the manuscript:
1. The 2-fold measurement is on a **731X/WT parent**, not on the patient (731X/Y155C). The paper says so:
   "although the relevant parental controls are missing".
2. The obvious counter-objection — that the antibody simply cannot see a truncated protein — **is closed by the
   paper**. Figure 2A legend, verbatim: "Antibodies can recognize truncated proteins if overexpressed in HeLa."
   The Figure 2A blot is also explicitly annotated with the expected truncation sizes ("753X (84kDa)",
   "731X (81kDa)", "386X (43kDa)"), i.e. the authors looked for those bands at the right molecular weights and
   found nothing. So the absence of truncated protein in patient lysates is a real negative, not a detection
   artefact.

**Verdict 1(c): the referee's stated premise is not what the paper says. Evidence level L1.**

### 1(d) How many amino acids does 731X encode? — **The paper says 715.**

Verbatim:

> "Second, stable kinetochore-microtubule attachments rely on the central part of human BUBR1 (484-715 (note that
> 731X contains only 715 amino acids of BUBR1 sequence))."

**The paper's own supplement settles it, and the 715 in the main text is off by one.** See Appendix A for the
verbatim Supplemental Table 1 row. In short: the allele is **IVS16-2A>G** (an intron-16 acceptor splice-site
mutation, not a coding indel), and the protein consequence is **S714fsX731**. The supplement prints both the
mutant and wild-type peptide from residue 712:

> `712-ETSGTLLSHHGVHSIADSYX-731` (Mutant)
> `712-ETSENPTQSPWCSQYRRQLL-731` (WT)

Reading that off: E712, T713, S714 are shared with wild type; from residue 715 the mutant diverges
(`GTLLSHHGVHSIADSY`, 16 frameshift-derived residues, 715–730) and terminates at codon 731.

**So: 714 amino acids of genuine BUBR1 sequence + 16 novel residues = a 730-residue product, stop at codon 731.**

That reconciles everything except the paper's own parenthetical. "731X contains only 715 amino acids of BUBR1
sequence" should read **714**. The main text is off by one against its own Supplemental Table 1. The claim
"731X encodes 730 amino acids" is right about the total length but wrong if it implies 730 residues of BUBR1.

The paper also states the general class the mutation falls into:

> "The mutations in BUBR1 associated with MVA fall in two classes: missense or frameshift mutations that result in
> truncated protein products (hereafter referred to as 'truncation'), and missense mutations that cause single
> amino acid substitutions (hereafter referred to as 'substitution')."

**A size corroboration for 715 rather than 730:** the Figure 2A blot annotation gives the expected size of the
731X product as **"731X (81kDa)"**. Full-length BUBR1 (1,050 aa) runs at 120 kDa in the same figure, i.e. ~114
Da/residue, which puts 715 residues at ~81.5 kDa and 730 residues at ~83 kDa. 81 kDa is the figure for the
BUBR1-derived portion.

**Recommendation:** write it as "731X (IVS16-2A>G, p.Ser714fsTer731)" and describe it as "714 amino acids of
BUBR1 sequence followed by 16 frameshift-derived residues, terminating at codon 731". Do not write "a stop at
codon 731 gives a 730-residue BUBR1 protein" — arithmetically right for a clean nonsense codon, wrong for this
allele. And do not simply repeat the paper's "715": it is off by one against the paper's own supplement, and a
referee who checks the supplement will catch it.

---

## 2. Bisogno G et al., Lancet Oncol 2019;20(11):1566–1575 (PMID 31562043) — RMS 2005 maintenance

**The referees are right; the manuscript's 85.0 / 72.4 is wrong.**

Abstract, verbatim (publisher-deposited, retrieved via NCBI eutils efetch):

> "The primary outcome was disease-free survival in the intention-to-treat population. Secondary outcomes were
> overall survival and toxicity."

> "Between April 20, 2006, and Dec 21, 2016, 371 patients were enrolled and randomly assigned to the two groups:
> 186 to stop treatment and 185 to receive maintenance chemotherapy. Median follow-up was 60·3 months (IQR
> 32·4-89·4). In the intention-to-treat population, 5-year disease-free survival was 77·6% (95% CI 70·6-83·2) with
> maintenance chemotherapy versus 69·8% (62·2-76·2) without maintenance chemotherapy (hazard ratio [HR] 0·68 [95%
> CI 0·45-1·02]; p=0·061), and 5-year overall survival was 86·5% (95% CI 80·2-90·9) with maintenance chemotherapy
> versus 73·7% (65·8-80·1) without (HR 0·52 [95% CI 0·32-0·86]; p=0·0097)."

Structured answers:
- **Primary endpoint:** disease-free survival, intention-to-treat.
- **5-year DFS:** 77.6% (95% CI 70.6–83.2) maintenance vs 69.8% (62.2–76.2) no maintenance; **HR 0.68 (95% CI 0.45–1.02); p=0.061** — i.e. the primary endpoint did **not** reach significance.
- **5-year OS (secondary):** 86.5% (95% CI 80.2–90.9) vs 73.7% (65.8–80.1); **HR 0.52 (95% CI 0.32–0.86); p=0.0097**.
- Interpretation as published: "Adding maintenance chemotherapy seems to improve survival for patients with high-risk rhabdomyosarcoma."

**Verdict: 86.5 vs 73.7. Evidence level L2 (publisher abstract via eutils; the Lancet Oncol body text is
paywalled, but these are the abstract's own figures and there is no ambiguity).**

A point worth making in the manuscript, since the numbers are being used to argue for an effect: the trial's
**primary endpoint was negative (p=0.061)**; the 86.5-vs-73.7 gap is the **secondary** overall-survival endpoint.
Citing 86.5 vs 73.7 without saying it is secondary and that the primary missed significance overstates the trial.

---

## 3. Mouse BubR1 1002 vs human BUBR1 1012 — **equivalent. Confirmed.**

Sieben CJ et al., J Clin Invest 2020;130(1):171–188 (PMID 31738183, PMC6934189), Results, verbatim:

> "BUBR1 2211insGTTA, a mutant BUBR1 allele that results in a frameshift and yields an unstable truncated protein
> referred to as BUBR1 X753 , has been identified in 2 biallelic MVA patients, one of which also inherits BUBR1
> 3035T>C, a mutant allele that encodes BUBR1 L1012P ( 2 ). To model this particular patient, we used a previously
> established mouse strain in which we mimicked the BUBR1 2211insGTTA allele ( 21 ) and a new strain in which we
> converted the leucine at position 1002 into a proline (**human L1012 corresponds to mouse L1002**; Figure 1A and
> Supplemental Figure 1, A–C)"

(Bold added; the parenthetical is verbatim from the paper.)

Abstract, verbatim:

> "we mimicked the BUBR1L1012P mutation in mice (BubR1L1002P)"

**Consequence, stated plainly:** the mouse BubR1-L1002P allele is a model of the **human p.Leu1012Pro**
substitution. It is **not** a model of a human p.Asn1002Lys variant. The numeric coincidence between "mouse 1002"
and "human 1002" is a false friend: mouse BubR1 is 10 residues shorter in this region, so human N1002 is mouse
N992, not mouse 1002. Any sentence in the manuscript that presents BubR1-H/L1002P as functional evidence about a
human N1002K variant must be deleted, not softened.

**Evidence level L1.**

---

## 4. The ECG J-point defect — **North 2014, male BubR1-H/H. Not Sieben 2020.**

North BJ et al., "SIRT2 induces the checkpoint kinase BubR1 to increase lifespan", EMBO J 2014 (PMID 24825348,
PMC4194088), Results, verbatim:

> "We next tested whether there was altered cardiac electrocardiography (ECG) in **male BubR1 H/H mice** that was
> influenced by SIRT2. We found that electrophysiology in BubR1 H/H mice was altered including a lengthened
> duration of the QTc interval, the QRS complex, and an increase in amplitude of the R- and P-wave, and a decrease
> in the PR duration (Supplementary Fig S5B–F). However, the most prominent effect was depression of the J-point,
> which represents the approximate end of depolarization and beginning of repolarization (Gussak et al, 1995). We
> observed a suppression of the J-point in ECG tracings (Fig 5 E)."

Figure 5E–5G legend, verbatim:

> "Representative ECG tracings from 3-month-old wild-type, BubR1 H/H , and SIRT2tg / BubR1 H/H mice with inset
> highlighting J-point. Electrocardiography measurements from **male** 3-month-old wild-type ( n = 12), BubR1 H/H
> ( n = 14), and SIRT2tg / BubR1 H/H ( n = 12) mice representing (F) J-point amplitudes and (G) normalization of
> J-point to R-wave amplitude."

**Sieben 2020 contains no electrocardiography at all.** A full-text search of PMC6934189 for "J-point", "J point",
"ECG" and "electrocardio" returns **zero hits**. Sieben's cardiac finding is a pharmacological stress test, not an
ECG, verbatim:

> "To determine whether cardiac stress tolerance might be reduced in BubR1 H/L1002P mice, and if so, whether the
> magnitude of the decline might correlate with the extent of lifespan shortening, we performed an isoproterenol
> challenge test. […] As expected, BubR1 H/H mice were highly sensitive to repeated isoproterenol administration,
> with half of the animals dying within 5 injections ( Figure 7H ). Lethality was also observed in BubR1 H/L1002P
> mice, but to a lesser extent, as 50% of the animals expired after 18 injections and some of the remaining mice
> showed no overt susceptibility."

**Verdict: North 2014, BubR1-H/H, male, 3 months old, Fig 5E–5G. Evidence level L1.**

---

## 5. ClinVar — **VCV004600147 confirmed; no c.3006T>G record exists.**

Queried via NCBI eutils (`esearch`/`esummary`, db=clinvar), 2026-09-05.

**c.3006T>A confirmed:**

| Field | Value (verbatim from the ClinVar API) |
|---|---|
| Accession | `VCV004600147` (version `VCV004600147.1`) |
| Title | `NM_001211.6(BUB1B):c.3006T>A (p.Asn1002Lys)` |
| Protein change | `N1002K` |
| Type | `single nucleotide variant` |
| SPDI | `NC_000015.10:40220611:T:A` |
| GRCh38 | chr15:40220612, band 15q15.1 |
| GRCh37 | chr15:40512813 |
| Germline classification | `Uncertain significance` |
| Last evaluated | `2025/09/19` |
| Review status | `criteria provided, single submitter` |
| Submitter | Ambry Genetics |
| SCV / RCV | `SCV007198955` / `RCV006331804` |
| Condition | `Inborn genetic diseases` (MedGen C0950123) |
| Molecular consequence | `missense variant`, `intron variant` |

**c.3006T>G: no record.** A position-level query (`BUB1B[gene] AND 40220612[chrpos38]`) returns exactly **two**
records at that base, and neither is T>G:

1. `VCV004600147` — `NM_001211.6(BUB1B):c.3006T>A (p.Asn1002Lys)` — Uncertain significance, 2025/09/19.
2. `VCV004842697` — `NM_001211.6(BUB1B):c.3006T>C (p.Asn1002=)` — **Likely benign**, last evaluated 2025/12/17,
   SCV007571611 / RCV006672444. This is the **synonymous** change, not a missense.

So the only two alternative alleles deposited at chr15:40220612 are T>A (missense, VUS) and T>C (synonymous,
likely benign). **c.3006T>G is absent from ClinVar.**

Two things to be careful about in the manuscript:
- Absence from ClinVar is absence of a *submission*, not evidence of absence in the population. Do not write "no
  such variant exists".
- The T>C record shows the same codon is already under submitter attention; if the manuscript argues N1002K is
  novel, it should acknowledge the neighbouring synonymous record.

**Evidence level L1 (NCBI eutils API). Submitter name confirmed from the ClinVar variation page.**

---

## 6. Does Welch 2007 or Floquet 2012 support "UGA is the leakiest stop codon and the best readthrough substrate"?

### Floquet C et al., PLoS Genet 2012;8(3):e1002608 (PMID 22479203, PMC3315467) — **partly yes, with an important limit.**

What Floquet actually measured: readthrough of 66 stop-codon-containing sequences (65 nonsense mutations plus one
natural stop) in NIH3T3 cells, with and without gentamicin, split into 14 UAA, 25 UAG and 27 UGA contexts.

On the **leakiness ranking**, verbatim (Results):

> "After Box-Cox transformation which allowed us to obtain a normal distribution for these 3 variables, an ANOVA
> test revealed that the three groups differed significantly in terms of their basal and induced readthrough
> levels. A LSD test yielded the following hierarchy: **UGA>UAG>UAA** (the sign>represents a statistical
> difference) for both basal and induced readthrough levels ( Table 1 and Table S5 ). This hierarchy is consistent
> with previous reports but, to our knowledge, this study provides the first evidence of a statistically
> significant difference between stop codons. **However, some UAA codons have higher readthrough levels than some
> UGA or UAG codons (i.e. CF 122), highlighting the crucial role of nucleotide context in determining readthrough
> level in the presence or absence of gentamicin.**"

Figure 5 legend, verbatim:

> "Figure 5. Effect of stop codon identity on readthrough levels and the factor of increase.
> Graphical representation of medians (before Box-Cox transformation) for the parameters B, G and I are shown for
> the three different stop codons: UAA, UAG and UGA. The results of the statistical analysis after Box-Cox
> transformation are shown in Table S5 . For basal and gentamicin-induced readthrough levels, the following
> hierarchy of readthrough level was established: UGA>UAG>UAA. (with>indicating a significant difference). For the
> factor of increase, **UGA = UAG = UAA**."

On whether **stop codon identity affected the gentamicin response** — the explicit answer is **no**. Abstract,
verbatim:

> "**The identity of the stop codon did not affect the response to gentamicin treatment.**"

Results, verbatim:

> "Conversely, ANOVA test revealed that the factor of increase did not differ significantly between the three
> groups ( Table S5 ). We show here that the factor of increase, which reflects the capacity of a nonsense
> mutation to respond to treatment, was independent of the nature of the stop codon. The factor of increase
> therefore probably depends only on the nucleotide context of a given nonsense mutation."

What Floquet found to be the actual determinant, verbatim (abstract):

> "We highlight for the first time that the presence of a uracil residue immediately upstream from the stop codon
> is a major determinant of the response to gentamicin. Moreover, this effect was mediated by the nucleotide
> itself, rather than by the amino-acid or tRNA corresponding to the -1 codon. Finally, we point out that a uracil
> at this position associated with a cytosine at +4 results in an optimal gentamicin-induced readthrough, which is
> the therapeutically relevant variable."

**So Floquet supports "UGA is the leakiest stop codon" (median basal and median induced readthrough, UGA>UAG>UAA,
statistically significant). It does NOT support "UGA is the best readthrough substrate" in the therapeutic sense
— the responsiveness to a readthrough drug was identical across the three codons, and nucleotide context (U at
-1, C at +4) beat codon identity on Floquet's own data.** Floquet also gives an explicit counter-example (a UAA,
CF 122, with higher readthrough than some UGA and UAG codons).

**Evidence level L1.**

### Welch EM et al., Nature 2007;447:87–91 (PMID 17450125) — **supports the UGA>UAG>UAA ranking; never uses the word "leaky"; and the ranking is cited, not established, by this paper.**

Welch tested all three nonsense codons. Main text, verbatim:

> "PTC124 promoted dose-dependent readthrough of all three nonsense codons in stable cell lines harbouring
> LUC-190 nonsense alleles. **Levels of suppression correlated inversely with established termination
> efficiencies11,17–19, with the highest readthrough at UGA, followed by UAG and then UAA (Fig. 1a).** Differences
> in transcript levels do not account for the observed differences in readthrough (Supplementary Fig. 3a)."

Cell-free system, verbatim:

> "PTC124 promoted readthrough at each of the nonsense codons (Fig. 1c), showing maximal activity with UGA, while
> having no effect on mRNA levels (data not shown)."

> "Unlike the stable cell line assays (Fig. 1a, b), PTC124 did not discriminate significantly between the UAG and
> UAA mRNAs."

Figure 1 legend, verbatim (cross-checked against the free legend page on nature.com):

> "Figure 1 | PTC124 suppresses premature nonsense codons. a, b, Cultured HEK293 cells harbouring UAA, UAG or UGA
> LUC-190 nonsense alleles were treated with increasing concentrations of PTC124 (a) or gentamicin (b) for 16 h,
> and assayed for luciferase activity. c, d, Synthetic LUC mRNAs, each harbouring different premature termination
> codons, were incubated with HeLa cell-free extract supplemented with varying concentrations of PTC124 (c) or
> gentamicin (d), and assayed for luciferase activity after 4 h. Luminescence ratio, drug-treated:control; error
> bars (±s.d.) are derived from three independent experiments."

On nucleotide context, verbatim:

> "Termination efficiencies are also influenced by the nature of the nucleotide following the nonsense codon (the
> +1 position)18–20. Like gentamicin11, PTC124 was most active when a pyrimidine (in particular cytosine, C) was
> located in the +1 position (data not shown). The UGAG termination context was the only efficiently suppressed
> exception to this trend."

Two things Welch does **not** do:
1. The words "leaky", "leakiest" and "leak" appear **zero times** in the article (main text, figure legends,
   Methods). Anyone citing Welch 2007 for the phrase "the leakiest stop codon" is paraphrasing, not quoting.
2. Welch **cites** the UGA>UAG>UAA termination-efficiency ranking to refs 11, 17–19 — it does not establish it.
   The ranking Welch measures is *PTC124-induced readthrough of a reporter*, which the authors describe as
   correlating inversely with the already-established termination efficiencies. Note also that the compound was
   found by a screen that was **UGA-based from the outset** ("Two high-throughput screens (comprising ~800,000 low
   molecular weight compounds) were performed to identify compounds that promoted UGA nonsense suppression"), so
   a UGA bias in the resulting molecule is partly built into the discovery pipeline, not purely a property of the
   codon.

**Evidence level: L1 for the figure legends (free on nature.com); L1-minus for the main-text sentences — they
come from a third-party PDF mirror of the Nature Letter, whose text matches the free nature.com abstract and all
four figure legends word for word. Supplementary Fig. 3a (the transcript-level control for the codon comparison)
could not be inspected; static-content.springer.com returns 403.**

### Combined verdict on claim 6

The claim "UGA is the leakiest stop codon and the best readthrough substrate" is **half-supported and needs
splitting into two sentences**:

- **Supported:** UGA gives the highest readthrough of the three nonsense codons. Floquet 2012 establishes this
  statistically (UGA>UAG>UAA for both basal and gentamicin-induced readthrough, n=66 contexts, ANOVA + LSD);
  Welch 2007 observes the same ranking for PTC124-induced readthrough and attributes it to previously established
  termination efficiencies.
- **Not supported:** that UGA is therefore "the best readthrough substrate" in a therapeutic sense. Floquet
  explicitly finds gentamicin responsiveness independent of stop-codon identity ("The identity of the stop codon
  did not affect the response to gentamicin treatment"; factor of increase UGA = UAG = UAA), and identifies the
  −1 U / +4 C nucleotide context as the determinant. Welch likewise puts weight on the +1 nucleotide, and his
  compound came out of a UGA-targeted screen.
- **Not supported at all:** the word "leakiest" as a quotation from either paper. Neither uses it.

---

## What this means for the manuscript, in one place

1. **Keep Figure 5A–5C** for the LAP-731X rescue. Add the clarification that Figure 4 tests the low-abundance
   mutants and that "as in Fig. 4A-4C" in the Results is a reference to the assay, not to the data.
2. **Keep "1.44 times wild type" but move the citation.** It is Dev Cell 2012 Figure 3D (U2OS), not Cancer Res
   2010. Say the cell line. If both papers are being cited, note that the 2010 study reported 2.05 (U2OS) and
   3.70 (HeLa) for the same construct.
3. **Rewrite the mRNA/NMD argument.** The 2-fold reduction in a heterozygote is consistent with total loss of the
   mutant transcript, which is what the authors conclude. The manuscript's inference (NMD escape would give
   functional protein) is actually the one the paper's plasmid-driven experiment supports — but the premise as
   currently written misstates the data and hands a referee an easy hit.
4. **Describe 731X correctly: IVS16-2A>G, p.Ser714fsTer731 — 714 residues of BUBR1 plus 16 frameshift residues,
   730 total, stop at codon 731.** Do not repeat the 2010 paper's "715"; it is off by one against its own
   Supplemental Table 1. And note that **731X is a splice-acceptor frameshift, not a nonsense allele** — if any
   part of the manuscript uses 731X in a stop-codon readthrough argument (section 6 above), that argument has no
   premature stop codon to work on and must be dropped.
5. **Correct the RMS 2005 numbers to 86.5% vs 73.7%**, and state that this is the *secondary* endpoint while the
   primary endpoint (DFS) was p=0.061.
6. **Remove BubR1-H/L1002P as evidence about a human N1002K variant.** Mouse 1002 = human 1012.
7. **Reattribute the ECG J-point finding to North 2014, male BubR1-H/H.**
8. **Cite ClinVar as VCV004600147 (Ambry, VUS, 19 Sep 2025)**; note that only T>A and T>C exist at that base and
   that no T>G record has been submitted.
9. **Soften the stop-codon claim.** Floquet supports UGA>UAG>UAA for readthrough *level*, and explicitly refutes
   any effect of codon identity on *drug response*.

---

## Appendix A — Suijkerbuijk 2012 Dev Cell Fig 3D, and the DNA-level identity of the 731X allele

### A1. Where "1.44" actually comes from

Suijkerbuijk SJE et al., "The vertebrate mitotic checkpoint protein BUBR1 is an unusual pseudokinase",
Dev Cell 2012;22:1321–9 (PMID 22698286).

**Access caveat, stated up front.** The published Dev Cell article is closed: not in Europe PMC (`inEPMC: N`), no
PMC record, cell.com returns HTTP 403, the Utrecht repository record ([hdl 1874/272568](https://dspace.library.uu.nl/handle/1874/272568))
is embargoed to 2050-01-01, the Radboud record is metadata-only, and there is no Wayback snapshot of the PDF.
What was used instead is the **author's own open-access PhD thesis**: Saskia Suijkerbuijk, *The role of BUBR1 in
the maintenance of chromosomal stability*, Utrecht University, [hdl 1874/241974](https://dspace.library.uu.nl/handle/1874/241974).
Chapter 4 is this paper, same author line-up, footer "Adapted from Developmental Cell - in Press". Figure 3 and
its legend are on thesis page 64. **Evidence level L1-minus: this is the accepted-manuscript version, not verified
character-for-character against the printed Dev Cell article.**

**Figure 3D, read directly off the 400 dpi page render** — blot of LAP-BUBR1 (YFP over Tubulin), row labelled
"Relative intensity of BUBR1/Tubulin":

| LAP-BUBR1 | WT | **731X** | K795R | D882N | D911N |
|---|---|---|---|---|---|
| Relative intensity BUBR1/Tubulin | 1.00 | **1.44** | 0.50 | 0.98 | 0.45 |

I verified this panel myself from the rendered crop rather than relying on the report of it; the digits are
unambiguous.

Figure 3 legend, verbatim (thesis p. 64):

> "**Figure 3. BUBR1 kinase activity is dispensable for error-free chromosome segregation in human cells.**
> (A, B) Analysis of chromosome segregation by live imaging of HeLa cells expressing H2B-EYFP and transfected with
> control (Mock) or BUBR1 shRNA in combination with control or RNAi-insensitive LAP-BUBR1 cDNA. Graph in A,
> indicates the percentage of cells with chromosome missegregations (average of at least 100 cells in three
> experiments, ±SEM). Stills in B, are from representative cells. Arrowheads point to missegregating chromosomes.
> (C) Flow cytometric analysis of MPM-2 positivity of nocodazole-treated U2OS cells transfected as in A. Graph
> represents the percentage of MPM-2–positive cells of 4N population (average of three experiments, ±SEM).
> **(D-F, I) Quantitative immunoblot of lysates of U2OS cells transfected with wild-type or mutant LAP-BUBR1 or
> LAP-BUB1 together with pBabe-puro and selected for transfection by puromycin. Band intensity of BUBR1 (corrected
> for tubulin) relative to wild-type is indicated (average of at least three experiments).** (G)
> Temperature-dependent denaturation of full length wild-type and K795A GST-BUBR1 monitored by intrinsic protein
> fluorescence, Inset highlights the denaturation range. (H) Immunoblot of lysates HeLa and U2OS cells transfected
> with wild-type or mutant LAP-BUBR1, grown at 27°C and 37°C for 24h."

Note that panel D has **no D-specific sentence** — D, E, F and I share one legend sentence, and the lane
identities live in the figure image, not in the legend. There is no prose sentence anywhere stating "1.44". The
only running text tied to the panel is:

> "Indeed, we found that these mutants, but not D882N/A and 731X, were present in cells in lower levels than WT
> (Figure 3D; Figure S3B)."

**Conclusion for 1(b):** "731X is expressed at 1.44 times wild type" is a **real, sourceable number** — from
**Dev Cell 2012 Figure 3D, U2OS cells**. It is **not** in Cancer Res 2010, which gives 2.05 (U2OS) and 3.70
(HeLa) for the same construct in its Figure 2D. The referee was right that it is absent from the 2010 paper; the
earlier pass was right that the number exists. Fix the citation, keep the number, and say which cell line and
which paper it comes from. If the manuscript needs to survive a hostile check, quote it as "1.44-fold in U2OS
(Dev Cell 2012, Fig 3D)" and note that the 2010 study reported a higher figure for the same construct — the
three values (1.44, 2.05, 3.70) are all above wild type, which is the point being made, but they are not
interchangeable.

### A2. The DNA-level identity of the 731X allele — **IVS16-2A>G, p.Ser714fsTer731**

Source: **Suijkerbuijk et al. Cancer Res 2010, Supplemental Table 1** ("Overview of MVA mutations in BUB1B"),
in `NIHMS30245-supplement-1.pdf`, linked from PMC2887387. I extracted and read the supplement text myself.

Verbatim row (columns: Name | Mutation | Effect | Amino acid sequence | | Allele 2 | Patient cells?):

> `731X       IVS16-2A>G*      S714fsX731    712-ETSGTLLSHHGVHSIADSYX-731 Mutant     Y155C*     Yes,`
> `                                          712-ETSENPTQSPWCSQYRRQLL-731 WT                    Fibroblast`

Neighbouring rows, verbatim, for calibration:

> `483X        IVS10-1G>T      Q467fsX483  465-GDQRNFTCGEHLAGTTSFX-483   Mutant   R550Q   No`
> `             (∆exon11)                  465-GDQQEETMPTKETTKLQIA-483    WT`

> `753X       2211-2insGTTA    S738fsX753   735-PELVKCLCRVVYRRQTNAX-753  Mutant   R814H   Yes, Fibroblast`

Table footnote, verbatim as printed: `* All mutations except those marked with * have been described (Hanks et
al., 2004)`. (The sentence is self-contradictory as printed; from the data, the starred entries — IVS16-2A>G,
1156C>T, R727C, Y155C — are the ones new to the 2010 paper.)

**Three things follow.**

1. **731X is a splice-acceptor mutation, not a coding nonsense codon and not a coding indel.** IVS16-2A>G hits
   the −2 acceptor position of intron 16. The "X" in "731X" is the position of the resulting stop, not a
   substituted codon. Any sentence in the manuscript treating 731X as a nonsense allele — in particular any
   readthrough or stop-codon argument built on it — is built on a wrong premise. **This matters for section 6:
   a splice-acceptor frameshift allele has no premature UGA/UAG/UAA to read through in the first place.**
2. **The residue count is 714, not 715 and not 730.** E712, T713, S714 are shared with wild type; the mutant
   diverges from residue 715.
3. **Hanks et al., Nat Genet 2004 does NOT contain this allele.** The Hanks Table 1 mutation list is 580C-T
   (R194X), 2530C>T (L844F), 2763G-C (Q921H), 2211–2insGTTA (S738fsX753), 2441G-A (R814H), 3035T-C (L1012P),
   IVS10–1G-T, 1649G-A (R550Q), 2726T-C (I909T). No IVS16-2A>G, no 731X, no Y155C. **Suijkerbuijk 2010's
   supplement is the original description of the 731X allele** — cite it there, not to Hanks 2004.

**Modern HGVS coordinate — flagged as a derivation, not a quotation.** Mapping Ensembl BUB1B-201/ENST00000287598
exon coordinates to cDNA, calibrated against ClinVar's own naming of the Hanks IVS10-1G>T allele
(ClinVar VCV000006767 = `NM_001211.6(BUB1B):c.1402-1G>T`, and exon 11 does begin at c.1402): exon 16 = c.2010–2143,
exon 17 = c.2144–2284, therefore **IVS16-2A>G ≈ NM_001211.6(BUB1B):c.2144-2A>G**. This conversion is inferred, not
quoted from any source. It is consistent with S714fs (the last intact codon, 714, ends at c.2142). **Do not put
this coordinate in the manuscript without an independent check against the reference transcript.**

**Database status: the 731X allele is in neither ClinVar nor public LOVD.**
- **ClinVar: absent.** All 2,493 BUB1B ClinVar records were pulled via E-utilities and every title scanned. The
  only acceptor-site variants present are `c.582-1G>A`, `c.36-1G>A`, `c.967-2A>T`, `c.1402-1G>T` (the Hanks 483X
  allele), `c.2285-2A>G`, `c.2386-2A>G`, `c.2851-1G>C`. **There is no c.2144-2A>G.** The nearest records are
  intronic `c.2143+12/13/15/17/19` and the missense `c.2144A>G (p.Glu715Gly)`.
- The **753X** sister allele is likewise effectively absent in that form; the closest ClinVar entries are
  `c.2210del (p.Glu736_Leu737insTer)` and `c.2210T>G (p.Leu737Ter)`, neither of which is the 2211-2insGTTA
  insertion.
- **LOVD (public shared BUB1B instance): absent.** That instance holds 63 BUB1B variants; the nearest are
  `c.2143+6delinsTC` and `c.2143+15C>T`. No intron-16 acceptor variant. Restricted or gene-specific LOVD
  instances were not checked.

### A3. What could not be verified

- The **printed Dev Cell** wording of the Figure 3 legend, and whether the published Dev Cell **supplement**
  contains any other occurrence of 1.44. The thesis version is the best reachable source; treat the legend as
  accepted-manuscript text.
- **Welch 2007 Supplementary Fig 3a** (the transcript-level control behind the UGA/UAG/UAA comparison) —
  static-content.springer.com returns 403.
- Whether IVS16-2A>G appears in any login-gated diagnostic database.
- The exact 2.05 / 3.70 digits in Cancer Res 2010 Fig 2D were read from a 418×601 px deposited image, upscaled.
  Unambiguous at magnification, but worth one confirmation against the publisher PDF if they are to be quoted.

