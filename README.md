# MVA Hackathon 2026 (henkvaness)

Two tracks for one child with mosaic variegated aneuploidy caused by biallelic *BUB1B* variants.

## Track 1: variant identification

`pipeline/run.sh data/<sample>.vcf.gz work/` runs in 61 seconds and produces the ranked CSV, the evidence and the figures. Steps: header facts; consequences and ClinVar for the known MVA genes, annotated offline; gnomAD v4.1 frequencies by HTTP range read of public sites files; a genome-wide recessive scan with no gene list; a mosaic aneuploidy profile computed from the VCF's own allele depths; an ACMG SF v3.2 secondary-findings screen; CSV construction by a written rule; and a rehearsal against the challenge's own scorer before upload.

Result: *BUB1B* c.2210T>G p.Leu737Ter with c.3006T>G p.Asn1002Lys. Scored 100.0 rank points, F-max 1.000. Model 2 confirms the pair ranks first genome-wide under phenotype-driven prioritisation with no gene list (`pipeline/exomiser_analysis.yml`).

Report: `REPORT_track1.md`. Submission: `submissions/`.

## Track 2: drug repurposing

Report: `REPORT_track2.md`. The short version: no approved medicine acts on BubR1. What survives is not a treatment. It is four surveillance additions that add no visit and no cost, a renal work-up before any renal drug, a measurement gate, and a prescribing rule that the report labels a **hypothesis for follow-up** rather than an established finding, with a carve-out so it can never be read as a reason to change cancer treatment. Two attractive candidates were removed by verification and refereeing rather than by opinion.

Two later findings are the most directly usable and are in the lay summary. Cancer risk in this syndrome tracks how severely the mitotic checkpoint fails rather than the aneuploidy itself, and this child's gene is one of the two that break it, for which the source recommends close surveillance in those words; the same result makes the gate's mitotic-arrest measurement prognostic. Separately, the supplied phenotype dates the renal finding to birth while both causes the report considers are postnatal, so one date from the records decides between two opposite prescriptions.

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

## Method note: what the simulated panels were and were not

`SIMULATED_PANELS.md` states the lesson this project learned the hard way. Thirteen simulated specialist seats were good at two things, generating a candidate space no single line of reasoning would reach, and disagreeing with each other productively. They are not a source of evidence, and this project treated them as one when narrowing candidates.

The audit checked 577 claims the report asserts. It never checked what the report dropped, because an exclusion does not present itself as a claim. Checking the exclusions afterwards found five that do not survive, two of them contradicted by files already inside this repository. The rule that follows is to audit exclusions exactly as assertions are audited, and to put that audit after the narrowing rather than only after the writing.

## For the family, and for any doctor who prescribes

`FAMILY_CARD.md` is one page, written to be handed to a clinician who does not know this syndrome. It is graded by evidence strength, because an earlier draft was not and read as an instruction where the report has a hypothesis. Part 1 carries what is well established, and the reason there is the kidney finding rather than the syndrome: it is ordinary practice for any child with calcium deposits in the kidneys. Part 2 states the chromosome-separation question as an open question and says plainly that nobody has tested whether cells from a person with this syndrome are more sensitive, and that the two available lines of laboratory evidence point in opposite directions. Part 3 is three questions for the specialist team. The protection clause is in the first block. Every line is drawn from `REPORT_track2.md` and adds no new claim.

It exists because the most immediately useful thing this project produced for a family was buried inside a seventeen-thousand-word document written for specialists.

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
