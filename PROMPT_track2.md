# Prompt: Track 2, drug repurposing for PROBAND01

## Facts

- Genotype (Track 1, verified by the organisers' scorer): BUB1B compound heterozygous. Allele 1: c.2210T>G p.Leu737Ter, exon 17 of 23, ClinVar pathogenic/likely pathogenic for MVA syndrome 1. Allele 2: c.3006T>G p.Asn1002Lys, exon 23 of 23, in the C-terminal kinase domain, gnomAD allele count 1 of 1,461,878, no ClinVar record.
- Mosaic aneuploidy in the sequenced sample: not detected above about 10% of cells (per-chromosome BAF and depth, 44x WGS).
- Phenotype terms: HP:0002859 rhabdomyosarcoma, HP:0000121 nephrocalcinosis, HP:0004322 short stature, HP:0001508 failure to thrive, HP:0003202 skeletal muscle atrophy, HP:0001622 premature birth, HP:0001518 small for gestational age, HP:0200067 recurrent spontaneous abortion (parental history).
- Scope set by the organisers: market-approved medications only; combinations allowed; investigational compounds are out of scope. Judged on scientific rigor 35%, potential impact 25%, innovation 25%, scalability 15%. Deliverables: report (PDF or MD), GitHub repo, 3-minute video. Three uploads; the panel reads the last one.
- Constraints: no contact with the family or the MVA Society. Public sources only. Every statement in the report carries a citation that can be checked. Generative AI use is recorded (Anthropic, Claude Code, Max plan, sharing disabled).

## Questions

1. Mechanism. What does the literature say about BubR1 function, the consequence of a premature stop at codon 737 (nonsense-mediated decay versus truncated protein), and the role of the C-terminal kinase domain? What is known about compound heterozygous null plus missense genotypes in MVA1 relative to other genotypes (residual protein level, phenotype severity)? Is the kinase domain catalytically active, and does a lysine substitution at position 1002 have a predicted effect on folding or stability?
2. Consequences. Which downstream processes are altered by reduced BubR1: spindle assembly checkpoint strength, chromosome mis-segregation rate, aneuploidy tolerance, cellular senescence and p16/p19 accumulation, DNA damage response, growth signalling, tumour formation? Which of these have been measured in BUB1B patient cells or in Bub1b hypomorphic mice?
3. Interventions in models. Which interventions changed outcomes in Bub1b hypomorphic or mutant mice or in patient-derived cells: genetic (p16 removal, senescent cell clearance, BubR1 overexpression), pharmacological (list every compound tested, dose, outcome, whether market-approved)? Which market-approved drugs act on the same targets as compounds that worked in models?
4. Clinical care. What do published management guidelines or case series for MVA recommend for cancer surveillance, growth, renal calcification, nutrition? Which approved drugs are already used in this population and with what evidence?
5. Candidates. For each candidate market-approved drug or combination: target, mechanism relating to items 1-3, evidence tier (human MVA, human other, animal BubR1 model, cell model, inference), paediatric approval status and dosing, interactions with the phenotype (renal calcification, low muscle mass, cancer history and treatment), the risk that the drug worsens chromosome segregation or promotes aneuploid cell survival, and a measurable readout that would test the hypothesis (for example micronucleus frequency in blood lymphocytes, p16 expression, senescence markers).
6. Harms. Which candidates carry a plausible harm in a child with a checkpoint defect and a cancer history (for example drugs that are themselves aneugenic, immunosuppressive, or growth-promoting)?
7. Family perspective. From public statements by MVA families and the MVA Society (published text only, no contact), what outcomes do families report as priorities, what burdens do current treatments carry, and how do those priorities rank the candidates?
8. Scalability. Which parts of the method (mechanism to target to approved-drug mapping, harm screen, readout selection) apply to another chromosomal instability disorder or another N-of-1 case?

## Procedure

1. Literature and database collection with citations (PubMed, OMIM 257300, Orphanet, ClinicalTrials.gov, DrugBank, Open Targets, ChEMBL, FDA and EMA paediatric labels).
2. Panel: five specialists (clinical geneticist, mitosis cell biologist, paediatric oncologist, clinical pharmacologist, patient-family representative working from public statements) each produce a ranked list with reasons. Round two: each reads the others and writes objections. Round three: a moderator records agreements, disagreements, and what evidence would settle each disagreement.
3. Report in the methods-form structure. Include the disagreements, not only the consensus.
4. Video script, 3 minutes, from the report.
5. Repository update, upload.
