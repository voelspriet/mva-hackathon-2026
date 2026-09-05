# gemini-3.1-pro-preview / A_deliverables / pass2_numbers

Here are the derived numbers found in the corpus, along with their stated inputs, recomputed values, and whether they match.

### File: `REPORT_track1.md`

**1. Number:** 7.9e-5
*   **Section:** 2. Result
*   **Inputs given:** 115 exomes, 1,461,846 total exomes
*   **Recomputed value:** 115 / 1,461,846 = 0.000078667... (7.87e-5)
*   **Match:** Yes (rounds to 7.9e-5).

**2. Number:** 6.8e-7
*   **Section:** 2. Result
*   **Inputs given:** 1 exome, 1,461,878 total exomes
*   **Recomputed value:** 1 / 1,461,878 = 0.000000684... (6.84e-7)
*   **Match:** Yes (rounds to 6.8e-7).

**3. Number:** about 0.14
*   **Section:** 4. Mosaic aneuploidy measured from the VCF
*   **Inputs given:** BAF excess = 0.032; formula: moves from 0.5 to (1+f)/(2+f)
*   **Recomputed value:** (1+f)/(2+f) - 0.5 = 0.032 → f / (4+2f) = 0.032 → f = 0.13675...
*   **Match:** Yes (0.13675 is about 0.14).

### File: `REPORT_track2.md`

**4. Number:** 64.6 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** s = 0.2, added harm = 0.05, baseline risk = 38.7 percent (0.387); formula: 0.05 / (0.2 x 0.387)
*   **Recomputed value:** 0.05 / (0.2 * 0.387) = 0.64599...
*   **Match:** Yes (rounds to 64.6 percent).

**5. Number:** 33.3 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** s = 0.2, added harm = 0.05, baseline risk = 75 percent (0.75); formula: 0.05 / (0.2 x 0.75)
*   **Recomputed value:** 0.05 / (0.2 * 0.75) = 0.3333...
*   **Match:** Yes.

**6. Number:** 32 to 130 fold
*   **Section:** 7. Explicitly not recommended, and why
*   **Inputs given:** Tested at 0.5 and 1.0 mM (500 and 1000 micromolar), paediatric plasma is 7.7 to 15.5 micromolar.
*   **Recomputed value:** 500 / 15.5 = 32.25; 1000 / 7.7 = 129.87
*   **Match:** Yes.

**7. Number:** about 39 micromolar
*   **Section:** 7. Explicitly not recommended, and why
*   **Inputs given:** 5 mg/L.
*   **Recomputed value:** The corpus does not state the inputs for it (the molecular weight of metformin is missing).

**8. Number:** 2.5 to 5 fold
*   **Section:** 7. Explicitly not recommended, and why
*   **Inputs given:** Toxic ceiling 39 micromolar, paediatric plasma 7.7 to 15.5 micromolar.
*   **Recomputed value:** 39 / 15.5 = 2.516; 39 / 7.7 = 5.064
*   **Match:** Yes.

**9. Number:** 12.9 to 25.8 fold
*   **Section:** 7. Explicitly not recommended, and why
*   **Inputs given:** Tested at 500 and 1000 micromolar, toxic ceiling 39 micromolar (or 38.7 micromolar as stated later in referee 3's report).
*   **Recomputed value:** Using 39: 500 / 39 = 12.82; 1000 / 39 = 25.64. Using 38.7: 500 / 38.7 = 12.91; 1000 / 38.7 = 25.83.
*   **Match:** Yes (matches exactly if using the unrounded 38.7 micromolar figure).

**10. Number:** 22 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** CV = 9.49 percent; formula = 2.8 x CV x sqrt(2/3)
*   **Recomputed value:** 2.8 * 9.49 * sqrt(2/3) = 21.696...
*   **Match:** Yes (rounds to 22 percent).

**11. Number:** 41 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** CV = about 17 percent; formula = 2.8 x CV x sqrt(2/3)
*   **Recomputed value:** 2.8 * 17 * sqrt(2/3) = 38.86...
*   **Match:** No (38.86% does not match 41%). 

**12. Number:** 37.5 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** CV = 16.4 percent; formula = 2.8 x CV x sqrt(2/3)
*   **Recomputed value:** 2.8 * 16.4 * sqrt(2/3) = 37.493...
*   **Match:** Yes (rounds to 37.5 percent).

**13. Number:** 5.0 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** CV = 0.022 (2.2 percent); formula = 2.8 x CV x sqrt(2/3)
*   **Recomputed value:** 2.8 * 2.2 * sqrt(2/3) = 5.029...
*   **Match:** Yes (rounds to 5.0 percent).

**14. Number:** 10.9 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** 1,000 nuclei gives CV 9.49 percent. Moving to 4,000 nuclei (which halves the CV to 4.745 percent); formula = 2.8 x CV x sqrt(2/3).
*   **Recomputed value:** 2.8 * 4.745 * sqrt(2/3) = 10.848...
*   **Match:** Yes (rounds to 10.9 percent).

**15. Number:** 15.4 percent
*   **Section:** 8. Endpoints and their power limits
*   **Inputs given:** CV = 9.49 percent; formula = 2.8 x CV x sqrt(2/n) where n=6.
*   **Recomputed value:** 2.8 * 9.49 * sqrt(2/6) = 15.34...
*   **Match:** Yes (rounds to 15.4 percent).

### File: `track2/gate/G1_biobank_and_data.md`

**16. Number:** $434
*   **Section:** 1. Bottom line
*   **Inputs given:** GM21284 ($262) + NA21284 ($172)
*   **Recomputed value:** 262 + 172 = 434
*   **Match:** Yes.

**17. Number:** $1,220
*   **Section:** 1. Bottom line
*   **Inputs given:** Single case ($434) + GM22006 trio ($786)
*   **Recomputed value:** 434 + 786 = 1220
*   **Match:** Yes.

**18. Number:** $786
*   **Section:** 2. Findings table
*   **Inputs given:** $262 each, 3 ampoules
*   **Recomputed value:** 262 * 3 = 786
*   **Match:** Yes.

**19. Number:** 65.7%
*   **Section:** 4. A number obtained today, from public data, for nothing
*   **Inputs given:** Probe value (mean) 8.97, Control 9.58 (Data are log2).
*   **Recomputed value:** 2^(8.97 - 9.58) = 2^(-0.61) = 0.6552 (65.5%)
*   **Match:** No (65.5% does not match 65.7%).

**20. Number:** 108.1%
*   **Section:** 4. A number obtained today, from public data, for nothing
*   **Inputs given:** Probe value 9.69, Control 9.58 (Data are log2).
*   **Recomputed value:** 2^(9.69 - 9.58) = 2^(0.11) = 1.0792 (107.9%)
*   **Match:** No (107.9% does not match 108.1%).

**21. Number:** 93.6%
*   **Section:** 4. A number obtained today, from public data, for nothing
*   **Inputs given:** Probe value 8.06, Control 8.16 (Data are log2).
*   **Recomputed value:** 2^(8.06 - 8.16) = 2^(-0.10) = 0.9330 (93.3%)
*   **Match:** No (93.3% does not match 93.6%).

**22. Number:** ~$15,000
*   **Section:** 7.3 Total cost and elapsed time
*   **Inputs given:** $1,220 + ~$4,000 + ~$700 + ~$900 + ~$800 + ~$5,800 + ~$750 + ~$2,000
*   **Recomputed value:** 1220 + 4000 + 700 + 900 + 800 + 5800 + 750 + 2000 = 16,170
*   **Match:** No (16,170 does not match 15,000).

### File: `track2/gate/G2_nmd_prediction.md`

**23. Number:** 746 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** Last junction at tx 3,109. PTC occupies tx 2,361-2,363.
*   **Recomputed value:** 3109 - 2363 = 746
*   **Match:** Yes.

**24. Number:** 748 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** Last junction at tx 3,109. PTC occupies tx 2,361-2,363.
*   **Recomputed value:** 3109 - 2361 = 748
*   **Match:** Yes.

**25. Number:** 73 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** Exon 17/18 boundary at tx 2,436. PTC's last base at 2,363.
*   **Recomputed value:** 2436 - 2363 = 73
*   **Match:** Yes.

**26. Number:** 699 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** Penultimate exon's last 50 nt = tx 3,060-3,109. PTC at tx 2,361.
*   **Recomputed value:** 3060 - 2361 = 699
*   **Match:** Yes.

**27. Number:** 2,208 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** PTC starts at c.2209.
*   **Recomputed value:** 2209 - 1 = 2208
*   **Match:** Yes.

**28. Number:** 70.1%
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** c.2209 of 3,153.
*   **Recomputed value:** 2209 / 3153 = 0.7006...
*   **Match:** Yes (rounds to 70.1%).

**29. Number:** 70.2%
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** codon 737 of 1,050.
*   **Recomputed value:** 737 / 1050 = 0.7019...
*   **Match:** Yes (rounds to 70.2%).

**30. Number:** 942 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** PTC at c.2209, native stop at c.3151-3153.
*   **Recomputed value:** 3151 - 2209 = 942
*   **Match:** Yes.

**31. Number:** 39 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** PTC at codon 737, in-frame ATG at codon 750.
*   **Recomputed value:** (750 - 737) * 3 = 13 * 3 = 39
*   **Match:** Yes.

**32. Number:** 736 codons
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** PTC at codon 737.
*   **Recomputed value:** 737 - 1 = 736
*   **Match:** Yes.

**33. Number:** 364 nt
*   **Section:** 2.2 Rule-by-rule verdict
*   **Inputs given:** tx 3,306-3,669.
*   **Recomputed value:** 3669 - 3306 + 1 = 364
*   **Match:** Yes.

**34. Number:** 0.009
*   **Section:** 4.2 gnomAD v4, the variant itself
*   **Inputs given:** AN = 1,461,846, AF = 7.867e-5; formula: AN × AF²
*   **Recomputed value:** 1,461,846 * (0.00007867)^2 = 0.00904...
*   **Match:** Yes (rounds to 0.009).

### File: `track2/gate/G3_dose_response.md`

**35. Number:** 714 d
*   **Section:** 1.1 Master table
*   **Inputs given:** 102 wk
*   **Recomputed value:** 102 * 7 = 714
*   **Match:** Yes.

**36. Number:** 210 d
*   **Section:** 1.1 Master table
*   **Inputs given:** 30 wk
*   **Recomputed value:** 30 * 7 = 210
*   **Match:** Yes.

**37. Number:** 630 d
*   **Section:** 1.1 Master table
*   **Inputs given:** 90 wk
*   **Recomputed value:** 90 * 7 = 630
*   **Match:** Yes.

**38. Number:** 651 d
*   **Section:** 1.1 Master table
*   **Inputs given:** 93 wk
*   **Recomputed value:** 93 * 7 = 651
*   **Match:** Yes.

### File: `track2/referees/referee1_geneticist.md`

**39. Number:** 9.49 percent
*   **Section:** 5. Statistics
*   **Inputs given:** fraction 0.10, 1,000 nuclei.
*   **Recomputed value:** SD = sqrt(0.1 * 0.9 / 1000) = 0.0094868. CV = SD / mean = 0.0094868 / 0.1 = 0.094868 (9.49%)
*   **Match:** Yes.

**40. Number:** 5.48
*   **Section:** 5. Statistics
*   **Inputs given:** CV 9.49 percent, pooling three.
*   **Recomputed value:** 9.49 / sqrt(3) = 5.479...
*   **Match:** Yes (rounds to 5.48).

**41. Number:** 7.75
*   **Section:** 5. Statistics
*   **Inputs given:** Pooled CV 5.48.
*   **Recomputed value:** sqrt(5.48^2 + 5.48^2) = 7.749...
*   **Match:** Yes (rounds to 7.75).

**42. Number:** 21.7
*   **Section:** 5. Statistics
*   **Inputs given:** 2.80 x 7.75
*   **Recomputed value:** 2.80 * 7.75 = 21.7
*   **Match:** Yes.

### File: `track2/verify/V1_tang_suijkerbuijk.md`

**43. Number:** 730
*   **Section:** 1(d)
*   **Inputs given:** 714 native BUBR1 residues + 16 frameshift residues
*   **Recomputed value:** 714 + 16 = 730
*   **Match:** Yes.

**44. Number:** ~81.5 kDa
*   **Section:** 1(d)
*   **Inputs given:** 715 residues, ~114 Da/residue
*   **Recomputed value:** 715 * 114 = 81,510 Da (81.51 kDa)
*   **Match:** Yes.

**45. Number:** ~83 kDa
*   **Section:** 1(d)
*   **Inputs given:** 730 residues, ~114 Da/residue
*   **Recomputed value:** 730 * 114 = 83,220 Da (83.22 kDa)
*   **Match:** Yes (rounds to ~83 kDa).
