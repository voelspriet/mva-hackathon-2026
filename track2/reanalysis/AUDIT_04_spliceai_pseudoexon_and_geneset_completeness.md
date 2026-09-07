# AUDIT 04. Running SpliceAI locally to close the deep-intronic pseudoexon question, and an ontology-driven completeness check on R5's modifier universe

**Run 04 of `PROMPT_relevant_additions.md`, 7 September 2026.** `AUDIT_03` ended by naming its item 1 (score the
deep-intronic *BUB1B* variant with SpliceAI if any route is now reachable) and item 2 (a gene-set-completeness check
on `R5`'s modifier enrichment — is the 80+18-gene list the right universe?). This run takes both.

Before writing I read `R1`, `R5`, `R12`, `R18`, all three prior `AUDIT_NN` files and `SYNTHESIS_for_judging.md`.
**Rule 3 credits:** the deep-intronic variant and its gnomAD-absence are `R12`'s; its deterministic non-effect on the
canonical splice signals is `AUDIT_02`'s; `R5` owns the modifier screen, its three named hits (RANBP2/SGO1/ANAPC2) and
the enrichment table; `AUDIT_02`/`AUDIT_03` closed those three. What is new below is (a) an **actual SpliceAI score**
for the deep-intronic variant, run locally, which converts `AUDIT_02`'s bounded gap into a measurement; and (b) an
**ontology-driven** completeness pass that does not depend on a hand-assembled gene list, plus the characterisation of
what it surfaces.

## Egress correction, stated first because it is what made Entry 1 possible and it disconfirms both prior audits

`AUDIT_02` wrote that egress "reaches only gnomAD and Ensembl"; `AUDIT_03` widened that to "+ NCBI." **Both are wrong.**
Tested this run by TCP connect (`work/venv_spliceai/bin/python`, `socket.create_connection`, 8 s timeout):

| Host | Result |
|---|---|
| `pypi.org`, `files.pythonhosted.org` | **reachable** |
| `github.com`, `raw.githubusercontent.com` | **reachable** |
| `storage.googleapis.com`, `basespace.illumina.com` | **reachable** |
| `mygene.info`, `www.ebi.ac.uk`, `api.geneontology.org`, `rest.genenames.org` | **reachable** |
| `spliceailookup-api.broadinstitute.org` (34.71.77.14) | **times out** (as `AUDIT_02` found) |

So the *only* thing `AUDIT_02` established about SpliceAI — that the Broad **web API host** is unreachable — is true and
still true. But its inference that "the model … also cannot be fetched from this server" is false: **PyPI is open, and
the `spliceai` package ships its five trained Keras models inside the wheel.** The model does not need the dead web
host; it installs and runs locally. That is the whole of Entry 1.

Tooling note for reproduction: no `bcftools`/`tabix`/`mosdepth`/`spliceai` on `PATH`, and the Ensembl-116 GFF3 the task
brief says is "under `work/ref/`" is **not present** (only `GRCh38.fa` + `.fai`), confirming `AUDIT_01`. SpliceAI was
installed into an isolated venv **inside the repo** (`work/venv_spliceai`, nothing touched outside `/root/mvarepo`) with
`pip install spliceai tensorflow-cpu`; two one-line compatibility fixes were needed and are recorded in the measurement
table (setuptools pin for `pkg_resources`; `np.fromstring`→`np.frombuffer` for numpy 2.x). The VCF uses contigs
`1..22,X`; the reference FASTA and the SpliceAI run use `chr15`.

---

## Entry 1 — Converts a bound into a measurement. The deep-intronic *BUB1B* variant creates no splice signal: SpliceAI scores 0.00 on all four modes, with positive controls in the same intron scoring 0.44–0.94.

`REPORT_track1.md:26` recorded "one deep-intronic BUB1B variant absent from gnomAD … **no splice prediction run**."
`R12` called it "not assessable for a splicing effect here." `AUDIT_02` did the deterministic half — the variant
(**chr15:40216470 A>G**, intron 20) creates no canonical `GT`/`AG` and lies 1,025 bp / 2,996 bp from the two splice
sites, far outside their regulatory windows — but left the model-scored half, **deep-intronic pseudoexon activation**,
explicitly open with SpliceAI named as the remedy. This run ran that remedy.

SpliceAI 1.3.1 (bundled models `spliceai1–5.h5`, GENCODE annotation, `chr`-prefixed to match the reference), lookup
distance `-D 4999` so cryptic sites anywhere in the 10 kb window are reported. SpliceAI INFO is
`ALLELE|SYMBOL|DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DL` (delta scores for acceptor/donor gain/loss, then their
positions relative to the variant):

| Variant | DS_AG | DS_AL | DS_DG | DS_DL | max Δ | interpretation |
|---|---|---|---|---|---|---|
| **chr15:40216470 A>G (deep-intronic, target)** | **0.00** | **0.00** | **0.00** | **0.00** | **0.00** | **no predicted effect** |
| chr15:40209701 T>G (causal allele 1, p.Leu737Ter — exonic control) | 0.03 | 0.00 | 0.00 | 0.01 | 0.03 | no splice effect (expected) |
| chr15:40220612 T>G (causal allele 2, p.Asn1002Lys — exonic control) | 0.02 | 0.00 | 0.00 | 0.00 | 0.02 | no splice effect (expected) |

A negative delta score is only meaningful if the assay can score a positive in the same place. Two synthetic positive
controls that destroy the canonical splice sites of the very intron the variant sits in (intron 20), run identically:

| Positive control | DS_AG | DS_AL | DS_DG | DS_DL | reads as |
|---|---|---|---|---|---|
| chr15:40213475 G>C (disrupt intron-20 **donor** `GT`) | 0.01 | 0.45 | 0.00 | **0.44** | strong donor loss + acceptor loss |
| chr15:40217495 G>C (disrupt intron-20 **acceptor** `AG`) | 0.38 | **0.94** | 0.00 | 0.04 | strong acceptor loss |

The controls fire at 0.44–0.94 in this exact intron, so the assay is wired correctly and has real dynamic range here.
Against that, the deep-intronic variant's **0.00 across all four modes** is a decisive negative, not a silent zero:
SpliceAI predicts no acceptor gain, no donor gain (the pseudoexon signatures), and no loss anywhere in the window. The
delta score is essentially sequence-driven, so the annotation choice does not change a flat-zero result.

**What this changes.** Track 1's "no splice prediction run" and `R12`'s "not assessable" are now resolved. `AUDIT_02`'s
bound ("only the model-scored pseudoexon component remains") becomes a measurement: the model scored it, and it is
negative. The submission's stance — the variant is real (`AUDIT_02` Entry 2 confirmed it at the read level) but
"recorded, not built on" — is now positively evidenced rather than merely defensible. The last DNA-adjacent open item
inside the causal gene is closed. The only readout that could still add anything is a direct RNA assay
(`REPORT_track2.md` §4 item 2), which would *observe* splicing rather than predict it; nothing in the DNA motivates
prioritising it over the assays the report already ranks first.

## Entry 2 — Converts an assertion into a measurement, and transfers. `R5`'s modifier enrichment rests on a hand-assembled 80+18-gene universe; an ontology-driven scan reproduces its hits, shows its "rare coding variant" input contains common variants, and surfaces one candidate its named trio did not include: SMC4.

`R5`'s conclusion — "the network is depleted … not a modifier signal" — rests on an enrichment test over a gene
universe `R5` assembled by hand: the 80-gene mitotic-checkpoint/NMD list in
`pipeline/track2_compute/genes_network.txt` plus an 18-gene "cohesion and centromere set added here." The load-bearing
assumption is that **this list is the right universe**: a segregation gene carrying a rare coding variant but omitted
from the list would be invisible to the test. The 18-gene addition is **not enumerated in any file present** (searched
the repo; `R5` names only SGO1 and RANBP2 from it, and reports "5 observed" in the 97-gene set while naming 3), so the
assumption cannot be checked against `R5`'s own list. It can be checked a better way: let an ontology, not a
remembered list, define which genes are chromosome-segregation genes.

**Method (transferable — this is the point).** All **704** genes that carry a rare coding variant in
`work/coding_nodbsnp.gene.vcf.gz` were GO-annotated in one batch via `mygene.info` (12 unmatched, mostly Ensembl-ID
loci). Genes with any GO term matching a chromosome-segregation / cohesion / kinetochore / centromere / SAC / condensin
pattern were flagged. This removes the dependence on anyone remembering to include a gene. It recovers the causal
*BUB1B* and `R5`'s in-network ANAPC2 and its cohesion-set SGO1 — a positive control that the scan works — and then adds:

| Gene (not in the 80-gene network file) | child GT | gnomAD v4.1 | in-silico | segregation relevance |
|---|---|---|---|---|
| **SMC4** chr3:160411998 G>A | 0/1, AD 18,12, DP 30, GQ 99 | ex AF **1.37e-6** (AC 2), ge 6.57e-6, **0 hom** | **SIFT deleterious 0, PolyPhen probably_damaging 1** | **core: condensin II ATPase** |
| INO80 chr15:40984286 C>T | 0/1, AD 23,45, DP 68 | ex AF 8.89e-5, 0 hom | SIFT tolerated_low_conf 0.18, PolyPhen benign 0.027 | chromatin remodeller (peripheral) |
| CHMP1A chr16:89657392 G>A | 0/1, AD 10,13, DP 23 | ex absent, ge AF 6.63e-6 | intron on MANE (no missense there) | ESCRT (peripheral) |
| CDC7 chr1:91511686 T>G | 0/1, AD 18,8, DP 26 | ex AF **1.08e-2** | — | replication checkpoint; **not rare** |
| PPP2R1B chr11:111737358 C>T | 0/1, AD 17,17, DP 34 | ex AF 1.30e-3, **4 hom** | — | PP2A scaffold (paralog of in-list PPP2R1A) |
| DIS3L2 chr2:232329984 A>C | 0/1, AD 33,22, DP 55 | ex AF 3.90e-4, **5 hom** | — | RNA decay (peripheral) |
| TTN chr2:178565250 G>A | 0/1, AD 22,22, DP 44 | ex AF 2.53e-4, 0 hom | — | titin; GO link spurious |
| CENPV chr17:16353372 G>ins | **1/1**, AD 0,20 | ex AF **0.464**, **121,430 hom** | — | **common polymorphism** |
| FANCD2 chr3:10046720 / 10046723 | 0/1, 0/1 | ex AF **0.349 / 0.321** | — | **common polymorphisms** |
| H2BW1 chrX:104013293 T>C | **1/1**, AD 0,21 | ex AF **0.358**, **49,244 hom** | — | histone; **common polymorphism** |

**Two measured results fall out, one confirming and one that is uncomfortable and is recorded with equal prominence.**

**(a) The input file is not a "rare variant" file, which loosens `R5`'s enrichment (disconfirming / method).**
`work/coding_nodbsnp.gene.vcf.gz` is defined by *absence from the caller's dbSNP build*, which is not the same as *rare
in gnomAD*. Three of the segregation-gene entries above are common polymorphisms — **CENPV AF 0.464 (121,430
homozygotes; child is 1/1), H2BW1 AF 0.358 (49,244 hom; child 1/1), FANCD2 AF 0.35/0.32** — plus CDC7 at ~1%. `AUDIT_01`
already noted this file *misses* catalogued rare variants; the measured converse is that it *contains common ones*. So
`R5`'s "rare coding variants observed" counts (1 in the 80-gene set, 5 in the 97-gene set) are counts of *coding,
non-dbSNP-build* variants, some of which are common. The **direction** of `R5`'s finding is not threatened — a set
carrying single variants roughly in proportion to its coding length is what depletion looks like — but the **precision**
of the p-values (0.0012, 0.021) rests on a variant definition looser than "rare," and that should travel with the
result. I did **not** recompute the p-values across an expanded universe: that needs per-gene CDS lengths from an
annotation not present as a file (the GFF3 is absent), and each added gene contributes n=1, which is uninformative at
the single-gene level. `R5`'s own numbers imply a genome-wide density of 9.0/296,459 = **3.04e-5 rare-coding
calls/base**; every candidate above is a single heterozygote, so none introduces the biallelic hit that would open a
recessive modifier, and adding single-het genes does not reverse a depletion.

**(b) SMC4 is the one omission that is not benign, and it deserves at least the status `R5` gave SGO1 (disconfirming).**
`R5`'s three named hits and the two `AUDIT`-closed cohesion candidates (SGO1, RANBP2) are all **benign** by SIFT and
PolyPhen. SMC4 **p.Asp256Asn** (MANE `NM_001002800.3`, `c.766G>A`) is not: it is **ultra-rare** (gnomAD 2 exome alleles,
0 homozygotes — the same order as SGO1/ANAPC2/RANBP2), a genuine heterozygous PASS call, in a **core** chromosome-
segregation gene (SMC4 is the ATPase subunit of condensin I/II), and **SIFT deleterious (0) + PolyPhen probably_damaging
(1)** — a damaging prediction that SGO1 (SIFT tolerated, PolyPhen benign) never had. It has no ClinVar assertion. It has
**no second rare coding hit** in the gene (the one non-dbSNP coding variant in SMC4 is this one — recorded, incidentally,
as a **duplicate line** in the input file, a data-quality note for anyone tallying per-gene counts), so it does not
satisfy a recessive model; and there is no established SMC4 Mendelian segregation disease (the recognised MVA genes are
*BUB1B*, *CEP57*, *TRIP13*, all in `R5`'s network). **It does not overturn anything:** the *BUB1B* compound-het
diagnosis is established and causal, and one damaging heterozygote with no second hit is not a diagnosis. But it is a
candidate `R5`'s benign-predicted trio did not include, on slightly firmer in-silico footing than the SGO1 thread `R5`
kept, and whether it was inside `R5`'s unlisted 18-gene addition cannot be determined from files present. The honest
placement is `R5`'s own: **worth one sentence in a family study, nothing more** — but SMC4, not (or as well as) SGO1,
should carry that sentence, and the reason it was not visible before is that it sits outside the hand-assembled list,
which is exactly the failure mode an ontology-driven universe removes.

---

## What this run found, against the prompt's own relevance test

- **Entry 1 (converts a bound into a measurement):** SpliceAI, installed from PyPI and run locally against a dead web
  API, scores the deep-intronic *BUB1B* variant chr15:40216470 A>G at **0.00 on all four delta modes**, while positive
  controls disrupting the same intron's splice sites score 0.44–0.94. The pseudoexon question `AUDIT_02` could only
  bound is now measured and negative. The last DNA-adjacent open item inside the causal gene is closed.
- **Entry 2 (converts an assertion into a measurement / transfers):** an ontology-driven completeness scan reproduces
  `R5`'s hits without a hand-curated list, shows `R5`'s "rare coding variant" input contains common polymorphisms
  (CENPV AF 0.46, H2BW1 0.36, FANCD2 0.35) so the enrichment p-values rest on a loose definition, and surfaces **SMC4
  p.Asp256Asn** — ultra-rare, in-silico-damaging, single-het, in a core segregation gene — a candidate `R5`'s
  benign-predicted trio did not name.

**No load-bearing conclusion of the submission is overturned.** Entry 1 supports the submission's treatment of the
deep-intronic variant; Entry 2 leaves `R5`'s no-modifier direction intact (every candidate is a single het, no biallelic
hit, no enrichment reversal). **Three results are recorded as disconfirming with equal prominence** (rule 2): the egress
characterisation in `AUDIT_02`/`AUDIT_03` is wrong and SpliceAI was runnable all along; `R5`'s enrichment input mixes
common variants into "rare"; and SMC4 is an in-silico-damaging segregation-gene candidate that the hand-assembled
universe did not surface. The transferable contribution is the ontology-driven universe: a different team reusing the
modifier screen on a different patient would not have to remember every segregation gene.

## Measurement table

| # | What was measured | Value | Command / script |
|---|---|---|---|
| 1 | Egress reachability | PyPI/files.pythonhosted/GitHub/GCS/Illumina/mygene/EBI/GO all TCP-OK; Broad SpliceAI host times out | `socket.create_connection((host,443),timeout=8)` per host |
| 2 | SpliceAI install (isolated, in-repo) | spliceai 1.3.1 + tensorflow-cpu 2.21 + bundled models `spliceai1–5.h5` | `python3.12 -m venv work/venv_spliceai; pip install spliceai tensorflow-cpu pyfaidx` |
| 3 | Two compat fixes to run under py3.12/numpy2 | `pip install "setuptools<81"` (restores `pkg_resources`); `utils.py` `np.fromstring(seq,int8)`→`np.frombuffer(seq.encode('latin-1'),int8)` | edits recorded in `work/venv_spliceai/.../spliceai/utils.py` |
| 4 | SpliceAI, deep-intronic chr15:40216470 A>G | DS_AG/AL/DG/DL = **0.00/0.00/0.00/0.00** (DP −3138/884/942/−3205) | `spliceai -I query.vcf -O out.vcf -R work/ref/GRCh38.fa -A work/spliceai_run/bub1b.annotation.txt -D 4999` |
| 5 | SpliceAI, causal alleles (exonic controls) | 40209701 T>G 0.03/0.00/0.00/0.01; 40220612 T>G 0.02/0.00/0.00/0.00 | same run |
| 6 | SpliceAI positive controls (intron 20) | donor 40213475 G>C → 0.01/0.45/0.00/0.44; acceptor 40217495 G>C → 0.38/0.94/0.00/0.04 | `spliceai … -I pos_control.vcf … -D 4999` (ref bases GGTTG / TCAGA verified from FASTA) |
| 7 | Variant-carrying genes in coding_nodbsnp | 1,694 records, **704 distinct genes** | pysam scan of `work/coding_nodbsnp.gene.vcf.gz`, `INFO/GENE` |
| 8 | Segregation-GO genes among the 704 | ANAPC2(in-net), BUB1B(causal), SGO1, SMC4, INO80, CHMP1A, CDC7, PPP2R1B, DIS3L2, TTN, CENPV, FANCD2, H2BW1 | `mygene.info` batch `go.BP/CC/MF`, regex on term names |
| 9 | gnomAD v4.1 for the candidates | SMC4 ex AF 1.37e-6/0 hom; CENPV 0.464/121,430 hom; H2BW1 0.358/49,244 hom; FANCD2 0.349,0.321; CDC7 1.08e-2; PPP2R1B 1.30e-3/4 hom; DIS3L2 3.90e-4/5 hom; INO80 8.89e-5; CHMP1A absent-ex; TTN 2.53e-4 | gnomAD GraphQL `variant(variantId, dataset:gnomad_r4)` per variant |
| 10 | child genotypes for candidates | all 0/1 PASS GQ 99 except CENPV 1/1 and H2BW1 1/1 (see table) | pysam `fetch` on `data/WGS_EX2312012_HGWCNDSX7.vcf.gz` |
| 11 | SMC4 consequence / in-silico / ClinVar | MANE `NM_001002800.3` (ENST00000357388) `c.766G>A` **p.Asp256Asn**; SIFT deleterious 0; PolyPhen probably_damaging 1; no ClinVar assertion (COSV61007941, rs766073090) | Ensembl REST `vep/human/region/3:160411998-160411998:1/A?mane=1&hgvs=1&sift=1&polyphen=1` |
| 12 | INO80 / CHMP1A in-silico | INO80 SIFT tolerated_low_conf 0.18 / PolyPhen benign 0.027; CHMP1A intron on MANE | Ensembl REST VEP |
| 13 | SMC4 second-hit + duplicate record | one non-dbSNP coding variant in SMC4 (chr3:160411998), **listed twice** in the file; no other rare coding hit in gene body | pysam scan of coding_nodbsnp (GENE==SMC4) + full-VCF PASS calls chr3:160393000–160470000 |
| 14 | `R5` implied genome-wide density | 9.0 / 296,459 = 3.04e-5 rare-coding calls per coding base | arithmetic on `R5`'s enrichment table |

gnomAD via `POST https://gnomad.broadinstitute.org/api` (`gnomad_r4`); annotation via `https://rest.ensembl.org`; GO via
`https://mygene.info/v3/query`. SpliceAI inputs/outputs are in `work/spliceai_run/` (`query.vcf`, `out.vcf`,
`pos_control.vcf`, `pos_control.out.vcf`, `bub1b.annotation.txt`).

## Where the next run should start

1. **The causal gene is now closed at the DNA level end to end.** With Entry 1, every variant class inside *BUB1B* that
   DNA can interrogate has been measured (coding pair, deep-intronic splice, upstream regulatory, phase, dosage). The
   only remaining *BUB1B* readouts are wet-lab (RNA for NMD/splicing, parents for phase), already ranked in the report.
   A next run should not re-open *BUB1B*; there is no DNA-only measurement left to make.
2. **SMC4 p.Asp256Asn is the one loose end this run created and did not fully close.** It is closed at the population,
   zygosity and in-silico layers, but "in-silico damaging" is a prediction. If a next run wants to settle it, the
   options are: (a) run SpliceAI/other predictors are irrelevant (it is a clean missense, not a splice variant); (b)
   AlphaMissense — the repo already fetched AlphaMissense for *BUB1B* (`pipeline/track2_compute/get_alphamissense_bub1b.sh`);
   the same public table could be queried for SMC4 p.Asp256Asn for an orthogonal pathogenicity score to SIFT/PolyPhen;
   (c) parental genotyping, the only thing that could make it more than an incidental heterozygote. Absent those, its
   status is "one sentence in a family study," same as SGO1.
3. **The enrichment p-values in `R5` should be re-derived on a gnomAD-rarity-filtered input**, now that the input file is
   shown to contain common variants. That needs per-gene CDS lengths (fetchable from Ensembl now that egress is known
   wide) and a gnomAD-AF cutoff applied to the observed counts. It would tighten `R5`'s 0.0012/0.021 onto a defensible
   "rare" definition rather than "non-dbSNP-build." This is a bounded, self-contained computation.
4. **`AUDIT_01` item 3 (STR-aware comparator for the upstream regulatory scan) remains the one untouched methodological
   to-do** across all four runs.
5. Tooling for whoever runs next, corrected: `python3.12` (pysam 0.24.0); an isolated SpliceAI venv now exists at
   `work/venv_spliceai` (models bundled, two source fixes applied); **egress is wide** — PyPI, GitHub, GCS, Illumina
   BaseSpace, mygene.info, EBI, GO API, gnomAD, Ensembl, NCBI are all reachable; only the Broad SpliceAI web host times
   out (and is not needed). VCF contigs `1..22,X`; reference FASTA and SpliceAI use `chr…`.
