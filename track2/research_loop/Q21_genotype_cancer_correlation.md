# Q21. Does the genotype predict which children get cancer, and can surveillance be targeted by it?

**Asked because** a Utrecht doctoral thesis claimed its chapter 3 "uncover[s] a striking correlation between the mutations in these genes and the occurrence of specific childhood cancers in MVA patients". If that holds, surveillance in this syndrome could be directed by genotype rather than applied uniformly, which is the most actionable clinical claim this project has found.

## Answer

**It holds, it is published in a primary source, and it is graded by function rather than by gene identity. This child sits in the high-risk group, and the report had no genotype-specific justification for its surveillance until now.**

The chapter is published as **Yost S, de Wolf B, Hanks S, Zachariou A, Marcozzi C, Clarke M, de Voer R, Etemad B, Uijttewaal E, Ramsay E, Wylie H, Elliott A, Picton S, Smith A, Smithson S, Seal S, Ruark E, Houge G, Pines J, Kops GJPL, Rahman N. "Biallelic TRIP13 mutations predispose to Wilms tumor and chromosome missegregation." Nat Genet 2017;49(7):1148-1151, PMID 28553959, PMC5493194, open access.** Institute of Cancer Research and Hubrecht Institute, the same consortium behind the original *BUB1B* discovery.

### The correlation, verbatim

From the abstract:

> "Individuals with biallelic TRIP13 or BUB1B mutations have a high risk of embryonal tumors, and here we show that their cells display severe SAC impairment. MVA due to biallelic CEP57 mutations, or of unknown cause, is not associated with embryonal tumors and cells from these individuals show minimal SAC deficiency."

From the full text:

> "all MVA cases with childhood solid tumors in our series have either BUB1B or TRIP13 mutations"

> "BUB1B and TRIP13 mutation-positive individuals are at high risk of cancer and require close surveillance, whereas other individuals with MVA may be at lower cancer risk."

**The predictor is the severity of spindle assembly checkpoint failure, not the gene name.** Genes that abolish the checkpoint carry the tumour risk. Genes that leave it largely intact do not.

### The measurement, and why it matters to the gate

| Cells | Mitotic arrest maintained |
|---|---|
| Control | more than 2 hours |
| *TRIP13* mutant | escaped within one hour |
| *BUB1B* mutant | rapid escape, same direction |
| *CEP57* mutant and unknown-cause MVA | checkpoint maintained |

Section 4 of the report proposes functional readouts and the gate files discuss mitotic arrest duration under nocodazole or S-trityl-L-cysteine. Until now that was justified as mechanistic characterisation. **Yost 2017 makes it prognostic.** An arrest duration under an hour against a control of over two hours is the phenotype that separates the MVA children who get embryonal tumours from those who do not. That is a published threshold, in patient cells, on the same assay the gate already contemplates.

### Three consequences for the report

1. **The surveillance intensity now has a genotype-specific citation.** The report argued its additions from mechanism, from costing nothing, and from the field's 5 percent threshold. It can now cite a primary source naming this child's gene and saying such individuals "require close surveillance". That is a materially stronger footing.
2. **Pooled MVA cancer-risk figures understate the risk for this genotype.** Any figure averaged across MVA mixes *CEP57* and unknown-cause patients, who are not associated with embryonal tumours, with *BUB1B* and *TRIP13* patients, who are. This bears on the unresolved 38.7 versus 75 percent dispute in section 8: Pavone's 38.7 percent is MVA1 specifically and so is unaffected, but any pooled figure is a lower bound for *BUB1B*, not an estimate of it.
3. **The differential now carries a prognostic split.** Section 11 lists the widened gene set. It should say that the split is not cosmetic: two of those genes carry embryonal tumour risk and the others, on current evidence, do not.

### What the paper does not give

No breakdown of which tumour type follows which gene within the high-risk pair. The *TRIP13* side is clean, six of six with Wilms tumour, five successfully treated. The *BUB1B* side is described as 14 individuals with biallelic mutations and cancer predisposition, without a per-tumour tabulation in the text reached. So the correlation supports **how intensively** to watch this child, not **what to watch for**. Rhabdomyosarcoma and Wilms tumour both remain in scope, which is what the report already says.

## Access levels reached

Full abstract via NCBI efetch; full text via PMC, open access. The de Wolf thesis that pointed here was retrieved from the Utrecht DSpace REST API.
