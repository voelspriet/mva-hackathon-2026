# Referee 3, clinical pharmacology and methodology

Checks were made by direct retrieval of primary records (NCBI eutils, PMC, EMA, the openFDA label API), the web search quota having been exhausted. All arithmetic was recomputed.

## 1. What the manuscript claims

No approved drug acts on BubR1, so the highest-value outputs are a prescribing avoidance rule, three cost-free surveillance additions, a renal work-up, and measurements that would show whether any gene-directed hypothesis has a target in this child. Every mechanism-directed candidate is excluded on exposure or evidence grounds or held as a named experiment, and the method is the transferable product. The claim is statable in two sentences.

## 2. Validity

**Supported.** Nakano 2024 (PMID 39264246) contains, verbatim, "Renal ultrasound q 3m until age 7". Kajii 2001 (PMID 11746029) gives parental PCS of 3.5 to 41.7 percent, Rio Frio 2010 (PMID 21190457) the homozygous intronic case, Baker 2013 (PMID 23242215) the quoted sentence with its original misspelling. The EMA confirms the Commission decision of 28 March 2025 not to renew ataluren. Suijkerbuijk 2010 (PMC2887387) states that LAP-731X "restored the response to nocodazole as well as proper chromosome segregation in unperturbed mitosis", so the 731X correction is real.

**Supported, expected to fail.** The dasatinib formulation asymmetry: openFDA returns 16 current US dasatinib labels, all tablets, none a powder for oral suspension.

**Contradicted.** Bisogno 2019 (PMID 31562043) reports 5-year overall survival 86.5 versus 73.7 percent, and disease-free survival, the primary endpoint, 77.6 versus 69.8 at p=0.061. The manuscript prints "85.0 percent against 72.4 percent" twice and never says the primary endpoint missed significance. Both errors favour the argument.

**Contradicted as attributed.** PMID 9412992 is Ramírez, Mutagenesis 1997, not "Vanhauwaert 1998": right content, wrong source, in a manuscript whose method claim is verification against primary sources.

**Overstated.** PMID 36588761 says only that MVA2 patients "probably do not benefit" from growth hormone; "no response in the two MVA2 patients tested" is not in it. Matsuura 2006 (PMID 16411201) studies *monoallelic* *BUB1B*, so its ">50 percent decrease" is an inference about causation, not a residual measured in a biallelic patient. G6PD status does not gate hydroxychloroquine as it gates primaquine.

**Unverifiable, and load-bearing.** The metformin exclusion rests on Tang 2011 Figure S1A and Table S1. The accessible record (PMC3532042) is abstract-level and metformin is nowhere in it, so two dissents, a removal from the ranked list and question 5 rest on numbers in no reachable primary record.

## 3. Logic

The metformin arithmetic is right and understated. 500/15.5 = 32.3, 1000/7.7 = 129.9, 5 mg/L = 38.7 micromolar, 38.7/15.5 = 2.5, 38.7/7.7 = 5.0. The number that settles it is never printed: at the toxicological ceiling the gap is still 12.9 to 25.8 fold. But "cannot be closed by dose, salt, formulation or tissue" overreaches on the last word, since metformin is transporter-concentrated and enterocyte and hepatic exposures are not plasma. Scope the claim to a fibroblast or lymphocyte target.

The transcript conclusion does not follow. The manuscript reports 731X mRNA reduced about two-fold, and the same paper states the truncated proteins "could not be detected in lysates of MVA patient cell lines". Transcript at half with no detectable protein is evidence against "the therapeutic object is the transcript, not the fold"; detectability came from a strong promoter and a tag, not from NMD bypass. This is the largest silent tier upgrade, and it reopened four panel positions.

The carve-out contradicts row 6: §5 forbids substituting any agent in a rhabdomyosarcoma protocol, row 6 substitutes cyclophosphamide for ifosfamide. Schneider 2020 reviews predisposition among genitourinary rhabdomyosarcomas, so citing it to show MVA rhabdomyosarcoma is characteristically genitourinary conditions on the outcome. Withdraw Baker 2013 and the BubR1-raising bar returns; withdraw the Tang supplement and §7's metformin paragraph, both dissents and question 5 fall.

## 4. Criteria

**Rigour, 6.** Tier tagging, printed dissents and the 731X correction are the right instincts; against them, a headline statistic wrong in the argument's favour, a misattributed safety citation, two overstated citations, and a quantitative section that is not internally consistent. Fix those and declare one variance model for 8.

**Impact, 5.** Only the avoidance rule and the surveillance additions act this month, and the one called free is weakest: *UGT1A1\*28* is a promoter TA-repeat that short-read WGS calls unreliably, and rhabdomyosarcoma salvage gives irinotecan at 20 to 50 mg/m2/day, below the exposures at which \*28 guidance changes dosing.

**Innovation, 6.** The method did more than opinion would, since four positions moved on primary sources, but nothing measures whether another architecture yields the same list and no seat found an error inside a dossier. A held-out dossier with a planted error would test it.

**Scalability, 6.** The tool transfers in principle and the transfer was not run; the aggregated crossover is the most scalable idea here and its sample size is unreliable.

## 5. Quantitative claims

Reproducing the detection limits with the obvious model, a two-sided 5 percent test at 80 percent power on two period means of three measurements, gives 2.8 x CV x sqrt(2/3).

- FISH, 1,000 nuclei at fraction 0.10: binomial CV 9.49 percent gives 21.7 percent, so the stated 22 is counting error only.
- Micronuclei, 2,000 binucleated cells: 41 percent implies a baseline near 15 per 1,000, never stated, in a child said to have no baseline.
- Micronucleated reticulocytes: with the stated CV of 0.022 the formula gives 5.0 percent, not 37.5. Reaching 37.5 needs a CV of 16.4 percent, a biological variance term used here and nowhere else; applied to the FISH line, 22 becomes about 43.
- Aggregated crossover: 17 subjects for a 20 percent change implies a CV of 20.8 percent, where the FISH assumptions need 4. Both cannot stand, and against an enrollable population of 15 to 20 it needs near-complete enrolment with no dropout.
- "The three-per-period design, not the assay, binds" is false on its own model: 1,000 to 4,000 nuclei gives 10.9 percent, three to six measurements only 15.4.
- Thresholds: 0.05/(0.2 x 0.387) = 64.6 percent, so "exceeds 60 percent" silently adopts 38.7 percent; with the Orphanet 75 it is 33, and the next sentence declines to choose between them.
- Mosaicism: 10 percent of cells and "near 4 percent" are joined by a model not shown; 21 percent across five chromosomes assumes five independent equal clones.
- Passing: 115/1,461,878 = 7.87e-5, and 2210 + 747 = 2957, upstream of c.3006. Unexplained: a stop at codon 731 encodes 730 residues, not 715.

## 6. What is missing

Age, weight, renal function, current medicines, and whether ifosfamide was given. The manuscript names this blind spot and prescribes around it: no agent carries a mg/kg, a formulation, or a licence status for the relevant age. Obtainability is asserted, and fails in places. Mebendazole and albendazole are barred while every other barred drug gets a substitute, leaving no licensed equivalent for threadworm in a young child. Anakinra is a daily subcutaneous biologic, not a substitute for colchicine. Hydroxychloroquine has no licensed paediatric liquid in the major markets, and the retinal screening demanded is not performable at this age. Dexrazoxane's US label states paediatric safety and effectiveness have not been established, which row 6 omits. There is no interaction analysis beside the QT stacking section and no *CYP2D6* call for ondansetron despite a genome in hand. No n-of-1 model is specified: no randomisation, no carryover handling, no multiplicity control, no number behind the "pre-filed threshold", no regulatory route.

## 7. Ethics and framing

Defensible: the opening refusal, the statement of what no test can show, the consent architecture, and treating a cis result as a re-diagnosis. Three problems: the carve-out and row 6 contradict each other, and row 6 is what an oncologist would act on; the renal branch logic reads as a protocol, naming agents, sequence and a six-week readout; the surveillance additions are sold as costing nothing, true of scanner time but not of the *UGT1A1* claim.

## 8. Verdict

Major revision.

1. Rebuild §8: correct Bisogno, recompute the detection limits and crossover size under one declared variance model, state the micronucleus baseline 41 percent assumes, print the 12.9 to 25.8 fold residual metformin gap, and name the risk figure behind the 60 percent threshold.
2. Resolve the carve-out against row 6, correct the four citations above, and restate the allele 1 conclusion to account for undetectable 731X protein at half-normal transcript.
3. Add an obtainability appendix: licence status by age, formulation, mg/kg, renal adjustment and interaction check per agent, a substitute for the barred anthelmintics, and a statement that weight, age and renal function were unavailable.
