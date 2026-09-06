# R19. Testing the labels instead of trusting them, and what survived

**Asked 6 September 2026.** `OBSERVATIONS_2000.md` assigned every line a status: 1,372 `raw`, 433 `artefact-prone`, 208 `notable`. Those labels were rules, not measurements. `artefact-prone` was awarded on a gene-name prefix (MUC, HLA, TRBV, IGHV, LILR, KIR, OR) with no number behind it, and `raw` meant literally "enumerated, unexamined". Triaging only the 208 would have been an audit of my own guesses.

This note tests the 600 coverage windows with four measurements. The remaining classes follow.

## The four discriminators, and the two that failed

| Test | What it asks | Result |
|---|---|---|
| Adjacency | is the window within 500 kb of unmappable sequence? | useful |
| Coherence | do the neighbouring windows deviate the same way? | **failed** |
| Plausible ratio | is the ratio near 0.5, 1.5 or 2.0, the only values a germline copy number can take? | useful |
| Distance to centromere | is it within 3 Mb of a centromere or acrocentric arm? | decisive |

**Coherence failed and the failure is instructive.** It promoted chr1 122-125 Mb, chr13 16-18 Mb, chr15 20 Mb and chr21 10 Mb with ratios of 3 to 7. Those are heterochromatin blocks where reads from elsewhere pile up. Mismapping is spatially coherent for the same reason a real duplication is, so coherence cannot separate them. Magnitude can: a ratio of 7 is not a copy number, it is an accumulation.

| Stage | Windows remaining |
|---|---|
| deviating more than 3 SD | 600 |
| after ratio and adjacency and GC | 107 |
| after excluding pericentromeric | **17** |

Of the 107 that survived the first three tests, **90 sat within 3 Mb of a centromere**. The residual signal of this method is pericentromeric mismapping, and without a mappability mask no focal call can be made there. That is a stated limit, not a finding.

## What the 17 are

Every one falls in a locus that is copy-number variable in the general population: *TBC1D3* on chr17 (a primate-specific family that varies in copy number), *NBPF20* and *PPIAL4D* at 1q21.1, the beta-defensin cluster at chr8 11.9-12.1 Mb, and one region that is different enough to name separately.

## chr5:69.6-71.1 Mb, the SMA locus

Window by window, with flanks at exactly 1.00:

```
69.5 Mb  0.92     70.1 Mb  0.62     70.7 Mb  0.98
69.6 Mb  0.74     70.2 Mb  0.72     70.8 Mb  0.77
69.7 Mb  0.48     70.3 Mb  0.72     70.9 Mb  0.72
69.8 Mb  0.60     70.4 Mb  0.70     71.0 Mb  0.60
69.9 Mb  0.86     70.5 Mb  0.74     71.1 Mb  0.85
70.0 Mb  0.83     70.6 Mb  0.64     71.2 Mb  1.07
```

The genes inside it are *SMN1*, *SMN2*, *SERF1A*, *SERF1B*, *NAIP* and *GTF2H2*.

**What can be said.** Coverage across this 1.5 Mb is genuinely reduced, the boundaries are sharp, and the flanking sequence is normal. The reduction is ragged rather than a clean step at 0.5.

**What cannot be said, and this is the larger part.** Short-read coverage cannot distinguish reduced *SMN* copy number from mismapping between the near-identical paralogous halves of this locus. The raggedness is equally consistent with either. Nothing here establishes an *SMN1* copy number, and a deletion carrier state is common in the general population at roughly 1 in 40 to 1 in 60, so a single copy would not be causal on its own. Biallelic *SMN1* loss causes spinal muscular atrophy, a different clinical picture that would not go unnoticed.

**Why it is worth recording anyway.** The supplied phenotype includes skeletal muscle atrophy (HP:0003202), low muscle mass and failure to thrive. A coverage reduction at the SMA locus in a child with those features is not something to leave in a screening file unnamed, whatever its most likely explanation. The enumeration that found it never saw the phenotype document, which is the only reason it is interesting rather than circular.

**The concrete next step** is a caller built for this locus, `SMNCopyNumberCaller`, which resolves *SMN1* against *SMN2* by paralogous sequence variants rather than by depth. That is a one-hour job on the alignment already in hand, and it either produces a copy number or shows that the reduction is a mapping artefact. Until it is run, this is an observation and not a finding.

## What this changes about the screening file

The status column in `OBSERVATIONS_2000.md` should be read as provisional for every class that has not yet had a second pass. For the coverage windows it is now measured. The gene-level labels, which were assigned on name prefixes alone, have not been tested and remain the weakest part of that file.
