# Anomaly analysis

Run under `track2/audit/PROMPT_D_anomaly.md`, over the whole-genome VCF, the clinical phenotype document and the dataset documentation. Expectations were stated before each measurement and are recorded here whether or not the measurement matched them.

---

## Departures

### D1. The phenotype document dates the renal finding to birth; both causes under consideration are postnatal

**Expectation, and its source.** Every clinical feature has a cause that could have operated before the feature was observed. The report offers two causes for the nephrocalcinosis: nephrocalcinosis of prematurity, from neonatal furosemide and parenteral nutrition, and ifosfamide proximal tubulopathy from the rhabdomyosarcoma treatment.

**Measurement.** The phenotype document states: "Nephrocalcinosis · HP:0000121 · Calcium deposits in kidney tissue; **present since birth**". Nephrocalcinosis of prematurity develops over weeks of neonatal intensive care, as a consequence of the treatment a 32-week, one-kilogram infant receives. Ifosfamide followed the rhabdomyosarcoma diagnosis, years later. The strings "since birth", "at birth", "antenatal" and "in utero" occur zero times in `REPORT_track2.md`.

**A second, independent measurement points the same way.** The project's own dossier records: "Targeted searching retrieved no published report of nephrocalcinosis as a recognised MVA feature" (`track2/research/02_clinical_care_drugs.md`). So the single feature the syndrome does not account for is also the one whose stated timing excludes both offered causes.

**Class: UNDECIDABLE.** Two readings remain and the data held cannot separate them. Either the document's wording is loose and means documented during the neonatal period, leaving the report's branch intact; or it is literal, and a congenital cause has not been considered, in which case the thiazide-versus-alkali algorithm is being applied to the wrong differential.

**Data that would decide it.** The date of the first renal imaging showing nephrocalcinosis, and whether any antenatal scan showed it. Cost: one line in an existing records request.

### D2. Four of the eight supplied phenotype features are never named in the report

**Expectation, and its source.** A report whose stated purpose is to address this child's phenotype refers to the features it was given.

**Measurement.** Counts of each term and its synonyms in `REPORT_track2.md`:

| Supplied feature | HPO | Occurrences in the report |
|---|---|---|
| Premature birth, 32 weeks | HP:0001622 | **0** as a feature of this child. All six occurrences of "prematur" are "premature stop codon", "premature chromatid separation", or "nephrocalcinosis of prematurity" |
| Small for gestational age, about 1 kg | HP:0001518 | **0**. "birth weight", "gestation", "IUGR", "growth restriction" all zero |
| Short stature | HP:0004322 | **0**. "stature" zero, "growth failure" zero |
| Failure to thrive | HP:0001508 | **0**. "thrive" zero |
| Skeletal muscle atrophy | HP:0003202 | Present only as "low muscle mass" in a creatinine-dosing sentence |
| Rhabdomyosarcoma | HP:0002859 | 11 |
| Nephrocalcinosis | HP:0000121 | 5 |
| Recurrent spontaneous abortion | HP:0200067 | "miscarriage" zero; "pregnancy loss" twice, both about published cohorts rather than this family |

The report does address the growth and nutrition axis functionally, through mid-upper-arm circumference, lean mass index, cyproheptadine and the endocrine gate. It does so without anchoring any of it to the supplied observations.

**Class: UNEXPLAINED.** No technical or biological cause applies. It is an omission, and it is systematic rather than incidental: the omitted features are exactly the growth and perinatal cluster.

**What would resolve it.** An edit, not a measurement. The most quantitative feature in the whole document, one kilogram at 32 weeks, sits below the third centile for gestational age against a median near 1.8 kg, and is the earliest measurable manifestation of the syndrome, preceding the tumour and the renal finding.

### D3. The metrics reported earlier were computed over a mixture of passing and failing calls

**Expectation.** Sample-level quality metrics are computed over records that passed filtering.

**Measurement.** The file is not PASS-only. It carries 4,740,790 PASS records and roughly 155,000 that fail one or more of six declared filters, dominated by MQ40 at 177,522 filter applications. An earlier pass in this project computed the heterozygous ratio and the transition-to-transversion ratio over all records without restriction.

**Class: UNEXPLAINED**, as a fault in this project's own method rather than in the data. Recomputed over PASS autosomal records only: heterozygous to homozygous-alternate 1.62 against an expectation of 1.5 to 2.0, and transition to transversion 2.028 against an expectation of 2.0 to 2.1. **Both sit inside expectation, and the uncorrected figures of 1.57 and 1.968 sat just outside on one measure.** The conclusion does not change; the method did.

---

## Departures classified and closed

### D4. Allele balance has a low tail 7 times heavier than its high tail

**Expectation.** Under reference bias the low tail exceeds the high tail modestly. Contamination produces a genome-wide excess; mapping artefact produces a regional one.

**Measurement.** Of heterozygous calls at depth 20 or more: 4.34 percent below allele balance 0.25, against 0.62 percent above 0.75. Localised, 43 percent of the low tail sits in fifteen 5 Mb bins, every one centromeric or acrocentric.

**Class: ARTEFACT.** Regional, not global, which is the discriminator. Supported by D3's normal global metrics.

### D5. A residual low-allele-balance signal at two immune loci

**Expectation.** After removing repeat regions and requiring genotype quality 90 and depth 30, a residual low tail should be flat unless a somatic process is operating.

**Measurement.** 17,318 calls survive, concentrated at chr6:32 Mb (794 calls), chr7:142 Mb (718), chr22:22 Mb (287) and segmental duplication blocks.

**Class: EXPECTED.** chr7:142 Mb is the T-cell receptor beta locus and chr22:22 Mb the immunoglobulin lambda locus, both of which undergo somatic recombination in lymphocytes; the sample is blood. chr6:32 Mb is the major histocompatibility complex, the most polymorphic region of the genome.

**Detection capability: this is the positive control for the allele-balance scan.** It recovers a somatic process known to be present, so the absence of focal signal elsewhere carries weight.

### D6. Chromosome Y at 73x mean depth against 42.7x autosomal

**Expectation.** One Y in a male gives about half the autosomal depth.

**Measurement by region.** The male-specific single-copy region, 3 to 22 Mb, runs at median 17 to 21, which is half of autosomal. The excess comes from three blocks: Y 10 to 11 Mb, Y 26 Mb, and Y 56 Mb at median 138 with 94 percent of calls heterozygous. Pseudoautosomal Y 2 Mb shows 21 percent heterozygosity as expected.

**Class: ARTEFACT.** A mean across repeat blocks. The genome is a normal male genome.

### D7. Regions with no calls

**Expectation.** At a mean spacing near 600 bp, a gap of 150 kb is roughly 250 times the mean and should not occur outside assembly gaps and heterochromatin.

**Measurement.** 33 such gaps, 59.7 Mb in total. Every one of the twenty largest is a known heterochromatic block or centromere: 1q12, 9q12, 16q11, the acrocentric short arms of 13, 14, 21 and 22, and the centromeres of 2, 5, 17 and 19.

**Class: ARTEFACT.** No evidence of a large homozygous deletion.

### D8. Sustained low-depth runs at 100 kb resolution

**Expectation.** A focal deletion gives a run of windows below half the genome median with calls retained.

**Measurement.** 500 windows of 26,133 fall below half the median of 43. Forty runs of three or more consecutive windows. Every run is centromeric, pericentromeric, or in a named segmental duplication block: chr5:70.1 to 71.3 Mb spans the SMN1 and SMN2 locus, chr15:21.7 to 22.2 Mb the proximal 15q11 duplication region, chr22:18.5 to 18.8 Mb the 22q11 low-copy repeats, chr1:0.5 to 0.8 Mb subtelomeric, and the chromosome 9 entries the 9q12 heterochromatin.

**Class: ARTEFACT**, with a stated blind spot. Those same regions are where recurrent microdeletions occur, including 22q11.2 and 15q11-q13, and this method cannot see into them. A deletion there would be invisible to every scan run in this project.

### D9. Phase field structure

**Expectation.** Read-backed phasing links variants sharing a sequencing fragment, so a few hundred base pairs.

**Measurement.** 290,389 phase sets over 641,174 variants. Median span 7 bp, ninetieth percentile 26 bp, **maximum 288 bp**, and zero sets exceed 5 kb. The longest sets cluster in the major histocompatibility complex, where variant density is highest.

**Class: EXPECTED.** This quantifies a claim made elsewhere in the project: the two *BUB1B* variants sit 10.9 kb apart, which is 38 times the longest phase set anywhere in this genome. The failure to phase them is not a marginal miss.

### D10. Mitochondrial contig

**Expectation.** A pathogenic heteroplasmy causing a growth or muscle phenotype would appear at a detectable minor fraction against depth of 1,700 to 5,200 reads.

**Measurement.** Thirteen variants, all at or near homoplasmy. Highest minor fraction 2.1 percent, at position 16093 in the hypervariable control region. Six of the thirteen are the near-universal differences from the reference sequence.

**Class: EXPECTED.** Common background. **Detection capability: adequate**, since the depth would have shown heteroplasmy of a few percent.

---

## Scans run, with detection capability

| Scan | Expectation stated first | Result | Would it have detected a departure |
|---|---|---|---|
| Sample metrics, PASS only | het/hom 1.5-2.0; Ti/Tv 2.0-2.1 | 1.62; 2.028 | Yes. Both metrics move measurably under contamination |
| Allele balance tails | low tail modestly exceeds high | 7-fold, regional | Yes. Positive control D5 |
| Depth outliers, 1 Mb and 100 kb | window medians track 43 | outliers all repeat-associated | Partly. Blind inside segmental duplications, D8 |
| No-call regions, 150 kb | none outside assembly gaps | 33, all heterochromatic | Yes for large deletions outside repeats |
| Sex chromosome dosage by region | Y at half autosomal | confirmed, D6 | Yes |
| Filters and declared fields | — | six filters used; 17 INFO, 7 FORMAT fields | Yes, found D3 |
| Phase field structure | sets of a few hundred bp | max 288 bp | Yes |
| Mitochondrial contig | no heteroplasmy above a few percent | max 2.1 percent | Yes |
| Contigs unused by any analysis | — | 78,917 PASS calls on 1,582 non-primary contigs, 1.66 percent, never examined | No. Not examined, recorded as a scope limit |
| Cross-source phenotype consistency | every feature addressed, every cause able to operate by the stated time | found D1 and D2 | Yes |

---

## Unexplained, ordered by what resolution would change

1. **D1, the renal timing.** Resolving it decides which branch of the renal algorithm applies, and those branches carry opposite prescriptions. Cost: the date of the first renal ultrasound, one line in a records request already being made.
2. **D2, the unnamed features.** Resolving it anchors the nutrition arm and the endocrine gate to the observations that motivate them. Cost: an edit.
3. **D3, metrics over a mixture.** Already resolved by recomputation. The corrected figures are in the table above.

## Scope limits of this pass

The 78,917 PASS calls on unplaced and alternate contigs were not examined. Regions inside segmental duplications, including the two commonest recurrent microdeletion loci, are not visible to any depth or allele-balance method applied here. Structural variants are not callable from a single-sample SNV and indel VCF. The raw reads were not downloaded.
