# What was sent where, and the rule it was tested against

Written so that a judge, or Sage Bionetworks' Privacy and Compliance Office, can check this without reading the code.

## The rules that bear on it

- "You will not release or otherwise grant data access to anyone, and you will establish appropriate safeguards to prevent unauthorized data use."
- "No data may be reshared through any channel."
- "All data must be deleted within 30 days of Hackathon close from all environments (local machines, cloud instances, notebooks, private repos, and any intermediate or derived datasets)."
- "Participants are free to publicly share their code, models, and derived outputs at any time."

## What never left this machine

**The supplied genomic data.** `WGS_EX2312012_HGWCNDSX7.vcf.gz`, 315 MB, and its index. Never uploaded, never sent to any model, never copied to any server. Every genomic computation in this project ran locally.

**The raw sequencing reads.** Never downloaded.

## What was sent, to whom, and in what form

| Recipient | What | Form |
|---|---|---|
| Anthropic, Claude Code on a Max plan | The working session itself: this project's own analysis, code and prose | Model-improvement sharing disabled, no output rating |
| OpenAI API, GPT-5 | 68 of this project's own documents | De-identified before transmission |
| Google Vertex AI, Gemini 3.1 Pro, run on the author's own server | The same 68 documents | De-identified before transmission |
| Anthropic API, Fable 5.1 | Four files: the supplied phenotype document, and three of this project's own derived summaries | De-identified before transmission |

**The de-identification.** `vertex/redact.py` replaces variant coordinates, protein changes, sample and proband identifiers, HPO identifiers and the named clinical features with stable tokens. 331 substitutions across 68 files, counts recorded in `vertex/redaction_report.json`, output checked afterwards for leaks. The substitution mapping is kept locally and was not sent.

## The reasoning, and the one item that is a judgement call

**The 68 documents are derived outputs.** They are this project's own writing about the data, not the data. The rules state that participants "are free to publicly share their code, models, and derived outputs at any time", so transmitting them to a contracted processor is permitted by a rule that permits publishing them outright.

**The phenotype document is not a derived output, and that is the judgement call.** It is supplied material. It was sent to the Anthropic API in redacted form, with the HPO identifiers, the tumour type, the renal finding, the gestation and the growth term all tokenised. What remained was an unlabelled clinical summary with no identifiers of any kind.

The position taken here is that this is processing under a no-training arrangement rather than release or resharing, and that it is materially different from granting a person or an organisation access to the dataset. **It is recorded here rather than left implicit, because it is the closest this project came to a line, and the author should be the one to decide whether it needs declaring to the organisers.**

## Environments to clear at deletion

- This machine: `data/`, `work/`, and the scratch directories under `/private/tmp/claude-501/`.
- The author's own server at `/root/mva_check/`, which holds the de-identified bundle and the Gemini outputs.
- `vertex/bundle/`, `vertex/pkg/` and `vertex/out/` in this repository, which hold de-identified derived documents rather than data, and are listed here so the deletion is complete rather than partial.

Deletion confirmation goes to **RarediseaserealkidMVAhackathon2026@synapse.org**.
