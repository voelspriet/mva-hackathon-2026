# Q4. What is the real within-patient variance of these endpoints?

**Asked because** section 8 concedes that within-patient variance of its endpoints "has never been measured in this disease", declares every power figure void until question 10 answers it, and then rests all three figures on an assumed biological coefficient of variation of 0.20 that no source supports. If that number can be derived from published data, the report's largest unsourced assumption becomes a sourced range. If it cannot, the concession stands and should be stated more sharply.

## Answer

**It can be derived, the assumption survives, and it was at the optimistic end of what the data support.**

### The derivation

Two primary sources, both reached, neither previously used for this purpose in the project.

**Between-subject spread.** Gajski G, Gerić M, Oreščanin V, Garaj-Vrhovac V. Ecotoxicol Environ Saf 2018;148:561-570, PMID 29127818. Two hundred subjects from the general population: "The background frequency of micronuclei (MNi) for the 200 subjects assayed was 5.06 ± 3.11 per 1000 binucleated cells." That is a between-subject coefficient of variation of **0.615**.

**Test-retest correlation.** Bolognesi C et al. Sci Total Environ 2019;652:513-522, PMID 30368181. One hundred and three healthy platelet donors, repeated blood samples: "High correlation between the results of the three blood samplings in two separate scoring sessions of MNBN/1000BN (R2 values were 0.83, 0.74 and 0.68; P < 0.0001)."

For a repeatability correlation `r`, the within-subject coefficient of variation is `CV_total × sqrt(1 - r)`.

| R² between samplings | r | Implied within-subject CV |
|---|---|---|
| 0.83 | 0.911 | **0.183** |
| 0.74 | 0.860 | **0.230** |
| 0.68 | 0.825 | **0.257** |

**Derived range: 0.18 to 0.26.** The appendix assumed 0.20 with 0.30 as a sensitivity. The assumption is inside the range and at its optimistic end; the sensitivity value is above the range and is more pessimistic than the data require.

### What it does to the three endpoints

At three measurements per period, on the same model the appendix already uses:

| Endpoint | At CV 0.18 | At the assumed 0.20 | At CV 0.26 |
|---|---|---|---|
| Micronuclei, baseline 40 per 1,000, 2,000 binucleated cells | 39.4 percent | 41.4 percent | 47.8 percent |
| Micronucleated reticulocytes, 1e6 cells | 35.1 percent | 37.5 percent | 45.1 percent |
| Interphase FISH with the same biological term added | 39.1 percent | 41.1 percent | 47.6 percent |

The figures move by six to eight percentage points across the whole derived range. **No conclusion in section 8 changes.** The endpoints remain able to see a change of roughly 35 to 48 percent and unable to see the 20 to 30 percent change any plausible intervention would produce. That was the report's conclusion and it now rests on data rather than on an assumption.

### The four caveats, which matter

1. **Two populations, spliced.** The spread is from Zagreb, the correlation from Genoa. Bolognesi's own mean and standard deviation are in a paywalled full text and were not reached, so the two could not be taken from one cohort.
2. **Both adult.** No paediatric test-retest figure was found. Children have lower baselines, 4.07 ± 1.87 per 1,000 at 3 to 15 years, and nothing establishes that their repeatability matches adults'.
3. **The correlation includes scoring error**, so `r` is a lower bound on the purely biological correlation and the derived CV is therefore an upper bound on the purely biological variance. If anything the true biological term is smaller and the endpoints slightly better than this.
4. **None of it is measured in this disease.** A child with premature chromatid separation in 48.5 to 83.2 percent of lymphocytes is not a healthy platelet donor, and the report's own question 10 asks for the figure in MVA specifically. That question stays open. What closes is the narrower complaint that the number was invented.

### A misattributed citation, corrected

While checking these sources: `archive/creative/F_math.md` cites the paediatric baseline meta-analysis as "Neri and Bonassi, Environ Health Perspect 2005, PMID 16140629". **PMID 16140629 is Rajaraman et al., "Delta-aminolevulinic acid dehydratase polymorphism and risk of brain tumors in adults."** The intended paper is **PMID 16140632**, Neri M, Ceppi M, Knudsen LE, Merlo DF, Barale R, Puntoni R, Bonassi S, "Baseline micronuclei frequency in children: estimates from meta- and pooled analyses," Environ Health Perspect 2005;113:1226-9, whose abstract gives "Overall means of 4.48 [95% confidence interval (CI), 3.35-5.98] and 5.70 (95% CI, 4.29-7.56) MN per 1,000 binucleated cells" exactly as the appendix quotes them. The audit had flagged this and supplied the correct identifier; the appendix had not been updated. It is now.

### Corrections applied

`archive/creative/F_math.md`: the PMID is corrected, and the assumed biological coefficient of variation is replaced by the derived range with both sources named. `REPORT_track2.md` section 8: question 10 is now recorded as partly answered, with the derived range, the band it puts on each endpoint, and the four caveats.

## Access levels reached

Full abstracts for all four papers via NCBI efetch. Bolognesi 2019 and Gajski 2018 full texts are paywalled; the abstracts carry the figures used, so the derivation does not depend on the bodies. An intraclass correlation of 0.905 attributed to Bolognesi elsewhere in this project sits in the paywalled body and was not verified here, so the derivation uses only the R² values printed in the abstract.
