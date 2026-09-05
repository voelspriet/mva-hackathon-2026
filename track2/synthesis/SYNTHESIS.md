# Synthesis: what this project established, what it did not, and what the review process was worth

Produced under `track2/audit/PROMPT_C_synthesis.md`, after the five audit partitions and both cross-model passes. No care recommendation is restated here; those live in `REPORT_track2.md`. Nothing in this file is a new claim about the world.

---

## Part 1. What the project established

Ordered by how much would have to be retracted if it were wrong.

### 1. The two variants, and that they are the answer to Track 1

**Claim.** The child carries *BUB1B* c.2210T>G p.Leu737Ter with c.3006T>G p.Asn1002Lys, and that pair is the causal genotype for mosaic variegated aneuploidy.

**Tier: measured in this project, and independently confirmed.** The pair was called from the proband's own VCF by `pipeline/run.sh`, scored 100.0 rank points and F-max 1.000 against the challenge's own scorer, and ranks first genome-wide under phenotype-driven prioritisation with no gene list supplied (Exomiser 15.1.0, `pipeline/exomiser_analysis.yml`).

**Files.** `REPORT_track1.md`, `submissions/`, `work/exomiser/results/`. It survived every layer, including the audit partition on genetics and databases, which retrieved both ClinVar and gnomAD records live.

**Falsified by.** Trio genotyping showing the two variants in cis, or a third variant elsewhere that better explains the phenotype. The first is a real possibility and is the reason phase heads the gate.

### 2. Phase is unproven, and the report says so

**Claim.** The trans configuration is favoured but has never been demonstrated in this family.

**Tier: computed here, and declared as unresolved.** The Bayesian treatment in `track2/creative/F_math.md` section 1 puts the posterior above 0.98 across the plausible range of co-occurrence enrichment, and collapses to 0.32 at the hard ceiling where every copy of the rarer allele sits on a Leu737Ter background. The calculation cannot settle phase, and says so in its own reading.

**Falsified by.** Nothing in this project can falsify it. A trio or a long-read amplicon replaces the whole table, which is why the gate asks for one.

### 3. No approved medicine acts on BubR1

**Claim.** There is no marketed drug whose mechanism raises, stabilises or substitutes for BubR1, so the repurposing question has no direct answer.

**Tier: measured in this project, by a tool that reports against itself.** `pipeline/track2_drugmap/` maps gene and mechanism to ranked approved drugs with an openFDA label harm screen. Its own top-ranked hit pointed the wrong way, and that is documented rather than removed.

**Files.** `REPORT_track2.md` sections 5 to 7, `track2/creative/E_drugmap*.md`.

**Falsified by.** A drug acting on the spindle assembly checkpoint reaching approval, or an existing agent shown to raise BubR1 protein at reachable exposures. Neither exists now.

### 4. What survives is a drug-avoidance rule, surveillance additions, a renal work-up and a measurement gate

**Claim.** The useful output is negative and procedural rather than therapeutic: avoid elective aneugens and calciuric agents, with a carve-out that protects cancer treatment; add four surveillance items that cost nothing; work up the kidney before any renal drug, because two competing causes call for opposite prescriptions; and run one measurement gate led by an RT-PCR returning NMD efficiency and allele-specific expression together.

**Tier: inference from primary pharmacology, with the carve-out as the safety-critical element.** No part of it is measured in this child. The carve-out is written to state intent rather than to list drug names, because a closed list protects only what it names.

**Falsified by.** Evidence that MVA or *BUB1B* patient cells are not differentially sensitive to aneugens, which would remove the rule's premise. No MVA patient-derived line has been tested against any spindle agent, so this is open in both directions.

### 5. Allele 1's therapeutic object is the transcript, not the protein fold

**Claim.** p.Leu737Ter is predicted to trigger nonsense-mediated decay, so there is no misfolded protein to rescue.

**Tier: predicted by rule, supported indirectly, never measured on this allele.** The stop sits 747 nucleotides upstream of the last exon junction with six downstream junctions, which the 50 to 55 nucleotide rule predicts will trigger decay. The indirect support is that a different truncating allele's transcript was undetectable in patient cells, and that a heterozygous parent carried about half the normal transcript.

**Falsified by.** The gate's own RT-PCR. This is the single claim in the report most cheaply testable, which is why it leads the gate.

### 6. The sequenced tissue carries no large mosaic aneuploid clone

**Claim.** Blood carries no whole-chromosome mosaic aneuploidy above roughly 10 percent of cells per segment, or about 4 percent for a single clonal trisomy on a large autosome.

**Tier: computed here, from the VCF's own allele depths.** The detection model and its floors are in `track2/creative/F_math.md` section 2 and reproduce from `pipeline/track2_math/f_math.py`.

**Falsified by.** Not much, and that is the point: the bound is weak against genuinely variegated burden, where clearing the floor on any one chromosome needs about 58 percent total burden spread over five.

### 7. Two attractive candidates were removed on evidence

**Claim.** Metformin and dasatinib do not survive, and were struck from the ranked list rather than demoted.

**Tier: measured in primary sources.** Metformin's tested concentrations sit 32 to 130 fold above paediatric plasma, and still 12.9 to 25.8 fold above at the toxicological ceiling. Dasatinib fails on three independent grounds.

**Falsified by.** A metformin concentration-response in human cells at reachable exposures, which does not exist.

---

## Part 2. What the project failed to establish

### 2a. Answered in the negative

These are results, not gaps. They cost real work and they close real options.

- **Metformin as a prescription.** The exposure gap cannot be closed by dose, salt or formulation for a fibroblast or lymphocyte target.
- **Dasatinib as a senolytic.** The rationale rests on genetic clearance in a mouse, which is not a drug; the growth signal is real and prepubertal; and the immune objection points the wrong way for a child whose aneuploid compartment may be under immune restraint.
- **Chaperone inducers, chemical chaperones and rapalogs.** They buy tolerance of aneuploidy, not correction of it.
- **Growth hormone and mecasermin outside the endocrine gate.** No MVA1 efficacy data, and a labelled contraindication with a malignancy history.
- **Ataluren.** Not authorised outside Great Britain, and in any case allele 1 offers no premature stop codon argument once 731X is understood correctly.

### 2b. Unreachable

Forty claims carry an UNVERIFIABLE verdict. The routes already tried are recorded so nobody repeats them. The ones that carry argumentative weight:

| What could not be reached | Why it matters | Routes already tried |
|---|---|---|
| Orphanet ORPHA 1052 | Carries the 75 percent cancer-risk figure and therefore the whole 33.3 percent threshold row | orpha.net disease detail, the legacy consor URL, the API paths and api.orphacode.org, all returning a connection-verification page; orphadata product1.xml carries cross-references only |
| Baker 2004 full text (PMID 15208629) | The median lifespan figure attributed to it | No PMC record; nature.com redirects to the identity provider; the PDF URL returns a paywall page |
| Welch 2007 (PMID 17450125) | Half of the readthrough ranking sentence | Paywalled |
| Sklar 2018 (PMID 29982476) | The one-disease-free-year condition on growth hormone | PubMed abstract, DOI 10.1210/jc.2018-01175 |
| Tang 2011 supplement, panel positions | The metformin concentration-response, which is load-bearing for a removal | PMC article page, the PMC /bin/ path, the Europe PMC supplementaryFiles endpoint |
| Several Cancer Res 2010 figure-level claims | Figure identity in the 731X argument | AACR article page through a text-extraction proxy; no PMC deposit located |

The pattern is worth naming: **what could not be reached is overwhelmingly publisher-gated full text and supplementary material.** Every unreachable item above is reachable to someone with an institutional subscription, in under an hour.

### 2c. Never asked

The failures that matter most, because no layer was positioned to find them.

1. **The primary data was re-analysed once and never re-interrogated.** `track2/audit/PROMPT_B_reanalysis.md` lists what the VCF was never asked: phasing information in the PGT and PID fields across the genome, runs of homozygosity, the mitochondrial genome, copy number from depth, absent-coverage regions, structural variant signatures, the X and Y evidence, uniparental disomy, copy-neutral loss of heterozygosity, segmental rather than whole-chromosome mosaicism, and whether the bins the mosaicism filter discarded are informative rather than artefactual. None of this has been run. The prompt exists; the work does not.
2. **One paper carries the mechanism.** The cross-model reuse pass counted **28 citations to Suijkerbuijk 2010** across the corpus, more than any other source by a wide margin. Nobody asked what the report would look like if that paper were wrong, retracted, or simply not generalisable from its three patient genotypes. The 731X correction is a warning: one allele in that paper was misunderstood by every layer of this project for the whole of its life.
3. **Nobody costed surveillance itself.** The report adds four surveillance items on the ground that they are free. Free in money is not free in burden, and the report never asked what three-monthly imaging does to a family, or what the false-positive rate of the additions is.
4. **No treating clinician has read it.** The report is addressed to a treating team and a family. Thirteen simulated seats and three simulated referees are not one real reader, and the project has no mechanism to get one.
5. **The modifier question was never asked properly.** Whether a second hit, a modifier, or a variant in a kinetochore-interacting gene contributes was raised in the reanalysis prompt and never executed.

---

## Part 3. The review process, judged on its own output

Six layers ran in sequence. Each is judged on what it caught that no earlier layer had.

| Layer | Caught first | Missed, caught later | Verdict |
|---|---|---|---|
| Ten creative lenses | The candidate space itself, including both candidates later removed, and the quantitative appendix that every power figure rests on | Every citation error it introduced | Earned its place. It generated the material; it was never going to check it. |
| Panel 1, five seats, two rounds | Scope disputes, the carve-out's necessity, the dissents that are printed in section 10 | All of the citation errors, the RMS 2005 figures, the residue-numbering trap | Earned its place, narrowly, and for the dissents rather than the facts. |
| Panel 2, eight seats, blind to panel 1 | **The renal work-up**, from its nephrologist finding two causes that demand opposite prescriptions, and **the metformin exposure arithmetic** from its PK seat, which is what removed metformin from the ranked list. Both are headline outputs of this report | The same citation errors panel 1 missed | **Earned its cost.** An earlier draft of this section claimed it duplicated panel 1. That was refuted on checking: the two panels shared no specialty, the integrating record names team 2's contributions 23 times against 26 for team 1, and two of the four surviving recommendations came from it (`VERIFY_headline_claim.md`). |
| Final objection round | Procedural closure | Nothing new of substance | Cheap, and worth keeping for the record it leaves. |
| Verification passes V1 to V3 | The supplementary material that settled two arguments; and at V3, that 731X is a splice-acceptor allele and not a nonsense allele, which withdrew the readthrough argument entirely | That it took three passes to reach an allele identity present in the source's own supplement | Earned its place. The single largest correction in the project came from here. |
| Three referees, no access to working files | Three consequential errors. **Only one was a fact the project did not hold**: the RMS 2005 survival figures, absent from every panel, creative and research file while the wrong figures sat in ten of them, found independently by two referees. The other two, the mouse-to-human residue correspondence and the ECG attribution, were **stated correctly in the project's first research dossier and corrupted in the report** | The report's misdescription of its own arithmetic | **Highest yield per unit of cost.** Not because they knew more, but because they were the only readers not briefed from the project's own dossiers, so they read the report against the sources instead of against their own priors. |
| Five audit partitions, 577 claims | 185 non-supported verdicts. That section 8 misstated its own coefficients of variation and baselines in seven places while the appendix it summarised recomputed exactly; that the Kajii "under 2 percent in controls" comparator does not exist; that Baker 2011's cause of death is data not shown; that Baker 2008 already answers a question the report printed as unresolved | Nothing later found that it should have | **Highest absolute yield.** Also the most expensive. |
| Two cross-model passes | An arithmetic error in the gate cost table, two rounding errors in the expression table, and the structural fact that one paper carries 28 citations | Almost everything the audit found | **Lowest yield, lowest cost.** Fifteen of fifteen recomputations matched, which is a real result: the arithmetic is sound and the errors are in the prose about the arithmetic. |

### What a second project should run instead

1. **Keep the second panel, and brief it differently.** An earlier version of this list said to drop it. That was wrong and is withdrawn: it produced the renal work-up and the arithmetic that killed the leading candidate. What correlated the two panels was the shared dossier briefing, not the panels themselves, so the fix is to vary what reviewers are briefed on, not how many there are.
2. **Bring the referees forward.** They were the cheapest source of consequential corrections and they ran last, so their findings had to be retrofitted into a finished document.
3. **Run the source audit before the panels, not after.** Every seat inherited claims from five dossiers that had never been checked against source. The panels then reasoned carefully from wrong numbers, which is the most expensive failure mode available.
4. **Run the cross-model numeric pass continuously and cheaply.** It is the only layer that costs minutes rather than hours, and its one job, recomputing derived numbers, it does perfectly.
5. **Do not claim novelty for this comparison without checking.** Whether anyone has published equivalent measurements on a real project was asserted here with no search behind it and is recorded as not established (`VERIFY_headline_claim.md`).
6. **Cap the reliance on any single source.** A rule as blunt as "no more than N claims from one paper without a second source" would have surfaced the Suijkerbuijk dependence at the start rather than at the end.

---

## Part 4. What remains

The ordered action list is in `track2/synthesis/NEXT.md`, split into what must happen before submission and what is research in its own right.
