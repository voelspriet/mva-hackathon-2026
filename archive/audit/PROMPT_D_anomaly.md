# Prompt D: anomaly analysis

## Purpose

Claims already stated are checked elsewhere. Specific questions of the primary data are asked elsewhere. This pass examines the supplied material for deviations that no question was framed to detect.

## Definition

An anomaly is a measurement that differs from what the supplied data itself predicts. Three forms:

1. Two statements in the supplied material that cannot both be true.
2. A value distant from what the remainder of the same data implies, where the implied value can be stated in advance.
3. An absence at a location where the data's own density implies presence.

Excluded by this definition: a finding that is unexpected to the reader but common in the population; a value that departs only from an expectation imported from outside the supplied material; a measurement whose result would be the same whether or not the thing it tests is true.

## Data in scope

1. The whole-genome VCF: genotypes, allele depths, total depths, genotype qualities, quality scores, filter fields, phase fields, the contig set, and the header's declared fields.
2. The clinical phenotype document: every term, every note attached to a term, and every statement of timing, sequence or family history.
3. The dataset documentation and the stated terms of use.
4. Outputs already derived from the above, and the files that summarise them.

## Method

### Order of operations

State the expected value or distribution, and what would constitute a departure from it, before taking the measurement. Record where the expectation comes from. An expectation recorded after the measurement is not used.

### Classification

Assign each departure to one class, with the evidence for that class:

- **ARTEFACT.** Attributable to a stated technical cause. Evidence takes the form of showing the departure is confined to the conditions under which that cause operates.
- **EXPECTED.** Attributable to a stated property of the sample, the tissue, the individual or the population.
- **UNEXPLAINED.** Neither of the above applies after both were tested.
- **UNDECIDABLE.** Separating the above requires data not held. Name the data.

A departure recorded without a class is not reported.

### Detection capability

For each scan, state whether a departure of the kind sought would have been detected had one been present, and on what basis. Where a positive control exists in the data, name it. Where none exists, the negative result is recorded as uninformative rather than as clean.

### Cross-source consistency

Compare statements across the supplied sources against each other and against the mechanisms assumed for them elsewhere. Include any stated timing, sequence, or order of events. Where sources disagree, record the disagreement rather than selecting between them.

## Scans

Each requires its expectation stated first. The list is neither ordered nor exhaustive.

- Sample-level metrics with published reference ranges: heterozygous to homozygous-alternate ratio, transition to transversion ratio, depth distribution. State which subset of records the metric is computed over.
- Allele balance across heterozygous calls, with each tail localised.
- Depth outliers, high and low, at more than one window size.
- Locations with no calls where local density implies calls.
- Sex chromosome dosage and heterozygosity, by region.
- Genotype quality, quality score and filter behaviour, including which declared filters are used and at what rate.
- Phase field structure: count, span, and what is and is not phased.
- The mitochondrial contig, including minor allele fraction against depth.
- Any contig, field, record class or filter value present in the file that no analysis has used.

## Output

`track2/anomalies/ANOMALIES.md`:

- One section per departure: the expectation, its source, the measurement, the class assigned, and the evidence for that class.
- A table of every scan run, its expectation, its result, and its detection capability.
- A list of the departures classified UNEXPLAINED, each with the measurement that would resolve it and the cost of that measurement.

## Constraints

Computed results are labelled computed and reproduce from a script saved under `pipeline/`. Inference is labelled inference. An expectation that the measurement contradicted is recorded as stated, not revised. Nothing is proposed that requires contact with the family or the organisers. Patient data does not leave the machine; public resources are read as static files and are not queried with patient coordinates. No em or en dashes. No adjectives of praise or alarm. No statement of which scan is expected to yield more than another.
