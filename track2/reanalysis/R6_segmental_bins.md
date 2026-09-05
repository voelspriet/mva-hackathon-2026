# R6. The bins the mosaicism scan discarded, and the outliers it recorded but never followed

**Question.** `mosaic_robust.py` reports a median across bins and writes the individual bins that exceeded the segmental threshold into a field called `hi_bins`. Nothing in this project ever read that field. Are those bins segmental mosaicism that the chromosome median averaged away?

**Data.** In hand. Recomputed with `pipeline/reanalysis/bin_outliers.py`, which prints every bin instead of the median.

**Computed answer. Fifty-six bins exceed the threshold. None is a credible mosaic event, and the reason is arithmetic rather than judgement.**

Twenty-seven of 563 autosomal bins, 4.8 percent, were discarded outright for holding under 500 heterozygous sites. Of the 56 bins above a BAF excess of 0.06, 31 pass the existing depth-ratio filter and would therefore have been believed.

**They cannot be believed, because the implied cell fraction exceeds one.** The model converts BAF excess to a trisomic cell fraction by `f = 4d / (1 - 2d)`. At the observed excesses this returns values of 1.0 to 2.3, meaning more than every cell carries the gain. That is not a marginal result to be weighed; it is a statement that the model has left its domain.

Where they sit confirms it. The largest cluster is 1q12 heterochromatin at chromosome 1, 120 to 145 Mb; then 9q12 at chromosome 9, 60 to 65 Mb; the acrocentric short arms of chromosomes 15, 21 and 22; the centromeres of chromosomes 16, 17 and 20; and the single highest heterozygous count in the genome, 18,207 sites in chromosome 6 at 30 Mb, which is the major histocompatibility complex. These are the standard low-mappability and hyperpolymorphic regions, where allele balance is distorted by reads from paralogous sequence rather than by a third chromosome.

**What this changes, and it is a real change.** The detection floor quoted in both reports, 11.7 percent per bin under genome-wide correction, is a genome-average figure that does not hold in these regions. The method needs a third filter, either a mappability mask or the trivial one of rejecting any bin whose implied fraction exceeds a plausible ceiling. The negative result itself is unaffected: no bin anywhere shows the modest, internally consistent excess that a real subclonal gain would produce.

**What remains.** Overlaying a segmental duplication and mappability track would convert the argument from "these are the regions where this happens" to "these bins overlap known unmappable sequence by X percent". That track is not held offline here and the overlay is the step left undone.

**Tier.** Computed here. **Cost.** Two minutes of compute.

**Why it was not asked before.** The field was written and never read. The chromosome median was the number the reports quoted, and a median is designed to hide exactly this.
