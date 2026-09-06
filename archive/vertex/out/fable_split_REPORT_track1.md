**Derived numbers found**

1. **7.9e-5** — `REPORT_track1.md`, §2 Result (table, gnomAD column, row p.ALLELE_A)
 - Inputs: exome allele count 115, allele number 1,461,846
 - Recomputed: 115 / 1,461,846 = 7.87e-5 → 7.9e-5
 - Match: yes

2. **6.8e-7** — `REPORT_track1.md`, §2 Result (table, gnomAD column, row p.ALLELE_B)
 - Inputs: exome allele count 1, allele number 1,461,878
 - Recomputed: 1 / 1,461,878 = 6.84e-7 → 6.8e-7
 - Match: yes

3. **"115 of 1.46 million exome alleles"** — `REPORT_track1.md`, §3 Interpretation and limits
 - Inputs: 115 / 1,461,846 from §2 table
 - Recomputed: 1,461,846 ≈ 1.46 million
 - Match: yes (restatement, consistent)

4. **f ≈ 0.14** — `REPORT_track1.md`, §4 Mosaic aneuploidy measured from the VCF
 - Inputs: trisomy in fraction f shifts heterozygous BAF from 0.5 to (1+f)/(2+f) and 1/(2+f); observed 95th-percentile bin-level BAF excess = 0.032
 - Recomputed: excess = (1+f)/(2+f) − 0.5 = f / (2(2+f)); setting equal to 0.032 gives f = 0.064(2+f) → f(1 − 0.064) = 0.128 → f = 0.137 ≈ 0.14
 - Match: yes

5. **Nine conflicting variants = one homozygous + eight heterozygous** — `REPORT_track1.md`, §5 Secondary findings
 - Inputs: 1 homozygous, 8 heterozygous
 - Recomputed: 1 + 8 = 9
 - Match: yes

**Derived numbers whose inputs the corpus does not state**

- **"10.9 kb apart"** (§3): depends on POS_A and POS_B, which appear only as placeholders. Cannot recompute.
- **"six residues from the PLK1 phosphosite T1008"** and **"between Q921 and L1012"** (§3): depend on the residue number in p.ALLELE_B, which is a placeholder. Cannot recompute.
- **Depth ratio (2+f)/2** (§4): given as a formula only; no specific f and depth-ratio pair is stated to check.

**Not derived (stated directly, no recomputation possible):** 4.74 M PASS variants, 44x depth, 314 genes, 389 genes, p = 0.0009, score 0.79, MVP 0.71, 10,895 variants in 81 genes, 5/152,174 (no frequency given), depth-ratio range 0.977–1.022, run times.

Side note (not a derived-number check): §3b reports a 37 GB reference download for Exomiser, while §6 states "1 GB of reference downloads" and "61 s" total; §6 appears to describe model 1 only, but the report does not say so.