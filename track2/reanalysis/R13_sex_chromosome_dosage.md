# R13. The sex chromosomes, and a second way of asking whether the aneuploidy is visible

**Asked 6 September 2026.** The Y chromosome had never been examined in this project at all.

## Why this is not a housekeeping question

The report's mosaicism analysis rests on B-allele fraction, and R6 found that method has a hole. Every autosome returns f_BAF of 0.000, and the report states a detection floor near 10 percent, so the position is that the child's aneuploidy is real but not visible in this blood sample.

That claim currently rests on **one measurement principle**. The sex chromosomes allow a second one, because in a male they are present at a single copy, so mosaic loss shows up directly in **depth** with no allele fraction involved. Depth and B-allele fraction fail for different reasons, so agreement between them is worth something.

There is a specific reason to look, too. **Mosaic loss of Y is the commonest acquired aneuploidy in human blood.** In a child whose syndrome is constitutional chromosome missegregation, an elevated rate would be exactly the thing to expect.

## Result

Depths are means over PASS calls with depth between 5 and 200, against three autosomal control windows averaging **41.98**.

| Region | Calls | Mean depth | Ratio to autosomal | Heterozygous |
|---|---|---|---|---|
| chrX non-PAR, 2.8 to 154 Mb | 100,925 | 20.67 | **0.4924** | 1.3% |
| chrY unique, 2.8 to 10 Mb | 945 | 21.05 | **0.5014** | 18.8% |
| chrY, 20 to 26.6 Mb | 476 | 23.91 | 0.5694 | 36.7% |
| chrY ampliconic, 10 to 20 Mb | 6,136 | 30 (median) | 0.698 | **75.8%** |
| chrY heterochromatin, 26.6 Mb onward | 2,125 | 137 (median) | **3.2** | **93.6%** |

**One copy expected is a ratio of 0.50.**

**chrX is at one copy**, 0.4924. There is no X anomaly and no mosaic X loss.

**chrY is at one copy** in the cleanest unique window, 0.5014. **There is no detectable mosaic loss of Y.**

## What the bound actually is, which is looser than the arithmetic suggests

The statistical standard error on the chrY 2.8 to 10 Mb ratio is ±0.0085, which would imply detecting mosaic loss above about 3 percent. **That number should not be quoted, and the reason is in the table above.**

Two problems, both visible in the data rather than assumed.

1. **The two usable Y windows disagree by 14 percent of a copy**, 0.5014 against 0.5694. Since both cannot be right, the systematic error between windows is an order of magnitude larger than the statistical error within one.
2. **Every Y window carries heterozygous calls on a haploid chromosome**, from 18.8 percent in the best window to 93.6 percent in the heterochromatin. A haploid chromosome cannot be heterozygous. Those calls are reads from elsewhere, and they distort depth as well as genotype.

**So the honest bound on mosaic loss of Y here is set by systematics at roughly 10 to 15 percent, not by counting at 3 percent.** That lands in the same place as the B-allele fraction floor the report already declares, by a completely different route.

## What that is worth

**Two independent methods now agree that no mosaic aneuploidy is detectable in this blood sample.** B-allele fraction across the autosomes returns zero everywhere; haploid depth across the sex chromosomes returns one copy of each. They share no failure mode: the first is blind to whole-chromosome events that preserve allele ratios and depends on heterozygous sites, the second depends on mappability and GC and needs no heterozygous sites at all.

That does not make the aneuploidy less real. It confirms, by a second route, that **this tissue at this depth cannot show it**, which is what the report says and what the gate's proposed karyotype or single-cell work exists to address.

## A reusable caution about chrY

Most of chrY is not analysable from short-read whole-genome data, and this dataset shows exactly where the boundary falls.

- **Usable**: the unique male-specific region, roughly 2.8 to 10 Mb, and with care 20 to 26.6 Mb.
- **Not usable**: the ampliconic and palindromic region from 10 to 20 Mb, where 75.8 percent of calls are heterozygous.
- **Never usable**: the Yq12 heterochromatic block beyond 26.6 Mb, at **3.2 times autosomal depth and 93.6 percent heterozygous**. It is a repeat array, and every call in it is an artefact.

Anyone reusing this project's tooling on a male sample should restrict chrY analysis to the unique region, and should treat the non-PAR heterozygous rate as the artefact floor, exactly as R10 established for the X at 1.27 percent.

## What R13 changes

| | |
|---|---|
| New findings | **None** |
| Compartment examined for the first time | chrY |
| Independent confirmation | The mosaicism detection floor, via depth rather than allele fraction |
| Bound established | No mosaic loss of Y above roughly 10 to 15 percent |
| Reusable caution | The three-way usability split of chrY, measured rather than cited |
| Recommendations added | **None** |
