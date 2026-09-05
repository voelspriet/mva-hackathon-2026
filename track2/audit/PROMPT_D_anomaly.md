# Prompt D: anomaly analysis

## Purpose

The audit asks whether stated claims are true. The re-analysis asks specific questions of the primary data. Neither finds what nobody thought to ask about. This pass looks for what is odd, without a hypothesis, and reports what remains odd after the ordinary explanations have been tried.

## What counts as an anomaly

A measurement that differs from what the data itself predicts. Not a surprising fact, and not a gap in knowledge. Three kinds qualify:

1. **An internal contradiction.** Two things in the supplied material cannot both be true, or a stated fact is incompatible with a mechanism assumed elsewhere.
2. **A distributional outlier.** A value that sits far from what the rest of the same data implies, where the expected value can be written down in advance.
3. **A missing thing that should be present.** An absence where the data's own density predicts presence.

**Anything that fails this test is not an anomaly and is not reported**: an unexpected finding that is common in the population, a value that is unusual only against an assumption imported from outside, a result that would look identical whether or not the underlying claim were true.

## Data in scope

Everything the challenge supplied, and everything derived from it, treated as equally likely to hold the anomaly:

1. The whole-genome VCF: genotypes, allele depths, total depths, genotype qualities, quality scores, filter fields, phase sets, contig set.
2. **The clinical phenotype document.** It is data, not background. Every term, every note attached to a term, and every statement about timing or family history.
3. The dataset README and the challenge's stated terms.
4. Derived outputs already computed, and the reports and working files that summarise them.

## Method

### Expectation before measurement

For every scan, write the expected value or distribution **before** looking, and say what would count as a deviation. A scan whose expectation is written afterwards cannot detect anything, because any result confirms it. Where the expectation comes from the data itself, say which part.

### Triage every deviation into one of four

- **ARTEFACT.** Explained by a known technical cause: mapping into repeats, segmental duplication, reference bias, filter behaviour, an assembly gap. Give the evidence, usually that the deviation is confined to regions where that cause operates.
- **EXPECTED BIOLOGY.** Real, and predicted by something ordinary about the sample or the person. Somatic rearrangement in a blood sample, sex chromosome dosage, population polymorphism.
- **UNEXPLAINED.** Survives both. This is the output that matters.
- **UNDECIDABLE HERE.** Distinguishing the above would need data not held. Say which data.

An anomaly reported without this triage is noise. The commonest failure is calling an artefact a finding, and the second commonest is dismissing a real signal as an artefact without checking where it sits.

### Required positive control

At least one scan must recover something already known to be present, and the report must say which. A scan that finds nothing has told you nothing unless it has been shown capable of finding something. If no positive control can be constructed for a scan, its negative result is reported as uninformative rather than as clean.

### Cross-source consistency, run first

The highest-yield class is a fact in one supplied source that contradicts an assumption in another. Check at minimum:

- Every phenotype term against the mechanism the analysis assumes for it, **including timing**: when a feature is stated to have appeared, and whether every cause under consideration could have operated by then.
- Every statement about family history against what the genome shows and against what the analysis infers from it.
- Perinatal facts against the exposures any explanation requires.
- The derived outputs against the documents that summarise them, in both directions.

## Scans to run, as detectors rather than questions

Not a list to work through in order, and not exhaustive. Each needs its expectation written first.

- Global sample quality: heterozygous to homozygous ratio, transition to transversion ratio, depth distribution. These have published expected ranges and a sample that fails them invalidates everything downstream.
- Allele balance across all heterozygous calls, with the low and high tails localised. Contamination is global; mapping artefact is regional; somatic events are focal.
- Depth outliers, high and low, at several window sizes.
- Regions with no calls where the local density predicts calls.
- Sex chromosome dosage and heterozygosity by region, separating pseudoautosomal from male-specific sequence.
- Genotype quality and filter behaviour: calls that pass but should not, and classes of call that are systematically absent.
- Phase set structure: how many, how long, and whether any span something the analysis claims cannot be phased.
- The mitochondrial contig, including minor allele fractions against read depth.
- Any contig, field or record class present in the file that no analysis has used.

## Output

`track2/anomalies/ANOMALIES.md`, containing:

- One section per anomaly, each stating the expectation, the measurement, the triage class, and the evidence for that class.
- A table of everything scanned and found clean, with the positive control for each scan named, so that a later reader knows what was looked at and how well.
- A separate list of the UNEXPLAINED, ordered by what each would change if resolved, with the single cheapest measurement that would resolve it.

## Constraints

Computed results are labelled computed and reproduce from a saved script under `pipeline/`. Inference is labelled inference. An expectation that turned out to be wrong is reported as such rather than quietly revised. Nothing is proposed that requires contact with the family or the organisers. Patient data does not leave the machine; public resources are read as static files, never queried with patient coordinates. No em or en dashes. No adjectives of praise or alarm.
