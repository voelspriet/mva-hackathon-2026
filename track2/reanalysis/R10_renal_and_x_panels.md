# R10. Two gene-scope questions the phenotype demanded and nobody asked

**Asked 6 September 2026.** Both are negatives, and both are worth having because in each case the report had been reasoning as though the question were closed when it had never been opened.

## Part 1. Is there a genetic cause of the nephrocalcinosis?

### Why this had to be asked

`track2/anomalies/ANOMALIES.md` D1 is the sharpest unresolved item in this project:

> The phenotype document states: "Nephrocalcinosis, HP:0000121, Calcium deposits in kidney tissue; **present since birth**". Nephrocalcinosis of prematurity develops over weeks of neonatal intensive care. Ifosfamide followed the rhabdomyosarcoma diagnosis, years later.

**Both causes the report considers are postnatal, and the supplied document says the finding was there at birth.** D1 proposed to settle this with a date from the records, which nobody here can obtain. It never considered the third possibility: that the child has an inherited tubulopathy or hypercalciuric disorder, which would be present at birth by definition and would explain the anomaly outright.

That question is answerable from data already in hand, and it had not been asked. The renal genes in `work/track2/genes_pgx.bed` were never scanned as a panel, as R8 records.

### Method

A 50-gene panel in `pipeline/reanalysis/renal_genes.txt`, covering hypercalcaemia and vitamin D handling, calcium sensing, the Bartter and Gitelman genes, Dent and Lowe, distal renal tubular acidosis, the hypomagnesaemia genes, all three primary hyperoxalurias, cystinuria, purine handling and cystinosis. 49 of the 50 resolved against the local Ensembl CDS annotation, giving **1,029 coding intervals** with 8 bp of flank so canonical splice sites are included. *SLC9A3R1* did not resolve under that symbol and is the one gap.

Variants were taken PASS-only, annotated for consequence with snpEff GRCh38.86, matched against the full local ClinVar release, and any variant of interest was checked for population frequency in gnomAD v4.1 by byte-range read.

### Result

| | |
|---|---|
| PASS variants in the panel's coding sequence | **123** |
| Carrying a ClinVar record at that exact allele | 110 |
| **Pathogenic or likely pathogenic** | **0** |
| Conflicting classification | 5 |
| Benign or likely benign | 105 |
| Frameshift, nonsense or splice-site variants | **0** |

**Not one pathogenic or likely pathogenic variant in 49 renal genes, and not a single truncating variant of any kind.**

The five conflicting records and every homozygous missense resolve on frequency. Each was checked individually.

| Variant | gnomAD AF | Homozygotes | Verdict |
|---|---|---|---|
| *SLC3A1* p.Met618Ile, homozygous | 0.660 | 324,999 | Common. The reference carries the minor allele |
| *CASR* p.Glu1021Gln, homozygous | 0.956 | 668,521 | Near-fixed |
| *SLC34A3* p.Glu513Val, homozygous | 0.853 | 532,609 | Near-fixed |
| *VDR* p.Met1?, "start lost" | 0.625 | 288,010 | rs2228570, the FokI polymorphism. Translation restarts downstream |
| *SLC34A1* p.Ala133Val | 0.0041 | 21 | Already assessed in creative D as likely benign. Confirmed |
| *ATP6V1C2*, 37 bp deletion, no rsID | 0.0188 | 57 | **Intronic**, c.826-611_826-575del. Not coding at all |

The *ATP6V1C2* deletion was the only variant in the whole panel with no rsID and no ClinVar record, so it was the one candidate for something genuinely new. It is an intronic indel carried by 1.9 percent of people.

### What this settles

**A monogenic renal cause of this child's nephrocalcinosis is excluded, to the resolution a coding panel can reach.** D1 listed two candidate causes, both postnatal, against a document saying the finding was present at birth. The third candidate, the one that would have resolved the contradiction, is not there.

D1 is therefore **narrowed, not closed**. The contradiction stands and still needs the date from the records. But the explanation that would have dissolved it without any new information has been looked for and is absent.

Limits, stated because a negative is only as good as its scope: coding sequence and canonical splice sites only, so deep intronic, regulatory, copy-number and repeat variation are not covered, and a gene outside the 49 is not covered.

## Part 2. The X chromosome, in a male

### Why this had to be asked

The proband is male. This was measured earlier in the project, from an X to autosome depth ratio near 0.5, a non-PAR X heterozygosity of about 1 percent, and the presence of chrY. **In a male every non-PAR X variant is hemizygous, so a single damaging allele is fully expressed with nothing to mask it.** No recessive scan and no gene-list scan in this project ever treated the X that way. The genome-wide recessive scan in Track 1 looks for two hits, and on the X there is only ever one.

### Method

All 12,001 coding intervals of the 867 X-linked genes in the local CDS annotation, PASS variants only, snpEff GRCh38.86, restricted to HIGH-impact consequences, which is where a fully penetrant hemizygous allele would sit.

### Result

445 PASS coding X variants, of which **12 carry a HIGH-impact annotation. All twelve are explained and none survives.**

**Three are mismapping, and the genome says so itself.** *SLC25A5* carries two frameshifts and a stop-gain at chrX:119469743, 119469998 and 119471038, and **all three are called heterozygous**. A heterozygous call at a non-PAR X locus in a male is not a variant; it is reads from more than one place stacked on one locus. *SLC25A5* has close paralogues and processed pseudogenes, which is exactly the configuration that produces this.

This gives a general filter worth naming. **Across non-PAR X, this genome has 101,751 hemizygous calls and 1,310 heterozygous ones, a heterozygous rate of 1.27 percent.** In a male that 1.27 percent is the artefact background, and any X finding that lands inside it should be treated as artefact before it is treated as biology.

**One is in a pseudoautosomal region.** *ASMT* at chrX:1636511 sits inside PAR1, where two copies and therefore heterozygosity are normal.

**Eight are common polymorphisms**, and most of them are the same phenomenon: GRCh38 carries the minor allele, so matching the population looks like a mutation.

| Gene | snpEff call | gnomAD AF | Homozygotes |
|---|---|---|---|
| *TCEAL6* | frameshift p.Gln175fs | **0.999** | 365,669 |
| *HUWE1* | structural interaction | **0.999** | 366,511 |
| *NUDT11* | frameshift and start lost | **0.998** | 345,900 |
| *PRICKLE3* | frameshift p.Leu61fs | **0.943** | 301,208 |
| *G6PD* | structural interaction | **0.867** | 280,377 |
| *AIFM1* | stop lost | 0.416 | 65,871 |
| *TLR8* | start lost | 0.281 | 30,940 |
| *PIR* | structural interaction | common | n/a |

**There is no hemizygous loss-of-function variant of any consequence on this child's X chromosome.**

## The pattern across R7, R8 and R10, which is the reusable part

Four separate screens in this project have now produced a confident-looking damaging call that dissolved on population frequency alone:

| Screen | Call | What killed it |
|---|---|---|
| R7 | *PRSS1* pathogenic missense | AF 0.386 with zero homozygotes in 59,319 genomes, against about 8,839 expected |
| R8 | *G6PD* coding variant in a hemizygous male | AF 0.867 |
| R10 | *TCEAL6*, *NUDT11*, *PRICKLE3* frameshifts | AF 0.94 to 0.999 |
| R10 | *SLC3A1*, *CASR*, *SLC34A3* homozygous missense | AF 0.66 to 0.96 |

**A consequence predictor tells you what a variant would do if it were rare. It does not tell you whether it is rare.** In several of these the reference genome carries the minor allele, so a variant call means the child resembles almost everybody. Frequency triage is not a refinement step to run at the end; run without it, every one of these screens returns a false positive with a plausible protein consequence attached.

## What R10 changes

| | |
|---|---|
| New findings | **None** |
| Anomaly D1 | Narrowed. The third possible cause is excluded; the contradiction still needs a date from the records |
| X chromosome | Positively screened for the first time, and clean |
| New artefact filter | The non-PAR X heterozygous rate, 1.27 percent here, as a floor for X findings in a male |
| Recommendations added | **None** |
