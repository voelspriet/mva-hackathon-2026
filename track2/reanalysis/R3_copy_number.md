# R3. Copy number and structural events from read depth

**Question.** The mosaicism analysis used allele balance. Depth carries an independent channel. Does it show a constitutional deletion or duplication that the variant-level analysis would not see?

**Data.** In hand. Per-variant depth for all autosomal PASS variants, median per megabase.

**Computed answer, on PASS calls. Nothing that is not a known mapping artefact.** Genome median per-window depth is 43. **Eleven** windows fall below 0.7 times that and **nineteen** rise above 1.4 times. An earlier version, computed without the PASS filter, gave 50 and 14; most of the apparent low-depth windows were failing calls, which is what a depth filter would be expected to remove.

Every low window is pericentromeric: chromosome 11 at 51 to 53 Mb, chromosome 8 at 44 Mb, chromosome 9 at 44 to 45 Mb, chromosome 17 at 24 to 25 Mb, chromosome 18 at 17 to 19 Mb, chromosome 2 at 93 Mb, chromosome 6 at 59 Mb. Every high window is an acrocentric short arm or a centromere: chromosome 22 at 10 to 11 Mb, chromosome 21 at 7 to 12 Mb, chromosome 15 at 20 Mb, chromosome 17 at 22 Mb.

**What each possible result would change.** A deletion spanning *BUB1B* would have changed the genotype from compound heterozygous to hemizygous, and the whole mechanism section with it. None exists. A large constitutional aneuploidy would have changed the diagnosis. None exists.

**Limit, stated plainly.** A variants-only VCF gives depth at called sites, not across the genome, so this test has megabase resolution and detects nothing exon-sized. It does not replace a copy-number caller run on the reads.

**Tier.** Computed here. **Cost.** Under a minute.

**Why it was not asked before.** The mosaicism work used depth only as a per-chromosome sanity ratio, never as a per-window scan for a discrete event.
