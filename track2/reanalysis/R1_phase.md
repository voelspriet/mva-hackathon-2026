# R1. Can phase be read out of the VCF that is already in hand?

**Question.** The whole Track 2 argument rests on the two *BUB1B* variants being in trans, and the report concedes that phase is unproven. Before asking for a trio, does the existing whole-genome VCF already carry the answer?

**Data.** In hand: `data/WGS_EX2312012_HGWCNDSX7.vcf.gz`, which carries GATK's `PGT` and `PID` fields wherever the caller phased by read evidence.

**Computed answer. No, and the negative is clean.**

| Variant | GT | PGT | PID | DP |
|---|---|---|---|---|
| chr15:40209701 T>G, p.Leu737Ter | 0/1 | absent | absent | 46 |
| chr15:40220612 T>G, p.Asn1002Lys | 0/1 | absent | absent | 28 |

Neither variant carries a phase set. The phase sets that do exist in the region are local and short: `40216568_TA_T` spans two positions 2 bp apart, and `40229717_C_G` spans 5 bp. Every heterozygous site between the two variants, at 40216470 and 40221421, is likewise unphased.

**Why.** The two variants are 10.9 kb apart. Read-backed phasing joins variants that share a sequencing fragment, which for this library means a few hundred base pairs. Ten kilobases is three orders of magnitude beyond that. No re-processing of these reads can bridge it, so the 84 GB of raw FASTQ on the gated dataset would not answer this question either.

**What each possible result would change.** A phased pair in trans would have removed the gate's first item and settled the ACMG PM3 code. It does not exist, so nothing changes: the report's statement that phase is unproven stands, and the routes that remain are parental genotyping or a long-read amplicon across the 10.9 kb, both already item 1 of the gate.

**Tier.** Computed here, from the VCF itself. **Cost.** Minutes.

**Why it was not asked before.** The project treated phase as a wet-lab question from the start and never checked whether the caller had already answered it. It had not, but that was assumed rather than shown.
