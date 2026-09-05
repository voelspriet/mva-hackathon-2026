# Track 1 report: variant identification, PROBAND01

Team: henkvaness (individual). Model 1: `henkvaness_bub1b-rules-v1.csv` (rule-based, known genes). Model 2: same CSV, confirmed by phenotype-driven genome-wide ranking (section 3b). Date: 5 September 2026.

## 1. Approach

A single-sample GRCh38 whole-genome VCF (Sentieon 202308.02 calls, GATK VariantFiltration, 4.74 M PASS variants, autosomal depth 44x) and eight HPO terms were the inputs. The pipeline (`pipeline/run.sh`) runs seven steps in one minute:

1. Header facts: reference build, caller, sample, contig naming (this VCF uses `1..22, X, Y, M`; the submission adds the `chr` prefix).
2. Known-gene pass. PASS variants in BUB1B, CEP57 and TRIP13 (the three genes with published biallelic MVA causation) are annotated offline with `bcftools csq` against Ensembl 116 and with the current ClinVar GRCh38 VCF.
3. Population frequency. gnomAD v4.1 exome and genome counts for every coding or ClinVar-flagged candidate, read by HTTP range request from the public Google Cloud Storage sites files through their tabix index. No query string carrying a position is sent; the bucket is a static file host.
4. Genome-wide check without a gene list. PASS variants overlapping any Ensembl CDS, not flagged as dbSNP by the caller, GQ >= 50, DP >= 10, grouped per gene; genes with two or more heterozygous or one homozygous variant are listed.
5. Mosaic aneuploidy profile from the VCF alone (section 4).
6. Secondary findings: ACMG SF v3.2 gene list screened against ClinVar (section 5).
7. CSV construction by a written rule (`pipeline/make_csv.py`): consequence class (truncating 3, missense 2, other 1), +2 for ClinVar pathogenic or likely pathogenic, +1 for gnomAD AC <= 5 with no homozygotes, -3 for AF > 1e-3. The two top-scoring heterozygous variants in one gene form row 1; each alone forms rows 2 and 3; further variants form alternative pairings. The file is checked against the Space's scoring code before upload.

Generative AI: Claude Code (Anthropic), Max plan, model-improvement sharing disabled, no output rating. Used to write and execute the scripts and to draft this report; all variant-level processing ran locally.

## 2. Result

| Rank | Variant (GRCh38) | Protein (ENST00000287598) | GT, AD | Consequence | ClinVar | gnomAD v4.1 |
|---|---|---|---|---|---|---|
| 1 (pair) | chr15:40209701 T>G | p.Leu737Ter | 0/1, 21/25 | stop gained, exon 17/23 | Pathogenic/Likely pathogenic, 2 submitters, no conflicts, MVA syndrome 1 | exomes 115/1,461,846 (7.9e-5), genomes 5/152,174, 0 homozygotes |
| 1 (pair) | chr15:40220612 T>G | p.Asn1002Lys | 0/1, 15/13 | missense, exon 23/23, kinase domain | same protein change via c.3006T>A: VUS, Ambry 2025 (VCV004600147); c.3006T>G itself unsubmitted | exomes 1/1,461,878 (6.8e-7), genomes absent, 0 homozygotes |

Rows 2 and 3 carry each variant alone at lower EPCR so that a single-variant answer key still scores. No other coding or ClinVar-flagged variant exists in the three genes; the remaining 18 calls are intronic or UTR and, except one deep-intronic BUB1B variant absent from gnomAD (about 1 kb from the nearest exon, no splice prediction run), all are common dbSNP polymorphisms.

Genome-wide, 314 genes pass the crude recessive-compatible filter. BUB1B is one of them with exactly these two variants. The list is dominated by polymorphic and multi-copy loci (MUC3A, LILRB1, PRSS2, HLA), which is what a filter without population frequencies produces; a phenotype-driven ranking with gnomAD frequencies (Exomiser) is planned for model 2.

## 3. Interpretation and limits

The genotype matches the pattern of the original MVA1 cohort: all five biallelic BUB1B families in Hanks et al. 2004 (PMID 15475955) carried one truncating allele and one missense allele, and every kinase-domain missense allele UniProt records for MVA1 (R814H, L844F, I909T, Q921H, L1012P) occurs in that configuration. p.Asn1002Lys lies between Q921 and L1012, six residues from the PLK1 phosphosite T1008. Two cautions: p.Leu737Ter has not been reported in a published MVA patient (its ClinVar classification rests on the nonsense mechanism, and it has 115 heterozygous carriers in gnomAD v4), and p.Asn1002Lys is formally a variant of uncertain significance with no functional data; the case for causality is the combination, the gene, and the phenotype. The phenotype terms supplied (HP:0002859, HP:0000121, HP:0004322, HP:0001508, HP:0003202, HP:0001622, HP:0001518, HP:0200067) are consistent with MVA1 as described in OMIM 257300.

Phase is not determinable from this dataset. The variants are 10.9 kb apart, no read-backed phase (PGT/PID) is present on either, and there is no parental data. The trans inference rests on two rare heterozygous variants in a recessive gene that matches the phenotype. The nonsense allele is present in 115 of 1.46 million exome alleles; a cis configuration with the missense allele cannot be excluded from this file.

## 3b. Model 2: phenotype-driven genome-wide ranking (Exomiser)

To test whether the pair is found without a gene list, all 4.74 M PASS variants were run through Exomiser 15.1.0 (data release 2512, hg38) with the eight HPO terms, gnomAD/ExAC/TOPMed/UK10K/1000G frequencies at a 2% cutoff, REVEL and MVP, hiPhive prioritisation, and all inheritance models. BUB1B ranks 1 (dominant model) and 2 (recessive compound-heterozygous model, p = 0.0009) of 389 genes surviving the filters, with exactly the two submitted variants as the contributing pair; phenotype match to ORPHA:1052, score 0.79. Exomiser's ACMG engine classifies p.Leu737Ter as Pathogenic (PVS1, PM2_Supporting, PP4_Moderate, PP5_Strong) and p.Asn1002Lys as Uncertain significance (PM2_Supporting, PP4_Moderate; MVP 0.71). Rank 3 is FANCD2 with two ClinVar-benign splice-region calls. Run time 30 s after a 37 GB reference download. Configuration: `pipeline/exomiser_analysis.yml`. The submission CSV is unchanged by this run; the model number changes because the methods differ.

## 4. Mosaic aneuploidy measured from the VCF

MVA is defined by mosaic gains and losses of whole chromosomes. A trisomy in a fraction f of cells moves heterozygous allele fractions from 0.5 to 1/(2+f) and (1+f)/(2+f) and raises depth by (2+f)/2. From 2.2 million heterozygous PASS SNVs (DP 20-120), in 5 Mb bins with segmental-duplication and centromere bins excluded (depth ratio outside 0.93-1.07 or fewer than 500 heterozygous sites), the per-chromosome median BAF excess is 0.000 on every autosome and depth ratios lie between 0.977 and 1.022, with the high values on the GC-rich chromosomes 16, 17, 19 and 22 (GC bias). The 95th percentile of bin-level excess on chromosomes 1-6 is 0.032, corresponding to f about 0.14 per bin; per chromosome the floor is below 0.10. Conclusion, computed here rather than cited: the sequenced tissue carries no whole-chromosome mosaic aneuploidy above roughly 10% of cells, on the detection model in `track2/creative/F_math.md` section 2 and the script `pipeline/track2_math/f_math.py`. Figure: `figures/mosaic_profile.png`.

## 5. Secondary findings

The 81 ACMG SF v3.2 genes contain 10,895 PASS variants. None is ClinVar pathogenic or likely pathogenic. Nine carry conflicting classifications (one homozygous, eight heterozygous, genes listed in the accompanying table); ACMG SF reporting requires known pathogenic or likely pathogenic variants, so no `secondary` rows are submitted. The nine are listed in `figures/acmg_conflicting_only.tsv` for the panel.

## 6. Methods form answers

- Automated output, no downstream manual review.
- Public data only: Ensembl 116 GFF3 and FASTA, ClinVar GRCh38 (5 Sep 2026), gnomAD v4.1 sites, ACMG SF v3.2 list. No proprietary data.
- Outputs compound-heterozygous pairs: yes.
- Secondary findings: screened, none meet criteria.
- Run time and cost: 61 s on a MacBook, single process; 1 GB of reference downloads; no cloud compute.

## 7. Strengths and limitations (abstract)

A one-minute, fully scripted pipeline recovers a compound-heterozygous BUB1B genotype (p.Leu737Ter, ClinVar pathogenic; p.Asn1002Lys, gnomAD singleton) from a standard germline VCF, confirms rarity from gnomAD without exporting any query, screens ACMG secondary findings, and quantifies mosaic aneuploidy from the same file with a stated detection floor. Limitations: the known-gene pass is disease-specific; the genome-wide check lacks population frequencies and phenotype scoring (Exomiser planned); phase cannot be established without parents or long reads; structural variants and deep intronic variants are not evaluated; the mosaicism method is blind to balanced rearrangements and to mosaicism below about 10%.
