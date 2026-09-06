# Index to the checking

Nineteen files record what was checked and what it changed. This is the map. Each row says what the file is, what it found, and what happened as a result.

Nothing here asks to be believed. Every file names its sources, its access level, and what it could not reach.

---

## The prompts the checking ran under

Five, none of which names a gene or a disease, so all five transfer.

| File | Asks for |
|---|---|
| `track2/audit/PROMPT_A_source_audit.md` | Every factual claim checked against the primary source it cites, with a verdict and a replacement sentence |
| `track2/audit/PROMPT_B_reanalysis.md` | The primary data re-examined for questions the project never asked |
| `track2/audit/PROMPT_C_synthesis.md` | What the project established, what it failed to establish, and what each review layer caught |
| `track2/audit/PROMPT_D_anomaly.md` | Deviations from what the data itself predicts, with the expectation stated before the measurement |
| `track2/audit/PROMPT_E_external_read.md` | An outside model asked for contradictions, open questions and unsupported statements |

---

## What each check found

### Claims against the literature

| File | Scope | Result |
|---|---|---|
| `track2/audit/AUDIT_a` … `AUDIT_fg` | Five partitions by source domain | **577 claims checked, 184 not supported.** 178 of those are table rows in the summary and 6 sit in partition prose; the rows split as 44 contradicted, 45 overstated, 42 with no source, 39 unverifiable, 8 misattributed |
| `track2/audit/AUDIT_SUMMARY.md` | All non-supported verdicts in one table | Generated from the partitions by `build_summary.py`, so it cannot drift from them |

### Claims against the supplied data

| File | Scope | Result |
|---|---|---|
| `track2/audit/DATA_CLAIM_CHECKS.md` | Every claim about the VCF, the phenotype document, or a retrievable database record | **13 numbers corrected, no conclusion changed.** Track 1 was 10 of 11 exact. Nine corrections came from one fault, a query run without the PASS filter, which matters because the excluded records concentrate in the regions the analyses were reasoning about |
| `track2/anomalies/ANOMALIES.md` | Deviations found without a prior hypothesis | The supplied phenotype dates the renal finding to birth while both causes the report considers are postnatal. One date from the records settles it |
| `track2/reanalysis/` | Ten questions the project had never asked of the genome | Six negatives: no readable phase, no runs of homozygosity of consequence, no copy-number event, no mitochondrial explanation, no modifier, and the mosaicism method's floor fails where mapping is poor. A seventh, added 6 September, drops the gene list entirely and screens the whole genome against the whole of ClinVar: seven heterozygous hits, nothing homozygous, no gene hit twice, so no second diagnosis. An eighth scans the drug-handling genes and finds two genotypes worth recording, neither worth acting on, alongside the finding that the irinotecan allele the family card promised could be looked up for free cannot be read from this file at all. A ninth asks whether the project's own rarity arguments used the right denominator, infers West Eurasian ancestry from 85 markers chosen without reference to the child, and finds every gnomAD copy of both causal alleles is European. A tenth scans 49 renal genes and the whole X of a male proband, finds nothing pathogenic in either, and narrows the report's sharpest open anomaly by excluding the congenital renal cause that would have dissolved it |

### The project's own reasoning

| File | Scope | Result |
|---|---|---|
| `track2/audit/EXCLUSION_AUDIT.md` | What the report **dropped**, which nothing else checked | **Five exclusions do not survive.** Two were contradicted by files already in this repository |
| `track2/synthesis/VERIFY_headline_claim.md` | This project's own headline methodological claim, attacked rather than confirmed | **Three of its four parts did not survive** and were withdrawn |
| `track2/synthesis/SYNTHESIS.md` | What was established, what was not, and what each review layer caught | Three referees with no access to the working files found errors thirteen briefed specialists missed |
| `track2/anomalies/EXTERNAL_READ_RESPONSE.md` | An outside model reading this project's own files | Nine errors identified, five checked the same day; the stated blind spot at the two commonest microdeletion loci was disproved and both are now positively excluded |

### The referees and the earlier passes

| File | Scope |
|---|---|
| `track2/referees/` | Three independent reports, written without access to the working files, all returning major revision |
| `track2/verify/` | Three primary-source verification passes, including the one that found an allele had been misunderstood for the project's whole life |
| `vertex/out/` | Two other model families over a de-identified corpus, four neutral prompts each. Their raw responses, not a summary of them |
| `vertex/REFUSAL_EXPERIMENT.md` | Why a third model could not be used, measured rather than assumed |

---

## What the checking changed

| | |
|---|---|
| Claims checked against primary sources | 577 |
| Not supported | 184 |
| Numbers corrected against the supplied data | 13 |
| Exclusions that did not survive | 5 |
| Parts of this project's own headline claim withdrawn | 3 of 4 |
| Candidates removed from the ranked list on evidence | 2 |

**Two of those rows are about this project's own errors rather than the literature's.** They are here because a submission that only reports what it got right is not reporting.

---

## What was not checked, and cannot be

Named plainly rather than left for a reader to discover.

- **No clinician has read the report.** Thirteen simulated seats and three simulated referees are not one real reader, and `SIMULATED_PANELS.md` sets out why that distinction matters.
- **Forty claims carry an unverifiable verdict**, almost all publisher-gated full text or supplementary material, with the routes already tried recorded so nobody repeats them.
- **The exclusions were audited only after the fact.** No candidate has been reinstated, because that needs the work that was skipped rather than a note.
- **The pitch video predates the last two days of findings.**
