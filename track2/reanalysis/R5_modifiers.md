# R5. Is there a modifier in the mitotic checkpoint, the cohesion machinery or the decay pathway?

**Question.** Phenotypic severity in mosaic variegated aneuploidy varies between patients with similar *BUB1B* genotypes. A rare variant elsewhere in the same machinery would be a candidate explanation, and neither the gene-list approach nor the phenotype-driven ranking would surface one, because neither is looking for a second gene that is not causal on its own.

**Data.** In hand. The 1,694 rare coding variants the Track 1 pipeline already isolated, being PASS calls inside coding sequence and absent from dbSNP, intersected against the 80-gene mitotic checkpoint and nonsense-mediated decay network the project had already assembled, and against a cohesion and centromere set added here.

**Computed answer. Three variants outside *BUB1B*, and no enrichment. The network is depleted.**

| Gene | Position | Change | Consequence | Genotype | Depth | gnomAD |
|---|---|---|---|---|---|---|
| RANBP2 | chr2:108751880 | C>T | synonymous | 0/1 | 59 | exomes AC 9, AN 1,459,684, AF 6.2e-6 |
| SGO1 | chr3:20174258 | T>C | missense p.Thr425Ala | 0/1 | 40 | exomes AC 4, AF 2.7e-6; genomes AC 2, AF 1.3e-5 |
| ANAPC2 | chr9:137185989 | C>T | missense p.Gly297Asp | 0/1 | 53 | genomes AC 25, AN 152,312, AF 1.6e-4 |

RANBP2 chr2:108751880 is in ClinVar as likely benign, a synonymous change, and drops out. Neither of the missense variants is in ClinVar. Neither gene carries a second hit, so neither satisfies a recessive model.

**The enrichment test, which is what decides this.**

| Gene set | Genes | Coding bases | Rare coding variants observed | Expected on coding length | P(X ≤ observed) |
|---|---|---|---|---|---|
| Mitotic checkpoint and decay network | 80 | 296,459 | 1 | 9.0 | 0.0012 |
| Plus cohesion and centromere | 97 | 391,955 | 5 | 11.9 | 0.021 |
| Cohesion and centromere alone | 18 | 96,982 | 2 | 3.0 | 0.43 |

The network carries **fewer** rare coding variants than its coding footprint predicts, not more. That is what constraint on essential mitotic genes predicts, and it is the opposite of a modifier signal. The two missense variants sit inside chance expectation for their gene set.

**What each possible result would change.** An enriched set, or a second hit in one gene, would have opened a digenic or modifier hypothesis and given the gate a second measurement to make. It did not. The report's statement that no rare variant exists in the decay machinery, previously an assumption carried from one working file, is now a computation with a frequency lookup behind it.

**What survives as a hypothesis, and how weak it is.** *SGO1* p.Thr425Ala is the only entry with a mechanistic story: shugoshin protects centromeric cohesion, and this is a chromosome segregation disorder. Against it: a single heterozygous missense in a recessive-associated gene, no second hit, no functional data, and a gene set that is not enriched. It is worth one sentence in a family study if one ever happens, and nothing more. It is not a recommendation and it does not enter the report.

**Tier.** Computed here for the variants and the enrichment; the frequencies are retrieved from gnomAD v4.1 by HTTP range read of the public sites files, never by an API query on patient coordinates. **Cost.** Under an hour, no money.

**Tooling note.** htslib could not reach the public bucket from this machine, so the indexed range read is implemented directly in `pipeline/reanalysis/gnomad_range.py`. It reproduces the published record for chr15:40209701 exactly, AC 115 and AN 1,461,846, which is the check that it is reading the right bytes.

**Why it was not asked before.** Every seat was briefed on one gene. A modifier is by construction a question about a gene nobody was asked about.
