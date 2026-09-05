# MVA Hackathon 2026 (henkvaness)

Two tracks for one child with mosaic variegated aneuploidy caused by biallelic *BUB1B* variants.

## Track 1: variant identification

`pipeline/run.sh data/<sample>.vcf.gz work/` runs in 61 seconds and produces the ranked CSV, the evidence and the figures. Steps: header facts; consequences and ClinVar for the known MVA genes, annotated offline; gnomAD v4.1 frequencies by HTTP range read of public sites files; a genome-wide recessive scan with no gene list; a mosaic aneuploidy profile computed from the VCF's own allele depths; an ACMG SF v3.2 secondary-findings screen; CSV construction by a written rule; and a rehearsal against the challenge's own scorer before upload.

Result: *BUB1B* c.2210T>G p.Leu737Ter with c.3006T>G p.Asn1002Lys. Scored 100.0 rank points, F-max 1.000. Model 2 confirms the pair ranks first genome-wide under phenotype-driven prioritisation with no gene list (`pipeline/exomiser_analysis.yml`).

Report: `REPORT_track1.md`. Submission: `submissions/`.

## Track 2: drug repurposing

Report: `REPORT_track2.md`. The short version: no approved medicine acts on BubR1, so what survives evidence is a drug-avoidance rule with a carve-out protecting cancer treatment, four no-cost surveillance additions, a renal work-up before any renal drug, and a measurement gate. Two attractive candidates were removed by verification and refereeing rather than by opinion.

How it was produced, in `track2/`:

| Directory | Contents |
|---|---|
| `research/` | Five cited dossiers: mechanism and models, clinical care and drug landscape, family perspective, variant context, genome-wide ranking |
| `creative/` | Ten divergent lenses (allele-directed pharmacology, consequences and tissue, analogies and trial design, two computational, mathematics, open-source investigation, clinical nutrition, dispensing pharmacy, lateral reframing) |
| `panel/` | Team 1, five specialists, two rounds plus synthesis, the integrated moderator record, and the final objection round from all seats |
| `panel2/` | Team 2, eight specialists, blind to team 1, two rounds |
| `verify/` | Three primary-source verification passes, including the supplementary-material lookups that settled two arguments |
| `referees/` | Three independent referee reports, written without access to the working files |

The verification and referee passes changed the output. What they caught is listed in section 13 of the Track 2 report, including an incorrect survival figure inside a safety clause and a supporting allele that turned out to be a splice variant rather than a nonsense variant.

## Reusable tooling

- `pipeline/` Track 1 end to end, plus the mosaic aneuploidy profiler, which reads whole-chromosome allele balance and depth from a standard germline VCF with a stated detection limit.
- `pipeline/track2_drugmap/` gene and mechanism to ranked approved drugs, with an openFDA label harm screen. Config-driven, so it transfers to another gene. Its own top-ranked hit was the wrong direction, which is documented rather than hidden.
- `pipeline/track2_compute/` and `pipeline/track2_math/` offline variant computation and the quantitative appendix.
- `scoring/score_local.py` rehearses a Track 1 CSV against the challenge's scorer offline.

## Data handling

No patient data is committed. `data/` and `work/` are gitignored; the only proband-derived content in this repository is the two submitted variant coordinates, per-chromosome aggregate figures and the reports. Annotation ran offline; public resources were read as static files rather than queried with patient coordinates. All data will be deleted within 30 days of the hackathon close and the deletion confirmed by email, per the rules.

Generative AI, stated in full because three vendors were used and an earlier version of this line named only one:

- **Anthropic, Claude Code on a Max plan**, model-improvement sharing disabled, no output rating. This did all of the analysis, computation and writing.
- **Anthropic API, Fable 5.1.** Cross-model checking and an external read of this project's own derived files.
- **OpenAI API, GPT-5**, and **Google Vertex AI, Gemini 3.1 Pro** (run on the author's own server). Four neutral prompts each, for cross-model checking only. Neither contributed content; both are used as checks and their outputs are in `vertex/out/`.

**What was sent, and what was not.** No patient data left this machine. The whole-genome VCF was never sent to any model. What was sent to the second, third and fourth of the above is a de-identified corpus of this project's own documents: variant coordinates, protein changes, sample and proband identifiers, HPO identifiers and the named clinical features were replaced with stable tokens before transmission, 331 substitutions across 68 files, leak-checked afterwards, with the substitution counts recorded in `vertex/redaction_report.json` and the script at `vertex/redact.py`. The mapping is kept locally and is not sent.

## Acknowledgement

Required by the Hackathon rules, reproduced verbatim:

> "This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible."

The dataset is to be cited using the reference given on the Hackathon Synapse page at the time of publication.

## Licence and data handling

This submission is released under **CC-BY**, per the Hackathon rules.

No patient data is committed to this repository. `data/` and `work/` are gitignored. The only proband-derived content here is the two submitted variant coordinates, per-chromosome aggregate figures, and the reports.

**Deletion commitment.** All data will be deleted within 30 days of Hackathon close from every environment used, which for this project means the local machine, the author's own server, and the scratch directories listed in `track2/anomalies/COMPLIANCE.md`. Deletion will be confirmed by email to **RarediseaserealkidMVAhackathon2026@synapse.org**, the address given in the official rules.

**No recontact.** No approach has been made, or will be made, to the data subject, the family, or any contact at the MVA Society. Where this project's outputs name a next step that would ordinarily involve the family, it is written for the treating team to consider rather than as an approach to be made.

What was sent to third-party model providers, and what was not, is set out in `track2/anomalies/COMPLIANCE.md`.

Requirements: bcftools/htslib 1.24 with libcurl, Python 3.11 with pysam, matplotlib, openpyxl. Reference data downloads on first run.
