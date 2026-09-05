# Referee 1: clinical and molecular geneticist

## 1. Summary of the claim

For one child with biallelic *BUB1B* variants, the defensible repurposing output is not a drug but a sequence: medicines to avoid as aneugens or hypercalciuric agents, three no-cost surveillance additions, a renal work-up, and measurements that must precede any gene-directed prescribing, because phase, residual BubR1 and the class of the missense allele are all unknown. Secondarily, an automated pipeline extends the manual shortlist and the procedure is said to transfer. That states in two sentences; it is a claim about method, not about a medicine.

## 2. Validity

**Supported, expected to hold.** Recomputed from NM_001211.6: codon 737 is TTA at c.2209 to c.2211, so c.2210T>G gives TGA while c.2209T>G would give GTA (Val), and the §12 correction of the Exomiser HGVS is right. Codon 1002 is AAT and c.3006T>G gives AAG (Lys). The -1 base c.2208 is G, +4 c.2212 is A. c.2210 lies in exon 17 of 23, 747 nt upstream of the last junction with six downstream junctions, so Nagy and Maquat (PMID 9644970) is applied correctly; c.3006 is in the last exon. The sites are 10,911 bp apart on GRCh38 (chr15:40,209,701 and 40,220,612), matching 10.9 kb.

**Supported.** gnomAD v4.1: c.3006T>G AC 1, AN 1,461,878, exactly as claimed; c.2210T>G AC 115, AN 1,461,846, AF 7.87e-5, no homozygotes.

**Supported.** Suijkerbuijk 2010 full text (PMC2887387) confirms every allele-level statement drawn from it: 731X encodes only 715 residues; Q921H "indistinguishable from wild-type LAP-BUBR1, both on protein level and functionality"; I909T and R727C turnover ~2-fold, geldanamycin-sensitive and MG132-rescuable; I909T and L1012P overexpression "fully restored the response to nocodazole"; 386X mRNA undetectable, 731X/WT 2-fold reduced; HeLa and U2OS only. North 2014 (PMC4194088) confirms 58 and 21 percent, P=0.0384, n=31 vs 33, males +123 percent P=0.004, females P=0.7915, and NMN at 500 mg/kg/day for 7 days clear only in testes. Kajii 2001, verbatim: "Their parents had 3.5%-41.7% of their lymphocytes in total PCS."

**Contradicted, expected to fail.** The bolded flagship, "A verified correction", puts 731X in "Cancer Res 2010 Figures 5A to 5C". The truncation rescue is Figure 4A to 4C; Figure 5 covers R550Q and Y155C, the mutants that do not affect stability. A verification pass whose headline output is a corrected citation has miscited the figure.

**Contradicted.** "no ClinVar record for this nucleotide" holds only at nucleotide level. ClinVar uid 4600147, c.3006T>A p.(Asn1002Lys), Uncertain significance, criteria provided, evaluated 19 Sep 2025. The identical protein change is already classified, and that is omitted.

**Unverifiable.** "runs at 1.44 times wild type" is absent from the paper, which says only "comparable to or higher than wild-type BUBR1". Three-figure densitometry presented as a source statement, without a method.

**Overstated.** "UGA is the leakiest stop and the best readthrough substrate (shown; Welch 2007)". Welch 2007 is the PTC124 paper and makes no such general claim, and Floquet 2012, cited in the same sentence, reports that "the identity of the stop codon did not affect the response to gentamicin treatment". Two disagreeing sources cited as cumulative. Floquet's actual finding, uracil at -1 as "a major determinant of the response to gentamicin", is reported correctly.

**Overstated.** Rio Frio and Foulkes 2010 supports "an adult-onset MVA1 phenotype exists", but that patient is homozygous for a leaky intronic allele, c.2386-11A>G, with adult gastrointestinal neoplasia and no childhood syndrome. §12 criticises itself for reasoning across allele classes from a mouse hypomorph, then does it here.

## 3. Logic

The largest unmarked leap is the mouse allele. "BubR1^H/L1002P" appears repeatedly beside "p.Asn1002Lys" without stating once that mouse 1002 is human 1012 and the shared number is arithmetic; Sieben 2020 says so plainly. A reader will take gate item 6 for a mouse carrying this child's missense allele. That item also attributes an "ECG J-point defect" to BubR1^H/L1002P citing Sieben 2020 and North 2014, when the J-point work is North 2014 on BubR1^H/H in male mice only: genotype and sex both swapped in one sentence.

"No rare variant in the NMD machinery or EJC core exists, so NMD efficiency should be assumed normal" upgrades absence of rare coding variation into a functional assumption. NMD is called predicted, then assumed.

The frequency argument runs one way. §12 offers 115 heterozygotes as reason to doubt p.Leu737Ter, omitting five further alleles in gnomAD genomes and that 111 of 115 are non-Finnish European (AF 1.0e-4), and never computing a maximum credible allele frequency, which for a recessive disorder below 1e-6 prevalence sits above 1e-4. ClinVar records it Pathogenic/Likely pathogenic, multiple submitters, no conflicts, for MVA1. Scepticism without the arithmetic that disciplines it, in a document that disciplines metformin with arithmetic.

§4 correctly derives opposite cDNA signatures for cis and trans under efficient decay, then §10 prints the team 1 dissent, unannotated, asserting the opposite premise: its conclusion survives, its stated reason does not. The gate is also built around the assay carrying the artefact. An 11 kb genomic long-read amplicon spanning both sites, or trio genotyping alone, settles phase without cDNA, NMD blockade, living cells or cycloheximide; long-read sequencing appears only inside a dissent. Parental genotyping is credited with detecting a de novo allele without noting that such an event leaves phase unresolved by that route.

Withdraw Suijkerbuijk 2010 and the allele 1 conclusion collapses, with it the withdrawn digoxin mechanism objection and "the therapeutic object is the transcript, not the fold". Withdraw Baker 2013 and §7 changes sign. Only the second is flagged.

## 4. Criteria

**Rigour 6.** Sequence work correct and checkable, tier tagging real; against it, a miscited flagship figure, an unsourced 1.44, a missed ClinVar record for the same protein change, an unflagged species-numbering coincidence, and power figures assuming zero biological variance. Raise it by fixing those and assigning ACMG codes to both alleles.

**Impact 6.** The avoidance rule and surveillance additions act now and cost nothing, but the highest-value item, reading *UGT1A1* from a file already on disk, sits below a page-long rule. Raise it by putting zero-cost, zero-consent outputs first.

**Innovation 6.** The gate as primary deliverable, exposure arithmetic killing metformin, and power before endpoint choice are unusual here, and the tool is honest about its failure mode. But the persona machinery yields caution rather than discovery, and no pipeline candidate survived.

**Scalability 5.** The claim is a two-change transfer and the manuscript states the transfer has not been run, which is honest and is also the entire test. Raise it by running one other chromosomal instability gene and reporting what broke.

## 5. Statistics

The FISH figure reproduces only under an unstated assumption. At fraction 0.10 with 1,000 nuclei, binomial SD is 0.00949 (CV 9.49 percent); pooling three gives 5.48; the difference of two such means has SE 7.75; 2.80 x 7.75 = 21.7, the stated 22. That is counting error with a normal approximation and zero between-measurement variance; as three paired observations with t critical values the same inputs give roughly 29 to 42 percent. The 41 percent micronucleus figure reproduces the same way at a baseline near 1.5 percent. The 37.5 percent reticulocyte figure does not: a scoring CV of 0.022 pooled over three gives about 5 percent, so that entry carries a biological variance term the other two omit. The three do not share a variance model, and §9 question 10 concedes that the term set to zero is unmeasured.

§8's threshold is not recomputable as printed. With s=0.2 and added harm 5 percent, a required reduction above 60 percent follows only from a 38.7 percent baseline (64.6 percent); at the Orphanet figure near 75 percent it is 33 percent. The manuscript refuses to choose between the two estimates, then prints a threshold that depends silently on the choice. "17 subjects, inside an enrollable population of roughly 15 to 20" is true at the upper bound and false at the lower.

## 6. What is missing

No ACMG classification for either allele. The codes a geneticist wants: PVS1 on the NMD prediction plus PM2 for allele 1; PM2 and at most PP3 for allele 2, with PM3 unavailable precisely because phase is unproven. The right conclusion is reached without the framework that makes it auditable.

No cytogenetic confirmation. MVA is a cytogenetic diagnosis, and gate item 3 proposing a PCS karyotype implies none exists, so the prescribing architecture rests on unproven phase, one VUS and no PCS count. §12 notes "Neither team asked whether the diagnosis is right" and then reorders nothing.

Nothing on whether a 737X protein would accumulate at all: Suijkerbuijk 2010 states that none of 386X, 731X or 753X could be detected in patient or parental lysates, so the transcript-not-fold conclusion needs three untested steps and two are named. Nothing on the allele 2 missense escaping NMD in the last exon, so the immunoblot at gate item 4 will largely measure the allele 2 product, which makes item 5 the more informative test; the ordering does not reflect it.

## 7. Ethics and framing

Defensible. The lay summary opens by saying nothing is expected to reduce cancer risk and that surveillance remains the only thing acting on it; the oncological carve-out is repeated verbatim with its intent-based wording correctly argued; "We do not know whether the target is present in him" is the right sentence. Nothing reads as a promise or a verdict. Two problems: the family is nowhere told in §1 that the second allele is a variant of uncertain significance and that the diagnosis is provisional on that ground too, and §5, written to be photocopied, names substitutes to swap in (terbinafine, levetiracetam, a thiazide) that will be read as advice by anyone who does not reach §6. Adding "for the treating team to consider" inside the box costs nothing.

## 8. Verdict

**Major revision.** The genotype work is more careful than most submissions of this kind and verifies against primary sources where it matters. Three fixes, in order:

1. Correct the allele-level errors: Figure 4 not Figure 5; source or drop 1.44; add the c.3006T>A ClinVar VUS; repair the Welch and Floquet sentence.
2. State everywhere that mouse BubR1 1002 is human 1012, and correct the J-point sentence to BubR1^H/H, male mice. As written it reads as though a mouse carries this child's missense allele.
3. Reorder the gate: trio genotyping and a PCS karyotype first and alone, an 11 kb genomic long-read amplicon as the definitive phase test, explicit ACMG codes for both alleles, and §8 rerun with a variance model that does not set the unmeasured term to zero.
