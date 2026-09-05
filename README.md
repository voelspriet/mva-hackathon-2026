# MVA Hackathon 2026, Track 1 pipeline (henkvaness)

Single-sample GRCh38 VCF in, ranked Track 1 CSV plus evidence out. One command, about one minute on a laptop.

    pipeline/run.sh data/<sample>.vcf.gz work/

Steps (see `pipeline/run.sh`): header facts; PASS variants in BUB1B, CEP57, TRIP13 with `bcftools csq` (Ensembl 116) and ClinVar (offline); gnomAD v4.1 counts by HTTP range read of the public sites files (no query leaves the machine); genome-wide recessive-compatible scan without a gene list; mosaic aneuploidy profile from allele depths; ACMG SF v3.2 secondary-findings screen; CSV construction by a written rule set (`pipeline/make_csv.py`); offline rehearsal against the Space's own scorer (`scoring/score_local.py`).

Patient data is never committed: `data/` and `work/` are ignored. The only proband-derived content here is the submission CSV (the two candidate variants), the per-chromosome aggregate figure, and the report.

Requirements: bcftools/htslib 1.24 with libcurl, Python 3.11 with pysam, matplotlib, openpyxl. Reference files (about 1 GB) download on first run.

LLM use: Claude Code (Anthropic) on a Max plan with model-improvement sharing disabled, no output rating; used to write and run the scripts. Report: `REPORT_track1.md`.
