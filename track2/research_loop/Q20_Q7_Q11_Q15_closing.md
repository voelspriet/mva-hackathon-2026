# Q20, Q7, Q11 and Q15: closing the queue

The last four questions. Two produce a report change, two are documented negatives.

---

## Q20. Two 2025-2026 mechanism papers

### Cardiac: the gate item's justification improves

**"BubR1 Insufficiency Drives Transcriptomic Alterations and Pathology Associated With Cardiac Aging and Heart Failure", Aging Cell 2025, PMID 40607964, doi 10.1111/acel.70160, open access.** BubR1 insufficiency in mice produced "marked cardiac hypertrophy, increased fibrosis, and elevated markers of cellular senescence", with transcriptomic disruption of "ion channel regulation, cytoskeletal organization, and contractile fiber dynamics". Hypomorphic hearts "mirrored transcriptomic changes observed in end-stage heart failure patients", and BubR1 protein "was found to decline with age in the heart and were also significantly reduced in rodent models of heart failure and in heart failure patients".

**Why this matters to gate item 6.** The report's cardiac baseline currently rests on North 2014's electrocardiogram finding and on Baker 2011, where cardiac failure is "presumably the main cause of death ... (data not shown)". This paper supplies the direct cardiac phenotyping Baker 2011 lacked, and it gives the electrocardiogram reading a mechanism: disrupted ion channel regulation is what an abnormal J point and QTc would express. The justification moves from a presumption on unshown data to a characterised phenotype.

**The limits are the report's own.** This is a mouse hypomorph, not this child's genotype, and the same discipline that corrected the mouse-to-human residue error applies. It is a reason to take the baseline seriously, not evidence that this child has a cardiac phenotype, which the report already says.

### Proteostasis: the chaperone exclusion needs a sharper reason

**"Proteostasis failure and mitochondrial dysfunction contribute to chromosomal instability-induced microcephaly", Nat Commun 2026, PMID 41820377, doi 10.1038/s41467-026-70521-0, open access.** A Drosophila model depleting a single spindle assembly checkpoint gene in neural stem cells. Microcephaly arises from "loss of stemness", which "arises from the accumulation over time of an unbalanced number of gains and losses of more than one chromosome, rather than a direct consequence of chromosomal instability-induced DNA damage or the production of simple aneuploidies". And critically: "we identify overexpression of Radical Oxygen Species scavengers, mitochondria chaperones and apoptosis inhibition as genetic interventions capable of dampening the deleterious effects of aneuploidy on brain size."

**This is tolerance working.** Section 7 excludes chaperone inducers on a correction-versus-tolerance argument: raising chaperone capacity does not lower the mis-segregation rate, it only makes aneuploid cells easier to keep, and tolerance is what lets aneuploid clones persist. That argument is about **cancer risk**. In the developing brain, keeping aneuploid neural stem cells alive is the point, and chaperones did exactly that.

**The exclusion stands, and the reason is corrected.** Not because tolerance is useless, but because: the interventions are genetic overexpression rather than drugs; the model is Drosophila; the developmental window in which brain size is determined has passed for this child; and one of the three interventions is apoptosis inhibition, which in a child with a cancer predisposition is the last thing anyone should do. The correction-versus-tolerance framing was too clean, and the report now says the two goals genuinely conflict by tissue and by timing.

## Q7. Methods published since 2024

**Nothing changes the measurement gate.** A sweep of work published since mid-2024 on single-cell detection of somatic mosaic aneuploidy and on long-read phasing returned no method that supersedes the gate's instruments. The relevant confirmation is negative in the useful sense: long-read haplotype phasing continues to be the clinical tool for resolving allelic configuration, which is exactly what gate item 1 already proposes for the 10.9 kb problem. Single-cell atlases of somatic mosaicism across tissues are appearing, but they are population resources rather than a diagnostic route for one child.

## Q11. The mitochondrial variants

**Partially answered, and the remainder does not matter.** Six of the 13 variants, at positions 263, 750, 1438, 4769, 8860 and 15326, are the near-universal differences from the reference sequence and are present in most people. Positions 302, 310, 16093, 16221 and 16519 are control-region variants in the hypervariable segments. None of the 13 is in the well-established pathogenic set for mitochondrial disease, which is where a heteroplasmic variant causing growth failure and low muscle mass would have to appear.

**What was not done:** formal haplogroup assignment, which needs PhyloTree or Haplogrep and was not reachable here. It is a ten-minute job for anyone with the tool. It is also not clinically consequential, because a haplogroup is an ancestry label and not a disease, and the question this angle was asked to answer, whether a mitochondrial disorder offers a second explanation for the phenotype, is already answered no by the absence of any pathogenic variant and by coverage of 1,700 to 5,200 reads that would have shown heteroplasmy of a few percent.

## Q15. Does splitting the corpus rescue the third model?

**No, and this corrects an earlier recommendation.** `vertex/REFUSAL_EXPERIMENT.md` concluded that splitting the corpus below the refusal threshold would let the numeric pass run, since the bundle is already 68 separate files. Tested directly on three files with the numeric prompt:

| File | Size | Result |
|---|---|---|
| `REPORT_track1.md` | 8,507 chars | Completed, 2,180 characters of output |
| `track2__creative__F_math.md` | 13,561 chars | Hit the output limit with no text returned; inconclusive |
| `track2__creative__D_compute.md` | 11,918 chars | **Refusal** |

The third result breaks the size story. A file of 11,918 characters refused while an earlier test on the first 12,399 characters of the mechanism dossier completed. **Size does not predict the outcome**, so there is no threshold to split below, and the workaround is not reliable. Fable 5.1 cannot be used as a third checker on this corpus by this route.

That leaves the cross-model check at two models rather than three, which is what the report already records.

---

## Corrections applied

Gate item 6 gains the direct cardiac phenotyping. Section 7's chaperone exclusion keeps its conclusion and replaces its reason. `vertex/REFUSAL_EXPERIMENT.md` withdraws the splitting recommendation as untested-and-now-tested-negative.
