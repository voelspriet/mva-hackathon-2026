# MVA Hackathon 2026 (henkvaness)

One child, a whole-genome VCF and eight clinical features. Two tracks: name the cause, then say what could be done about it.

## Results

**Track 1.** The cause is two changes in *BUB1B*, c.2210T>G p.Leu737Ter and c.3006T>G p.Asn1002Lys, compound heterozygous. Scored 100.0 rank points, F-max 1.000, on the challenge scorer. The same pair ranks first genome-wide under phenotype-driven prioritisation with no gene list. Report: `REPORT_track1.md`.

**Track 2.** No approved medicine acts on BubR1, and this project found no treatment. What it produced instead: four additions to existing surveillance that add no visit, a renal work-up before any renal drug, the measurements that would show whether any gene-directed idea has a target in this child at all, and a prescribing question the report labels a hypothesis. Two candidates that looked good were removed by verification against primary sources. Report: `REPORT_track2.md`. One page for a clinician: `FAMILY_CARD.md`.

**Measured on the child's own genome.** Sixteen re-analyses in `track2/reanalysis/`, summarised in `track2/reanalysis/SUMMARY.md`. Each states its scope.

| Question | Result |
|---|---|
| Every pathogenic position in ClinVar, no gene list | 7 heterozygous hits, nothing homozygous, no gene hit twice |
| Does any other gene look like *BUB1B*? | No. Zero competing recessive diagnoses |
| Is any protein truncated? | Only the known causal allele |
| The drug-handling genes | Two genotypes recorded, neither acted on |
| 49 renal and tubular genes | Nothing pathogenic, no truncating variant |
| The X chromosome, in a male | No hemizygous loss of function |
| The mitochondrial genome | None of 78 pathogenic ClinVar records carried |
| The introns of the causal gene | One novel deep intronic allele, recorded, not built on |
| Which population the frequency claims apply to | West Eurasian. Both causal alleles European-private |
| Mosaic aneuploidy, by depth rather than allele fraction | One copy of each sex chromosome. No mosaic loss of Y |
| Is the causal gene well covered? | Yes, 42.3 against a control median of 41.9 |

Three of these corrected the report. One corrected the family card. Two contained faults of this project's own making, recorded in the files.

## Where things are

| | |
|---|---|
| `REPORT_track1.md`, `REPORT_track2.md` | The two reports |
| `FAMILY_CARD.md` | One page for any prescriber, graded by evidence strength, protection clause first |
| `pipeline/` | Track 1 end to end, the mosaic profiler, the gnomAD byte-range reader, the genome-wide screens, the drug mapper |
| `track2/reanalysis/` | The sixteen genome re-analyses, each with its script |
| `track2/research/`, `track2/gate/`, `track2/anomalies/` | The cited dossiers, the measurement gate, deviations found in the supplied data |
| `submissions/`, `video/`, `scoring/` | Submitted files, the pitch video with subtitles, and an offline rehearsal of the challenge scorer, which needs the organisers' own scorer modules placed beside it; see `scoring/README.md` |
| `archive/` | The working record: simulated panels, audit partitions, verification passes, referee reports, cross-model outputs, prompts. The reports cite it. Map: `archive/README.md` |

## Reproducing it

`pipeline/run.sh data/<sample>.vcf.gz work/` runs Track 1 in about a minute. Requirements: bcftools/htslib 1.24 with libcurl, Python 3.11 with pysam, matplotlib, openpyxl. Reference data downloads on first run.

## Data handling

No patient data is committed. `data/` and `work/` are gitignored; the only proband-derived content here is the two submitted variant coordinates, per-chromosome aggregate figures and the reports. Public resources were read as static files, never queried with patient coordinates. All data will be deleted within 30 days of the Hackathon close from every environment used, and the deletion confirmed by email to RarediseaserealkidMVAhackathon2026@synapse.org. No approach has been made, or will be made, to the family or to the MVA Society.

Generative AI, all three vendors named:

- **Anthropic, Claude Code on a Max plan**, model-improvement sharing disabled: all of the analysis, computation and writing.
- **Anthropic API, Fable 5.1**: cross-model checking and an external read of this project's derived files.
- **OpenAI API, GPT-5**, and **Google Vertex AI, Gemini 3.1 Pro** on the author's own server: four neutral prompts each, as checks only. Outputs in `archive/vertex/out/`.

The whole-genome VCF was never sent to any model. What the second, third and fourth received was a de-identified corpus of this project's own documents, with coordinates, protein changes, identifiers, HPO terms and named clinical features replaced by stable tokens before transmission: 331 substitutions across 68 files, leak-checked afterwards, counts in `archive/vertex/redaction_report.json`, script in `archive/vertex/redact.py`. The mapping is kept locally. Full statement: `track2/anomalies/COMPLIANCE.md`.

## Acknowledgement

Required by the Hackathon rules, reproduced verbatim:

> "This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible."

The dataset is to be cited using the reference given on the Hackathon Synapse page at the time of publication.

## Licence

CC-BY, per the Hackathon rules.
