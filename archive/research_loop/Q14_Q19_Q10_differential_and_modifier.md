# Q14, Q19 and Q10: the widened differential, and the last modifier hypothesis

Three related completeness questions, answered together because they share sources.

---

## Q14. What is the biallelic *BUB1* disorder, and does it change the differential?

The Neuropediatrics 2025 conference abstract that prompted this question is a follow-up on two patients first published in full: **Carvalhal S, Bader I, Rooimans MA, Oostra AB, Balk JA, Feichtinger RG, Beichler C, Speicher MR, van Hagen JM, Waisfisz Q, van Haelst M, Bruijn M, Tavares A, Mayr JA, Wolthuis RMF, Oliveira RA, de Lange J. "Biallelic BUB1 mutations cause microcephaly, developmental delay, and variable effects on cohesion and chromosome segregation." Sci Adv 2022;8(3):eabk0114, PMID 35044816, PMC8769543**, open access. Gulbenkian, Amsterdam UMC, Salzburg and Graz; no overlap with the Utrecht or Institute of Cancer Research groups.

The clinical picture is microcephaly and intellectual disability with patient-specific features, and the authors note it "partially resemble[s] previously described syndromes, including autosomal recessive primary microcephaly, mosaic variegated aneuploidy, and cohesinopathies".

**The mechanistic detail is what matters here, and it independently corroborates the Q21 finding.** The abstract states that both patients' cells show "prolonged mitosis duration, chromosome segregation errors, and **an overall functional spindle assembly checkpoint**", with the aneuploidy arising instead because impaired kinase activity "prohibits centromeric recruitment of Aurora B, SGO1, and TOP2A, correlating with anaphase bridges, aneuploidy, and defective sister chromatid cohesion".

So here is a gene that produces mosaic aneuploidy **with the checkpoint intact**. Yost 2017 established that embryonal tumour risk in this syndrome tracks severe checkpoint impairment, not aneuploidy as such: *BUB1B* and *TRIP13* abolish the checkpoint and carry the tumour risk, *CEP57* and unknown-cause MVA leave it largely intact and do not. Biallelic *BUB1* is a third, independent data point that fits: aneuploidy present, checkpoint functional, and the reported phenotype is neurodevelopmental rather than oncological.

**That is a testable prediction rather than an established fact**, on two patients, and it is recorded as such.

## Q19. Does the wider differential change anything for this child?

**No, and the reason is worth stating rather than assuming.** This child's genotype is settled by three independent routes: the challenge's own scorer, a phenotype-driven ranking with no gene list supplied, and live retrieval of the ClinVar and gnomAD records for both alleles. A differential matters when the gene is in doubt. It is not.

Where it does matter is the report's claim to transfer to other families, and section 11 already carries the consequence after Q21: the gene set is *BUB1B*, *CEP57*, *TRIP13*, *CENATAC*, *KNL1* and *ZWINT*, plus mosaic variegated aneuploidy now reported as a feature of Mulibrey nanism from biallelic *TRIM37* and of recessive *SMC5* variants, and **the split is prognostic**. Biallelic *BUB1* is added to the low-checkpoint-impairment side of that split on the evidence above.

**One practical consequence for a transferred pipeline:** a child with mosaic aneuploidy, microcephaly and developmental delay but no tumour is a different prior from this child. The checkpoint assay discussed in section 4 distinguishes them, which is a second use for a measurement the gate already proposes.

## Q10. Is the *SGO1* variant anything?

**No. The hypothesis is closed rather than carried forward.**

The re-analysis found *SGO1* c.1273A>G p.Thr425Ala in this child, heterozygous, at gnomAD allele frequency 2.7e-6 in exomes and 1.3e-5 in genomes, absent from ClinVar. It was the only entry with a mechanistic story, since shugoshin protects centromeric cohesion and this is a chromosome segregation disorder. Four things kill it.

1. **The residue sits in a disordered region.** UniProt Q5FBB7 places residues 348 to 441 in a disordered region; residue 425 is threonine, in the threonine- and proline-rich stretch EGSKPTKTPTTTPPE. It is not in a domain, not in either D-box motif at 438-446 or 457-465, not in the KEN box at 310-312, not in the PP2A-interaction region at 1-176, and not an annotated phosphosite; the nearest annotated phosphoserine is 436.
2. **Threonine to alanine in a disordered stretch is a conservative change** at a position with no annotated function.
3. **Heterozygous, with no second hit.** *SGO1*-related disease is recessive.
4. **The gene set is depleted, not enriched.** The checkpoint and decay network carries one rare coding variant where its coding length predicts nine.

**The one thread that remains, and it is thin.** The biallelic *BUB1* paper reports that loss of BUB1 kinase activity prevents centromeric recruitment of SGO1, so the two genes act in one pathway. That makes SGO1 a plausible place for a modifier in principle. It does not make this variant one, and nothing above changes.

---

## Corrections applied

Section 11's differential gains biallelic *BUB1* on the functional-checkpoint side of the prognostic split, with the caveat that it rests on two patients. No other change: the differential does not affect this child, and the *SGO1* hypothesis is recorded as closed in the re-analysis file rather than promoted into the report, where it never appeared.

## Access levels reached

Full abstract for Carvalhal 2022 via NCBI efetch; the paper is open access in PMC. UniProt Q5FBB7 retrieved live through the REST API for the domain, motif and modified-residue annotations and the sequence.
