# Every claim about the hackathon data, checked against the hackathon data

## Why this is separate from the source audit

The five audit partitions checked 577 claims against the **literature**. They did not check the claims this project makes about **the data it was given**: variant coordinates, genotypes, allele depths, variant counts, frequencies, and everything derived from the VCF and the phenotype document.

Those are the claims a judge can check fastest, because the data is in their hands too. This file checks them one file at a time. It is built up over repeated passes and records the check even where the claim was right.

**Method.** Each claim is recomputed from `data/WGS_EX2312012_HGWCNDSX7.vcf.gz` or from the supplied phenotype document, or retrieved from gnomAD v4.1 by indexed byte range. The recomputation is stated so it can be repeated.

---

## `REPORT_track1.md` — 11 claims, 10 exact, 1 correct but underspecified

| Claim | Recomputed | Verdict |
|---|---|---|
| "4.74 M PASS variants" | `bcftools view -H -i 'FILTER="PASS"'` gives **4,740,790** | **Exact** |
| "autosomal depth 44x" | Over PASS single-nucleotide variants at depth 20 to 120, autosomes, which is what `mosaic_baf.py` computes: **median 44**. Over all PASS autosomal variants including indels: median 43, mean 43.2 | **Correct for the pipeline's definition, which the sentence does not give.** Corrected to say which |
| Allele 1 `chr15:40209701 T>G`, genotype 0/1, allele depths 21/25 | Queried directly: `0/1`, `AD=21,25`, `DP=46`, `GQ=99` | **Exact** |
| Allele 2 `chr15:40220612 T>G`, genotype 0/1, allele depths 15/13 | Queried directly: `0/1`, `AD=15,13`, `DP=28`, `GQ=99` | **Exact** |
| Allele 1 gnomAD exomes 115/1,461,846, AF 7.9e-5 | Byte-range read of the public sites file: `AC=115 AN=1461846 AF=7.87e-05 nhomalt=0` | **Exact** |
| Allele 1 gnomAD genomes 5/152,174 | `AC=5 AN=152174 AF=3.29e-05 nhomalt=0` | **Exact** |
| Allele 2 gnomAD exomes 1/1,461,878, AF 6.8e-7 | `AC=1 AN=1461878 AF=6.84e-07 nhomalt=0` | **Exact** |
| "The variants are 10.9 kb apart" | 40,220,612 minus 40,209,701 = **10,911 bp** | **Exact** |
| "no read-backed phase (PGT/PID) is present on either" | Both records carry `.` in PGT and PID. Genome-wide, the longest phase set spans 288 bp | **Exact, and stronger than stated** |
| "314 genes pass the crude recessive-compatible filter" | `work/recessive_compatible_genes.txt` holds **314** lines | **Exact** |
| "The 81 ACMG SF v3.2 genes contain 10,895 PASS variants" | Gene list holds **81** symbols; `work/acmg.vcf.gz` holds **10,895** PASS records | **Exact, both halves** |

**Nothing in Track 1 is wrong.** The single imprecision is a depth figure that is right under the definition its own pipeline uses and ambiguous as written, which is the same failure mode the audit found elsewhere: a number correct at source and underspecified in the summary.

---

## Still to check

`REPORT_track2.md`, `FAMILY_CARD.md`, `track2/anomalies/*`, `track2/reanalysis/*`, `track2/creative/F_math.md`, `track2/gate/*`, and the remaining files that assert something about the supplied data. Then the external sources those files cite, which the audit partitions covered for the literature but not for the database records retrieved live.
