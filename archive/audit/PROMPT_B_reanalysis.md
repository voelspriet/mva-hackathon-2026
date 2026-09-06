# Prompt B: re-analysis of the primary data for new angles

## Purpose

The primary data are re-examined without reference to the conclusions already drawn, to identify questions the project has not asked.

## The primary data

1. The patient's whole-genome VCF at data/WGS_EX2312012_HGWCNDSX7.vcf.gz: 4,740,790 PASS variants, GRCh38, single sample, GATK VariantFiltration over Sentieon calls, FORMAT fields GT, AD, DP, GQ, PL, PGT, PID.
2. The clinical phenotype document, extracted at work/phenotype.txt: eight HPO terms and the notes accompanying them.
3. Derived outputs already computed: work/mosaic_robust.json and mosaic.json (per-chromosome and per-bin allele-balance and depth statistics), work/exomiser/results/ (genome-wide phenotype-driven ranking), work/coding_nodbsnp.gene.vcf.gz, work/acmg.clinvar.vcf.gz, pipeline/track2_compute/ outputs in work/track2/.
4. The raw sequencing reads, 8 FASTQ files, about 84 GB, on the gated Hugging Face dataset and not downloaded.

## Constraints on handling

Patient data does not leave this machine. Public resources are read as static files or through range requests, never queried with patient coordinates. Gene-level and protein-level lookups against public databases are unrestricted.

## The task

Examine the data for what has not been asked. The following are starting points, not a list to work through:

1. Signals in the VCF that no analysis so far has used: phasing information in PGT and PID across the genome, runs of homozygosity, the mitochondrial genome, copy number inferable from depth, regions of low or absent coverage, structural variant signatures visible in a germline VCF, and the X and Y evidence.
2. Whether any second hit, modifier or contributing variant is present that the gene-list and phenotype-driven approaches would both miss: regulatory and deep intronic variants near BUB1B, variants in genes whose products interact with BubR1 at the kinetochore, variants in the mitotic checkpoint that would not be called causal alone.
3. What the mosaicism computation did not look for: segmental rather than whole-chromosome events, uniparental disomy, copy-neutral loss of heterozygosity, mosaicism in the regions the bin filter discarded, and whether the method's discarded bins are informative rather than artefactual.
4. Whether the phenotype terms, read again, imply an investigation nobody proposed. The eight terms and their notes are the clinical information in the dataset. The notes name a family history as phenotypic input.
5. What the raw reads would answer that the VCF cannot, and whether any of it changes a decision. Specify what would be run, on what, and what result would change what.
6. Approaches published since 2024 in chromosomal instability, aneuploidy detection, single-cell and long-read methods, and rare disease diagnosis that apply to this data and were not considered.
7. Questions answerable from public data alone, without this patient: population-scale evidence about this gene, this variant class, or this disease that nobody in the project has looked up.

## Method

For each angle proposed:
- State the question.
- State what data answers it, and whether that data is in hand, obtainable, or absent.
- Where it is in hand, compute the answer and report it, with the script saved under pipeline/.
- State what each possible result would change: which hypothesis, which recommendation, which measurement.
- State the evidence tier and the cost.
- State why it was not asked before, if that is identifiable.

## Output

track2/reanalysis/R<n>_<topic>.md per angle, and one file track2/reanalysis/SUMMARY.md ranking every angle by what it would change per unit of effort, separating angles already computed from angles proposed.

## Constraints

Computed results are labelled computed and are reproducible from a saved script. Inference is labelled inference. Nothing is proposed that requires contact with the family or the organisers. No em or en dashes. No adjectives of praise or alarm. An angle that turns out to be a dead end is reported as a dead end, with what was checked, so that it is not repeated.
