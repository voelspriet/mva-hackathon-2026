# External read of the attached material

Preliminary note on scope. `REPORT_track2.md` is referred to throughout files B, C and D but is not attached. Wherever a pair or a finding involves the report, I can quote only what B, C or D say the report contains. Part 3b is therefore built from what the attached files state or imply about the report, and each item is marked accordingly. Files not attached but needed to complete parts of the task are listed at the end.

---

## Part 1. Statements that cannot both be true

Order is by file position, not importance.

**1.1**
- File D, Part 2c item 1: "`track2/audit/PROMPT_B_reanalysis.md` lists what the VCF was never asked: phasing information in the PGT and PID fields across the genome, runs of homozygosity, the mitochondrial genome, copy number from depth, absent-coverage regions, structural variant signatures, the X and Y evidence, uniparental disomy, copy-neutral loss of heterozygosity, segmental rather than whole-chromosome mosaicism, and whether the bins the mosaicism filter discarded are informative rather than artefactual. None of this has been run. The prompt exists; the work does not."
- File C, header and table: "Run under `track2/audit/PROMPT_B_reanalysis.md` ... Every angle below was computed from data already in hand", with R1 (phase), R2 (runs of homozygosity, uniparental disomy), R3 (copy number from depth), R4 (mitochondrial genome), R6 (discarded bins). File B additionally reports D6 (Y evidence), D7 (absent-coverage regions), D9 (phase field structure).
- For both to hold: D must have been written before C and B were run. D's own header says it was produced "after the five audit partitions and both cross-model passes", and C's header says it was run "after the audit round and both cross-model passes", so the ordering is not settled by the files. Alternatively D's list refers to a different, stricter notion of "asked" than C's.

**1.2**
- File D, Part 2c item 5: "The modifier question was never asked properly. Whether a second hit, a modifier, or a variant in a kinetochore-interacting gene contributes was raised in the reanalysis prompt and never executed."
- File C, R5: "Is there a modifier in the checkpoint, cohesion or decay machinery? No ... Closes the digenic hypothesis."
- For both to hold: same condition as 1.1, or "asked properly" means something C's 80-gene coding scan does not satisfy, which D does not specify.

**1.3**
- File C, header: "No patient data left this machine; gnomAD was read as a static public file by byte range, never queried with a patient coordinate."
- File D, Part 1 item 1: "It survived every layer, including the audit partition on genetics and databases, which retrieved both ClinVar and gnomAD records live."
- For both to hold: C's statement must be scoped to C's pass only rather than to the machine, or the live retrieval must have used an identifier that is not a patient coordinate (a ClinVar accession or rsID, for example). Retrieving a gnomAD record for a specific variant normally requires sending that variant's position or identifier.

**1.4**
- File B, D3: "It carries 4,740,790 PASS records and roughly 155,000 that fail one or more of six declared filters, dominated by MQ40 at 177,522 filter applications."
- Same passage. A single filter cannot be applied to more records than the total number of failing records.
- For both to hold: a record must be able to carry the MQ40 tag more than once, or the two counts must have different denominators (for example, 155,000 over primary contigs and 177,522 over all contigs), or "roughly 155,000" must be a very loose rounding of a figure above 177,522.

**1.5**
- File C, R5: "Two rare missense variants outside *BUB1B* (SGO1 p.Thr425Ala, ANAPC2 p.Gly297Asp) and one synonymous likely-benign."
- File C, R5, same cell: "The 80-gene network carries 1 rare coding variant where its coding length predicts 9."
- For both to hold: the "1" must be counted under a different frequency or consequence threshold from the "two", which the row does not state. As written, the observed count is either 1, 2 or 3.

**1.6**
- File C, P5: "Only two things: exon-level copy number, and coverage in the regions where no variant was called. Neither changes a recommendation, and neither answers phase."
- File C, P2: "The VCF carries no split-read or discordant-pair evidence; a caller on the reads is the right instrument." File B, D8: "Those same regions are where recurrent microdeletions occur, including 22q11.2 and 15q11-q13, and this method cannot see into them. A deletion there would be invisible to every scan run in this project."
- For both to hold: structural variant calling from reads must count as one of the "two things" (it is not named), and a 22q11.2 or 15q11-q13 deletion, if found, must not change any recommendation. The second condition is unlikely to be intended, since B treats the blind spot as material.

**1.7**
- File D, Part 1 item 1: "that pair is the causal genotype for mosaic variegated aneuploidy. Tier: measured in this project, and independently confirmed."
- File D, Part 1 item 2: "The trans configuration is favoured but has never been demonstrated in this family."
- For both to hold: "causal genotype" must mean "the pair the challenge key expects" rather than "a compound heterozygous genotype", since for a recessive condition the pair is causal only if trans. Item 1's own falsifier ("Trio genotyping showing the two variants in cis") concedes that the causal claim rests on the thing item 2 says is unproven.

**1.8**
- File D, Part 2a: "Ataluren ... in any case allele 1 offers no premature stop codon argument once 731X is understood correctly."
- File D, Part 1 item 5: "p.ALLELE_A is predicted to trigger nonsense-mediated decay ... The stop sits 747 nucleotides upstream of the last exon junction with six downstream junctions."
- For both to hold: "offers no premature stop codon argument" must mean "no evidence-based precedent for readthrough in BUB1B", since allele 1 is itself described as a premature stop codon. The 731X correction concerns an allele in a published patient, not this child's allele. Inference: the sentence conflates the loss of a literature precedent with a change in the nature of allele 1.

**1.9**
- File D, Part 1 item 7: "Metformin and dasatinib do not survive ... Tier: measured in primary sources. Metformin's tested concentrations sit 32 to 130 fold above paediatric plasma."
- File D, Part 2b table: "Tang 2011 supplement, panel positions | The metformin concentration-response, which is load-bearing for a removal | [unreachable]".
- For both to hold: the concentration figures must come from the main text and only the panel positions from the unreachable supplement, so that "measured in primary sources" is true of the numbers while the load-bearing figure identification is not verified.

**1.10**
- File D, Part 3: "Six layers ran in sequence."
- File D, Part 3 table: eight rows (ten creative lenses; panel 1; panel 2; final objection round; verification passes V1 to V3; three referees; five audit partitions; two cross-model passes).
- For both to hold: two of the rows must be sub-layers of others, and the text does not say which.

**1.11**
- File D, Part 3, cross-model row: "Fifteen of fifteen recomputations matched, which is a real result: the arithmetic is sound and the errors are in the prose about the arithmetic."
- File D, Part 3, same row, "Caught first" column: "An arithmetic error in the gate cost table, two rounding errors in the expression table".
- For both to hold: the gate cost table error and the rounding errors must lie outside the fifteen recomputed quantities, or must be classed as prose rather than arithmetic. An arithmetic error in a cost table is not obviously prose.

**1.12**
- File D, Part 3, audit row, "Missed, caught later" column: "Nothing later found that it should have".
- File D, Part 3, cross-model row: "Caught first: An arithmetic error in the gate cost table, two rounding errors in the expression table". D's header orders the passes as "after the five audit partitions and both cross-model passes", and the table lists cross-model after audit.
- For both to hold: the cross-model passes must have run before the audit, or arithmetic recomputation must be outside what the audit "should have" found. Neither is stated.

**1.13**
- File B, D1: "Cost: one line in an existing records request", and in the closing list: "the date of the first renal ultrasound, one line in a records request already being made."
- File D, Part 2c item 4: "No treating clinician has read it ... the project has no mechanism to get one."
- For both to hold: the records request must be something the report recommends the treating team make, rather than something the project is making, or the mechanism for requesting records must differ from the mechanism for obtaining a clinical reader.

**1.14** (measurement against assumption)
- File A: "the index renal finding | HPO_TERM | Calcium deposits in kidney tissue; present since birth".
- File D, Part 1 item 4: "work up the kidney before any renal drug, because two competing causes call for opposite prescriptions", where B, D1 identifies those two causes as "neonatal furosemide and parenteral nutrition, and ifosfamide proximal tubulopathy", both postnatal.
- For both to hold: "present since birth" must mean "documented during the neonatal admission" rather than "congenital". B already records this as UNDECIDABLE; it is listed here because it is a supplied observation against a differential assumed elsewhere.

**1.15**
- File B, D2: "one kilogram at PRETERM_GA ... is the earliest measurable manifestation of the syndrome, preceding the tumour and the renal finding."
- File A: "Calcium deposits in kidney tissue; present since birth". File B, D1 entertains the literal reading: "or it is literal, and a congenital cause has not been considered".
- For both to hold: the loose reading of "since birth" must be the correct one. Under the literal reading B itself keeps open, the renal finding is contemporaneous with or antecedent to birth weight, and D2's ordering fails.

**1.16**
- File B, header: "Expectations were stated before each measurement and are recorded here whether or not the measurement matched them."
- File B, scans table: the rows "Filters and declared fields" and "Contigs unused by any analysis" carry "—" in the "Expectation stated first" column.
- For both to hold: those two rows must not count as measurements, or the expectation must have been stated but not recorded.

**1.17**
- File B, D3: "Class: UNEXPLAINED, as a fault in this project's own method rather than in the data."
- File B, closing list: "D3, metrics over a mixture. Already resolved by recomputation."
- For both to hold: UNEXPLAINED must be a class describing the origin of a departure (no biological or technical cause in the data) rather than its status. B's other uses of the class (D2, "It is an omission") do not make that distinction explicit.

**1.18**
- File D, Part 1 item 6: "Blood carries no whole-chromosome mosaic aneuploidy above roughly 10 percent of cells per segment".
- File C, R6: "The 11.7 percent per-bin detection floor is a genome average". File D, Part 3, audit row: "an internal 11.2 against 11.7 percent inconsistency".
- For both to hold: "roughly 10 percent" must be a rounding of a figure that is itself given as two different numbers. D flags the 11.2 against 11.7 problem itself; the third figure is recorded here because it appears in a summary claim.

**1.19**
- File D, Part 1 item 4: "add four surveillance items that cost nothing".
- File D, Part 2c item 3: "Free in money is not free in burden, and the report never asked what three-monthly imaging does to a family, or what the false-positive rate of the additions is."
- For both to hold: "cost" in item 4 must mean monetary cost only. D raises the conflict itself; the two statements remain in the same file with the first unqualified.

**1.20**
- File B, D4: "Localised, 43 percent of the low tail sits in fifteen 5 Mb bins, every one centromeric or acrocentric."
- File B, D4: "Class: ARTEFACT. Regional, not global, which is the discriminator."
- For both to hold: the remaining 57 percent of the low tail, distributed outside those bins, must occur at a rate consistent with reference bias alone. That residual rate is not reported. Arithmetic on B's figures: 57 percent of 4.34 percent is about 2.5 percent of heterozygous calls, still about four times the high-tail figure of 0.62 percent.

**1.21**
- File D, Part 2b: "Every unreachable item above is reachable to someone with an institutional subscription, in under an hour."
- File D, Part 2b table, Orphanet row: "orpha.net disease detail, the legacy consor URL, the API paths and api.orphacode.org, all returning a connection-verification page".
- For both to hold: an institutional subscription must defeat a connection-verification page. Orphanet is not subscription gated; the failure described is a bot or browser check, which a subscription does not address.

---

## Part 2. Questions the attached data supports asking

**2.1 Is the residual low allele-balance tail outside the fifteen artefact bins consistent with reference bias, or with low-level contamination?**
- Made askable by: B, D4 (4.34 percent below 0.25 against 0.62 percent above 0.75; 43 percent of the low tail in fifteen bins).
- Data: the same heterozygous-call table, restricted to calls outside the fifteen bins and outside D8's forty runs. In hand.
- Answers: if the residual low/high ratio falls to roughly 1.5 to 2, D4's ARTEFACT class stands and the contamination assumption behind D6's mosaicism floor is supported. If it stays near 4, a few percent of foreign DNA is not excluded, and the floor in D item 6, the "Both metrics move measurably under contamination" claim in B's scan table, and the allele-depth model in F_math all need a contamination term.

**2.2 What fraction of homozygous-alternate PASS calls at depth 30 or more carry reference reads, and at what median fraction?**
- Made askable by: B, D3 and D4 (allele depth fields are present and used; PASS count established).
- Data: the VCF's AD fields. In hand.
- Answers: this is the standard single-sample contamination estimate. A reference-read fraction near zero closes 2.1 in the direction of artefact. A fraction of 1 to 3 percent quantifies contamination directly and would need to be subtracted from every allele-balance based bound.

**2.3 Were R2, R3, R6 and the mosaicism floor computed over PASS records only?**
- Made askable by: B, D3, which found that an earlier pass "computed the heterozygous ratio and the transition-to-transversion ratio over all records without restriction", and by the 177,522 MQ40 applications concentrated in exactly the low-mappability regions that drive R6's outliers.
- Data: the code and parameters of C's scans. In hand (C says the scans "reproduce from `pipeline/track2_math/f_math.py`").
- Answers: if PASS-only, no change. If not, R6's 56 outlier bins may partly be MQ40 records and the fix C proposes ("The method needs a mappability filter") may already be a filter-status fix; R2's zero runs of homozygosity may be broken by failing heterozygous calls, which bears on 2.4.

**2.4 What thresholds were tried in R2, and is zero runs of homozygosity at any threshold itself an anomaly?**
- Made askable by: C, R2: "Zero runs at any threshold tried."
- Data: the R2 parameters and a rerun at 0.5, 1 and 1.5 Mb with a tolerance for isolated heterozygous calls. In hand.
- Answers: an outbred human genome normally carries several runs above 1 Mb. If runs appear at 1 Mb, R2's summary is loose but its exclusion of large isodisomy stands. If none appear at any threshold including 0.5 Mb, the method is not detecting homozygosity, and R2's "Excludes isodisomy and consanguinity" is not established.

**2.5 What is the depth and heterozygous call density in the unique sequence inside the recurrent 22q11.2 and 15q11-q13 deletion intervals, as opposed to the flanking low-copy repeats?**
- Made askable by: B, D8, which places its blind spot at "chr22:18.5 to 18.8 Mb the 22q11 low-copy repeats" and "chr15:21.7 to 22.2 Mb the proximal 15q11 duplication region", and states "A deletion there would be invisible to every scan run in this project."
- Data: the 100 kb depth windows and heterozygous calls B already computed, read across approximately chr22:19.0 to 21.4 Mb and chr15:22.8 to 28.3 Mb. In hand.
- Answers: the recurrent deletions are flanked by the repeats but their interiors are largely unique, mappable sequence. If depth there sits near 43 with normal heterozygosity, the blind spot as stated in D8 and in B's scope limits is narrower than claimed, and the scans do bear on the two commonest microdeletions. If depth is near half with no heterozygous calls, a deletion is present. Inference: this is a case where the attached measurements make an open item cheaper than B says.

**2.6 Do the fifteen bins from D4 and the forty runs from D8 account for all 56 outlier bins in R6?**
- Made askable by: B, D4 and D8 (explicit lists of artefact regions), against C, R6 (56 bins, "all sit in heterochromatin, acrocentric arms, centromeres or the MHC").
- Data: intersection of the two lists. In hand.
- Answers: C lists a mappability track overlay as P3, "Obtainable, free", but "not held offline". If the internal lists cover all 56, P3 costs nothing and the mosaicism floor can be re-stated as an exclusion-masked figure immediately. If some outliers fall outside both lists, those bins need individual reading before R6's "The negative result is unaffected" is safe.

**2.7 Is the depth profile across the T-cell receptor beta and immunoglobulin lambda loci reduced in the way somatic V(D)J deletion would produce, or is it normal?**
- Made askable by: B, D5, which classes 718 and 287 low allele-balance calls at those loci as EXPECTED and as "the positive control for the allele-balance scan".
- Data: D8's 100 kb depth windows at chr7:142 Mb and chr22:22 Mb. In hand (neither locus appears in D8's list of low runs).
- Answers: somatic recombination in a fraction of lymphocytes removes DNA and lowers depth over the deleted segments while skewing allele balance; mismapping among paralogous V segments skews allele balance without lowering depth. If depth is normal, the "positive control" is not discriminating a somatic process from a mapping artefact and the weight B places on "the absence of focal signal elsewhere" is reduced. If depth is reduced in the interior segments, the control stands.

**2.8 Which caller and which caller mode produced the VCF, and what are the semantics of its PGT and PID fields and its handling of the mitochondrial contig?**
- Made askable by: B's scan table ("six filters used; 17 INFO, 7 FORMAT fields") and D9 and D10.
- Data: the VCF header. In hand.
- Answers: a germline diploid caller does not emit low-fraction mitochondrial alleles at all; D10's "Detection capability: adequate" holds only if the caller was run in a mode that reports them. Physical phasing fields with a 288 bp maximum span indicate phasing within read pairs only, which fixes what D9 can and cannot say about any two variants.

**2.9 What is the inferred continental ancestry of the sample, and what are the het/hom and Ti/Tv expectations for that ancestry?**
- Made askable by: B, D3 (het/hom 1.62 against an expectation of 1.5 to 2.0), and by C's statement that gnomAD was read as a static file.
- Data: PASS genotype frequencies against gnomAD population frequencies from the static file. In hand or obtainable offline.
- Answers: the 1.5 to 2.0 expectation is population dependent. For some ancestries 1.62 is low and would reopen 2.1; for others it is central. The ancestry also fixes which gnomAD population's allele frequencies enter the co-occurrence enrichment behind D item 2's posterior, and therefore whether "above 0.98" is computed against the right denominator.

**2.10 What are the allele balances and depths at the two BUB1B variants themselves?**
- Made askable by: B's use of allele balance genome-wide and D item 1's claim that the pair was "called from the proband's own VCF".
- Data: two records in the VCF. In hand.
- Answers: both near 0.5 supports two germline heterozygous alleles. A markedly low balance at either would raise a somatic or mosaic origin for that allele in blood, which bears on item 1's tier and on what a trio would be expected to show.

**2.11 Are any of the 78,917 PASS calls on non-primary contigs duplicates of primary-contig calls, and were they included in the D3 recomputation over "PASS autosomal records"?**
- Made askable by: B's scan table ("78,917 PASS calls on 1,582 non-primary contigs, 1.66 percent, never examined") and D3.
- Data: contig names and positions in the VCF. In hand.
- Answers: B lists the contigs as a scope limit rather than a question; the count makes the cost small. If alt-locus calls duplicate primary calls and were included, D3's 1.62 and 2.028 shift slightly. If excluded, no change to D3, and the contigs remain a scope limit.

**2.12 Do the twenty largest of D7's gaps exhaust the informative ones, or do any of the thirteen smaller gaps fall in unique sequence?**
- Made askable by: B, D7 ("33 such gaps, 59.7 Mb in total. Every one of the twenty largest is a known heterochromatic block or centromere").
- Data: the remaining thirteen gap coordinates. In hand.
- Answers: a 150 to 300 kb no-call region in unique sequence is a homozygous deletion candidate; D7's "No evidence of a large homozygous deletion" currently rests on twenty of thirty-three.

**2.13 What is the sex-specific birth weight z-score at 32 weeks on a named chart?**
- Made askable by: B, D2 ("one kilogram at PRETERM_GA, sits below the third centile for gestational age against a median near 1.8 kg") together with B, D6 (male).
- Data: a published preterm growth reference. Obtainable, free.
- Answers: D2 names no chart and no sex. The z-score determines whether the phrase "below the third centile" understates a value near or below the first centile, which bears on how much weight the growth cluster carries as an MVA feature.

---

## Part 3. What is absent, and what is present but not visible

### 3a. Unsupported, overstated, or missing a step

1. B, D5: "this is the positive control for the allele-balance scan. It recovers a somatic process known to be present". Missing step: exclusion of paralogous mismapping at the TCR and IG loci, which produces the same allele-balance skew without any somatic process. The MHC entry in the same paragraph is explained by polymorphism, not somatic change, so the control mixes mechanisms. See 2.7.

2. B, D10 and C, R4: "Detection capability: adequate, since the depth would have shown heteroplasmy of a few percent" and "Removes a second explanation for the growth and muscle phenotype, and the drug contraindications that would follow it." Missing steps: (a) a diploid germline caller's VCF only records minor fractions at sites it called; a heteroplasmic variant at 5 to 20 percent would typically produce no record, so the 2.1 percent maximum is a property of called sites, not of the sample; (b) blood heteroplasmy can be low or absent for variants that are high in muscle; (c) nuclear-encoded mitochondrial disease genes are not addressed. "Removes" is stronger than the measurement supports.

3. C, R2: "Zero runs at any threshold tried." Unsupported as written: the thresholds are not given, and zero runs of homozygosity at conventional thresholds is itself an unusual result for a human genome. "Excludes isodisomy and consanguinity" inherits this.

4. C, R5: "Closes the digenic hypothesis." Overstated: the scan covers rare coding SNVs and indels in an 80-gene set whose membership and rarity threshold are not given; noncoding, copy-number and per-gene callable coverage are not addressed; and the observed count is given inconsistently (see 1.5). "The 80-gene network carries 1 rare coding variant where its coding length predicts 9" states an expectation without the rate it was derived from.

5. C, R1: "at 10.9 kb apart no short-read library can join them. The raw reads would not answer it either." Overstated: mate-pair libraries with inserts above 11 kb exist. Whether the reads would answer phase depends on the library that was sequenced, which the reads themselves would reveal.

6. C, P5: "Only two things: exon-level copy number, and coverage in the regions where no variant was called. Neither changes a recommendation". Missing: structural variant calling (C's own P2), and a depth read of the recurrent microdeletion interiors that B, D8 treats as material. See 1.6.

7. B, D6: "The genome is a normal male genome." Missing step: X chromosome depth and X heterozygosity are not reported. Y at half autosomal depth is consistent with 46,XY and with 47,XXY. The scans table says "Sex chromosome dosage by region: Y at half autosomal, confirmed" and says nothing about X.

8. B, D4: "Regional, not global, which is the discriminator." The residual outside the fifteen bins is 57 percent of the low tail and is not quantified. See 1.20 and 2.1.

9. B, D8: "Every run is centromeric, pericentromeric, or in a named segmental duplication block: ... chr1:0.5 to 0.8 Mb subtelomeric". The subtelomeric run is none of the three named categories. Minor; noted because the sentence is a universal claim.

10. B, D2: "one kilogram at PRETERM_GA ... is the earliest measurable manifestation of the syndrome". Missing step: attribution of the intrauterine growth restriction to MVA in this child rather than to any other cause of a 32-week delivery; the chart and sex behind "below the third centile" are not named. Also, B, D1 gives the gestation as "a 32-week, one-kilogram infant", which supplies a value the attached A file has tokenised as PRETERM_GA.

11. D, Part 1 item 1: "Tier: measured in this project, and independently confirmed. The pair was called from the proband's own VCF ... scored 100.0 rank points and F-max 1.000 against the challenge's own scorer, and ranks first genome-wide under phenotype-driven prioritisation". Missing step: agreement with a scorer and a prioritiser confirms that the pair is the expected answer, not that it is causal in this child; causality for a recessive condition requires trans, which item 2 says is unproven. See 1.7.

12. D, Part 1 item 4: "No MVA patient-derived line has been tested against any spindle agent, so this is open in both directions." A reader would ask whether this is true. Inference: the project's most-cited source (Suijkerbuijk 2010, per D Part 2c) characterised spindle-assembly-checkpoint function in patient cells, which is ordinarily done by challenging cells with a spindle agent. If so, the statement is false as written, and the rule's premise has at least one direct test in the literature the project already holds. This is flagged as a question to check against the source, not as a settled fact.

13. D, Part 1 item 5: "The indirect support is that a different truncating allele's transcript was undetectable in patient cells". Missing step: the identity of that allele. If it is the 731X allele that V3 found to be "a splice-acceptor allele and not a nonsense allele", then the support for nonsense-mediated decay of allele 1 comes from an allele whose transcript may be lost for a different reason.

14. D, Part 2a: "Ataluren. Not authorised outside Great Britain". No source or date in the attached material; the regulatory status of this drug has changed more than once and the statement cannot be evaluated as written. Also see 1.8 on "no premature stop codon argument".

15. D, Part 1 item 3: "There is no marketed drug whose mechanism raises, stabilises or substitutes for BubR1". Missing step: the coverage of `pipeline/track2_drugmap/` (which approved-drug set, which mechanism annotation source, which jurisdictions). A negative claim over a search space is only as strong as the space, and the space is not described in the attached material.

16. D, Part 2b: "what could not be reached is overwhelmingly publisher-gated full text and supplementary material. Every unreachable item above is reachable to someone with an institutional subscription". The Orphanet failure is a connection check on a free resource, not a paywall. See 1.21.

17. D, Part 3 table: "Six layers ran in sequence" against eight rows; "Fifteen of fifteen recomputations matched" against an arithmetic error caught. See 1.10 and 1.11.

18. A, Notes: "In chromosomal instability disorders, reproductive loss in parents or other family members can reflect heritable or de novo mechanisms". For a recessive condition, a de novo mechanism does not account for recurrent losses across pregnancies; the sentence does not distinguish. A is challenge-supplied, so this bears on how the phenotype document should be read rather than on the entrant.

19. A, feature row: "Very low birth weight | Small for gestational age". The clinical feature and the HPO term are different concepts (absolute weight below 1500 g against weight below a centile for gestation). Both apply here, but the row does not say so, and B, D2 relies on the centile reading.

### 3b. Present in the attached files, not visible to a reader of the main report

The report is not attached. Items marked (stated) are ones the attached files themselves say are absent from the report; items marked (inferred) are ones whose absence is inferred from the files' descriptions of what lives where.

1. (stated) B, D1: the phenotype document's "present since birth" against the report's two postnatal renal causes. B: "The strings 'since birth', 'at birth', 'antenatal' and 'in utero' occur zero times in `REPORT_track2.md`." Changes reading: the renal algorithm's branches may both be wrong; a reader of the report alone sees a two-way differential and no third option.

2. (stated) B, D2: four of eight supplied features are never named in the report, and the growth and nutrition arm is "without anchoring any of it to the supplied observations." Changes reading: the nutrition and endocrine sections cannot be traced by a reader to the observations that motivate them.

3. (stated) B, D8 and scope limits: "Regions inside segmental duplications, including the two commonest recurrent microdeletion loci, are not visible to any depth or allele-balance method applied here." Changes reading: any statement in the report that no deletion was found should be read with this exclusion, unless 2.5 narrows it.

4. (stated) C, R6 and closing paragraph: the mosaicism detection floor "is now known to be a genome-average figure that fails in low-mappability regions, and that qualification belongs beside the figure." C says the report "should be touched"; whether it was is not stated. Changes reading: the floor in the report is a best case.

5. (stated) B, scans table: "78,917 PASS calls on 1,582 non-primary contigs, 1.66 percent, never examined". Changes reading: a small, stated exclusion; does not alter recommendations on the attached evidence.

6. (stated) B, D3: earlier sample metrics were computed over passing and failing records together; corrected figures 1.62 and 2.028. Changes reading: if the report carries the earlier figures (1.57, 1.968), one of them sits outside the stated expectation.

7. (inferred) C, R5: the modifier scan is negative by computation. D item 1's "no gene list supplied" and C's "Converts the report's assumption ... into a computation" imply the report states this as an assumption. Changes reading: supports the report, with the caveats in 3a item 4.

8. (inferred) D, Part 2b: forty claims carry an UNVERIFIABLE verdict, including "Orphanet ORPHA 1052 | Carries the 75 percent cancer-risk figure and therefore the whole 33.3 percent threshold row". Changes reading: a threshold row in the report rests on a figure the project could not verify.

9. (inferred) D, Part 2c item 2: "28 citations to Suijkerbuijk 2010 across the corpus ... one allele in that paper was misunderstood by every layer of this project for the whole of its life." Changes reading: the mechanism section's independence from a single source is lower than a reader would assume from citation counts alone.

10. (inferred) D, Part 3, audit row: section 8 of the report has "7 contradicted claims in 21 audited, 33 percent"; the appendix it summarises "carries 17 non-supported claims of 60 including four misattributions and an internal 11.2 against 11.7 percent inconsistency"; the referees missed "The report's misdescription of its own arithmetic." Changes reading: the quantitative section is the least reliable part of the report by the project's own audit, and it is not stated whether the corrections were incorporated.

11. (inferred) D, Part 2c item 3: surveillance burden and false-positive rate were never costed. Changes reading: "cost nothing" in the report should be read as monetary only.

12. (inferred) D, Part 1 item 2: the phase posterior figures ("above 0.98 ... collapses to 0.32 at the hard ceiling") live in `track2/creative/F_math.md`, a creative-track file. Changes reading: if the report quotes only the favoured configuration, the collapse case is invisible.

13. (inferred) D, Part 2c item 4: "No treating clinician has read it." Changes reading: the report is addressed to a treating team and has had no clinical reader; this is a property of the document, not of its content.

14. (inferred) B, D6: the proband is male. A does not give sex. Whether the report states sex, and whether any dosing, growth or gate figure depends on it, cannot be determined from the attached material.

---

## Parts not completed, and material needed

- Part 1 pairs involving the report (1.14 and the postnatal causes in 1.6) rest on B's and D's descriptions of the report rather than on quotation from it. `REPORT_track2.md` is needed to quote the second half of each such pair directly.
- Part 3b cannot be verified. `REPORT_track2.md` is needed to confirm which of items 1 to 14 are in fact absent, and `track2/synthesis/NEXT.md` and `VERIFY_headline_claim.md` to establish whether the audit corrections and the R6 qualification were incorporated after C and D were written.
- Several 3a items (4, 11, 12, 13, 15) would be settled by files named in the attached material but not supplied: `track2/creative/F_math.md`, `pipeline/track2_math/f_math.py`, `pipeline/track2_drugmap/`, `track2/research/02_clinical_care_drugs.md`, `track2/audit/PROMPT_B_reanalysis.md`, and the VCF header.
- 3a item 12 is a check against a source (Suijkerbuijk 2010) I have not read for this exercise; it is recorded as a question to verify, not as a finding.