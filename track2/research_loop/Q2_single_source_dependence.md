# Q2. Does the mechanism section survive its dependence on one 2010 paper?

**Asked because** the cross-model reuse pass counted 28 citations to Suijkerbuijk 2010 across the corpus, more than any other source by a wide margin, and the 731X episode showed what happens when that one paper is misread: every layer of this project treated a splice-acceptor allele as a nonsense allele for the whole of its life. Nobody had asked what the mechanism section would look like if that paper were wrong.

## Answer

**Half of it survives on independent evidence and half of it does not, and the report did not distinguish the two.** The core of the mechanism has genuine independent corroboration from a different laboratory on a different continent. The specific results that carry the therapeutic argument do not.

### The authorship check, which is the part that changes the picture

| Paper | First author | Senior author | Institution |
|---|---|---|---|
| Suijkerbuijk 2010, Cancer Res 70:4891, PMID 20516114 | Suijkerbuijk SJ | Kops GJ | UMC Utrecht |
| Suijkerbuijk 2012, Dev Cell 22:1321, PMID 22698286 | Suijkerbuijk SJ | Kops GJ | UMC Utrecht |
| Hanks 2004, Nat Genet 36:1159, PMID 15475955 | Hanks S | Rahman N | Institute of Cancer Research, Sutton |

Suijkerbuijk 2010 carries **Hanks S and Rahman N as co-authors**. So the 2004 gene discovery and the 2010 mechanism paper share authors, and the 2010 and 2012 mechanism papers share first author, senior author and institution. What this project has been treating as three lines of evidence is closer to one group's programme with an overlapping collaboration.

The report said Dev Cell 2012 "independently" retested 731X. That word is wrong and is corrected.

### What an independent group has shown

**Matsuura 2006, Am J Med Genet A 140:358, PMID 16411201**, Hiroshima University, seven Japanese families, no author overlap with Utrecht or Sutton. Full abstract reached via NCBI efetch. It reports, verbatim:

- "Transcripts derived from the patients with the 1833delT mutation and the splice site mutation were significantly reduced, probably due to nonsense-mediated mRNA decay."
- "BubR1 in the cells from two patients showed both reduced protein expression and diminished kinetochore localization."
- "Microcell-mediated transfer of chromosome 15 (containing BUB1B) into the cells restored normal BubR1 levels, kinetochore localization of p55cdc, and the normal responses to colcemid treatment."
- "suggest that >50% decrease in expression (or activity) of BubR1 is involved in the PCS syndrome."

That is independent support for three of the report's load-bearing claims: nonsense-mediated decay of truncating *BUB1B* alleles, reduced BubR1 protein with a checkpoint defect in patient cells, and rescue by restoring *BUB1B*. Matsuura's rescue is chromosome transfer rather than plasmid-driven expression, which is a different method reaching the same result. A fourth, the quantitative dose model, is Matsuura's own conclusion.

**Rio Frio and Foulkes 2010, N Engl J Med 363:2628, PMID 21190457**, McGill, also independent, supplies the adult-onset phenotype the report uses in section 6.

### What remains Utrecht-only

| Claim | Where the report uses it | Second source |
|---|---|---|
| A BUBR1 protein lacking the kinase domain rescues checkpoint, alignment and segregation (731X, Figures 5A to 5C) | Section 2, the allele 1 argument | Suijkerbuijk 2012, **same laboratory** |
| Q921H sits in the kinase domain and behaves as wild type on level and function | Section 2, the argument that position does not predict class for allele 2 | **None** |
| Kinase-domain missense alleles turn over about two-fold faster, HSP90-dependent and proteasome-mediated | Section 2, and the HSP90-inhibitor row in section 7 | **None** |
| The identity of the 731X allele as IVS16-2A>G | Section 2 and section 13 | **None**; it is in that paper's supplement and in neither ClinVar nor public LOVD |

**The dependence is real but narrower than 28 citations suggests.** The claim that would fall hardest is the one about the kinase domain being dispensable, because it is what allows the report to say that the therapeutic object for allele 1 is the transcript rather than the fold. It rests on one laboratory, tested twice.

### Correction applied

Two changes to `REPORT_track2.md` section 2. The word "independently" is removed from the Dev Cell 2012 sentence and replaced with the authorship fact. And a short paragraph now states which mechanism claims have independent corroboration from Matsuura 2006 and which are single-laboratory, so a reader can see the load-bearing ones without doing this authorship check themselves.

## Access levels reached

Full abstracts for all five papers via NCBI efetch, which carries the author lists and affiliations in full. The Cancer Res 2010 article body remains unreachable, as recorded in the audit: the AACR page returns no article body through a text-extraction proxy and no PMC deposit of the body text was located. That does not affect this answer, which turns on authorship and on Matsuura's abstract, both fully reached.
