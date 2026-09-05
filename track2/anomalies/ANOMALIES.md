# Anomaly scan of the hackathon data

Run under `track2/audit/PROMPT_D_anomaly.md`, over what the challenge actually supplied: the whole-genome VCF and the clinical phenotype document. Unlike `track2/reanalysis/`, which asked six specific questions, this looks for whatever is odd. One finding is consequential and the report is wrong because of it.

**This is a partial execution of that prompt.** The cross-source consistency pass and the scans listed below were run. Not yet run: the phase-set structure scan, the filter-behaviour scan, the full expectation-first treatment of every scan, and the systematic table of everything checked with its positive control. Those are the remainder.

---

## A1. The nephrocalcinosis is dated to birth, and neither of the report's two causes can produce that

**The challenge's own phenotype document states, verbatim:** "Nephrocalcinosis · HP:0000121 · Calcium deposits in kidney tissue; **present since birth**".

**The report builds its renal branch on two acquired postnatal causes**, and on nothing else:

1. Nephrocalcinosis of prematurity, driven by neonatal furosemide and by calcium and vitamin D in parenteral nutrition.
2. Ifosfamide proximal tubulopathy from the rhabdomyosarcoma treatment.

**Neither can be present at birth.** Nephrocalcinosis of prematurity develops over weeks of neonatal intensive care; it is a consequence of the treatment a 32-week, one-kilogram infant receives, not a finding at delivery. Ifosfamide came years later. The phrase "present since birth" is incompatible with both, and **the report never registers it**: the strings "since birth", "at birth", "antenatal" and "in utero" appear nowhere in it.

**Two readings, and they need different actions.**

- **The document is loose.** "Since birth" may mean "documented from the neonatal period", with the finding first seen on a routine ultrasound some weeks into neonatal care. This is common in clinical summaries and would leave the report's framing intact.
- **The document is literal.** Then there is a third cause the project never considered, which is congenital or antenatal in origin: intrinsic to the syndrome, an in-utero exposure, or a primary tubular disorder. On that reading the report's competing-causes branch is not merely incomplete, it is looking in the wrong place, and the thiazide-versus-alkali decision it drives is being made on the wrong differential.

**The discriminator costs nothing and is already half-written.** The gate's records line asks for neonatal furosemide and parenteral nutrition exposure. It should also ask for **the date of the first renal ultrasound showing nephrocalcinosis, and whether any antenatal scan showed it**. One date separates the two readings and changes which branch of the renal algorithm applies.

This is the clearest thing the whole project missed, and it was in the challenge's own two-page phenotype document rather than in the literature.

---

## A2. A genuine somatic signal, at the loci where one is expected

Scanning allele balance across all 2.95 million heterozygous calls, and filtering to single-nucleotide changes with genotype quality at least 90, depth at least 30, and outside centromeric and acrocentric regions, leaves 17,318 calls whose allele balance falls below 0.20. They are not scattered at random. The megabases carrying most of them include:

| Locus | Calls | What it is |
|---|---|---|
| chr6:32 Mb | 794 | Major histocompatibility complex, the most polymorphic region of the genome |
| chr7:142 Mb | 718 | **T-cell receptor beta locus** |
| chr22:22 Mb | 287 | **Immunoglobulin lambda locus** |
| chr1:143 Mb, chr17:26 Mb, chr8:12 Mb, chr16:34 Mb | 354 to 580 each | Segmental duplication blocks |

The T-cell receptor and immunoglobulin entries are the interesting ones. Those loci undergo **somatic V(D)J recombination** in lymphocytes, deleting sequence in a fraction of cells. In a blood sample that produces exactly this signature: heterozygous calls whose minor allele sits well below half. It is expected biology rather than a finding about this child, and it is useful as a **positive control**: the method detects real somatic events, which means its silence elsewhere carries weight.

---

## A3. The apparent Y chromosome excess dissolves

An earlier pass recorded mean depth of 73 on chromosome Y against 42.7 on the autosomes, which would be odd in a male. Broken down by megabase it is not odd at all. The male-specific single-copy region, roughly 3 to 22 Mb, runs at median depth 17 to 21, which is **half the autosomal depth, exactly as one Y copy should be**. The whole excess comes from three pileups: Y 10 to 11 Mb and Y 26 Mb at the edges of heterochromatin, and Y 56 Mb at median depth 138 with 94 percent of calls heterozygous, which is unmappable repeat, not sequence. Heterozygosity of 21 percent at Y 2 Mb is the pseudoautosomal region behaving correctly.

**Conclusion: a normal male genome, and the earlier number was an artefact of averaging across repeat blocks.**

---

## A4. Nothing wrong with the sample

| Metric | Value | Expected |
|---|---|---|
| Heterozygous to homozygous-alternate ratio | 1.57 | 1.5 to 2.0 for an outbred genome |
| Transition to transversion ratio | 1.97 | about 2.0 to 2.1 genome wide |
| Median depth | 42 | — |

The low-allele-balance excess that might signal contamination is **regional, not global**: 43 percent of it sits in fifteen megabase bins, all centromeric or acrocentric. Contamination produces a genome-wide shift, and there is none.

## A5. No hidden homozygous deletion

Thirty-three regions of 150 kb or more contain no called variant, totalling 59.7 Mb. Every one of the twenty largest is a known heterochromatic block or centromere: 1q12, 9q12, 16q11, the acrocentric short arms of 13, 14, 21 and 22, and the centromeres of 2, 5, 17 and 19. Nothing unexplained, so no evidence of a large homozygous deletion anywhere in the genome.

## A6. The growth restriction is severe, and internally consistent

One kilogram at 32 weeks sits below the third centile for gestational age; the median is close to 1.8 kg. The document's own assignment of small for gestational age is right, and the severity is worth carrying because it is the earliest measurable manifestation of the syndrome, predating every other feature including the tumour.

---

## What was checked and found clean

Global quality metrics, contamination signature, large homozygous deletions, chromosome Y and X dosage, extreme-depth pileups, and the distribution of low-allele-balance calls. Added to the six negatives already recorded in `track2/reanalysis/SUMMARY.md`.

## Correction applied

The gate's records line now asks for the date of the first renal imaging showing nephrocalcinosis and whether any antenatal scan showed it, and section 6 records that the phenotype document dates the finding to birth, which neither competing cause explains.
