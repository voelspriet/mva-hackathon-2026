# G1. Can the missing MVA measurement be made without a new patient?

**Question.** Allele-specific expression (ASE) and nonsense-mediated decay (NMD) efficiency of *BUB1B*, plus residual BubR1 protein as a percentage of control, in cells from a person with mosaic variegated aneuploidy type 1 (MVA1, biallelic *BUB1B*, OMIM 257300). Has this been done, and can it be done from material and data that already exist?

**Date of search:** 5 September 2026.
**Answer in one line:** Yes. The cells are in a public catalogue, orderable today, and nobody has ever used them for this.

---

## 1. Bottom line

Three things are true at once, and they are the finding.

1. **The right cells exist and are for sale.** Coriell's NIGMS Human Genetic Cell Repository holds `GM21284`: an EBV-transformed lymphoblastoid line from a 4-year-old girl with MVA1 carrying exactly the genotype the measurement needs, a frameshift/PTC allele and a missense allele in trans: *BUB1B* c.2208_2211dupGTTA (p.Ser738Valfs\*16, "753X") and c.2441G>A (p.Arg814His). US academic price **$262**. It also holds a **complete trio** for a second biallelic *BUB1B* MVA1 case: proband `GM22006` with both parents, `GM22004` (father) and `GM22005` (mother).
2. **No omics data from any *BUB1B* MVA patient allows the allele-resolved answer.** One open human dataset exists (`GSE22206`, expression microarray, LCL + fibroblast from a *BUB1B*-homozygous PCS/MVA proband with controls and relatives). Arrays cannot phase alleles, so it gives total mRNA only. There is no RNA-seq, no proteomics, no ribosome profiling from a *BUB1B* MVA patient in GEO, SRA, ArrayExpress/BioStudies, ENA, dbGaP or EGA.
3. **The measurement has never been made, and the near-misses are documented.** The closest published work stops one step short in a way that is quotable, see §5.

**Shortest legitimate path to the number:** order `GM21284` (+ optionally `GM22006`/`GM22004`/`GM22005` as a trio) from Coriell under a standard MTA, grow, split into vehicle and NMD-inhibited arms, amplicon-sequence cDNA across both variant sites, and run a quantitative BubR1 immunoblot against controls. No new patient, no new consent, no clinical recruitment. Material cost $434 for the single case, $1,220 with the second family's trio. Full study roughly **$16,000** in consumables and sequencing, **3 to 4 months elapsed**, about 2.5 months FTE. See §7, which gives verified prices and the published protocols this would copy.

---

## 2. Findings table

| Resource | What it holds | Availability | Cost | What it would answer |
|---|---|---|---|---|
| **Coriell NIGMS `GM21284`** ([catalog](https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=GM21284)) | LCL (EBV) from MVA1 proband, female, 4y, New Zealand. *BUB1B* c.2208_2211dupGTTA (p.S738Vfs\*16 / "753X") **and** c.2441G>A (p.R814H), compound het. Karyotype 58% endoreduplication, 30% hyperdiploid. | Catalogue, orderable; MTA + Statement of Research Intent required | **$262** US academic / $448 international | **Everything.** ASE ratio at both sites, NMD efficiency ±inhibitor, residual BubR1 % of control |
| **Coriell `NA21284`** ([catalog](https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=NA21284)) | Genomic DNA from the same subject | Catalogue | $172 / $352 | gDNA reference for the ASE denominator (1:1 allele ratio control). Cheap insurance |
| **Coriell `GM22006` + `GM22004` + `GM22005`** ([GM22006](https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=GM22006)) | LCL trio, South African family 2741. Yost et al. 2017 methods, verbatim: "ID_0675 (patient with biallelic *BUB1B* mutations, Coriell ID:GM22006)". Parents clinically normal, karyotype 46,XY and 45,X[3]/46,XX[47] | Catalogue | $262 each ($786 trio) | Same measurement **plus** the carrier-parent comparison that turns an ASE ratio into a dosage model. Genotype not printed on the Coriell record, so resequence |
| **Coriell `GM14084`** ([catalog](https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=GM14084)) | **Fibroblast** (untransformed, passage 7), MVA proband, 13 months | Catalogue | $262 / $448 | Non-transformed cell type, but **no gene identified**. Would need sequencing first; may not be *BUB1B* |
| **Coriell `GM21654/55/56/57`** | MVA2, biallelic *CEP57*, proband pair plus parents | Catalogue | $262 each | Wrong gene. Useful as an MVA-not-BUB1B contrast |
| **Cellosaurus** ([GM21284 = CVCL_EF99](https://www.cellosaurus.org/CVCL_EF99)) | Cross-repository index of 150k+ lines | Open | Free | Confirms **every** MVA-annotated line worldwide traces to Coriell. No ECACC, JCRB, RIKEN, DSMZ, ATCC, KCLB or CCRID entry. Also records **zero publications** using `GM21284` |
| **GEO `GSE22206`** ([record](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE22206)) | Illumina humanRef-8 v2 arrays, LCL **and** fibroblasts from a PCS/MVA proband homozygous for *BUB1B* c.2386-11A>G, plus 2 relatives and 3 controls, 2 replicates each (14 arrays) | **Fully open**, no application | Free | **Total** *BUB1B* mRNA vs control, today. I computed it, see §4. Cannot resolve alleles |
| **GEO `GSE197267`** ([record](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE197267)) | scRNA-seq, PBMCs, MVA patient with biallelic *MAD1L1* | Open | Free | Wrong gene; 3'-biased scRNA-seq cannot phase *BUB1B* alleles anyway |
| **GEO `GSE134780` / `GSE134781`** | Mouse *BubR1* allelic-series MVA progeria RNA-seq | Open | Free | Mouse. Shows the allelic-dosage question is already framed, in mice, not humans |
| **Kops lab, Hubrecht/UMC Utrecht** | The four MVA fibroblast lines of Suijkerbuijk 2010 (absent/I909T, 386X/R727C, 753X/R814H, 731X/Y155C), SV40-transformed | **No materials availability statement.** Request by email: g.kops@hubrecht.eu | Unknown | Fibroblast versions of the same genotypes; would broaden n from 1 to 4 |
| **Rahman lab, ICR London** | Source of the Hanks 2004 families; deposited `GM21284`, `GM22004-6`, `GM21654-57` at Coriell | rahmanlab@icr.ac.uk | n/a | Already discharged its obligation via Coriell. That is why the catalogue route works |
| **Saitsu lab, Hamamatsu** ([J Hum Genet 2024](https://doi.org/10.1038/s10038-023-01211-8)) | **RNA-seq from a PCS/MVA patient's cells** (biallelic *BUB1B*: maternal c.1402-5A>G mis-splicing + paternal 3.0 kb Alu/SVA insertion in intron 2) plus a BUB1B immunoblot | **Not deposited.** No data availability statement, no accession. Contact hsaitsu@hama-med.ac.jp | n/a | The only existing patient *BUB1B* RNA-seq. Locked in a lab. Ask, or regenerate |
| **Solve-RD** ([data page](https://solve-rd.eu/results/solve-rd-data/)) | WES/WGS freezes released; short- and long-read RNA-seq listed as **pending**. EGA study `EGAS0000100385` | Data Access Agreement to solve-rd@med.uni-tuebingen.de, then EGA request; ≤8 weeks review | Free | Only if an MVA case happens to sit in a future RNA freeze. Not a route to a specific gene today |
| **GREGoR** (dbGaP `phs003047`, AnVIL) | WES, WGS, long-read WGS, **short-read RNA-seq**, long-read RNA-seq, ATAC, Fiber-seq from rare disease families | Controlled, dbGaP application | Free + cloud compute | Same caveat. Worth a targeted query for *BUB1B* biallelic cases |
| **Genomics England 100,000 Genomes** ([join](https://www.genomicsengland.co.uk/join-us)) | *BUB1B* is a **Green** gene on 9 PanelApp panels incl. severe microcephaly, DDG2P, childhood solid tumours ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/entities/BUB1B)) | Research Environment application | Free for academics | Genomes, not transcriptomes. Would find MVA cases; would not give ASE |
| **ECACC** ([site](https://www.culturecollections.org.uk/products/cell-cultures/chromosomal-abnormalities-collection/)) | Chromosomal Abnormalities Collection of LCLs. Suijkerbuijk 2010 states MVA LCLs came from "ECACC or Coriell"; Yost 2017 cites ECACC IDs `96061307`, `FACT5728DLB`, `FACT5728KC` and `91071212` for its *TRIP13* family and controls, so ICR does deposit at ECACC | Catalogue is JavaScript-only, not machine-queryable; **not resolvable without emailing ECACC** | ~£300 typical | Possible second source for MVA1 LCLs. **Unresolved, flagged below** |
| **Kops lab CENATAC study** ([EMBO J 2021, PMC8280824](https://europepmc.org/article/PMC/PMC8280824)) | **MVA patient RNA-seq exists** (CENATAC/CCDC84 genotype) | **Deliberately withheld.** Verbatim: "RNAseq data from the patient and control subject cannot be made publicly available for reasons of patient confidentiality. Qualified researchers may apply for access to these data, pending institutional review board approval." Only the HeLa arm was deposited (`GSE143392`, `PXD024682`) | Free if granted | Wrong gene (*CCDC84*, not *BUB1B*), but proves the withholding pattern and gives a named application route |
| **BioProject `PRJNA915310`** ([record](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA915310)) | Whole-exome, 3 MVA patients (*MAD2L1BP*), runs SRR22878115 / SRR22878114 / SRR25495555 | **Fully open** | Free | DNA only. No expression, no ASE |
| **PRIDE `PXD035765`** ([record](https://www.ebi.ac.uk/pride/archive/projects/PXD035765)) | Orbitrap proteomics, blood cells, MVA patient with biallelic *MAD1L1* | Open | Free | Wrong gene, and no BubR1 dosage question addressed |
| **EuroBioBank / RD-Connect Sample Catalogue** ([catalogue](https://www.eurobiobank.org/sample-catalogue/), [search](https://samples.rd-connect.eu/)) | Federated rare disease sample catalogue | Live search + a Feb 2016 aggregate spreadsheet | Free to search | **Nothing.** The downloadable EuroBioBank catalogue contains zero occurrences of "variegated", "BUB1B", "chromatid", "aneuploid" or "257300" |
| **dbGaP `phs001557`** ([study](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001557.v1.p1)) | "Mosaic Chromosomal Aneuploidies Detection in Clinical Samples" | Controlled | n/a | **A false positive.** Somatic mosaic aneuploidy in autism and hemihyperplasia cases, not constitutional MVA syndrome |
| **ATCC, DSMZ, JCRB, RIKEN BRC, KCLB, CCRID, Telethon Network** | n/a | n/a | n/a | **Nothing found.** No MVA or *BUB1B* patient line indexed in Cellosaurus from any of them |
| **DDBJ / JGA / GEA (Japan)** ([search](https://ddbj.nig.ac.jp/search/)) | n/a | n/a | n/a | **Zero** for MVA, *BUB1B*, PCS and MVA syndrome. Matters because the best-designed study (Saitsu 2024) is Japanese and is not in the Japanese archives either |

---

## 3. The strongest single fact

`GM21284` has been in the Coriell catalogue since at least 2016 (Cellosaurus record created 13 July 2016) and, as far as the literature index can tell, **has never been used in a published study**. A Europe PMC full-text search for `GM21284` returns 7 hits, every one of them about an unrelated mouse long non-coding RNA that happens to be called *Gm21284*. Zero hits for `GM21284 AND BUB1B`. Cellosaurus lists no `RX` publication cross-reference for the line.

The genotype-defining paper's own line, "753X/R814H", appears in exactly one publication ever: Suijkerbuijk et al. 2010. A Europe PMC search for `"753X" AND BUBR1` returns that one paper and nothing else.

So the material sitting on a shelf in Camden, New Jersey, priced at $262, is the closest thing that exists to the person whose measurement is missing, and in ten years nobody has ordered it for this.

There is a sharper version of this. Search Europe PMC for the mutation itself, `"2211insGTTA" OR "2208_2211dup"`, and you get five papers: van Deursen's mono-allelic BubR1 MVA mouse (PMID 23300461), the BubR1 allelic-series progeria mouse (PMID 31738183, data in `GSE134780`/`GSE134781`), and three reviews of those mice. The human allele has been built into mice, aged, RNA-sequenced and reviewed. In the human cells that carry it, sitting in a catalogue, it has never been read.

---

## 3b. And there is a live clinical reason to do it

The two variants in `GM21284` are both in ClinVar. The frameshift, [`VCV000006763`](https://www.ncbi.nlm.nih.gov/clinvar/variation/6763/), is classified **Pathogenic**. The missense, [`VCV000006764`](https://www.ncbi.nlm.nih.gov/clinvar/variation/6764/) (p.Arg814His), carries **conflicting classifications of pathogenicity**.

So the second allele of a named MVA1 patient, twenty-two years after her family was published, is still contested in the database clinical laboratories consult. An allele-resolved expression ratio and a residual-protein percentage from her own cells is exactly the functional evidence that a variant with conflicting classifications needs. The measurement is not only missing, it is the missing piece of an open ClinVar dispute.

---

## 4. A number obtained today, from public data, for nothing

`GSE22206` is open. I downloaded the series matrix and the GPL6104 annotation, found the single *BUB1B* probe (`ILMN_1733950`), and read the values. Data are lumi VST + robust spline normalised, so approximately log2.

| Sample group | Probe value (mean) | Linear, % of matched control |
|---|---|---|
| LCL, proband (homozygous *BUB1B* c.2386-11A>G) | 8.97 | **65.7%** |
| LCL, two relatives (carriers) | 9.68 | 108.0% |
| LCL, unaffected controls (n=2 individuals, 4 arrays) | 9.58 | 100% (reference) |
| Fibroblast, proband | 8.06 | **93.8%** |
| Fibroblast, control | 8.16 | 100% (reference) |

Reproduce with:
```
curl -s https://ftp.ncbi.nlm.nih.gov/geo/series/GSE22nnn/GSE22206/matrix/GSE22206_series_matrix.txt.gz | gunzip | grep ILMN_1733950
curl -s https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL6nnn/GPL6104/annot/GPL6104.annot.gz | gunzip | grep BUB1B
```

**Read this carefully.** It is a real, citable, free number, and it is *not* the missing measurement. Three reasons: (a) the proband is homozygous for an intronic splice variant, not compound heterozygous, so there is nothing to phase; (b) a single 50-mer array probe reports whatever transcript still hybridises, not the fraction that survived NMD; (c) there is no protein. What it does establish is a baseline expectation and a demonstration that the general shape of the question is answerable from existing data. It also shows the tissue dependence that matters for study design: 66% in LCL, 94% in fibroblast, from the same person on the same chips.

Provenance: submitted 8 June 2010 by Rio Frio, Foulkes and colleagues, McGill; BioProject `PRJNA128871`; contact thomas.riofrio@mail.mcgill.ca.

---

## 5. Why "never measured" survives scrutiny

The claim needed adversarial checking, because two papers come close. Both fall short, and the shortfall is on the record.

**Suijkerbuijk, Kops et al., Cancer Res 2010** (PMC2887387, "Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy") is the closest anyone has come. They used MVA patient LCLs and SV40-transformed fibroblasts of genotypes 731X/Y155C, 753X/R814H, 386X/R727C. They found full-length mutant BubR1 "decreased 2-6 fold compared to wild-type alleles", presented as normalised band intensity in a figure rather than as tabulated percentages. They ran **northern blots**, found mRNA from substitution alleles I909T, R727C and Y155C unaffected, could not detect 386X mRNA at all, saw a 2-fold reduction for 731X/WT, and **inferred** NMD: truncated BubR1 expression "may be prevented by nonsense-mediated mRNA decay". Inferred, from a bulk blot, with no allele-resolved read count and **no NMD-inhibition arm**. That is the gap.

**Kawakami, Saitsu et al., J Hum Genet 2024** (doi 10.1038/s10038-023-01211-8) did RNA-seq on patient-derived cells from a PCS/MVA girl with biallelic *BUB1B* and reported "severely diminished BUB1B protein level" by immunoblot. Severely diminished is not a percentage. The RNA-seq is not deposited anywhere; the article carries no data availability statement and no accession.

**Frontiers in Endocrinology 2026** (PMC13349884, two novel heterozygous *BUB1B* variants) is the most recent attempt and the most explicit admission. Its own methods state the assays "are qualitative in nature" and that "band intensity was assessed visually", reporting "a trend toward reduced BUBR1 band intensity compared to controls". No ASE, no NMD, no patient-derived line, PBMCs only.

So: mRNA has been blotted, protein has been eyeballed, NMD has been assumed. The allele-resolved ratio with an inhibitor arm, and residual BubR1 stated as a percentage with error bars, do not exist for any MVA patient.

---

## 6. What each route would and would not deliver

**Route A, the one that works (Coriell).** `GM21284` puts both variant sites 233 bases apart in the *BUB1B* cDNA (c.2208_2211dup and c.2441G>A). A single ~350 bp amplicon therefore spans both, so one sequencing library returns not two independent allele ratios but a phased read-by-read assignment: every read carries the identity of the allele it came from. That is the design the measurement wants. Add `NA21284` gDNA as the 1:1 allelic-balance control that calibrates PCR bias. Add the `GM22004/5/6` trio for carrier parents. All open catalogue, one MTA, no ethics application beyond institutional biosafety, because the consent is already in place at NIGMS.

**Route B (ask the labs).** Kops (g.kops@hubrecht.eu) for the four fibroblast genotypes; Saitsu (hsaitsu@hama-med.ac.jp) for the unpublished patient RNA-seq. Both are single emails and both are free. Neither is guaranteed. Recent-paper materials availability statements do not compel either: the 2010 paper predates mandatory statements and the 2017 TRIP13 paper says only that data "are available within the paper and its supplementary information".

**Route C (consortia).** Solve-RD, GREGoR and 100,000 Genomes all accept external proposals, but none of them can be steered at a named gene on demand. GREGoR is the best of the three because it actually generates short- and long-read RNA-seq from rare disease families and releases it via dbGaP `phs003047` on AnVIL. The realistic use is a query, not a study: ask whether any consented biallelic *BUB1B* case with RNA already exists. Timeline months, not weeks. Solve-RD's own RNA-seq freezes are still listed as pending.

**Route D (do not).** Recruiting a new MVA patient for a measurement obtainable from a $262 catalogue vial is not defensible.

---

## 7. Cost and feasibility

### 7.1 There is already a published protocol to copy

The design does not need inventing. Rio Frio et al., *J Clin Invest* 2008, ["Premature termination codons in PRPF31 cause retinitis pigmentosa via haploinsufficiency due to nonsense-mediated mRNA decay"](https://pmc.ncbi.nlm.nih.gov/articles/PMC2262031/) is the same experiment on a different gene: **patient lymphoblastoid lines** carrying a PTC allele, semiquantitative RT-PCR with primers amplifying both alleles in one reaction, allele-specific real-time PCR against a standard curve, and NMD blocked four independent ways:

| Inhibitor | Concentration | Duration |
|---|---|---|
| Cycloheximide | 28 µg/ml | 4 h |
| Emetine | 300 µg/ml | 6 h |
| Puromycin | 300 µg/ml | 6 h |
| Wortmannin (blocks UPF1 phosphorylation without inhibiting translation) | 100 µM | 6 h |

Chemically distinct arms matter, because cycloheximide alone is a weak control: it inhibits translation generally, so a rise in the PTC transcript is expected for trivial reasons. Wortmannin is the arm that separates NMD from translation, and the 2008 paper is the reason to include something of that kind. A selective SMG1 inhibitor is the modern version of that logic and should be the primary arm here, see §7.4.

Two footnotes make this template unusually apt. First, the first author, **Thomas Rio Frio**, is the same person who two years later generated `GSE22206`, the only public *BUB1B*-patient expression dataset. Second, that 2008 paper reads alleles by gel densitometry and capillary sizing. Amplicon sequencing replaces both with read counts, which is the upgrade that turns "an allele ratio" into a number with a confidence interval.

For the NMD-competence prediction, cite Kurosaki, Popp and Maquat, ["Quality and quantity control of gene expression by nonsense-mediated mRNA decay"](https://pmc.ncbi.nlm.nih.gov/articles/PMC6855384/), *Nat Rev Mol Cell Biol* 2019.

### 7.2 Verified prices

All checked 5 September 2026 by direct vendor fetch. Thermo Fisher and LI-COR geolocated to the Netherlands and returned EUR list prices; those are marked.

**Material**

| Item | Catalogue | Pack | Price | Source |
|---|---|---|---|---|
| `GM21284` LCL | Coriell NIGMS | 1 frozen ampoule | **$262** US academic / $448 international | [catalog](https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=GM21284) |
| `NA21284` genomic DNA, same subject | Coriell NIGMS | 1 | **$172** / $352 | [catalog](https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=NA21284) |
| `GM22004` + `GM22005` + `GM22006` trio | Coriell NIGMS | 3 ampoules | **$786** / $1,344 | [catalog](https://www.coriell.org/0/Sections/Search/Sample_Detail.aspx?Ref=GM22006) |
| Shipping surcharges | Coriell | per order | **+$20** dry ice, **+$10** international handling; shipped within 2 weeks of approved forms | [Ordering FAQ](https://www.coriell.org/1/Support/Ordering-FAQ) |

**Culture.** Our lines are **suspension LCLs in RPMI 1640 + 15% FBS**, not adherent fibroblasts, so they are cheaper and faster than the fibroblast figures below, which are given because the Kops fibroblast lines are the Route B alternative. DMEM high glucose (Gibco [11965092](https://www.thermofisher.com/order/catalog/product/11965092), 500 mL) €24.64; Pen-Strep ([15140122](https://www.thermofisher.com/order/catalog/product/15140122), 100 mL) €26.32; Trypsin-EDTA 0.25% ([25200056](https://www.thermofisher.com/order/catalog/product/25200056), 100 mL) €25.50; Corning T75 vented flasks ([430641U](https://ecatalog.corning.com/life-sciences/b2c/US/en/Cell-Culture/Cell-Culture-Vessels/Flasks/Corning%C2%AE-Cell-Culture-Treated-Flasks/p/430641U), case of 100) $424.22.

**FBS has no public price at any major supplier.** Gibco 16000044 and 26140079 are both quote-only. It is the largest and least transparent line item; budget roughly $400 to $600 per 500 mL at academic rates. Fibroblast culture runs about **EUR 350 to 400 per line per month** all-in; LCLs less.

**NMD inhibitors**

| Item | Catalogue | Pack | Price |
|---|---|---|---|
| **hSMG-1 inhibitor 11j (SMG1i)** | MedChemExpress [HY-124719](https://www.medchemexpress.com/hsmg-1-inhibitor-11j.html) | 1 / 5 / 10 mg | **$200 / $500 / $850** |
| Cycloheximide | Cayman [14126](https://www.caymanchem.com/product/14126) | 100 mg / 500 mg / 1 g | $33 / $50 / $66 |
| Emetine hydrochloride hydrate | Cayman [21048](https://www.caymanchem.com/product/21048) | 25 / 50 / 100 mg | $88 / $132 / $246 |
| Puromycin hydrochloride | Cayman [13884](https://www.caymanchem.com/product/13884) | 25 / 50 / 100 mg | $42 / $80 / $117 |
| Cycloheximide, ultrapure | Thermo/Alfa Aesar [J66901.03](https://www.thermofisher.com/order/catalog/product/J66901.03) | 1 g | EUR 92.00 list |

**RNA to cDNA**

| Item | Catalogue | Pack | Price |
|---|---|---|---|
| RNeasy Mini Kit | Qiagen [74104](https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/rna-purification/total-rna/rneasy-mini-kit) / 74106 | 50 / 250 preps | **$451 / $1,984** |
| QIAshredder | Qiagen [79654 / 79656](https://www.qiagen.com/us/products/discovery-and-translational-research/lab-essentials-and-accessories/qiashredder) | 50 / 250 | $137 / $601 |
| RNase-Free DNase Set | Qiagen [79254](https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/accessories/rnase-free-dnase-set) | 50 preps | **$170** |
| SuperScript IV RT | Thermo [18090010 / 18090050](https://www.thermofisher.com/order/catalog/product/18090050) | 10 / 50 rxn | EUR 141.00 / EUR 428.00 |

The on-column DNase step is not optional. Residual genomic DNA contributes a genuine 50:50 allele signal and would blunt the very ratio being measured.

**Sequencing**

| Route | What you get | Price |
|---|---|---|
| **Azenta/GENEWIZ [Amplicon-EZ](https://www.genewiz.com/public/services/amplicon-sequencing-services/amplicon-ez)** | 50,000 reads/sample, 150-600 bp amplicons, 2x300 bp, **no minimum**, 8 business days | **from $58/sample** US; **EUR 49 / GBP 43** on the [EU page](https://www.genewiz.com/en-gb/public/services/amplicon-sequencing-services/amplicon-ez) |
| **Illinois Carver Biotech core** ([rates](https://biotech.illinois.edu/dna-services-core/dna-services-pricing/)) | MiSeq Nano v2 500-cycle run | **$798** |
| same | Amplicon prep per sample | $92; **$22 each above 12 samples** |
| same | Sanger, single / 96-well plate | **$6.70 / $507** |
| Eurofins ([pricing](https://eurofinsgenomics.com/en/products/pricing/)) | Sanger reaction, plate (min 24) / tube | **$5.60 / $9.30** |
| Oxford Nanopore ([store](https://store.nanoporetech.com/us/)) | MinION Mk1D Pack; flow cell FLO-MIN114; SQK-LSK114 | $5,150; $840; $720 |

**Nanopore is not needed here.** The two variants sit 233 bases apart, comfortably inside one 600 bp Amplicon-EZ amplicon, so short reads phase them directly. Nanopore only earns its place if a future case has variants further apart than 600 bp.

**Antibodies and quantitative blotting**

| Item | Catalogue | Size | Price |
|---|---|---|---|
| **Mouse anti-BubR1, clone 9/BubR1** (the MVA-literature antibody) | BD [612503](https://www.bdbiosciences.com/en-us/products/reagents/western-blot-and-molecular-reagents/purified-mouse-anti-bubr1.612503) | 150 µg | **$580** |
| Rabbit recombinant anti-BubR1, EPR12259(2) | Abcam [ab183496](https://www.abcam.com/en-us/products/primary-antibodies/bubr1-antibody-epr19958-ab183496) | 100 µL | **$580** |
| Rabbit anti-BUB1B | Bethyl/Fortis [A300-386A](https://www.fortislife.com/products/primary-antibodies/rabbit-anti-bubr1-antibody/BETHYL-A300-386) | 100 µL / 10 µL trial | **$473 / $131** |
| BubR1 (D3A7) rabbit mAb | CST [4116S](https://www.cellsignal.com/products/primary-antibodies/bubr1-d3a7-rabbit-mab/4116) | 100 µL | **$317** |
| **Revert 700 Total Protein Stain Kit** | LI-COR [926-11010 / 926-11016](https://licorbio.com/reagents/revert-700-total-protein-stain-kits) | 20 / 50 mini blots | **EUR 173 / EUR 320** |
| IRDye 800CW goat anti-mouse | LI-COR [926-32210 / 925-32210](https://licorbio.com/reagents/irdye-800cw-goat-anti-mouse-igg-secondary-antibody) | 0.5 / 0.1 mg | EUR 236 / EUR 142 |
| IRDye 680RD goat anti-rabbit | LI-COR [926-68071 / 925-68071](https://licorbio.com/reagents/irdye-680rd-goat-anti-rabbit-igg-secondary-antibody) | 0.5 / 0.1 mg | EUR 236 / EUR 142 |

Take one mouse and one rabbit primary and run them on the same two-colour blot, so agreement between independent epitopes is the validation. **Total-protein normalisation is not optional for this question.** A single housekeeping band assumes the reference protein is unchanged across genotypes and across the inhibitor arm, and translation inhibitors break that assumption outright. Revert 700 works on existing blots with no special gels; Bio-Rad stain-free gels ([4568094](https://www.bio-rad.com/en-us/sku/4568094-4-15-criterion-tgx-stain-free-protein-gel-18-well-30-ul?ID=4568094)) require a compatible imager and are login-gated with no public price. Revert validated against housekeeping controls: [Anal Biochem 2023, doi:10.1016/j.ab.2023.115301](https://doi.org/10.1016/j.ab.2023.115301).

### 7.3 Total cost and elapsed time

Five lines (patient, two parents, two controls) x two conditions x three biological replicates = 30 samples.

| Block | Cost |
|---|---|
| Cells and DNA from Coriell (single case + trio) | $1,220 |
| Culture, 5 lines, 2 months (medium, FBS, plastics) | ~$4,000 (less for LCLs than the fibroblast figure) |
| NMD inhibitors (SMG1i 5 mg + cycloheximide + emetine) | ~$700 |
| RNA extraction, DNase, reverse transcription | ~$900 |
| PCR reagents and amplicon primers | ~$800 |
| Amplicon sequencing, ~100 submissions at $58 | ~$5,800 |
| Sanger cross-check, 120 reactions | ~$750 |
| Quantitative immunoblot (antibodies, Revert, gels, membranes) | ~$2,000 |
| **Total** | **~$16,200** |

**Range: about $13,000** if sequencing goes through a core at $22/sample plus one $798 MiSeq Nano run, **up to about $20,000** with a Nanopore phasing arm you almost certainly do not need.

**Elapsed time, one competent postdoc, cells in hand: 3 to 4 months, roughly 2.5 months FTE.** Thaw and expand five lines, 3 to 4 weeks. Primer design, validation on genomic DNA, SMG1i dose and timecourse, 2 to 3 weeks overlapping the expansion. Three biological replicates at one passage per week, 3 weeks. RNA to submission, 1 week. Amplicon-EZ turnaround, 8 business days. Immunoblots run in parallel with the sequencing wait, 2 to 3 weeks. Analysis and write-up, 1 to 2 weeks. Add Coriell's two-week shipping and the MTA signature time at the receiving institution, which is usually the longest single step and is entirely administrative.

Against that: the recruitment alternative is a disease with a few dozen documented cases worldwide, most of them children, many of whom have died. There is no world in which recruiting is faster or cheaper than $434 and a signature.

### 7.4 The design decisions that matter, and their sources

**Use matched genomic DNA as the 1:1 calibrator.** [Zhang, Sadee et al., *BMC Genomics* 2011;12:518](https://pmc.ncbi.nlm.nih.gov/articles/PMC3228908/) is the design template for ASE by amplicon sequencing. Amplify gDNA from the same line for every amplicon and correct the cDNA ratio by the inverse of the gDNA ratio; that removes PCR and sequencing allele bias. This is exactly why `NA21284` is worth its $172.

**Read depth sets your precision, and 50,000 is plenty.** The same paper quotes log2 error of **±0.16 (linear 0.895 to 1.117) at 1,000 reads** and **±0.10 (0.93 to 1.07) at 13,500 reads**. Target 10,000 to 15,000 reads per amplicon. Amplicon-EZ clears that roughly fourfold.

**Run independent PCR and library replicates, not just technical read replicates**, or the confidence intervals are wrong: [Nat Commun 2021;12:3327](https://pmc.ncbi.nlm.nih.gov/articles/PMC8184992/). This roughly doubles the submission count and is already in the $16,200 above.

**Correct reference-mapping bias**, which matters most at the missense site: [Castel et al., *Genome Biol* 2015;16:195](https://pmc.ncbi.nlm.nih.gov/articles/PMC4574606/). For expected effect sizes of ASE on protein-truncating variants generally, [Rivas et al., *Science* 2015;348:666](https://pmc.ncbi.nlm.nih.gov/articles/PMC4537935/).

**Prefer a selective SMG1 inhibitor over cycloheximide as the primary NMD arm.** Cycloheximide and emetine block translation globally and trigger a stress response, which confounds any downstream protein readout. The closest published analogue to this exact experiment, biallelic splice variants in a neurodevelopmental gene with NMD blocked in patient cells then RT-PCR and Sanger, used **SMG1i 11j (MedChemExpress HY-124719) at 0.5 µM in DMSO for 20 h**: [*HGG Advances* 2026, PMC12670907](https://pmc.ncbi.nlm.nih.gov/articles/PMC12670907/). At $200 for 1 mg (MW 566), one milligram makes about 3.5 mL of 0.5 mM stock, far more than 30 wells need. Keep cycloheximide and emetine as orthogonal confirmations. A published emetine arm on patient fibroblasts: **100 µg/mL for 4 h**, [*EJHG* 2022, PMC9259687](https://pmc.ncbi.nlm.nih.gov/articles/PMC9259687/).

**Expect the protein percentage and the mRNA ratio to disagree, and treat that gap as the finding.** Suijkerbuijk et al. showed BUBR1 missense mutants have roughly **2-fold faster protein turnover** than wild type under 5 h cycloheximide. So residual BubR1 is not a mirror of residual transcript. The distance between the two numbers is the mechanistic result, and it is the reason to measure both in the same cells rather than inferring one from the other.

### 7.5 Still unpriced, and I am saying so

Sigma-Aldrich/Merck (C7698, C4859, E2375, P8833) refuses automated access; Cayman substitutes are quoted above and are not the same SKUs. Tocris 0970 and bio-techne timed out. Selleck E0869 (SMG1i) is JavaScript-gated. Gibco FBS is quote-only at every supplier. Azenta/GENEWIZ Sanger is contact-form only in any currency. Bio-Rad 4568094 stain-free gels are login-gated. LI-COR and Thermo figures are EUR because the fetch geolocated to the Netherlands; USD will differ. Only one core facility (Illinois) publishes MiSeq Nano, amplicon prep and Sanger rates together; Utah covers only the newer MiSeq i100 generation, and Harvard's DF/HCC DNA Resource Core is permanently closed to new Sanger samples.

---

## 8. Why no public dataset can substitute

To measure allele-specific expression of *BUB1B* you need two things at once: RNA from a compound-heterozygous individual, and reads long enough to carry a heterozygous marker. Nothing public has both.

| Public dataset | Genotype | Assay | Read length | ASE possible? |
|---|---|---|---|---|
| `GSE22206` | *BUB1B* homozygous | Illumina beadchip | n/a | **No.** No reads to phase, and homozygous, so allelic expression is undefined |
| `PRJNA915310` | MVA, *MAD2L1BP* | Whole-exome, DNA | ~100-155 bp PE | **No.** DNA |
| `GSE197267` | MVA, *MAD1L1* | 10x scRNA-seq, PBMC | ~90 bp, 3'-biased | **No.** Wrong gene, and 3'-only reads never reach the coding variants |
| `PXD035765` | MVA, *MAD1L1* | LC-MS/MS | n/a | **No** |

The two datasets that could answer it are both unpublished, and both are one email away rather than one download away:

- **Kops lab, CENATAC study.** MVA patient RNA-seq exists and is explicitly withheld: "RNAseq data from the patient and control subject cannot be made publicly available for reasons of patient confidentiality. Qualified researchers may apply for access to these data, pending institutional review board approval." Wrong gene for our purposes, but the same lab holds the *BUB1B* fibroblasts.
- **Saitsu lab.** Patient RNA-seq plus nanopore adaptive-sampling long reads on a compound-heterozygous *BUB1B* MVA girl. Never deposited, no data availability statement, and DDBJ/JGA/GEA return zero. That is the single most on-target dataset in existence and it is on a hard drive in Hamamatsu.

---

## 9. Searches that returned nothing, so nobody repeats them

**Cell repositories.** Cellosaurus (`api.cellosaurus.org`) for `BUB1B`, `"mosaic variegated aneuploidy"`, `"premature chromatid separation"` (0 results), `CEP57`, `TRIP13`, `aneuploidy syndrome`. Every MVA-annotated line resolves to Coriell; no ECACC, JCRB, RIKEN BRC, DSMZ, ATCC, KCLB or CCRID cross-reference exists for any of them. EuroBioBank's downloadable aggregate catalogue: zero hits for `variegated`, `BUB1B`, `chromatid`, `aneuploid`, `257300`.

**Not resolvable, flagged rather than concluded.** The ECACC catalogue (`culturecollections.org.uk`) is JavaScript-only; every server-side query returned the country-selector shell, and the old `/products/celllines/search/` path 404s. Suijkerbuijk 2010 says MVA LCLs came from "ECACC or Coriell", and Yost 2017 cites ECACC `96061307` for a *TRIP13* line, so ECACC plausibly holds MVA1 material that Cellosaurus has not indexed. **This needs a human to email ECACC.** The Telethon Network (`biobanknetwork.telethon.it`) and Rare Disease HUB (`rd-hub.eu`) did not resolve at all from here. Treat all three as open, not as negative.

**Literature.** Europe PMC for `GM21284` (7 hits, all a mouse lncRNA of the same name), `GM21284 AND BUB1B` (0), `"753X" AND BUBR1` (1, the 2010 paper), `"R814H" AND BUBR1` (4, none new), `BUB1B AND "allele-specific expression"` (0 usable).

**GEO** (`db=gds`): `"mosaic variegated aneuploidy"` (8, all accounted for), `"premature chromatid separation"`, `"variegated aneuploidy"`, `"MVA syndrome"`, `BUB1B AND patient`, `BUBR1 AND (patient OR proband)`, `BUB1B AND (lymphoblastoid OR LCL)` (1, GSE22206 only), `"aneuploidy syndrome" AND lymphoblastoid` (0), `CENATAC`, `CCDC84`, and each of `GM21284`, `GM22006`, `GM14084`, `GM21654`, `GM21655`, `GM22004` (0 each).

**SRA** (`db=sra`): all of the above terms returned **0**, without exception.

**BioSample**: only `SAMN00806086` / `SAMN00806084`, Coriell catalogue registrations for GM22006 and GM22004 with no linked data.

**ENA portal API** (`result=study`): `*mosaic variegated aneuploidy*`, `*premature chromatid separation*`, `*MVA syndrome*` → 0 rows each.

**ArrayExpress / BioStudies**: `"mosaic variegated aneuploidy"` in the arrayexpress collection → 1 hit, `E-GEOD-22206`, the mirror of GSE22206. `CENATAC` → 0.

**PRIDE / ProteomeXchange**: `"premature chromatid separation"` → 0. `BUB1B`, `BUBR1` → cell lines and yeast only. MassIVE PROXI filter → 404.

**Ribosome profiling**: RPFdb unreachable, GWIPS-viz JS-only. Both index GEO/SRA submissions, and SRA is empty for every MVA term, so there is by construction no MVA or *BUB1B* patient ribosome profiling.

**dbGaP**: `BUB1B` → 0. `"mosaic variegated aneuploidy"` → 30 variable records, all inside `phs001557`, which is somatic mosaicism, not the syndrome.

**EGA**: browse UI for `mosaic variegated aneuploidy` → no matching studies. The only EGA accession any MVA paper cites is `EGAS00001000971`, which is the ICR1000 UK **control** exome series.

**DDBJ / JGA / GEA**: `jga-study`, `jga-dataset`, `gea` each returned total 0 for `mosaic variegated aneuploidy`, `BUB1B`, `premature chromatid separation`, `MVA syndrome`.

**OmicsDI** (federating GEO, ArrayExpress, PRIDE, MassIVE, jPOST, iProX, ENA, dbGaP, EGA): `"mosaic variegated aneuploidy"` → 51, of which the only real datasets are the ones already listed. Independent confirmation of the per-repository sweep.

**Rare disease programmes**: `"100,000 Genomes Project" AND ("mosaic variegated aneuploidy" OR BUB1B)` → 6 hits, all abstracts or unrelated cancer papers. `"Undiagnosed Diseases Network" AND (BUB1B OR "mosaic variegated aneuploidy")` → 2, both irrelevant. GREGoR dbGaP search → 4 unrelated study records, no *BUB1B* or MVA study. Genomics England does now hold blood RNA-seq at scale (5,412 rare disease individuals, 2026), but only inside the Research Environment under a Data Access Agreement, and no MVA or *BUB1B* case appears in any public output.

**Data availability statements checked and found empty**: CEP57/Snape 2011 (PMC3508359, RefSeq IDs only), TRIP13/Yost 2017 (PMC5493194, "available within the paper"), CDC20 progeria 2020 (PMC7681047, "on reasonable request"), SMC5/MVA 2025 (PMC12691382, "on reasonable request"), biallelic *BUB1* 2022 (PMC8769543, none), Hanks 2004, Matsuura 2006, Suijkerbuijk 2010, Ochiai 2014 (all predate or ignore deposition mandates).

---

## 10. What to do, in order

1. **Order today.** `GM21284` ($262) + `NA21284` gDNA ($172) + the `GM22004/5/6` trio ($786). Total **$1,220** US academic. One MTA (Form 1401-65 Rev D) and one Statement of Research Intent (Form 1401-05 Rev K), both institutionally signed. Ordering page: https://www.coriell.org/1/NIGMS/How-to-Order
   Coriell states standard catalogue orders are "typically shipped within 2 weeks once all required forms are submitted and the order has been approved". Catalogue prices exclude shipping; frozen orders carry a $20 dry-ice charge and international orders a $10 special-handling fee ([Ordering FAQ](https://www.coriell.org/1/Support/Ordering-FAQ)). Couriers are FedEx or Quick.
2. **Sequence the trio's *BUB1B* first.** Coriell prints the genotype for `GM21284` but not for `GM22006`. Yost 2017 identifies `GM22006` as the biallelic *BUB1B* patient; confirm it and recover both variants before designing the amplicon.
3. **Two emails, sent the same day, cost nothing.** Geert Kops (g.kops@hubrecht.eu) for the four MVA fibroblast genotypes of Suijkerbuijk 2010, which would take n from 1 to 4 and add a non-lymphoid cell type. Hirotomo Saitsu (hsaitsu@hama-med.ac.jp) for the undeposited patient RNA-seq and nanopore data.
4. **One email to ECACC**, because the catalogue cannot be queried from outside and two papers imply it holds MVA material.
5. **Run the assay.** Vehicle versus SMG1i 11j at 0.5 µM for 20 h as the primary NMD arm, with cycloheximide and emetine as orthogonal confirmations. One ~350 bp cDNA amplicon spanning both variant sites, independent PCR and library replicates, matched genomic DNA as the 1:1 allelic-balance calibrator, and a two-colour quantitative BubR1 immunoblot with Revert total-protein normalisation against age-matched controls.

The frameshift allele terminates at codon 753 of 1050, in roughly exon 17 of 23 on the canonical transcript `ENST00000287598`. That premature stop sits far upstream of the last exon-exon junction, so the allele is NMD-competent on the standard rule and the inhibitor arm should move it. If it does not, that is a result too.

---

## 11. Caveats worth stating out loud

- `GM21284` and `GM22006` are **EBV-transformed lymphoblastoid lines**. Immortalisation and long passage can distort both transcript abundance and mitotic phenotypes. `GSE22206` shows the size of the tissue effect in the same person: *BUB1B* at 66% of control in LCL and 94% in fibroblast. Report LCL numbers as LCL numbers.
- `GM14084` is the only catalogued MVA **fibroblast** line and its causal gene is not identified. It may not be *BUB1B* at all.
- The measurement is n=1, or n=2 with the second family. That is what a disease affecting a few dozen documented people permits. Framing matters more than sample size here: this is a first observation, not a study.
- Coriell restricts secondary distribution. Read the policy before promising anyone a vial.
- Expect the mRNA ratio and the protein percentage to disagree. Suijkerbuijk et al. measured roughly 2-fold faster turnover for missense BubR1 mutants, so residual protein is not a mirror of residual transcript. Measure both in the same cells; do not infer one from the other.
