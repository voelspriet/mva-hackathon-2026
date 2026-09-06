# Why the Anthropic pass returned nothing, tested rather than assumed

The first cross-model run recorded that Fable 5.1 "refused the corpus twice". That was a guess from an empty output. This is the measurement.

## The failure is real and it is a refusal

`stop_reason: refusal`, an empty `content` array, zero output tokens, and the input still billed. It reproduces on a single file, so it was never a context-length problem: `REPORT_track2.md` alone, 28,338 input tokens, refuses exactly as the full 390,000-token corpus did.

## The proposed fix does not work

The hypothesis was that the model lacked provenance: it saw what looks like an individual child's clinical dossier with no explanation. `archive/vertex/PREAMBLE.md` supplies it, truthfully and from the challenge's own dataset card: who runs the hackathon, that the family consented to share their data to advance rare disease research, that the corpus is the participant's own working documents rather than clinical records, that 331 substitutions across 68 files removed the variant coordinates and every identifier, and that the request is a consistency check on the participant's own writing with no clinical advice sought.

**It changes nothing.** With the preamble prepended, the same file returns `stop_reason: refusal` and zero output.

## What does change the outcome

| Input | Size | Result |
|---|---|---|
| `REPORT_track1.md` | 8,988 chars | Answers, 3,355 chars |
| `track2__creative__F_math.md` | 14,041 chars | Answers, 904 chars |
| `track2__creative__I_pharmacist.md`, drug formulations and paediatric dosing | 14,830 chars | Answers, 867 chars |
| `track2__research__01_mechanism_models.md`, first 12,000 chars | 12,399 chars | Answers, 1,876 chars |
| `track2__research__01_mechanism_models.md`, first 24,000 chars | 24,368 chars | **Refusal**, after emitting 577 chars |
| `track2__research__01_mechanism_models.md`, last 24,000 chars | 24,332 chars | **Refusal**, 0 chars |
| `track2__research__01_mechanism_models.md`, whole | 48,293 chars | **Refusal**, 0 chars |
| `REPORT_track2.md` | 77,900 chars | **Refusal**, 0 chars |
| Three benign files concatenated | 40,193 chars | Hit `max_tokens` with no text; inconclusive |

Three things follow, and the third is the interesting one.

1. **It is not size.** Forty thousand characters of one kind of content passes; twenty-four thousand of another refuses.
2. **It is not the drug content.** The pharmacist file, which is nothing but formulations, licensed status and paediatric dosing, answers without difficulty.
3. **It is a threshold within one document.** The first 12,000 characters of the mechanism dossier answer. The first 24,000 refuse. So do the last 24,000. The same material passes in a small enough piece and fails in a larger one, and one run began answering and then stopped, which is a mid-generation refusal rather than a pre-generation block.

## Inference, labelled as such

The trigger looks like the accumulated density of individualised therapeutic reasoning about one identifiable patient, not any single sentence. A short excerpt reads as discussion of published literature. Enough of it in one request reads as a treatment plan written for a specific child, which is a thing a model is right to be careful about. That the preamble does not shift it suggests the judgement is made on what the text does rather than on what the request says about it.

Worth noting the asymmetry: the same model does this work without hesitation inside an agent session, where it has the full history of how the document came to exist. The API call has only the document.

## What to do instead

Split the corpus into pieces below the threshold, which costs nothing since it is already 68 separate files, most of them under 20,000 characters. The numeric recomputation pass works per file and loses nothing. The contradiction pass is the one that genuinely needs the whole corpus at once, and that is the one this model cannot be used for. That is a real limitation on the method, not a workaround to be applauded.

**Tested, and the workaround fails.** Running the numeric prompt on three files: `REPORT_track1.md` at 8,507 chars completed with 2,180 characters of output; `F_math.md` at 13,561 chars hit the output limit returning no text, inconclusive; and `D_compute.md` at **11,918 chars refused**, while an earlier test on the first 12,399 characters of the mechanism dossier had completed. **Size does not predict the outcome**, so there is no threshold to split below and the recommendation above is withdrawn. This model cannot be used as a third checker on this corpus by this route, and the cross-model check stands at two models.
