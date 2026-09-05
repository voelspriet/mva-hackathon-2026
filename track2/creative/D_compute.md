# D. What can still be computed, and what it changes for drug selection

Everything below was executed on this machine on 5 September 2026. Scripts are in
`pipeline/track2_compute/`, intermediate outputs in `work/track2/`. The patient VCF was read
locally only. Network use was limited to reading static public files: the AlphaMissense bulk
tables, the AlphaFold model for O60566, and gnomAD v4.1 sites files by HTTP range. No patient
coordinate was submitted to any query API.

Evidence tiers: **computed**, **database**, **inference**.

---

## 1. The stop-codon context of c.2210T>G, from the local FASTA

Computed. The CDS of ENST00000287598 was rebuilt from the Ensembl 116 GFF3 and the chr15 FASTA,
3,153 nt over 23 blocks. Genomic 15:40209701 is c.2210, codon 737. Wild-type codon TTA, mutant
codon **TGA**. Context: `CCAGAG | TGA | AGTGCC`, so the **-1 base is G and the +4 base is A**.
The PTC lies 747 nt upstream of the last CDS junction with 6 downstream junctions, which
reproduces the dossier's NMD geometry independently.

What it changes. Readthrough drugs are not context-neutral. UGA is the most readthrough-permissive
of the three stop codons, so the allele is in the responsive class rather than the refractory one.
The +4 base ranks in the middle: the published efficiency order is C > U > A > G, so a +4 A is
neither the best nor the worst case (**inference** from the context hierarchy; no measurement on
this allele). The practical consequence is that ataluren, gentamicin and amikacin all have a
mechanistically coherent target here, whereas a UAA allele would have argued for dropping the
whole class. Because the predicted response is mid-range rather than high, a readthrough assay on patient cells
should precede any drug trial.

Limits. Context rules come from reporter constructs, not from BUB1B. Ataluren's mechanism remains
contested and its EU conditional authorisation for nonsense-mutation DMD was not renewed.

## 2. What a readthrough product would actually be

Computed. Translating through the PTC in frame, **the next in-frame stop is the native terminator
at codon 1051**. A readthrough event therefore yields full-length BubR1 with a single substitution
at residue 737, not a truncated or extended protein. Near-cognate decoding of UGA inserts Trp, Cys
or Arg. AlphaMissense protein-level scores for exactly those three products, pulled from the public
substitution table for O60566:

| Readthrough product | AlphaMissense | Call |
|---|---|---|
| L737W (Trp) | 0.150 | benign |
| L737R (Arg) | 0.189 | benign |
| L737C (Cys) | 0.322 | benign |

Every one of the 18 substitutions at 737 scores below 0.36, the highest being L737D.

What it changes. This is the strongest new argument for the readthrough arm. If readthrough
succeeds, the product is predicted to be a functionally intact protein, so the intervention
restores dosage rather than producing a dominant-negative or a kinase-domain-less fragment. The
counter-argument that "readthrough would only give you a broken protein" does not survive the
computation. It also reframes NMD inhibition: a stabilised transcript is useful only combined with readthrough,
since on its own it still terminates at 737 and drops the whole kinase domain (766 to 1050).

Limits. AlphaMissense is a pathogenicity predictor, not a stability or activity assay, and it was
not trained on readthrough products. Tier: computed prediction, inference for the therapeutic step.

## 3. AlphaMissense for p.Asn1002Lys, calibrated against alleles with functional data

Computed. The BUB1B slice of the AlphaMissense hg38 table holds 6,940 scored missense SNVs.
**N1002K scores 0.9229, likely pathogenic, the 96.0th percentile of the gene and the 95.7th of the
kinase domain.** Seventeen of the 18 substitutions at 1002 are called pathogenic, the exception
being N1002S at 0.35, so the position itself is strongly constrained.

The calibration matters more than the raw score. Scoring the MVA alleles that Suijkerbuijk 2010
tested functionally:

| Allele | AlphaMissense | Published behaviour |
|---|---|---|
| N1002K | 0.923 | this case, untested |
| L1012P | 0.872 | low protein level, rescued by overexpression |
| Q921H | 0.491 | indistinguishable from wild type |
| I909T | 0.451 | low level, rescued by overexpression |
| L844F | 0.292 | 5 to 10 fold reduced level |
| R814H | 0.221 | MVA allele |
| Y155C | 0.538 | normal protein level |
| R550Q | 0.066 | normal protein level |

What it changes. AlphaMissense ranks N1002K above every characterised MVA kinase-domain allele
including L1012P, the one modelled in mouse. But the same table scores L844F and R814H, both real
patient alleles with measurable protein loss, as likely benign. **Inference:** on this gene
AlphaMissense has poor sensitivity for the destabilising class, so its high call on N1002K raises
the prior that the variant is damaging, while its low calls elsewhere mean a low score would not
have exonerated anything. For drug selection this supports treating the case as a genuine biallelic
loss-of-dosage genotype, which is the premise every expression-directed and readthrough idea rests
on. It is not evidence for the specific-defect class over the destabilising class, and the
distinction matters: a destabilising allele is a chaperone or proteasome target, a specific-defect
allele is not.

## 4. Where N1002 sits in the AlphaFold structure

Computed from AF-O60566-F1 v6 (v4 has been withdrawn; the API resolves to v6). Residue 1002 has
**pLDDT 91.1**, so the local model is confident even though the whole-chain figure is 63.6. It has
16 CB neighbours within 10 A, the 38th percentile of the kinase domain, so it is **partially
exposed rather than buried**. Minimum heavy-atom distance to the PLK1 site T1008 is **9.14 A**, and
to L1012 **10.35 A**. Its 8 A neighbour set is almost entirely local in sequence (977, 978, 998 to
1004).

What it changes. Two mechanisms can be separated. A surface residue 9 A from T1008 with only local
packing is a weak candidate for a folding-core destabiliser, and a better candidate for a local
surface or phospho-recruitment effect. That argues **against** leaning hard on chaperone or
proteasome modulation as the allele-directed strategy for this variant, and **for** treating the
nonsense allele as the more tractable drug target of the two. By contrast L1012, the reference MVA
allele, has 26 CB neighbours and is buried, which is consistent with its published destabilising
behaviour. **Inference:** N1002K and L1012P are unlikely to act by the same mechanism, so mouse
BubR1-L1002P data should not be transferred to this patient without qualification.

Limits. AlphaFold is a single static monomer prediction with no ligand, no PLK1 docked, and no
experimental human BubR1 kinase-domain structure to check against. Burial by neighbour count is a
proxy for solvent accessibility, not a computed SASA.

## 5. Structural variant or CNV over BUB1B: excluded within the resolution available

Computed. Across chr15 in 50 kb bins, the two bins covering BUB1B show depth ratios of 0.97 and
1.06 against a chr15 PASS-SNP median depth of 44, with heterozygous fractions of 0.50 and 0.78.
Within the gene there are 7 heterozygous calls spread from 40,168,264 to 40,220,612, with variant
allele fractions of 0.50, 0.54, 0.50, 0.57, 0.54, 0.39 and 0.46. The two reported alleles are
balanced: 21/25 reads and 15/13 reads.

What it changes. A heterozygous deletion covering the gene body would remove heterozygosity and
depress depth; neither is present. The readthrough and dosage arguments therefore rest on two
point alleles and not on a hidden third hit, and residual BubR1 is expected to come from both
alleles rather than from one. It also removes a competing explanation for the phenotype that would
have redirected the whole drug question.

Limits. This is a variant-site depth proxy from a filtered VCF, not read-depth coverage from BAM.
It can exclude a deletion spanning tens of kilobases; it cannot exclude a single-exon deletion, a
balanced rearrangement, a deep intronic splice variant, or a promoter or upstream regulatory
variant of the kind that resolved the "monoallelic" Japanese families. BUB1B does not fall inside
any of the runs of homozygosity visible on chr15 at 40.45 to 40.70 Mb and 41.15 to 41.20 Mb.

## 6. Rare variants in the BubR1 network, the NMD machinery, and drug-handling genes

Computed. Gene spans for 80 SAC, PP2A, APC/C, BubR1-abundance and NMD or EJC genes, and 40
pharmacogenetic and tubulopathy genes, were built from the GFF3 and screened. Results that change
a drug decision:

- **MT-RNR1 is clean.** Mitochondrial coverage is about 4,000x. The only calls in the 12S rRNA gene
  are the common haplogroup variants m.750A>G and m.1438A>G, both homoplasmic. **m.1555A>G,
  m.1494C>T, m.1095T>C and m.827A>G are absent.** This is the single most actionable result here: it
  removes the mitochondrial contraindication to aminoglycoside readthrough with gentamicin or
  amikacin. Limit: a germline caller may miss low-level heteroplasmy, and aminoglycoside
  nephrotoxicity remains a separate and serious objection in a child with nephrocalcinosis.
- **CYP3A5 rs776746 is homozygous (*3/*3), a non-expressor.** Relevant if sirolimus or everolimus
  is used: standard weight-based dosing applies, with no upward adjustment for a CYP3A5 expresser.
  Tier: database genotype, guideline-level pharmacogenetics.
- **CYP2C19 rs12769205 heterozygous, a practice-guideline no-function allele**, so intermediate
  metaboliser status. Marginal for this case.
- **G6PD is normal.** The male sample (chrX depth 23 versus 45 autosomal, chrX heterozygosity 0.06,
  chrY present) carries only benign G6PD variants, so hydroxychloroquine and related agents face no
  G6PD bar.
- **DPYD rs1801160 heterozygous.** ClinVar shows an expert-panel drug-response record, but the
  allele frequency computed from gnomAD is 4.7 percent and CPIC assigns it normal function. **No
  fluoropyrimidine dose reduction is indicated.** Recorded because it is the kind of hit that gets
  over-called.
- **Only one rare non-dbSNP coding variant fell in the entire 80-gene network and NMD list**
  (ANAPC2 missense, heterozygous). Nothing in UPF1/2/3, SMG1/5/6/7, ETF1, GSPT1 or the EJC core
  modifies the NMD prediction.

Two leads were raised and then closed by computation, which is worth recording:

- **RBM8A c.-21G>A (rs139428292), heterozygous**, is the TAR-syndrome hypomorphic EJC allele and
  sits in the core NMD machinery. A dosage screen of 1q21.1 in 100 kb bins found depth ratios of
  0.80 to 1.19 and retained heterozygosity of 0.53 to 0.98 across 145.3 to 146.0 Mb, so **there is
  no 1q21.1 deletion in trans**. gnomAD gives AF 2.6 percent with 583 homozygotes, so the allele
  cannot reduce RBM8A output much. **Inference:** NMD efficiency in this patient should be assumed
  normal, which keeps the "no truncated protein" premise intact and keeps NMD inhibitors in the
  same weak position they started in.
- **SLC34A1 p.Ala133Val (rs148976897), heterozygous**, appears under Nephrocalcinosis and Infantile
  hypercalcemia 2 in ClinVar. It resolves to Likely benign in 7 of 8 submissions, with gnomAD AF
  0.41 percent and 21 homozygotes. It does not explain the nephrocalcinosis and should not change
  vitamin D or phosphate management.

## 7. What would move the needle next and is not computable here

A BAM would give read-backed phasing attempts, exon-level BUB1B coverage and low-level
mitochondrial heteroplasmy calling; parental samples would settle trans configuration, currently an
inference from allele frequencies alone. Neither is in this dataset. An RNA sample would convert
every NMD statement above from prediction to measurement, and is the single measurement that most
changes the readthrough case.
