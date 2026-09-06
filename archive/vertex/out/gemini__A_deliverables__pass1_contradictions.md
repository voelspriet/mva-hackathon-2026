# gemini-3.1-pro-preview / A_deliverables / pass1_contradictions

Here are the pairs of incompatible statements found in the corpus:

**Pair 1**
*   **Statement 1:** "overall survival 85.0% vs 72.4%"
    *   *File:* `track2/research/02_clinical_care_drugs.md`
    *   *Heading:* `4. the index malignancy treatment, and the mitotic-checkpoint problem`
*   **Statement 2:** "5-year overall survival was 86.5% (95% CI 80.2–90.9) with maintenance chemotherapy versus 73.7% (65.8–80.1) without"
    *   *File:* `archive/verify/V3_referee_challenges.md`
    *   *Heading:* `2. Bisogno G et al., Lancet Oncol 2019;20(11):1566–1575 (PMID 31562043) — RMS 2005 maintenance`
*   **What would have to be true for both to hold:** The two sets of percentages would have to refer to different data cuts, different follow-up periods (e.g., one is a 3-year survival rate and the other is a 5-year survival rate), or one is an uncorrected error/typo that was later revised in the literature.

**Pair 2**
*   **Statement 1:** "The accessible record (PMC3532042) is abstract-level and metformin is nowhere in it"
    *   *File:* `archive/referees/referee3_pharmacologist.md`
    *   *Heading:* `2. Validity`
*   **Statement 2:** "Metformin — YES, it was tested. Concentration: 0.5 mM and 1.0 mM in Figure S1A; 1 mM in Table S1."
    *   *File:* `archive/verify/V1_tang_suijkerbuijk.md`
    *   *Heading:* `1(b) Metformin — YES, it was tested. Concentration: 0.5 mM and 1.0 mM in Figure S1A; 1 mM in Table S1.`
*   **What would have to be true for both to hold:** The referee only checked the main text/abstract of the PMC record and missed the supplementary files, whereas the verification pass successfully accessed and read the separate supplementary PDF where the metformin data actually resides.

**Pair 3**
*   **Statement 1:** "The truncation rescue is Figure 4A to 4C; Figure 5 covers R550Q and Y155C, the mutants that do not affect stability."
    *   *File:* `archive/referees/referee1_geneticist.md`
    *   *Heading:* `2. Validity`
*   **Statement 2:** "Figure 5 is not 'R550Q and Y155C' as the referee states — it carries six constructs, three of them truncations, and 731X is one of them, in every one of panels A, B, C and D."
    *   *File:* `archive/verify/V3_referee_challenges.md`
    *   *Heading:* `1(a) Which figure shows the LAP-731X rescue? — Figure 5A–5C. The earlier pass was right; the referee is wrong.`
*   **What would have to be true for both to hold:** The referee misread the paper's text (likely confusing a reference to the *assay design* of Figure 4 with the actual *data* in Figure 5) and failed to check the x-axis labels on the published figures, while the verification pass accurately read the labels directly from the image files.

**Pair 4**
*   **Statement 1:** "Transcript at half with no detectable protein is evidence against 'the therapeutic object is the transcript, not the fold'"
    *   *File:* `archive/referees/referee3_pharmacologist.md`
    *   *Heading:* `3. Logic`
*   **Statement 2:** "a 2-fold reduction in a heterozygous 731X/WT cell is precisely what you expect if the mutant allele contributes nothing and the residual signal is the wild-type allele alone."
    *   *File:* `archive/verify/V3_referee_challenges.md`
    *   *Heading:* `1(c) The decisive point — does the 2-fold mRNA reduction argue AGAINST "if the transcript escaped decay the protein would accumulate and function"?`
*   **What would have to be true for both to hold:** The referee mistakenly assumed the 50% mRNA level meant the mutant transcript was partially stable, whereas the verification pass correctly notes that in a heterozygote, a 50% total mRNA level indicates the mutant transcript is completely absent (0%) and only the wild-type transcript (50%) remains.

**Pair 5**
*   **Statement 1:** "731X yields 'only 715 amino acids of BUBR1 sequence' (2010)."
    *   *File:* `archive/verify/V1_tang_suijkerbuijk.md`
    *   *Heading:* `2(d) Does either paper support the idea that a BUBR1 truncation ending near residue 737 would be functional if it escaped NMD?`
*   **Statement 2:** "The residue count is 714, not 715 and not 730. E712, T713, S714 are shared with wild type; the mutant diverges from residue 715."
    *   *File:* `archive/verify/V3_referee_challenges.md`
    *   *Heading:* `A2. The DNA-level identity of the 731X allele — IVS16-2A>G, p.Ser714fsTer731`
*   **What would have to be true for both to hold:** The authors of the 2010 paper made an off-by-one error in their main text parenthetical compared to their own supplementary sequence data, meaning "715" is a direct quote of a published error, while "714" is the true count derived from the sequence.

**Pair 6**
*   **Statement 1:** "Contradicting evidence on the sirtuin arm: SIRT2 transgenic overexpression did not extend lifespan in a later study (Wu 2023, Aging Cell, PMID 38009412)."
    *   *File:* `track2/research/01_mechanism_models.md`
    *   *Heading:* `4.1 Tested in BubR1 hypomorphic mice`
*   **Statement 2:** "Wu et al. (Aging Cell 2023) tested SIRT2 overexpression on a non-progeroid wild-type background and found no impact on health or lifespan. They explicitly accept the BubR1-hypomorph result and restrict their conclusion to mice where BubR1 is not under-expressed. This bounds the North 2014 finding to the progeroid model rather than refuting it."
    *   *File:* `archive/verify/V2_direction_and_status.md`
    *   *Heading:* `Wu LE et al., Aging Cell 2023 (PMID 38009412) — does it contradict?`
*   **What would have to be true for both to hold:** The first statement uses "contradicting" loosely to mean the intervention failed to extend lifespan in a subsequent study, while the second statement clarifies that the two studies used different genetic backgrounds (progeroid vs. wild-type), meaning they don't actually contradict each other biologically, but rather define the specific context in which the intervention works.

**Pair 7**
*   **Statement 1:** "p.ALLELE_B is not absent from ClinVar (VCV004600147.1, uncertain significance, Ambry, 19 Sep 2025)."
    *   *File:* `track2/research/01_mechanism_models.md`
    *   *Heading:* `2.4 The two alleles in this case, as the databases hold them`
*   **Statement 2:** "c.ALLELE_B is absent from ClinVar."
    *   *File:* `archive/verify/V3_referee_challenges.md`
    *   *Heading:* `5. ClinVar — VCV004600147 confirmed; no c.ALLELE_B record exists.`
*   **What would have to be true for both to hold:** The first statement refers to the *protein* change (p.ALLELE_B) being present in ClinVar due to a different nucleotide substitution (c.POS_BT>A), while the second statement refers strictly to the specific *nucleotide* change (c.ALLELE_B) being absent.
