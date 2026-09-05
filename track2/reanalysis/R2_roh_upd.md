# R2. Runs of homozygosity, consanguinity and uniparental disomy

**Question.** Does the genome carry long homozygous tracts, which would indicate relatedness between the parents, or uniparental disomy of chromosome 15, which is a recognised mechanism for unmasking a recessive allele and would change how the second allele is interpreted?

**Data.** In hand. Genotypes for 4,763,357 autosomal PASS variants, binned per megabase.

**Computed answer. No runs of homozygosity anywhere.**

| Measure | Value |
|---|---|
| Autosomal variants scored | 4,763,357 |
| Genome-wide heterozygous fraction | 0.628 |
| Median per-megabase heterozygous fraction | 0.633 |
| Runs of 3 Mb or more below 20 percent of median | 0 |
| Runs of 4 Mb or more below 50 percent of median | 0 |
| Total megabases in a run of homozygosity | 0 |

Chromosome 15 around *BUB1B* is unremarkable: the ten megabases spanning 36 to 45 Mb run at heterozygous fractions of 0.45 to 0.81, inside the genome-wide spread.

**What each possible result would change.** A long chromosome 15 tract would have raised isodisomy, under which the two variants would sit on one parental chromosome and the trans model would fail. It is absent. Consanguinity, which would have changed the prior on a second recessive condition, is also absent. Note the limit: heterodisomy leaves no homozygous tract and is not excluded by this test, though both variants being heterozygous already argues against isodisomy at this locus.

**Tier.** Computed here. **Cost.** Under a minute. Script: `pipeline/reanalysis/` and `work/roh_windows.json`.

**Why it was not asked before.** The Track 1 pipeline went straight from variant calling to gene ranking. Homozygosity is a standard first-pass genome observation and no stage of this project made it.
