# Research prompt: MVA Hackathon 2026, Tracks 1 and 2

## Context

One proband (PROBAND01, sample WGS_EX2312012) with a clinical diagnosis of Mosaic Variegated Aneuploidy. Whole-genome sequencing. The organisers hold an NHS-validated answer for Track 1. The public scoring code (evaluation.py) describes that answer as compound heterozygous. Track 2 has no answer key; it is judged by a panel.

Submissions close 24 October 2026, 23:59 UTC. Winners announced 25 November 2026.

## Inputs

Local paths under ~/vibecoding/mva-hackathon/:

- data/WGS_EX2312012_HGWCNDSX7.vcf.gz (+ .tbi): 4.74 M PASS variants, GRCh38 no-alt analysis set, contigs named 1..22, X, Y, M (no chr prefix). Caller: Sentieon 202308.02, then GATK VariantFiltration. FORMAT includes GT, AD, DP, GQ, PL, PGT, PID. INFO AF is the within-sample allele fraction, not a population frequency.
- data/Challenge_Clinical_Phenotype_1.docx, extracted to work/phenotype.txt: clinical description with HPO terms. No other clinical data exists (discussion #14).
- Raw reads: 8 FASTQ files (4 lanes, paired), 84 GB, on the HF dataset. Not downloaded.
- work/mva_genes.json: GRCh38 coordinates for BUB1B, CEP57, TRIP13, BUB1, MAD2L1, CENPE from Ensembl.
- work/core.annot.vcf.gz: PASS variants in BUB1B, CEP57, TRIP13, annotated with bcftools csq (Ensembl 116) and ClinVar. Not yet read.
- work/ref/: Ensembl GRCh38.116 GFF3, FASTA for chromosomes 5, 11, 15, ClinVar GRCh38 VCF.
- scoring/evaluation.py: the Space's scorer. scoring/score_local.py: offline rehearsal wrapper.
- docs/: About, Rules, FAQ, Submit tabs, methods_description_form.xlsx, track1_submission_template.csv, dataset README, discussions #2 #4 #5 #10 #13 #14 #17 #18.

## Constraints

Data handling:
- Do not send patient data to any service that can retain, train on, or reuse it (discussion #2, processor test). Annotation runs offline. Population-frequency and literature lookups use public resources at the gene or variant level only where the resource's terms meet the processor test; otherwise download the resource and query locally.
- LLM use: Claude Code on a Max plan with model-improvement sharing disabled; no output rating. Record this line in both methods forms.
- Keep patient data out of git. Delete all data, derived files and caches within 30 days of 24 October 2026 and email MVAHackathon2026@synapse.org to confirm.
- Do not contact the family or the MVA Society.

Submission mechanics:
- Track 1: CSV per docs/track1_submission_template.csv. Up to 10 rows. Contigs must carry the chr prefix. Coordinates GRCh38. epcr in (0, 1], rows ranked by epcr. finding_type primary or secondary. Six uploads per HF user; best counts. Each upload requires a report (PDF or MD) and a GitHub URL.
- Track 2: report (PDF or MD), GitHub URL, 3-minute video URL. Three uploads; the panel reads the latest only. Market-approved drugs only; combinations allowed (discussion #5).
- Methods form: docs/methods_description_form.xlsx, one per model. Questions cover: automated versus manually curated output, public versus proprietary data, ability to output compound-het pairs, handling of secondary findings, run time and cost, 500-word abstract with strengths and limitations.
- Repository: reproducible code and configuration; private until close, public afterwards.

## Research questions, Track 1

1. Which variants in the VCF are candidates for a compound-heterozygous recessive cause of MVA?
   a. In the known MVA genes (BUB1B, CEP57, TRIP13): list every PASS variant with genotype, consequence per transcript, ClinVar status, dbSNP membership, read depth and allele balance.
   b. Genome-wide, independent of gene list: apply the same filters to all genes, so the known-gene result can be compared with an unbiased ranking.
2. For each candidate pair: are the two variants on different haplotypes? Use PGT/PID where present. State what can and cannot be concluded without parental data.
3. What is the population frequency of each candidate? Identify a source that meets the processor test or can be queried offline.
4. What does the phenotype document add? Map the text to HPO terms and check each candidate gene against those terms.
5. Which variants outside the primary answer meet criteria for a secondary finding? Decide whether to include any and on what basis.
6. How does the ranking behave under the scorer? Run scoring/score_local.py against hypothetical answer sets to confirm format, ordering and the chr prefix before any upload.
7. Does re-calling from FASTQ change any of the above? Decide whether this is needed for the answer, for the write-up, or not at all, and record the reasoning.

## Research questions, Track 2

1. What is the mechanism of the Track 1 variants: loss of function, hypomorphic, dominant negative? What does the literature say about the same or similar variants in this gene?
2. What pathway is disrupted (spindle assembly checkpoint, chromosome segregation), and what are the downstream consequences that produce the phenotype (aneuploidy, cancer predisposition, growth, microcephaly)?
3. Which market-approved drugs act on that pathway or on its downstream consequences? Sources: DrugBank, ChEMBL, Open Targets, ClinicalTrials.gov, PubMed, OMIM, Orphanet, MVA Society research programme.
4. For each drug: mechanism of action, evidence in cell or animal models of this gene or pathway, evidence in humans, dose and safety in children, interaction with the child's phenotype (for example nephrocalcinosis, discussion #14), and what an experiment to test the hypothesis would look like.
5. Which candidates carry a plausible harm? Record contraindications alongside benefits.
6. What is the scalability argument: which steps of the method transfer to another undiagnosed individual or another gene?

## Order of work

1. Read work/phenotype.txt and work/core.annot.vcf.gz. Record the candidates.
2. Run the genome-wide filter. Compare.
3. Resolve phasing, frequency and ClinVar for the candidates.
4. Rehearse the CSV with score_local.py. Upload one Track 1 submission with the report and methods form.
5. Track 2 literature and database work. Draft the report with the methods form structure.
6. Record the pitch video. Upload Track 2.
7. Publish the repository at close. Delete data. Send the deletion email.

## Record for the report, as work proceeds

- Every tool and version, every public data source and version, every filter threshold.
- Every manual decision and its reasoning.
- Run time and cost per step.
- What was not done and why.
- The LLM line: provider, plan, setting.
