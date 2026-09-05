# Q1. Does the 75 percent cancer-risk figure exist, and where does it come from?

**Asked because** section 8 of `REPORT_track2.md` prints two cancer-risk figures side by side, 38.7 percent from Pavone 2022 and about 75 percent from Orphanet ORPHA 1052, and builds a decision threshold on each. The audit marked the second UNVERIFIABLE: the Orphanet record could not be retrieved. If it cannot be sourced, the 33.3 percent threshold row has nothing under it.

## Answer

**The figure circulates, but no counted series produces it.** It is not a published risk estimate in the sense the report implies, and printing it beside Pavone's 38.7 percent as though the two were comparable estimates overstates it.

### What the primary sources actually say

| Source | Figure | Denominator | Access reached |
|---|---|---|---|
| Hanks 2004, Nat Genet 36:1159, PMID 15475955 | **none** | Five families, two with embryonal rhabdomyosarcoma | Full abstract via NCBI efetch |
| Pavone 2022, PMID 35804254, PMC9616775 | **38.7 percent**, quoted as "Malignancies had noticeably a high incidence (38.7%)" | 12 of 31 published MVA cases, systematic review | PMC full text |
| Suijkerbuijk 2010, Cancer Res 70:4891 | **37 percent**, reached only as a search-engine extract of the introduction, not from the article body | Not stated in the extract | AACR page returns no article body; no PMC deposit for the body text located |
| OMIM 257300 | Reported by search extract as "high incidence of cancer (approximately 75%)" | **No denominator given in any extract obtained** | **Not reached.** omim.org returns HTTP 403 to automated fetch; the r.jina.ai text proxy returned 440 bytes of nothing |
| Orphanet ORPHA 1052 | The figure the report attributes to it | Unknown | **Not reached.** orpha.net does not resolve from this machine; the Polish government mirror of the same record carries the phrase "cancer predisposition" and no percentage at all |
| Nature Reviews Genetics 2024, MVA in development, ageing and cancer, s41576-024-00762-6 | Would settle it | | **Not reached**, paywalled behind the Springer Nature identity provider |

### The finding

Three different numbers are in circulation for the same quantity: 37, 38.7 and about 75 percent. Only one of them, Pavone's 38.7 percent, has a stated numerator and denominator that can be checked. The 75 percent has no traceable count behind it in anything reachable, and the two databases that carry it, OMIM and Orphanet, are both secondary sources summarising the same small literature that Pavone counted.

The likely explanation is not that anyone invented it. It is that the database summaries predate and do not use a systematic count: Orphanet's MVA record was last updated in 2012 on the report's own note, against Pavone's 2022 tabulation. A pre-2012 impression of a syndrome ascertained through childhood cancer will run high, because the syndrome was first described through cancer cases.

### Correction applied

The threshold table in section 8 now labels the second row as resting on a figure with no traceable denominator, and states the range that counted series support. The row is retained rather than deleted, because deleting it would silently adopt the low estimate, which is the error the earlier draft was criticised for. What changes is that the reader is told the two rows are not the same kind of number.

## Routes tried and failed, so nobody repeats them

- `omim.org/entry/257300`: HTTP 403 to automated fetch.
- `r.jina.ai` proxy on the same URL: 440 bytes, no content.
- `orpha.net` and the legacy consor URL: does not resolve from this machine, consistent with the audit's earlier finding of a connection-verification page.
- `chorobyrzadkie.gov.pl/en/disease_card/1052`, a government mirror of the Orphanet record: reached, carries no percentage.
- `nature.com/articles/s41576-024-00762-6`: 303 to the Springer Nature identity provider, paywalled.
- NCBI Genetic Testing Registry entry for the condition: reached, carries no percentage.

**What would close it.** Institutional access to OMIM's full text, which states the figure and would name its reference, and to the 2024 Nature Reviews Genetics review. Both are minutes of work for someone with a subscription and unreachable without one. This is action B5 in `track2/synthesis/NEXT.md`.
