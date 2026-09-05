# Exomiser 15.1.0 run (model 2 evidence), 5 Sep 2026

Input: all 4,740,790 PASS variants (chr-prefixed copy of the provided VCF), eight HPO terms, no gene list. Data release 2512 (hg38 + phenotype). Frequencies: gnomAD exomes/genomes, ExAC, TOPMed, UK10K, 1000G, ESP, cutoff 2%. Pathogenicity: REVEL, MVP. Prioritiser: hiPhive (human, mouse, fish, PPI). Inheritance: AD, AR (hom, comp het), XD, XR, MT. Mode PASS_ONLY. Run time 30 s on the laptop after 37 GB of reference data; 389 genes / 815 variants survived filtering.

| Rank | Gene (model) | p | combined | phenotype | variant | Contributing variants |
|---|---|---|---|---|---|---|
| 1 | BUB1B (AD) | 0.0005 | 0.586 | 0.563 | 1.000 | chr15:40209701 T>G, chr15:40220612 T>G |
| 2 | BUB1B (AR comp het) | 0.0009 | 0.499 | 0.793 | 0.926 | the same two |
| 3 | FANCD2 (AR) | 0.015 | 0.219 | 0.663 | 0.900 | two splice-region calls, both ClinVar benign |
| 4 | LZTR1 (AD) | 0.028 | 0.154 | 0.515 | 1.000 | |
| 5 | HLA-DRB1 (AD) | 0.057 | 0.085 | 0.684 | 1.000 | |

Phenotype match for BUB1B: ORPHA:1052 Mosaic variegated aneuploidy syndrome, human phenotype score 0.79 (rhabdomyosarcoma, growth, prematurity terms matched).

Exomiser ACMG assignments:
- c.2209T>G p.(Leu737Ter): PATHOGENIC. PVS1, PM2_Supporting, PP4_Moderate, PP5_Strong. ClinVar 533901, 2 stars. Max frequency in the 2512 bundle: gnomAD_E_NFE 1.0e-2 % (0.0000998).
- c.3006T>G p.(Asn1002Lys): UNCERTAIN_SIGNIFICANCE. PM2_Supporting, PP4_Moderate. Not in ClinVar. MVP 0.708, REVEL not the max source. gnomAD_E_NFE 9.0e-5 in the bundle's gnomAD release (gnomAD v4.1 live: AC 1 / AN 1,461,878).

Conclusion for the write-up: a standard phenotype-driven pipeline with no disease prior places the submitted pair first genome-wide. The missense allele is formally a VUS by ACMG rules; its causal role rests on trans configuration with a pathogenic null, the kinase-domain position among the Hanks 2004 missense alleles, and the phenotype, not on classification alone.

Files: work/exomiser/results/mva_model2.{html,genes.tsv,variants.tsv,jsonl}; analysis YAML in pipeline/exomiser_analysis.yml.
