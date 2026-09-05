# Q17. Could a regulatory allele near *BUB1B* have been discarded by a coding-only filter?

**Asked because** a 2025 Chinese case report describes MVA caused by compound heterozygous variants in *BUB1B* "and its upstream regulatory elements". The Track 1 pipeline filtered to coding sequence. If that filter can miss a real allele, the claim that this genome has been fully searched is weaker than it reads.

## Answer

**The allele class is real, functionally proven, and eleven years old. This genome does not carry one.**

### The precedent is stronger than the 2025 case report

Found through the reference list of a doctoral thesis, not through any PubMed search this project ran:

**Ochiai H, Miyamoto T, Kanai A, Hosoba K, Sakuma T, Kudo Y, Asami K, Ogawa A, Watanabe A, Kajii T, Yamamoto T, Matsuura S. "TALEN-mediated single-base-pair editing identification of an intergenic mutation upstream of BUB1B as causative of PCS (MVA) syndrome." Proc Natl Acad Sci U S A 2014;111(4):1461-6, PMID 24344301.**

The abstract, verbatim on the decisive points: the same seven Japanese families in which "no second mutation was found in the opposite allele", but with "a conserved BUB1B haplotype and a decreased transcript". Extending the search around the gene found "a unique single nucleotide substitution, G > A at ss802470619 ... in an intergenic region 44 kb upstream of a BUB1B transcription start site, which cosegregated with the disorder", and the authors then proved causality by TALEN-mediated two-step single-base-pair editing.

**This closes a loop the report left open.** Section 2 cites Matsuura 2006 for seven families with monoallelic *BUB1B* mutations. Those families were not monoallelic. Their second allele was regulatory and 44 kb away, and it took eight years and a genome-editing experiment to find it. Any exome, and any coding-filtered genome analysis, would have missed it.

### What this genome actually carries there

*BUB1B* begins at chr15:40,160,984 on the plus strand, so the equivalent position is near chr15:40,116,984. Every PASS variant in the 60 kb upstream window, chr15:40,100,984 to 40,160,984, was checked against gnomAD v4.1 genomes by a single indexed byte-range read of the public sites file.

| Measure | Value |
|---|---|
| Variants called in the window | 88 |
| Heterozygous | 53 |
| gnomAD genomes records in the same window | 13,418 |
| Our variants absent from gnomAD at that position and allele | **0** |
| Our variants present at under 1 percent frequency | **2** |

The two below one percent are chr15:40,114,056 A>G at AF 0.0021 with 323 carriers, and chr15:40,144,423, an AAAG-repeat expansion, at AF 0.0026 with 297 carriers. Neither is rare enough to be a candidate for a recessive allele, neither is near the 44 kb position, and the nearest call to that position at all is 456 bp away and homozygous, meaning common.

**Conclusion: no candidate regulatory allele upstream of *BUB1B* in this child.** The coding-only filter did not cost anything here.

### Where the negative stops

Sixty kilobases upstream, chosen because it contains the only functionally proven regulatory allele in this gene. It does not cover distant enhancers, deep intronic variants inside the gene, or structural variants, which a germline SNV and indel VCF cannot call. And this child already carries two coding alleles, so no third is required to explain the genotype. The finding matters for the method rather than for the diagnosis.

## Corrections applied

Section 2 records that Matsuura's seven families were later shown not to be monoallelic, that the second allele was intergenic and 44 kb upstream, and that this genome was checked there and carries nothing rare. Section 11 records that a coding filter is not sufficient for this gene, which matters for the claim that the pipeline transfers to other families.

## Where this came from, which is the wider point

Not from PubMed. From the reference list of **"Mosaic Variegated Aneuploidy: Elucidating the molecular causes of constitutional aneuploidy in humans"**, a doctoral thesis by Bas de Wolf, Utrecht University 2020, doi 10.33540/239, retrieved through the DSpace REST API after the repository's web interface refused automated access. The same thesis names four further MVA genes the report's differential does not carry, *TRIP13*, *CENATAC* (renamed from *CCDC84*, a minor spliceosome component), *KNL1* and *ZWINT*, and states that its chapter 3 "uncover[s] a striking correlation between the mutations in these genes and the occurrence of specific childhood cancers in MVA patients". That correlation, if it holds, would let surveillance be targeted by genotype rather than applied uniformly, and it is now queued as its own question.
