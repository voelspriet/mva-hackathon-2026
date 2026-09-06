# R20. The chr5 coverage reduction, resolved: two copies of *SMN1*, zero of *SMN2*

**Asked and answered 6 September 2026.** R19 recorded a coverage reduction across chr5:69.6-71.1 Mb, the SMA locus, and stated that depth alone cannot distinguish reduced *SMN* copy number from mismapping between the near-identical paralogues. The tool that can was run on the alignment already in hand.

## Method

`SMNCopyNumberCaller` (Illumina), the standard caller for this locus, run against GRCh38 on the merged BAM produced in R17. It resolves the paralogues by paralogous sequence variants at sixteen sites rather than by depth, then calls copy number from read support at each.

## Result

| | |
|---|---|
| **SMN1 copy number** | **2** |
| **SMN2 copy number** | **0** |
| *SMN2* delta7-8 | 1 |
| Total copy number, raw | 3.12 |
| Full-length copy number, raw | 1.87 |
| Is SMA | **False** |
| Is carrier | **False** |
| Confidence | 2 at all sixteen sites |
| Quality | `PASS:Majority`, median depth 55.3, coverage MAD 0.081 |

*SMN1* read support runs from 27 to 65 across the sixteen sites, with an *SMN1* fraction of 1.00 at fifteen of them and 0.94 at the sixteenth. *SMN2* read support is zero at fifteen sites and two at one.

## What this means

**Two copies of *SMN1* is the normal state.** The child is not a spinal muscular atrophy patient and not a carrier. This closes the observation.

**And it explains the coverage reduction exactly.** A typical genome carries two *SMN1* and two *SMN2* copies, four in total across the duplicated segment. This one carries three: two *SMN1*, zero *SMN2*, one delta7-8 form. Three quarters of four is 0.75, and the measured ratio across the region was 0.73 to 0.77. The dip was real, it was quantitative, and it was benign. Zero *SMN2* copies occurs in roughly ten to fifteen percent of people and has no consequence when *SMN1* is intact.

## Why this is worth keeping rather than deleting

The screen was run blind: the enumeration in `OBSERVATIONS_2000.md` never saw the phenotype document, and the four discriminators in R19 reduced 600 windows to 17 without reference to any gene name. One of those 17 was a genuine, correctly measured copy-number difference. The follow-up then classified it as benign in under an hour, using the alignment that already existed.

That is the chain working end to end: an unbiased screen surfaced a real structural difference, and a targeted tool resolved it. A screen that never surfaces anything real cannot be trusted when it reports nothing, and a screen that surfaces things it cannot resolve is noise. This one did both halves.

**Correction to R19.** The sentence there about the child's muscle atrophy and failure to thrive being a reason to look harder is now moot. The phenotype overlap was real and the finding is not. R19 stands as written, with this note attached.
