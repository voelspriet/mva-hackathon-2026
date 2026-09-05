# Q5. Is there a published within-subject repeatability figure for the aneuploid fraction itself?

**Asked because** the measurement gate leads with interphase FISH, and section 8 gives it the best figure of the three endpoints, 22 percent. Q4 derived a within-subject biological coefficient of variation for micronuclei from two primary sources. The FISH row needs its own, because a fraction of aneuploid cells and a frequency of micronuclei are different quantities measured in different ways.

## Answer

**Nothing was found. This is a documented dead end, and it makes the FISH row weaker than the report presents it, not stronger.**

No study was located that measures the aneuploid fraction by interphase FISH twice in the same healthy people and reports the agreement between the measurements. The nearest approaches are all missing at least one of the three things needed: same subjects, repeated in time, and a stated variance or correlation.

### What exists, and why each one fails

| Study | What it has | What it lacks |
|---|---|---|
| Auer 1999, Br J Haematol 104:742, PMID 10192434 | The closest match found. Interphase FISH for trisomy 12 in 85 patients with chronic lymphocytic leukaemia in 1993/94, **repeated in 41 of them in 1996/97**, reporting that "over the 4-year period there was no significant change in the percentage of trisomic cells" | It is a leukaemic clone, not constitutional mosaicism; the interval is four years, not the twelve weeks the gate design uses; and "no significant change" is a hypothesis test, not a variance estimate. It bounds drift, not measurement-to-measurement noise |
| Mukherjee 1996, Mech Ageing Dev 90:145, PMID 8869915 | Chromosome-specific aneuploidy by interphase FISH in 30,032 cells from 12 healthy donors across age groups | Between-subject and cross-sectional. Each donor measured once |
| Sperm aneuploidy FISH literature | The field where repeated sampling of the same men is routine | Every retrieved record was a case report, a patient series, or a study of teratozoospermia. None reported an intra-individual repeatability coefficient for aneuploidy frequency |
| Micronucleus literature (Q4) | A genuine test-retest design with usable correlations | Measures micronuclei, not aneuploid fraction. The two are related but not the same quantity, and a micronucleus can arise from a chromosome fragment as well as from a whole chromosome |

### What this changes in the report

Section 8's FISH row states a coefficient of variation of 10.7 percent, being a 9.49 percent binomial counting term and a 5 percent hybridisation and scorer term, with **biological variance set to zero**. That is now known to be the only one of the three rows with no biological term at all, and the only endpoint for which no biological term can be sourced from anywhere.

The report already prints what happens when the micronucleus biological term is imported into it: 22 percent becomes 41 percent. What the report should say, and now does, is that this import is a borrowing across assays rather than a measurement, and that the FISH row's apparent advantage over the other two endpoints is an artefact of a missing term rather than a property of the assay.

**The practical consequence for the gate.** The gate leads with FISH partly because section 8 makes it look like the most sensitive endpoint. On the evidence, it is the endpoint whose sensitivity is least well characterised. That does not remove it from the gate, because its counting properties are genuinely good and the aneuploid fraction is the quantity of interest. It does mean the gate should measure its own repeatability before anyone treats 22 percent as a design number: two baseline draws before any intervention, which costs one extra blood draw and answers the question for this child directly.

### Correction applied

`REPORT_track2.md` section 8 now states that no within-subject repeatability figure for the aneuploid fraction exists in the literature, that the 41 percent figure is a borrowing from the micronucleus assay, and that a second baseline draw would settle it for this child at the cost of one venepuncture.

## Routes tried

PubMed esearch across seven query formulations: interphase FISH aneuploidy in lymphocytes combined with reproducibility, repeatability, intraindividual and within-subject; FISH aneuploidy with interlaboratory variability; aneuploidy frequency with longitudinal, repeated measures and temporal variation; FISH aneuploidy baseline frequency in healthy donors with coefficient of variation; and three formulations across the sperm aneuploidy literature including an author search. Four of the seven returned no records at all. Every record returned by the other three was screened at abstract level via NCBI efetch.
