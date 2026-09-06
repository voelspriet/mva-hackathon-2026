# R9. Is this project's frequency reasoning using the right denominator?

**Asked 6 September 2026.** Never asked before.

## Why it matters

Every rarity claim in this project is stated against gnomAD's **global** allele frequency. Global frequency is a weighted average over gnomAD's sampling, which is dominated by European-ancestry cohorts, and it is the wrong number if the child comes from a population that gnomAD samples differently.

This is not a pedantic point here, because the single most load-bearing claim in the whole project is a frequency claim: that *BUB1B* allele 2 is a gnomAD singleton and therefore rare enough to be a candidate causal allele. If the denominator is wrong, the argument built on it is weaker than it looks.

Nobody had checked which population the child belongs to. The genome answers it.

## Method

`pipeline/reanalysis/ancestry_infer.py`, using the byte-range gnomAD reader already in the project, extended with a region query so one read returns a whole window instead of one position.

Two design choices do the work, and both are there to stop the answer being circular or overconfident.

1. **The marker panel is chosen from gnomAD alone, never from the child.** Within each window the script takes the single SNV with the largest spread in allele frequency across populations. Choosing on cross-population spread is what makes a marker informative. Choosing on the child's genotype would guarantee a flattering answer.
2. **Markers are at least one megabase apart**, one per window, spread across all 22 autosomes in proportion to length, so linkage disequilibrium cannot inflate the likelihood. The *BUB1B* locus is excluded from the panel.

Populations scored: African/African-American, Admixed American, Ashkenazi Jewish, East Asian, Finnish, Non-Finnish European, South Asian. **Middle Eastern is excluded**, because gnomAD v4.1 genomes carries only about 292 Middle Eastern alleles and a frequency from 146 people is not stable enough to score against.

A position where the child has no call is read as reference homozygous, which is the standard reading of a variant-only VCF. **The script tests that assumption rather than asserting it**, by comparing observed heterozygosity across the panel against the value the winning population predicts.

## Result

85 markers passed the filters.

| | |
|---|---|
| Markers used | 85 |
| Observed heterozygous | 30, or 35.3 percent |
| Predicted by the best-fitting population | 33.2, or 39.0 percent |

The heterozygosity check passes. Thirty observed against 33.2 expected is within one standard deviation of the binomial, about 4.5, so the reference-homozygous reading of an absent call is not distorting the result.

| Population | Log-likelihood | Behind best |
|---|---|---|
| **Non-Finnish European** | **-73.3** | **0.0** |
| Finnish | -74.1 | -0.8 |
| South Asian | -76.2 | -2.9 |
| Ashkenazi Jewish | -76.3 | -3.0 |
| Admixed American | -77.2 | -3.9 |
| East Asian | -110.6 | -37.3 |
| African/African-American | -117.0 | -43.6 |

**What this does and does not establish.** African and East Asian ancestry are excluded decisively, by 44 and 37 log units. Within West Eurasia the panel does **not** discriminate: European is the best fit but Finnish sits 0.8 log units behind, which is no separation at all, and three more populations sit within 4. Eighty-five markers is a small panel, and gnomAD's Non-Finnish European group is itself heterogeneous.

**So the honest reading is West Eurasian, with European the best single fit and no ability to refine further from this panel.**

## The independent corroboration, which is stronger than the panel

The causal alleles were not in the panel, and they answer the same question on their own.

| Allele | afr | amr | asj | eas | fin | **nfe** | sas |
|---|---|---|---|---|---|---|---|
| *BUB1B* allele 1, exomes | 0 | 0 | 0 | 0 | 0 | **111** | 0 |
| *BUB1B* allele 1, genomes | 0 | 0 | 0 | 0 | 0 | **5** | 0 |
| *BUB1B* allele 2, exomes | 0 | 0 | 0 | 0 | 0 | **1** | 0 |

**All 117 observed copies of both causal alleles, across 1.6 million sampled alleles, are Non-Finnish European. Neither allele has ever been seen in any other gnomAD population.** That is independent of the ancestry panel, it is not subject to the panel's small size, and it points the same way.

## The frequencies, restated in the denominator that applies

| Variant | Global AF | **NFE AF** | NFE / global |
|---|---|---|---|
| *BUB1B* allele 1, p.Leu737Ter | 7.44e-05 | **9.83e-05** | 1.32 |
| *BUB1B* allele 2, p.Asn1002Lys | 6.84e-07 | **8.99e-07** | 1.31 |
| *LZTR1* nonsense | 1.37e-06 | **8.99e-07** | **0.66** |
| *RBM8A* hypomorph | 0.0260 | **0.0302** | 1.16 |
| *F5* Factor V Leiden | 0.0219 | **0.0246** | 1.13 |

**No conclusion in this project changes.** Every one of these alleles keeps its classification. What changes is that the numbers are now stated against the population the child belongs to rather than against a global average, and the direction of the error is now known: **for four of the five, the global figure understated the frequency in this child's own population, by up to a third.**

Three specific consequences worth naming.

- ***BUB1B* allele 1 is commoner in Europeans than the report says**, at 1 in 10,173 European alleles, a carrier frequency near 1 in 5,100. The report quotes the global figure. The allele is still rare and the conclusion is untouched, but the quoted number was 1.32 times too small for the relevant population.
- ***LZTR1* runs the other way.** Its NFE frequency is **lower** than global, because one of its two gnomAD copies is African. In this child's population it is a singleton, not a doubleton. This slightly strengthens the rarity of the allele and does nothing whatever to the conclusion in R7, which turned on penetrance rather than on rarity.
- **Factor V Leiden is commoner still than R8 stated.** At an NFE allele frequency of 0.0246, the carrier frequency is 4.8 percent, **about 1 in 21 Europeans**. R8 said 1 in 25 to 50 from the general literature. The child's own population denominator puts it at the common end of that range, which makes the case for not acting on it stronger, not weaker.

## Limitations

- The panel cannot separate populations within West Eurasia and should not be quoted as though it had.
- Eighty-five markers is small. The script takes a marker count as an argument and the panel can be enlarged at the cost of more byte-range reads.
- Admixture is not modelled. A single best-fitting population is fitted, not a mixture, so an admixed individual would be reported as whichever single group fits best.
- gnomAD's population labels are its own, and they are social and sampling categories as much as genetic ones.

## What R9 changes

| | |
|---|---|
| Conclusions changed | **None** |
| Frequency figures that should be restated in the report | Two, both *BUB1B* alleles |
| Load-bearing claims tested | One, the singleton status of allele 2, which survives |
| Independent corroboration found | Yes. Both causal alleles are European-private across 1.6 million alleles |
| New tool | A region query on the gnomAD reader, reusable by any later analysis |

The useful general point: a rarity argument is a statement about a denominator, and this project stated five of them against a denominator it had never checked. The check took one script and returned the answer that the denominators were close enough not to matter, which is worth knowing precisely because it was not knowable before.
