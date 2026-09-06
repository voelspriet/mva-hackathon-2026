# R7. What does the whole genome look like against the whole of ClinVar?

**Asked 6 September 2026. Never asked before.**

## Why this question was missing

Every earlier screen in this project was bounded by a gene list.

| Screen | Bound |
|---|---|
| Track 1 secondary findings | the 81 ACMG SF v3.2 genes |
| R5, the modifier scan | an 80-gene mitotic, cohesion and decay network |
| The creative pass | *BUB1B*, the NMD machinery, and drug-handling genes |

R5 named its own blind spot in writing: "**Not covered**: non-coding variants, copy number, per-gene callable coverage, and **any gene outside the 80**." That sentence went into the record and nothing was done about it. This is the screen that does it.

The question here has no gene list at all. It asks the child's genome against every position in ClinVar carrying an unconflicted pathogenic assertion.

## Method

`pipeline/reanalysis/clinvar_genomewide.py`, run against the ClinVar GRCh38 release downloaded 6 September 2026 and `work/proband.chr.pass.vcf.gz`.

1. Keep every ClinVar record whose `CLNSIG` contains Pathogenic or Likely_pathogenic and does not contain Conflicting.
2. Reduce to unique positions and write a BED.
3. Query the proband with `bcftools query -i 'FILTER="PASS"' -R`, so failing records cannot enter. This project has already been bitten once by a missing PASS filter, and the correction is recorded in `track2/audit/DATA_CLAIM_CHECKS.md`.
4. Require an **exact reference and alternate allele match** in Python. `bcftools -R` matches positions, not alleles, so without this step a hit means only that ClinVar has some record somewhere at that coordinate.
5. Look up each surviving hit in gnomAD v4.1 by byte-range read, and re-read its full ClinVar record locally for consequence and review status.

ClinVar is read as a downloaded static file and gnomAD by byte range on a public object. No patient coordinate is sent to any interactive service.

| Stage | Count |
|---|---|
| ClinVar records read | 4,468,152 |
| Unconflicted pathogenic or likely pathogenic | 346,384 |
| Unique positions | 303,786 |
| Proband PASS calls at those positions | 264 |
| **Exact allele matches** | **7** |

## The seven hits

All seven are heterozygous. **No position is homozygous, and no gene is hit twice.**

| Position | Gene | rsID | Consequence | Our call | gnomAD v4.1 | Verdict |
|---|---|---|---|---|---|---|
| chr15:40209701 T>G | *BUB1B* | . | (allele 1) | 0/1 21,25 DP 46 | AC 115 / AN 1,461,846 | **Positive control. The scan works.** |
| chr22:20996720 C>G | *LZTR1* | rs1682503990 | nonsense | 0/1 24,24 DP 48 GQ 99 | AF 1.37e-06, 0 hom | Real and rare. Low absolute risk. See below |
| chr1:145927447 C>T | *RBM8A* | rs139428292 | 5'UTR | 0/1 17,19 DP 36 | AF 0.026, 583 hom | Common hypomorph. Qualifies a report sentence |
| chr1:152307547 G>A | *FLG* | rs138726443 | nonsense | 0/1 21,17 DP 38 | AF 0.00398, 14 hom | Carrier. Ichthyosis vulgaris and atopy |
| chr10:69315762 A>G | *HK1* | rs187500777 | intron | 0/1 27,21 DP 48 | AF 0.00207, 2 hom | Recessive carrier. No second hit |
| chr4:67753920 C>T | *GNRHR* | rs104893842 | missense | 0/1 28,32 DP 60 | AF 0.000142, 0 hom | Recessive carrier. No second hit |
| chr7:142750561 C>T | *PRSS1* | rs202003805 | missense | 0/1 **29,5** DP 34 | AF 0.386, **0 hom**, gnomAD filter InbreedingCoeff | **Artefact. Discarded.** See below |

### The headline negative

**The scan looked for a second recessive diagnosis and did not find one.** Nothing is homozygous, and no gene carries two hits. The three recessive carrier states, *HK1*, *GNRHR* and *FLG*, each have one allele and no partner. They are the ordinary carrier burden of any genome and explain nothing about this child.

### What the scan cannot do, by construction

*BUB1B* allele 2, chr15:40220612, **does not appear here**, and it should not. It is a gnomAD singleton with no ClinVar record. A screen against ClinVar can only find what ClinVar already knows. This is the method's ceiling and it is worth stating plainly: it recovered the known allele of the causal pair and was structurally blind to the novel one. Anyone reusing this script should read the 7 as a lower bound.

Also missed: copy number, repeat expansions, and any position where the child has no PASS call.

## *PRSS1*: how a pathogenic record becomes an artefact

This one is discarded, and the argument uses only public summary data.

**In our data.** Allele balance 0.147, with 29 reference and 5 alternate reads. QUAL 84.77, the lowest of the seven by a factor of five. The position sits inside the T-cell receptor beta locus, the exact region flagged for mismapping in `track2/anomalies/ANOMALIES.md` D5. ClinVar's own gene field for the position reads `PRSS1:5644|TRB:6957`, so the overlap is not our inference.

**In gnomAD.** The allele sits at frequency 0.386 in 59,319 genomes and gnomAD reports **zero homozygotes**. Hardy-Weinberg at that frequency predicts about 8,839. gnomAD's own pipeline fails the site on the InbreedingCoeff filter.

An allele at 39 percent frequency with none of 59,319 people homozygous is not a rare disease allele. It is one locus reading two paralogues at once, and gnomAD reproduces the same artefact. The finding is that this record should not be trusted by anyone, not only by us.

## *RBM8A*: a sentence in the report is wrong

The report says, at section 2:

> No rare variant in the NMD machinery or EJC core exists in this genome (creative D §6), so NMD efficiency should be assumed normal.

The child carries **rs139428292, the TAR-syndrome 5'UTR hypomorphic allele of *RBM8A***, heterozygous. *RBM8A* encodes Y14, a **core component of the exon junction complex**, which is the structure nonsense-mediated decay reads. The allele is not rare, at 2.6 percent, which is exactly why a rare-variant filter did not return it.

The conclusion does not change, but the reason for it does, and the reason is the part that was wrong.

Two things are true at once, and both were already on disk:

- `track2/creative/D_compute.md` lines 163 to 167 **found this variant**, ran a 1q21.1 dosage screen, established there is no deletion in trans, and reasoned from the allele's frequency to normal NMD. That working file did the job properly.
- The audit could not check it. `track2/audit/AUDIT_fg_genetics_stats.md` B54 marks the gnomAD figures **UNVERIFIABLE**, "Not re-queried in this audit".

**B54 is now verified.** gnomAD v4.1 returns AF 0.026 with 583 homozygotes in exomes, and AF 0.0184 with 33 homozygotes in genomes. The working file said "AF 2.6 percent with 583 homozygotes". Exact.

**The 1q21.1 result is now independently replicated.** The creative file reported depth ratios 0.80 to 1.19 and retained heterozygosity 0.53 to 0.98 across 145.3 to 146.0 Mb. Re-run here in 200 kb bins on PASS calls: mean depth 39.1 to 43.2 against a chr1 control window at 38.7 and an autosomal median of 44, with heterozygosity 82 to 85 percent. A heterozygous deletion would halve the depth and abolish the heterozygosity. **There is no 1q21.1 deletion in trans, so there is no TAR syndrome risk here.** The allele is a carrier state.

**The correction.** The EJC core is not variant-free. It carries one common hypomorphic allele in the heterozygous state. NMD should still be assumed normal, but because 583 people in gnomAD are homozygous for this allele without a reported decay phenotype, not because nothing was found. The report has been changed to say that.

This is the third time in this project that a claim of absence turned out to be a claim about a filter. It is the same failure the exclusion audit describes in `SIMULATED_PANELS.md`: the information was already in the repository and nobody was asked a question that would surface it.

## *LZTR1*: a real variant that does not earn a recommendation

This is the only genuinely new finding, and the honest version of it is much smaller than the first version.

**What is solid.**

- A **nonsense** variant, `NC_000022.11:g.20996720C>G`, ClinVar variation 1409252, asserted Pathogenic/Likely_pathogenic with criteria provided, multiple submitters and no conflicts.
- The call is clean: 24 reference and 24 alternate reads, depth 48, GQ 99, MQ 60, QUAL 650.77.
- It is genuinely rare: gnomAD v4.1 exomes AC 2 in AN 1,461,378, AF 1.37e-06, no homozygotes, PASS.
- Mapping was checked rather than assumed. Depth across the locus is 42.9 against flanks at 39.9 and 42.5 and a chr22 control at 39.4. Paralogue collapse raises depth. It is flat.
- *LZTR1* is a substrate adaptor for the CUL3 ubiquitin ligase that degrades RAS. Heterozygous loss of function predisposes to *LZTR1*-related schwannomatosis, autosomal dominant.

**This project already found it and did nothing.** `track2/research/04_exomiser_model2.md` ranks *LZTR1* **fourth genome-wide**, p 0.028, with a variant score of **1.000**, the maximum. It was never followed up in any later file. The word *LZTR1* appears nowhere else in the repository except the audit row that verified the rank table's arithmetic. The rank was checked. The gene was not.

**Why it still does not support a recommendation.** I looked for the evidence that would kill this finding, and found it.

- Loss-of-function *LZTR1* variants are carried by about **1 in 281 people** in the general population, 0.36 percent, which is common for a dominant tumour predisposition gene ([Deng 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9324957/)).
- The same study estimates that only about **1 in 1,203** such carriers develops clinical schwannomatosis, and concludes that germline *LZTR1* variants "may carry a lower risk of symptomatic schwannoma disease than other genes, such as *SMARCB1* and *NF2*". Penetrance elsewhere is put at 40 to 50 percent in ascertained families, which is a different and much more selected denominator.
- Schwannomatosis presents typically in adulthood, so this is a statement about distant future risk, not about anything a child has now.

**The mechanistic idea, and why it fails.** Schwannoma formation in an *LZTR1* carrier needs a somatic loss of the other 22q, which is found in about 90 percent of their tumours. Mosaic variegated aneuploidy generates random whole-chromosome loss, so it is tempting to argue that this child's syndrome supplies the rate-limiting second event. Two things refute it.

1. **The natural experiment has been done and came out negative.** Typical 22q11.2 deletion syndrome removes one *LZTR1* copy constitutionally in 89 percent of patients. Across **more than 1,500 patients there are no reports of schwannoma**, and the authors conclude the deletion may *reduce* risk ([Lyons-Warren / Genetics in Medicine 2021, PMID 33879870](https://pubmed.ncbi.nlm.nih.gov/33879870/)). Constitutional single-copy *LZTR1* loss in 1,500 people produced zero tumours.
2. **The event is not observed in this child.** `work/mosaic_robust.txt` gives f_BAF of 0.000 for every autosome including chromosome 22. The small positive depth ratio on chr22, 1.0194, is shared by chr16, chr17, chr19 and chr20 while every large chromosome is slightly negative, which is the signature of GC bias, not of aneuploidy. The method's floor is about 10 percent, so this is not evidence of absence either. It is simply not support.

**Verdict.** A real, rare, high-quality pathogenic-class truncating variant in a dominant tumour predisposition gene, carried by roughly 1 person in 281, with an estimated absolute risk near 1 in 1,203, no observed second event, and a natural experiment arguing against the mechanism that would have made it interesting here. **It is reported because it is true and because the project's own Exomiser run flagged it and was ignored. It is not carried into any surveillance recommendation, and it does not belong on the family card.**

## Whether these should be reported at all

This screen produces incidental findings, and that is a judgement, so it is written down rather than made quietly.

Track 1 already ran an ACMG SF v3.2 secondary-findings screen, so reporting findings unrelated to the referral question is inside this project's declared scope by design. *LZTR1* is **not** on the ACMG list, so reporting it goes beyond that standard, and the reason is that the project's own Exomiser run had already surfaced it and the failure to follow up is itself a finding about method.

Three restraints apply, and they are the reason this is publishable rather than reckless.

1. **No recommendation follows.** Nothing here reaches the family card or any surveillance schedule. The absolute-risk evidence in the *LZTR1* section is the reason, and it is quoted rather than summarised.
2. **No recontact.** The standing rule of this project holds. Nothing here is communicated to the family, the treating team or the MVA Society, and nothing here should be.
3. **The carrier states are named and dismissed in the same breath.** *FLG*, *HK1* and *GNRHR* are the ordinary background of any genome. Listing them without that sentence would invite a reader to treat length as significance.

The one thing this section cannot settle is whether a real clinical genetics service would return an *LZTR1* result to this family. That is a decision for people with duties to this child, and no part of this repository is a substitute for them.

## Correction, 6 September 2026: this screen was not genome-wide

**It skipped the mitochondrial genome, and reported nothing about having done so.** ClinVar names that contig `MT`; this script prefixed every ClinVar contig with `chr` and produced `chrMT`; the proband VCF calls it `chrM`. The intersection was empty and `bcftools -R` does not warn when a region names a contig that does not exist, so 184 mitochondrial positions were queried against a name that matches nothing.

The script now maps `MT` to `chrM` in both directions. **Re-run, it returns the same seven hits**, so the conclusion above is unchanged and only the scope claim was wrong. The mitochondrial genome has since been screened directly against all 78 unconflicted pathogenic ClinVar `MT` records and carries none of them. See `track2/reanalysis/R12_mitochondrial_and_bub1b_body.md`.

## What R7 changes

| | |
|---|---|
| New diagnosis | None. Nothing homozygous, no gene hit twice |
| Report corrections | One. The EJC sentence in section 2 |
| Audit rows resolved | One. B54, UNVERIFIABLE to SUPPORTED |
| Working-file results replicated | Two. The 1q21.1 dosage screen and the gnomAD *RBM8A* figures |
| Records shown to be untrustworthy | One. *PRSS1* rs202003805, on Hardy-Weinberg grounds |
| Follow-up failures found | One. *LZTR1* at Exomiser rank 4, never pursued |
| Recommendations added | **None** |

