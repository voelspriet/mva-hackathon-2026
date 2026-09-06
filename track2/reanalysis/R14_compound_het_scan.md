# R14. Does any other gene in this genome look like *BUB1B*?

**Asked 6 September 2026.** The diagnosis is a compound heterozygote. The direct test of it is therefore not "is *BUB1B* damaged" but "**is *BUB1B* the only gene that is damaged this way**". That question had never been asked in this form.

## Method

The snpEff-annotated coding set from R11: 33,416 PASS coding variants. Keep HIGH and MODERATE impact variants carrying **no rsID**, which is the ultra-rare proxy this project uses elsewhere. Group by gene and keep genes with two or more.

Then two filters, both derived from artefact classes R11 measured rather than guessed:

- **Drop clustered variants.** Any gene whose variants are less than 1 kb apart is a misaligned indel cluster, not a compound heterozygote.
- **Drop the hypervariable families.** Immunoglobulin and T-cell receptor V segments, HLA, taste receptors, olfactory receptors, mucins, *GOLGA*, *DSPP*, *HTT*, *FCGBP*. R11 established every one of these as an artefact source, and the unfiltered output is dominated by them.

## Result

123 genes carry two or more such variants. After filtering, **15 remain**, and *BUB1B* is one of them.

**The positive control is recovered exactly.**

| | |
|---|---|
| chr15:40209701 | HIGH, stop gained, p.Leu737\*, heterozygous |
| chr15:40220612 | MODERATE, missense, p.Asn1002Lys, heterozygous |
| Separation | 10,911 bp |

The scan found the causal genotype without being told the gene, the disease, or the phenotype.

**And *BUB1B* is the only one of the 15 that has the shape of a recessive diagnosis.** The other 14 fail on their genotypes or their consequences:

- **Six are homozygous for both variants**: *AKAP17A*, *EPHB6*, *EPPK1*, *SLC39A4*, *TMC4*, *ZNF180*. Two variants present on both haplotypes is one common haplotype carrying two substitutions, which is the opposite of a compound heterozygote.
- **Two sit in loci this project has already shown to be unreliable**: *CYP2D6*, where R8 established that star-calling from short reads without copy number is not valid, and *CRLF2*, in the pseudoautosomal region.
- **The remaining six pair two missense variants and nothing else**: *AADACL3*, *ALMS1*, *CEACAM21*, *HEG1*, *LILRA4*, *PRSS3*. None carries a truncating allele, and none has a phenotype resembling this child's. *ALMS1* is the only one naming a recognised recessive syndrome, Alström syndrome, whose features are obesity, retinal dystrophy, hearing loss and cardiomyopathy, none of which is in the supplied document; both of its variants are in-frame indels in a repeat-rich gene.

**No gene other than *BUB1B* pairs a truncating variant with a second rare allele in this genome.**

## What this is and is not

**It is** the first test of the diagnosis as a diagnosis rather than as a gene. Every earlier confirmation asked whether *BUB1B* explains the phenotype. This asks whether anything else could, and answers no, from an unbiased scan that recovers the right answer as its control.

**It is not** a complete recessive scan. Three limits, stated because a negative is only as good as its scope:

- **The rarity proxy is crude.** Absence of an rsID is not the same as rarity, and the surviving missense pairs were not individually frequency-checked, because none of them had a phenotype worth the lookup.
- **Coding sequence only**, so a second allele that is deep intronic, regulatory, or a copy-number change would be missed. R12 showed this genome does carry at least one novel deep intronic allele, in *BUB1B* itself.
- **Phase is unreadable.** R1 established the longest read-backed phase set in this genome spans 288 bp, so "two variants in one gene" is never directly shown to be "one on each copy", for *BUB1B* or for anything else. That limitation is already declared in the report and it applies here identically.

## What R14 changes

| | |
|---|---|
| New findings | **None** |
| Question answered for the first time | Whether any gene other than *BUB1B* carries a recessive-looking genotype |
| Positive control | Recovered without the gene being named |
| Competing diagnoses found | **Zero** |
| Recommendations added | **None** |
