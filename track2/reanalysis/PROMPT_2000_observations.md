# Prompt: enumerate 2,000 candidate observations from the MVA hackathon data

This is an instruction document, not a result. It defines a screening layer.

## What is being asked, and what is not

Produce **2,000 candidate observations**: statements about this genome that are computed from the data in hand, each carrying the number it rests on. A candidate observation is not a finding. It is a line an analyst could later confirm or dismiss.

Do not produce 2,000 findings. Two thousand verified findings do not exist in one genome and any list claiming otherwise is fabricated. The value of this exercise is coverage, not insight: it is a systematic sweep that leaves a record of what was looked at, including everything that turned out to be nothing.

## Neutrality requirements

These exist because the project already knows its answer, and a search run by someone who knows the answer stops early and looks in one place.

1. **Do not use the phenotype document.** No HPO terms, no clinical features, no disease names as input to the enumeration.
2. **Do not privilege the known candidate.** *BUB1B*, *CEP57* and *TRIP13* receive no special treatment, no separate section, and no earlier position in any ranking. If they appear, they appear because a rule put them there.
3. **Do not read the existing reports before enumerating.** Cross-check against `track2/reanalysis/` and `REPORT_track1.md` only after the list exists, and mark duplicates rather than deleting them; a duplicate independently reproduced is evidence, not waste.
4. **Enumerate before interpreting.** Rank, filter and comment in a separate pass. The first pass writes down what is there.

## Data available

| Source | Content | Status |
|---|---|---|
| `data/WGS_EX2312012_HGWCNDSX7.vcf.gz` | 4,895,706 variant records on the 24 primary units, one sample, GT/AD/DP/GQ/PGT/PID | supplied |
| `data/Challenge_Clinical_Phenotype_1.docx` | 8 HPO-coded features | supplied, **excluded by rule 1** |
| 8 FASTQ, 78.85 GB | raw reads, 4 lanes paired | supplied |
| `/root/mva/bam/all.bam` (server) | 1.059 billion aligned reads, median 51x, GRCh38 no-alt | derived today |
| `/root/mva/depth.regions.bed.gz` | 31,136 windows of 100 kb, mean coverage | derived today |
| `/root/mva/gc.pkl` | GC fraction per window | derived today |
| gnomAD v4.1 public API | allele frequencies | external, allowed, must be recorded per query |
| `work/` | ClinVar, Ensembl 116, coding subsets | derived earlier |

## What counts as one observation

Each line must have all five fields. A line missing any of them is not an observation and must not be written.

1. **Class** — which enumeration produced it (see below).
2. **Locus or scope** — chromosome and coordinates, or gene, or "genome-wide".
3. **Measurement** — the number, with its unit. Not "elevated" but "ratio 1.24".
4. **Comparator** — what the number is measured against: the genome median, the GC-matched median, a population frequency, an expectation. A number without a comparator is not an observation.
5. **Status** — one of: `raw` (enumerated, unexamined), `artefact-prone` (falls in a region or gene family known from this project's own measurements to produce false signal), `duplicate of Rn` (already recorded elsewhere in the project), `notable` (survives the obvious objections and is worth a human look).

Expect the overwhelming majority to end as `raw` or `artefact-prone`. That distribution is the honest outcome, and a list where many lines are `notable` is a list that has stopped being sceptical.

## Enumeration classes and target counts

These are chosen because each can be produced exhaustively by a rule, so the list is reproducible and nobody has to trust a judgement call about what was included.

| Class | Rule | Approximate yield |
|---|---|---|
| `coverage-window` | every 100 kb window deviating more than 3 SD from its GC-matched median, with its ratio | 600 |
| `coverage-run` | every run of 5 or more consecutive deviating windows, with extent and median ratio | 60 |
| `chromosome-dosage` | every chromosome, ratio before and after GC correction, window count, standard error, implied detection floor | 24 |
| `heterozygosity-window` | every 1 Mb window whose heterozygous fraction deviates from the autosomal distribution | 300 |
| `roh` | every run of homozygosity above 500 kb, with length and variant count | 100 |
| `gene-burden` | every gene carrying 2 or more coding variants absent from the common catalogue, with counts and consequences | 224 |
| `gene-frequency` | for every gene in the class above, the gnomAD frequency of each variant and the resulting minimum | 224 |
| `phase-set` | every gene whose variants share a phase set, with the cis or trans call | 151 |
| `clinvar` | every ClinVar pathogenic or likely pathogenic record present in this genome, with zygosity, depth, allele balance | 200 |
| `variant-quality` | every coding variant with allele balance outside 0.30 to 0.70, or GQ below 90, or strand skew beyond 0.75 | 150 |
| `spectrum` | each of the 96 trinucleotide contexts, its count and its share | 96 |
| `mitochondrial` | every chrM variant with its heteroplasmy fraction | 40 |
| `insert-size` | insert-size distribution per lane, and per-chromosome deviation from it | 30 |
| `mappability` | every window below 30 percent of median coverage, grouped into contiguous regions | 150 |
| **Total** | | **≈ 2,350, trimmed to 2,000** |

Any class that cannot be computed from the data listed above is dropped and recorded as dropped, with the reason. Do not substitute a guess for a computation.

## Output

A single file, `track2/reanalysis/OBSERVATIONS_2000.md`, containing:

- A header stating what the file is and, in the first paragraph, that it is a screening layer and not a list of findings.
- The count actually produced per class, against the target above.
- One table per class, one row per observation, five fields.
- A closing section listing every line marked `notable`, with the specific objection each would have to survive to become a finding.
- A statement of what the enumeration cannot see: structural variants below the resolution of coverage windows, balanced rearrangements, anything requiring parental data, and any mosaic event whose affected fraction falls below the floor recorded in the `chromosome-dosage` class.

## The failure mode to guard against

The temptation is to pad. A list of 2,000 is easy to reach by splitting one measurement into many lines, by including windows that are known artefacts without marking them, or by writing interpretations as though they were measurements. All three make the file longer and worthless.

If a class yields fewer rows than its target, write the smaller number and say so. A file of 1,400 honest lines is a contribution. A file of 2,000 padded ones is not, and it will be checked, because every number in it is reproducible from the data by anyone who has the same files.
