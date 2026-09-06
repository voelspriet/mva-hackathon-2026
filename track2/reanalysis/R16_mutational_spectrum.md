# R16. Does this genome carry an unusual mutational signature?

**Asked 6 September 2026.** Everything in this project rests on the variant calls being an ordinary germline set. That assumption had never been tested directly. The test needs no gene list, no phenotype and no catalogue: count the six substitution classes and their trinucleotide contexts, which is a property of the sequence alone.

## Method

PASS SNVs with GQ >= 90 on the five chromosomes for which a reference FASTA is held locally (3, 5, 9, 11, 15): 909,268 calls. Flanking bases read from `work/ref/Homo_sapiens.GRCh38.dna.chromosome.N.fa.gz`, collapsed to a pyrimidine reference, giving the standard 96 contexts.

## Result: unremarkable

| | |
|---|---|
| Transition / transversion | **2.01** (expected 2.0 to 2.1 for germline WGS) |
| C>T | 34.1% |
| T>C | 32.6% |
| C>G | 8.8% |
| C>A | 8.7% |
| T>G | 8.4% |
| T>A | 7.4% |
| C>T at CpG | 12.2% of all calls |

The top contexts are A[C>T]G, A[T>C]G, A[T>C]A, A[C>T]A, C[C>T]G: transitions with a 3' G, which is spontaneous deamination at CpG plus the clock-like component present in every germline genome.

There is no excess of C>A (oxidative damage during library preparation), no excess of C>G, and no context concentration that would indicate a localised mutational process.

## What this is and is not

It is a negative result and a control. It does not support or weaken the *BUB1B* conclusion. What it does is remove one alternative explanation for the analyses built on these calls: the set is not distorted by a systematic artefact of sequencing or library preparation, so a spectrum-level explanation for any downstream oddity can be set aside.

Limits: five chromosomes, not the whole genome, because only those references are held locally. Blood-derived germline DNA, so a tumour-derived signature would not be expected here even if the child's rhabdomyosarcoma carried one.
