# Prompt: find additions that are relevant, by auditing what the submission assumes

The previous prompt (`PROMPT_2000_observations.md`) optimised for coverage and got what it asked for: 2,013 lines, of which 1,372 were never examined and most of the rest were artefacts. Exhaustive enumeration answers "what is in the data". It cannot answer "what matters", because relevance is not a property of the data. It is a property of the gap between what a document claims and what it has measured.

This prompt searches that gap instead.

## The relevance test

Nothing may be written up unless it does one of four things. State which, in the first line of the entry.

1. **Closes an alternative explanation** for a conclusion the submission already draws.
2. **Converts an assertion into a measurement**, where the submission currently relies on plausibility, convention or a cited norm.
3. **Bounds what cannot be known**, with the number attached, so a limitation stops being an apology and becomes a result.
4. **Transfers**: a method or a negative result that changes what a different team would do on a different patient.

An item that does none of these is a curiosity. Curiosities go in the screening file, not in the report.

## Procedure

### Step 1. Extract every load-bearing claim

Read `REPORT_track1.md`, `REPORT_track2.md`, `submissions/henkvaness_track1_methods_model1.xlsx` and `SUBMISSION_track2.md`. A load-bearing claim is any sentence that, if false, would change a conclusion or a recommendation. Ignore descriptive sentences.

For each, record it verbatim with its file and line.

### Step 2. Classify each claim by what stands behind it

| Class | Meaning |
|---|---|
| `measured` | a number computed from the supplied data, reproducible from files in this repository |
| `cited` | taken from a database or the literature, with the source recorded |
| `conventional` | true by common practice or by definition, needing no evidence |
| **`assumed`** | none of the above |

**The `assumed` list is the work.** Everything else is already accounted for.

### Step 3. For each assumed claim, ask three questions in order

1. **Can it be measured with data already in hand?** The supplied VCF, the alignment in `/root/mva/bam/all.bam`, the coverage windows, gnomAD's public API, ClinVar, Ensembl. If yes, measure it and record the result whether or not it supports the claim.
2. **If not, can it be bounded?** A limit is a result. "Not detectable below 2% of cells" is worth more than silence.
3. **If neither, say so in the report** and name what would be needed. Parental genotypes, long reads, cultured lymphocytes, a tumour sample. An honest gap with a named remedy is a contribution; an unexamined gap is a liability.

### Step 4. Attack the submission on purpose

Write down the three strongest objections a hostile reviewer would raise, in their words, not ours. For each:

- Is it already answered somewhere in the repository? Give the file.
- If not, can it be answered with data in hand? Answer it.
- If it cannot be answered, put it in the limitations section **before** the reviewer finds it.

Anticipating an objection is worth more than the objection being wrong.

### Step 5. Check what a competitor would do differently

The scoring rewards innovation and scalability. For each method used, state in one line what the conventional alternative is and why this was chosen. If the conventional alternative is better, say so and use it. If the choice was made for expedience rather than merit, say that too; a defended shortcut reads better than an undefended one.

## Constraints

- **Every number must be reproducible** from the files in this repository by someone who has the same data. Record the command or the script alongside the result.
- **Measure before writing.** No entry may be drafted and then verified; the verification produces the entry.
- **Record disconfirming results with the same prominence as confirming ones.** A measurement that undermines a claim in the submission is the most valuable output this procedure can produce, and burying it is the failure mode that matters.
- **No claims about other people's practice.** Every count describes this analysis. Whether a technique is unusual elsewhere requires literature this project has not read.
- **Cite the internal record.** Every entry names the file it lives in, so a reader can check it without asking.

## Expected yield, stated in advance so the result can be judged

If the submission is well built, this procedure should find **fewer than twenty** assumed claims, of which perhaps half are measurable. That would be a good outcome and a short document.

If it finds sixty, the submission was resting on assertion more than its authors believed, which is also a good outcome and a longer document.

**A yield of zero means the audit was not performed properly.** Every document of this length rests on something unmeasured. If nothing was found, look again at the sentences that felt too obvious to check.
