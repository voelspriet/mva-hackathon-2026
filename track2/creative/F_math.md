# F. Quantitative appendix: five numbers that decide the Track 2 question

All arithmetic is reproducible from `pipeline/track2_math/f_math.py`. Assumptions are labelled **[A]**; published inputs carry a PMID or a URL. No recommendation is made anywhere in this file.

---

## 1. Phase: are the two *BUB1B* variants in trans or in cis?

**Inputs.** c.2210T>G p.(Leu737Ter), gnomAD v4 AF `p1 = 7.87e-5`; c.3006T>G p.(Asn1002Lys), gnomAD v4 singleton, AF `p2 = 6.84e-7` (dossier 01, section 2.4). Recessive model, complete penetrance for biallelic loss of function (Hanks 2004, PMID 15475955).

**Genotype prior.** Under Hardy-Weinberg and random mating, the child is a trans compound heterozygote with probability `2*p1*p2 = 1.08e-10`. He is a cis carrier with probability `2*q`, where `q` is the frequency of the haplotype carrying both changes. Define the co-occurrence enrichment `R = q / (p1*p2)`; `R = 1` is linkage equilibrium. The prior odds are

    odds(trans : cis) = 2*p1*p2 / (2*q) = 1/R

`R` is not observable from allele frequencies alone. Its hard ceiling is the case where every copy of the rarer allele sits on a Leu737Ter background, giving `q = p2` and `R = 1/p1 = 12,706`.

**Disease information.** Let `alpha = P(affected | trans)`, which under complete penetrance is essentially the probability that the VUS p.(Asn1002Lys) is genuinely hypomorphic. Let `beta = P(this phenotype | some other cause)`, since a cis child retains one wild-type allele. Then

    posterior odds(trans) = (1/R) * (alpha / beta)

**[A]** `beta = 1e-4`: embryonal rhabdomyosarcoma plus nephrocalcinosis plus severe growth failure plus preterm SGA, from any non-*BUB1B* cause, in a child referred for sequencing. Sensitivity at 1e-3 and 1e-5 is in the script.

**Posterior P(trans), beta = 1e-4**

| R (co-occurrence enrichment) | alpha = 0.3 | alpha = 0.6 | alpha = 0.9 |
|---|---|---|---|
| 1 (linkage equilibrium) | 0.9997 | 0.9998 | 0.9999 |
| 10 | 0.9967 | 0.9983 | 0.9989 |
| 100 | 0.968 | 0.984 | 0.989 |
| 1,000 | 0.750 | 0.857 | 0.900 |
| 12,706 (hard ceiling) | 0.191 | 0.321 | 0.415 |

Parental recurrent miscarriage adds an independent likelihood ratio for both parents being carriers; four prenatally diagnosed MVA1 pregnancies ended in demise or termination (Pavone 2022, PMID 35804254). At a conservative LR of 3, the R = 100, alpha = 0.6 cell moves from 0.984 to 0.9945.

**Reading.** Trans is favoured across the plausible range of `R`, and the conclusion is insensitive to the *BUB1B* prior `alpha` over 0.3 to 0.9. It is highly sensitive to one unmeasured parameter, `R`, which cannot be bounded from gnomAD because the singleton cannot be phased. The calculation therefore cannot settle phase; a trio or long-read test replaces the whole table.

---

## 2. Detection limit of the BAF and depth mosaicism method

**Model.** For a trisomy in cell fraction `f`, heterozygous B-allele fractions split to `1/(2+f)` and `(1+f)/(2+f)`, so the shift is

    delta = 0.5 - 1/(2+f) = f / (2*(2+f))        and        f = 4*delta / (1 - 2*delta)

which is what `mosaic_baf.py` and `mosaic_robust.py` invert. The per-bin statistic is `V = mean((AB - 0.5)^2)`, with `E[V] = sigma0^2 + delta^2`.

**Noise.** The empirical baseline is `sigma0 = 0.09456` (work/mosaic.json). Pure binomial at the observed autosomal median depth of 44x gives `sqrt(0.25/44) = 0.0754`, so the data are overdispersed by a factor 1.574 in variance. Using the empirical value, not the binomial ideal, is the conservative choice. For approximately Gaussian residuals, `SD(V) = sigma0^2 * sqrt(2/N)`, so the threshold is

    delta_min = sigma0 * sqrt( z * sqrt(2/N) )

**N.** From work/mosaic.json divided by the bin counts in work/mosaic_robust.json, autosomal 5 Mb bins hold 3,500 to 4,760 heterozygous sites; the median is about **3,900**, and `mosaic_robust.py` already discards bins below 500.

| Test level | N or bins | delta_min | f_min |
|---|---|---|---|
| single 5 Mb bin, one-sided 95% | N = 3,900 | 0.0183 | **7.6%** |
| single bin, Bonferroni over 563 bins | N = 3,900 | 0.0276 | **11.7%** |
| chr1, median of 45 bins, 95% | 45 bins | 0.0079 | **3.2%** |
| chr1, 45 bins, Bonferroni over 23 chr | 45 bins | 0.0104 | **4.2%** |
| chr21, 7 bins, Bonferroni over 23 chr | 7 bins | 0.0165 | **6.8%** |

The median over `k` bins costs a factor `sqrt(pi/2)` in efficiency against the mean, which is included.

**Verdict on "about 10%".** Correct as a per-segment statement under genome-wide correction (11.7%), and conservative as a whole-chromosome statement (4.2% on large autosomes, 6.8% on chr21). The depth channel is weaker: observed autosomal `f_depth` runs from -0.047 to +0.044 with SD 0.025 in a sample with no trisomy, so GC and mappability drift alone put a floor near 5%.

**The variegated-aneuploidy correction, which matters more than any of the above.** MVA is variegated: different cells carry different gains. If total aneuploid burden `F` is spread over `k` chromosomes, per-chromosome fraction is `F/k` and the requirement becomes `F >= k * f_min`.

| Spread over k chromosomes | F needed (per-bin, 11.7%) | F needed (per-chromosome, 4.2%) |
|---|---|---|
| 1 | 11.7% | 4.2% |
| 5 | 58.3% | 21% |
| 22 | above 100% (undetectable) | 92% |

So the negative result bounds a single clonal trisomy at roughly 4%, and bounds a genuinely variegated burden hardly at all.

**Tissue-confined clones.** A clone confined to kidney or muscle contributes no cells to blood, so sensitivity to it is zero at any fraction. A clone in the haematopoietic lineage must reach about **4% of nucleated blood cells** for a single gained chromosome, or about 21% total burden if spread over five chromosomes. The chrX row in mosaic_robust.json (excess 0.036, f_baf 0.156, depth ratio 0.93, 4,639 hets against 52,531 homozygotes) is a hemizygous male X, not mosaicism, and is a useful positive control for the statistic.

---

## 3. N-of-1 power: baseline, treatment, withdrawal

**Design.** Three periods, `n` measurements each, contrast treatment against the mean of baseline and withdrawal. On the log scale, `SE = sd * sqrt(1/n + 1/(2n))`, `df = 3n - 3`, and the minimum detectable effect at 80% power and two-sided 0.05 is `MDE = 1 - exp(-(t(0.975,df) + t(0.80,df)) * SE)`.

**(a) Cytokinesis-block micronuclei.** Healthy-child baseline is 4.07 +/- 1.87 per 1,000 binucleated cells at 3 to 15 years and 2.85 +/- 1.60 at 0 to 2 years (Sirin, PMC6944958); the pooled paediatric meta-analysis gives 4.48 (95% CI 3.35 to 5.98) and 5.70 (4.29 to 7.56) per 1,000 (Neri and Bonassi, *Environ Health Perspect* 2005, PMID 16140629); healthy adults 5.06 +/- 3.11 (Gajski 2018, PMID 29127818), with within-subject repeatability across three repeated blood samplings demonstrated separately (Bolognesi 2019, PMID 30368181, ICC 0.905, 95% CI 0.868 to 0.933). Scoring noise is Poisson, `CV_score = 1/sqrt(lambda * n_BN / 1000)`; total `CV = sqrt(CV_bio^2 + CV_score^2)`. **[A]** `CV_bio = 0.20` within-subject between occasions, with 0.30 shown as sensitivity. **[A]** An MVA1 child, with premature chromatid separation in 48.5 to 83.2% of lymphocytes (Kajii 2001, PMID 11746029), has a baseline near `lambda = 40` per 1,000 rather than 4.

| lambda | BN scored | CV_score | CV_total | n per period | MDE (relative reduction) |
|---|---|---|---|---|---|
| 4 (healthy child) | 1,000 | 0.500 | 0.539 | 3 | 70% |
| 4 | 4,000 | 0.250 | 0.320 | 3 | 52% |
| 40 (MVA child) | 1,000 | 0.158 | 0.255 | 3 | 45% |
| 40 | 2,000 | 0.112 | 0.229 | 3 | **41%** |
| 40 | 2,000 | 0.112 | 0.229 | 5 | 32% |

At an elevated baseline, scoring beyond 2,000 binucleated cells buys almost nothing; biological variation dominates. A flow micronucleated-reticulocyte readout counting 1e6 cells, as in BABY-HUG (PMC3277805), drives `CV_score` to 0.022 and still lands at 37.5% for 3+3+3: the 3-per-period design, not the assay, is the binding constraint.

**(b) Interphase FISH aneuploid fraction.** Binomial `CV = sqrt(p0(1-p0)/n)/p0`, plus a hybridisation and scorer term. **[A]** `CV_tech = 0.05` to 0.10.

| p0 | nuclei | CV_binom | CV_tech | n per period | MDE |
|---|---|---|---|---|---|
| 0.05 | 1,000 | 0.138 | 0.10 | 3 | 33% |
| 0.10 | 1,000 | 0.095 | 0.05 | 3 | **22%** |
| 0.10 | 1,000 | 0.095 | 0.10 | 3 | 28% |
| 0.10 | 2,000 | 0.067 | 0.05 | 5 | 13% |

FISH is the more sensitive of the two endpoints at any realistic aneuploid fraction, and it is the one that would be improved by scoring more nuclei.

**Period length.** Neither readout is instantaneous. CBMN scores damage carried by resting T cells that divide only in culture, so the peripheral pool must turn over before a change in new missegregation appears. **[A]** 12 weeks per period, with measurements at weeks 0, 6 and 12, plus a 4-week washout before the withdrawal period, giving about 11 months in total. A reticulocyte readout compartment turns over in 1 to 2 days and would permit 4-week periods, roughly a 4-month study.

---

## 4. Decision thresholds

**Inputs.** Lifetime cancer risk in MVA1 is 12/31 = 38.7% (Pavone 2022, PMID 35804254) at the low end and approximately 75% (Orphanet ORPHA 1052) at the high end; dossier 02, section 1 flags that the two are unreconciled and probably reflect tumour ascertainment. Take `R0` in {0.39, 0.57, 0.75}.

A drug delivering relative reduction `r` and carrying added harm probability `h` breaks even when `r * R0 * u_C >= h * u_H`, so

    r_min = (h / R0) * (u_H / u_C)      with     w = u_H / u_C

Weighting 1 is event-count neutral (`w = 1`, appropriate when the added harm is a second malignancy). Weighting 2 values a permanent growth deficit at one fifth of a cancer event (`w = 0.2`), the relevant case for the labelled growth warning on dasatinib (dossier 02, section 5).

| Added risk h | w = 1, R0 = 0.39 | w = 1, R0 = 0.75 | w = 0.2, R0 = 0.39 | w = 0.2, R0 = 0.75 |
|---|---|---|---|---|
| 1% | 2.6% | 1.3% | 0.5% | 0.3% |
| 2% | 5.1% | 2.7% | 1.0% | 0.5% |
| 5% | 12.8% | 6.7% | 2.6% | 1.3% |
| 10% | 25.6% | 13.3% | 5.1% | 2.7% |

**Timing correction, which dominates the table.** MVA tumours cluster at 2 to 16 months (Kajii 2001, PMID 11746029) and surveillance runs only to age 7 (Nakano 2024, PMID 39264246). A child who has already had and been treated for rhabdomyosarcoma faces a residual, not a lifetime, risk. If residual risk is a share `s` of `R0`, every threshold is multiplied by `1/s`.

| Residual share s | h = 2%, R0 = 0.39 | h = 5%, R0 = 0.39 | h = 5%, R0 = 0.75 | h = 10%, R0 = 0.39 |
|---|---|---|---|---|
| 30% | 17% | 43% | 22% | 85% |
| 20% | 26% | 64% | 33% | above 100% |
| 10% | 51% | above 100% | 67% | above 100% |

"Above 100%" means no achievable relative reduction offsets the harm. Since no approved drug has a measured effect on cancer incidence in MVA (dossier 02, section 6: zero registered trials), every row is a requirement, not an estimate.

---

## 5. Heterozygous parents as within-family controls, and the 40-patient study

**Are carriers normal?** No. PCS is present in 3.5 to 41.7% of carrier-parent lymphocytes (Kajii 2001, PMID 11746029) against under 2% in unrelated controls; 7 of 7 carrier parents were PCS-positive in García-Castillo 2008 (PMID 18548531). Treating that range as +/- 2 SD on the log scale gives `sd_log = 0.619`, a between-carrier CV of 68% and a geometric mean of 12.1%. Carriers are therefore an intermediate phenotype, not a normal reference, and cannot anchor an absolute normal range.

**Are they useful as a drift control?** Possibly, for a different job. Model `y_child = mu_c + b_t + e_c` and `y_parent = mu_p + b_t + e_p`, where `b_t` is a shared culture, batch and scorer effect. Differencing removes `b_t` at the cost of the parent's own residual:

    Var(y_child - mean of m parents) = sigma_e_c^2 + sigma_e_p^2/m

Differencing pays only when `sigma_b^2 > sigma_e_p^2 / m`, that is `sigma_b > 1.00 * sigma_e_p` with one parent and `sigma_b > 0.71 * sigma_e_p` with both. That inequality is testable in a three-draw pilot and should be tested before the design is committed. Note also that in a within-child crossover the between-person term is already removed, so parents add value only against between-occasion drift.

**Sample size for a shared MVA Society protocol.** The population ceiling is 31 published MVA1 cases (Pavone 2022) and about 40 published MVA cases overall (Scott 2006, PMID 16690728). **[A]** Half are alive, eligible and consenting, so 15 to 20 subjects. Using the endpoint variability from section 3, `n = 2*(z_0.975 + z_0.80)^2 * sd^2 / (log(1/(1-r)))^2`, with between-subject CV 0.50 for the parallel design and within-subject CV 0.229 for the crossover. Replicates within a period shrink only the scoring term, not the biological term, so they are not divided into `sd`.

| Relative effect | Parallel, per arm | Parallel, total | Crossover, total subjects |
|---|---|---|---|
| 20% | 71 | 142 | 17 |
| 25% | 43 | 86 | 10 |
| 30% | 28 | 56 | 8 (variance-estimation floor) |
| 40% | 14 | 28 | 8 |
| 50% | 8 | 16 | 8 |

**Reading.** A parallel randomised design in MVA is arithmetically impossible below a 50% effect: 20 subjects buy nothing under 45%. A shared multi-centre N-of-1 crossover protocol, aggregated across families, reaches a 20% biomarker change with 17 subjects, which is inside the enrollable population. That is the only design in this table that the disease can supply. It requires a single shared protocol, one central scoring laboratory to keep `sigma_b` common, and pre-registration of the endpoint, since the biomarker is not a clinical outcome and no drug in this space has a measured clinical effect.
