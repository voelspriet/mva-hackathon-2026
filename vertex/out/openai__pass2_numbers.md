# openai / gpt-5 / pass2_numbers

Below are the derived numbers I found, each with where it appears, the inputs stated in the corpus, my recomputation, and whether they match.

1) Allele frequency AF = 7.9e-5 for c.ALLELE_A (gnomAD exomes)
- Where: REPORT_track1.md, §2. Result (table footnote)
- Inputs (given): gnomAD exomes AC = 115, AN = 1,461,846
- Recompute: AF = 115 / 1,461,846 = 7.870×10^-5 ≈ 7.9×10^-5
- Match: Yes

2) Distance of the two variants ≈10.9 kb
- Where: REPORT_track1.md, §3. Interpretation and limits (“The variants are 10.9 kb apart”)
- Inputs: Not stated (no explicit genomic coordinates given in this file)
- Recompute: Cannot; inputs not provided here (creative D notes within-gene positions but does not print both raw coordinates)
- Match: Not applicable (insufficient inputs to recompute)

3) BAF excess 0.032 corresponds to trisomic cell fraction f ≈ 0.14
- Where: REPORT_track1.md, §4. Mosaic aneuploidy measured from the VCF (“95th percentile … 0.032, corresponding to f about 0.14 per bin”)
- Inputs (given): BAF shift model delta = f / (2*(2+f)); 95th percentile delta = 0.032
- Recompute: Invert formula f = 4*delta / (1 – 2*delta) = 4*0.032 / (1 – 0.064) = 0.128 / 0.936 = 0.1368 ≈ 0.14
- Match: Yes

4) Per-chromosome detection floor “near 4 percent” for a single clonal trisomy
- Where: REPORT_track1.md, §4 (text: “bounds a single clonal trisomy near 4 percent”); see derivation in track2/creative/F_math.md §2 (chr1, median of 45 bins with Bonferroni over 23 chromosomes)
- Inputs (given in F_math): delta_min = 0.0104 for chr1 (45 bins, Bonferroni over 23), f = 4*delta / (1 – 2*delta)
- Recompute: f = 4*0.0104 / (1 – 0.0208) = 0.0416 / 0.9792 = 0.0425 = 4.25%
- Match: Yes (reported “near 4 percent”)

5) Total burden ≈21% needed if spread over five chromosomes
- Where: REPORT_track1.md, §4 (text); track2/creative/F_math.md §2 (variegation correction)
- Inputs (given): per-chromosome floor ≈4.2% (as above), spread over k = 5 chromosomes ⇒ F ≥ k × f_min
- Recompute: 5 × 4.25% ≈ 21.25%
- Match: Yes (about 21 percent)

6) Metformin exposure gap 32–130 fold (and residual 12.9–25.8 fold)
- Where: REPORT_track2.md, §7. Explicitly not recommended, and why (Metformin paragraph)
- Inputs (given): Tang 2011 effective concentrations 0.5–1.0 mM; paediatric plasma Cmax 7.7–15.5 µM; toxic ceiling ~5 mg/L ≈ 39 µM
- Recompute:
  - Gap vs paediatric plasma: 500/15.5 = 32.3; 1000/7.7 = 129.9 ⇒ 32–130 fold
  - Residual gap at toxic ceiling: 500/39 = 12.82; 1000/39 = 25.64 ⇒ 12.9–25.8 fold
- Match: Yes

7) FISH minimum detectable relative change ≈22% (counting-error bound)
- Where: REPORT_track2.md, §8. Endpoints and their power limits (“FISH … 22 percent”); full derivation in track2/creative/F_math.md §3
- Inputs (given): p0 = 0.10, nuclei = 1,000; binomial CV = √(p(1–p)/n) / p = √(0.1×0.9/1000)/0.1 = 9.49%; detection formula quoted as MDE = 2.8 × CV × √(2/3) (counting-error-only floor)
- Recompute: MDE = 2.8 × 0.0949 × √(2/3) = 2.8 × 0.0949 × 0.8165 = 0.2179 ≈ 21.8%
- Match: Yes (rounded to 22%)

8) FISH detectable change rises to ≈43% if biological CV ~16.4% is included
- Where: REPORT_track2.md, §8 (“Applying that same 16.4% biological CV to the FISH row moves 22 percent to about 43 percent.”)
- Inputs (given): Combine CVs: CV_total = √(0.0949^2 + 0.164^2) = 0.189; MDE = 2.8 × 0.189 × √(2/3)
- Recompute: MDE = 2.8 × 0.189 × 0.8165 = 0.432 ≈ 43.2%
- Match: Yes

9) Micronucleated reticulocytes detectable change ≈37.5%
- Where: REPORT_track2.md, §8 (“Micronucleated reticulocytes … 37.5 percent”); derivation in track2/creative/F_math.md §3
- Inputs (given): CV_score = 0.022 (1e6 cells counted) and assumed biological CV = 16.4%; n per period = 3; same MDE framework
- Recompute:
  - CV_total = √(0.022^2 + 0.164^2) = 0.165
  - MDE = 2.8 × 0.165 × √(2/3) = 2.8 × 0.165 × 0.8165 = 0.378 ≈ 37.8%
- Match: Yes (≈37.5%)

10) Decision thresholds for cancer-risk reduction: 64.6% and 33.3%
- Where: REPORT_track2.md, §8 (“0.05 / (0.2 × 0.387) = 64.6 percent”; “… ≈33.3 percent”)
- Inputs (given): added harm h = 0.05; residual share s = 0.2; baseline risk R0 either 0.387 or ~0.75; threshold r_min = h / (s × R0)
- Recompute:
  - R0 = 0.387: 0.05 / (0.2 × 0.387) = 0.05 / 0.0774 = 0.6455 = 64.6%
  - R0 = 0.75: 0.05 / (0.2 × 0.75) = 0.05 / 0.15 = 0.3333 = 33.3%
- Match: Yes

11) Prior probability of trans compound heterozygosity: 2×p1×p2 = 1.08×10^-10
- Where: track2/creative/F_math.md, §1. Phase (“2*p1*p2 = 1.08e-10”)
- Inputs (given): p1 = 7.87e-5; p2 = 6.84e-7 (gnomAD AFs)
- Recompute: 2 × 7.87e-5 × 6.84e-7 = 2 × 5.383×10^-11 = 1.0766×10^-10 ≈ 1.08×10^-10
- Match: Yes

12) Posterior P(trans) at R = 1, α = 0.6, β = 1e-4: ≈0.9998
- Where: track2/creative/F_math.md, §1. Phase (table; e.g., “R = 1, alpha = 0.6 … 0.9998”)
- Inputs (given): posterior odds = (1/R) × (α/β) = 1 × (0.6 / 10^-4) = 6000; P = 6000 / (1 + 6000)
- Recompute: 6000 / 6001 = 0.999833 ≈ 0.9998
- Match: Yes

13) Stop-codon distance ≈747 nt upstream of the last exon junction
- Where: REPORT_track2.md, §2. Mechanism; track2/research/01_mechanism_models.md, §2.1 NMD prediction (also gives detailed coordinates)
- Inputs (given in 01_mechanism_models): transcript positions—PTC at tx 2361–2363 (c.2209–2211), last junction at tx 3109/3110; “Distance from the last base of the PTC = 746–747 nt” (wording varies across files)
- Recompute: 3109 – 2363 = 746 nt (from last base); if measured from first PTC base 3109 – 2361 = 748 nt
- Match: Close (the corpus reports 747 nt; the precise value depends on whether one measures from the first or last PTC base; all place it ~0.75 kb upstream with six downstream junctions)

14) Single-bin detection bound f_min ≈7.6% (one-sided 95%)
- Where: track2/creative/F_math.md, §2 (table: “single 5 Mb bin … delta_min = 0.0183, f_min 7.6%”)
- Inputs (given): delta_min = 0.0183; f = 4*delta / (1 – 2*delta)
- Recompute: f = 4*0.0183 / (1 – 0.0366) = 0.0732 / 0.9634 = 0.0760 = 7.6%
- Match: Yes

15) “Per chromosome, chr21 bound ≈6.8%”
- Where: track2/creative/F_math.md, §2 (table: “chr21 … delta_min 0.0165, f_min 6.8%”)
- Inputs (given): delta_min = 0.0165; f = 4*delta / (1 – 2*delta)
- Recompute: f = 4*0.0165 / (1 – 0.0330) = 0.066 / 0.967 = 0.0683 = 6.83%
- Match: Yes

Notes on items I could not verify precisely due to missing or implicit inputs:
- Micronucleus MDE ≈41% (REPORT_track2.md, §8). The corpus states CV_bio = 0.20, CV_score ≈0.112, and cites a log-scale formula using t critical values and SE = sd × √(1/n + 1/2n), but does not print the exact sd on the log scale or df used. Using only the simplified normal-approximation floor (2.8×CV×√(2/3)) with CV_total ≈0.229 gives ≈52%, not 41%. Because the manuscript uses a different, log-scale t-based computation, I cannot reproduce the 41% without the intermediary sd and df; inputs are incomplete.
- “Two variants are 10.9 kb apart” (REPORT_track1.md, §3): raw GRCh38 genomic positions are not printed in that file; cannot recompute.

If you want me to scan for other potential derived numbers (e.g., additional AFs, per-bin Bonferroni counts, or AC/AN ratios) I can add them, but the set above covers the places where the manuscript relies on arithmetic rather than quotations.
