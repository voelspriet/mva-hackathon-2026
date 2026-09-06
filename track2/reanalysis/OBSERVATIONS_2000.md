# 2.013 kandidaat-waarnemingen uit het geleverde genoom

**Dit is een zeeflaag, geen resultatenlijst.** Elke regel is een meting die uit de data volgt, niet een bevinding. De overgrote meerderheid is ruis, artefact of een bekend verschijnsel. De waarde zit in de dekking van het zoekgebied en in het schriftelijke bewijs van wat er is bekeken, inclusief alles wat niets bleek.

Opgesteld volgens `PROMPT_2000_observations.md`, 2026-09-06. Het fenotypedocument is niet gebruikt, *BUB1B*, *CEP57* en *TRIP13* hebben geen voorkeursbehandeling gekregen, en er is opgesomd voordat er is geinterpreteerd.

Er is niet teruggesnoeid naar precies 2.000. Dat zou betekenen dat er dertien echte metingen worden weggegooid om een rond getal te halen.

## Opbrengst per klasse

| Klasse | Doel | Geleverd | Wat de regel opsomt |
|---|---|---|---|
| `chromosome-dosage` | 24 | **24** | Elk chromosoom: ratio na GC-correctie, aantal vensters, standaardfout, detectiegrens |
| `coverage-run` | 60 | **54** | Aaneengesloten reeksen van 5 of meer afwijkende vensters |
| `coverage-window` | 600 | **600** | Dekkingsvensters van 100 kb die meer dan 3 sd van hun GC-gematchte mediaan afwijken |
| `mappability` | 150 | **87** | Aaneengesloten gebieden onder 30 procent van de mediane dekking |
| `heterozygosity-window` | 300 | **171** | Vensters van 1 Mb waarvan de heterozygote fractie afwijkt |
| `roh` | 100 | **3** | Aaneengesloten blokken onder 10 procent heterozygoot |
| `gene-burden` | 224 | **224** | Genen met 2 of meer coderende varianten buiten de gangbare catalogus |
| `gene-frequency` | 224 | **151** | Voor diezelfde genen: de gnomAD-frequenties van hun varianten |
| `phase-set` | 151 | **151** | Genen waarvan de varianten een fasegroep delen, met de cis- of trans-uitspraak |
| `clinvar` | 200 | **7** | ClinVar-records als pathogeen of waarschijnlijk pathogeen aanwezig in dit genoom |
| `variant-quality` | 150 | **432** | Coderende varianten met allelbalans buiten 0,30 tot 0,70 of kwaliteit onder 90 |
| `spectrum` | 96 | **96** | De 96 trinucleotidecontexten met hun aandeel |
| `mitochondrial` | 40 | **13** | chrM-varianten met hun heteroplasmiefractie |
| `insert-size` | 30 | **0** | Niet uitgevoerd: vereist een aparte pass over 119 GB BAM, niet gedraaid. |

Status over alle regels: **1372 raw**, **433 artefact-prone**, **208 notable**. Dat laatste label betekent alleen dat een regel de automatische bezwaren doorstaat, niet dat hij belangrijk is.


## `chromosome-dosage` (24)

Elk chromosoom: ratio na GC-correctie, aantal vensters, standaardfout, detectiegrens

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chr1 | ratio 0.9985 na GC-correctie | autosomale GC-gematchte mediaan; 2225 vensters, standaardfout 0.00071, drempel 0.43% mozaiek | `raw` |
| chr2 | ratio 0.9973 na GC-correctie | autosomale GC-gematchte mediaan; 2367 vensters, standaardfout 0.00069, drempel 0.41% mozaiek | `raw` |
| chr3 | ratio 0.9988 na GC-correctie | autosomale GC-gematchte mediaan; 1950 vensters, standaardfout 0.00076, drempel 0.46% mozaiek | `raw` |
| chr4 | ratio 0.9977 na GC-correctie | autosomale GC-gematchte mediaan; 1845 vensters, standaardfout 0.00078, drempel 0.47% mozaiek | `raw` |
| chr5 | ratio 0.9957 na GC-correctie | autosomale GC-gematchte mediaan; 1759 vensters, standaardfout 0.00080, drempel 0.48% mozaiek | `raw` |
| chr6 | ratio 0.9970 na GC-correctie | autosomale GC-gematchte mediaan; 1682 vensters, standaardfout 0.00082, drempel 0.49% mozaiek | `raw` |
| chr7 | ratio 0.9996 na GC-correctie | autosomale GC-gematchte mediaan; 1539 vensters, standaardfout 0.00086, drempel 0.51% mozaiek | `raw` |
| chr8 | ratio 0.9998 na GC-correctie | autosomale GC-gematchte mediaan; 1414 vensters, standaardfout 0.00089, drempel 0.54% mozaiek | `raw` |
| chr9 | ratio 1.0000 na GC-correctie | autosomale GC-gematchte mediaan; 1163 vensters, standaardfout 0.00099, drempel 0.59% mozaiek | `raw` |
| chr10 | ratio 0.9998 na GC-correctie | autosomale GC-gematchte mediaan; 1303 vensters, standaardfout 0.00093, drempel 0.56% mozaiek | `raw` |
| chr11 | ratio 0.9942 na GC-correctie | autosomale GC-gematchte mediaan; 1285 vensters, standaardfout 0.00094, drempel 0.56% mozaiek | `raw` |
| chr12 | ratio 1.0015 na GC-correctie | autosomale GC-gematchte mediaan; 1307 vensters, standaardfout 0.00093, drempel 0.56% mozaiek | `raw` |
| chr13 | ratio 1.0010 na GC-correctie | autosomale GC-gematchte mediaan; 948 vensters, standaardfout 0.00109, drempel 0.66% mozaiek | `raw` |
| chr14 | ratio 1.0017 na GC-correctie | autosomale GC-gematchte mediaan; 852 vensters, standaardfout 0.00115, drempel 0.69% mozaiek | `raw` |
| chr15 | ratio 1.0004 na GC-correctie | autosomale GC-gematchte mediaan; 843 vensters, standaardfout 0.00116, drempel 0.69% mozaiek | `raw` |
| chr16 | ratio 1.0116 na GC-correctie | autosomale GC-gematchte mediaan; 744 vensters, standaardfout 0.00123, drempel 0.74% mozaiek | `raw` |
| chr17 | ratio 1.0142 na GC-correctie | autosomale GC-gematchte mediaan; 714 vensters, standaardfout 0.00126, drempel 0.75% mozaiek | `raw` |
| chr18 | ratio 1.0007 na GC-correctie | autosomale GC-gematchte mediaan; 796 vensters, standaardfout 0.00119, drempel 0.71% mozaiek | `raw` |
| chr19 | ratio 1.0194 na GC-correctie | autosomale GC-gematchte mediaan; 421 vensters, standaardfout 0.00164, drempel 0.98% mozaiek | `raw` |
| chr20 | ratio 1.0014 na GC-correctie | autosomale GC-gematchte mediaan; 613 vensters, standaardfout 0.00136, drempel 0.81% mozaiek | `raw` |
| chr21 | ratio 1.0048 na GC-correctie | autosomale GC-gematchte mediaan; 364 vensters, standaardfout 0.00176, drempel 1.06% mozaiek | `raw` |
| chr22 | ratio 1.0082 na GC-correctie | autosomale GC-gematchte mediaan; 309 vensters, standaardfout 0.00191, drempel 1.15% mozaiek | `raw` |
| chrX | ratio 0.4978 na GC-correctie | autosomale GC-gematchte mediaan; 1495 vensters, standaardfout 0.00087, drempel 0.52% mozaiek | `notable` |
| chrY | ratio 0.5117 na GC-correctie | autosomale GC-gematchte mediaan; 236 vensters, standaardfout 0.00219, drempel 1.31% mozaiek | `notable` |

## `coverage-run` (54)

Aaneengesloten reeksen van 5 of meer afwijkende vensters

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chrX:62.5-115.7 Mb | 532 aaneengesloten vensters, mediane ratio 0.497 | GC-gematchte mediaan | `notable` |
| chrX:115.9-153.4 Mb | 372 aaneengesloten vensters, mediane ratio 0.496 | GC-gematchte mediaan | `notable` |
| chrX:2.8-37.1 Mb | 342 aaneengesloten vensters, mediane ratio 0.501 | GC-gematchte mediaan | `notable` |
| chrX:40.2-49.3 Mb | 90 aaneengesloten vensters, mediane ratio 0.505 | GC-gematchte mediaan | `notable` |
| chrX:49.5-58.5 Mb | 89 aaneengesloten vensters, mediane ratio 0.492 | GC-gematchte mediaan | `notable` |
| chrY:11.8-20.1 Mb | 83 aaneengesloten vensters, mediane ratio 0.516 | GC-gematchte mediaan | `notable` |
| chrY:2.8-9.3 Mb | 64 aaneengesloten vensters, mediane ratio 0.505 | GC-gematchte mediaan | `notable` |
| chrY:20.4-26.6 Mb | 61 aaneengesloten vensters, mediane ratio 0.503 | GC-gematchte mediaan | `notable` |
| chr18:15.6-20.7 Mb | 51 aaneengesloten vensters, mediane ratio 0.730 | GC-gematchte mediaan | `artefact-prone` |
| chrX:37.3-40.0 Mb | 27 aaneengesloten vensters, mediane ratio 0.488 | GC-gematchte mediaan | `notable` |
| chr7:58.2-60.8 Mb | 25 aaneengesloten vensters, mediane ratio 0.382 | GC-gematchte mediaan | `artefact-prone` |
| chr15:17.1-19.7 Mb | 25 aaneengesloten vensters, mediane ratio 0.402 | GC-gematchte mediaan | `artefact-prone` |
| chr1:122.5-124.8 Mb | 23 aaneengesloten vensters, mediane ratio 3.018 | GC-gematchte mediaan | `artefact-prone` |
| chr13:16.1-18.3 Mb | 21 aaneengesloten vensters, mediane ratio 2.403 | GC-gematchte mediaan | `artefact-prone` |
| chr11:52.5-54.6 Mb | 20 aaneengesloten vensters, mediane ratio 0.753 | GC-gematchte mediaan | `artefact-prone` |
| chr3:91.5-93.4 Mb | 19 aaneengesloten vensters, mediane ratio 0.634 | GC-gematchte mediaan | `artefact-prone` |
| chr2:92.7-94.2 Mb | 15 aaneengesloten vensters, mediane ratio 0.429 | GC-gematchte mediaan | `artefact-prone` |
| chr20:26.6-28.1 Mb | 15 aaneengesloten vensters, mediane ratio 1.334 | GC-gematchte mediaan | `artefact-prone` |
| chr16:36.9-38.3 Mb | 14 aaneengesloten vensters, mediane ratio 0.675 | GC-gematchte mediaan | `artefact-prone` |
| chr6:58.6-59.8 Mb | 12 aaneengesloten vensters, mediane ratio 1.384 | GC-gematchte mediaan | `artefact-prone` |
| chr12:36.2-37.4 Mb | 12 aaneengesloten vensters, mediane ratio 0.744 | GC-gematchte mediaan | `artefact-prone` |
| chr5:69.6-70.7 Mb | 11 aaneengesloten vensters, mediane ratio 0.717 | GC-gematchte mediaan | `artefact-prone` |
| chr9:43.4-44.5 Mb | 11 aaneengesloten vensters, mediane ratio 1.725 | GC-gematchte mediaan | `artefact-prone` |
| chrX:154.6-155.7 Mb | 11 aaneengesloten vensters, mediane ratio 0.490 | GC-gematchte mediaan | `notable` |
| chr4:50.8-51.9 Mb | 10 aaneengesloten vensters, mediane ratio 0.655 | GC-gematchte mediaan | `artefact-prone` |
| chr14:18.9-20.0 Mb | 10 aaneengesloten vensters, mediane ratio 2.069 | GC-gematchte mediaan | `artefact-prone` |
| chr21:9.6-10.8 Mb | 10 aaneengesloten vensters, mediane ratio 2.417 | GC-gematchte mediaan | `artefact-prone` |
| chrY:9.6-10.6 Mb | 10 aaneengesloten vensters, mediane ratio 0.497 | GC-gematchte mediaan | `notable` |
| chr8:45.1-46.0 Mb | 9 aaneengesloten vensters, mediane ratio 0.774 | GC-gematchte mediaan | `artefact-prone` |
| chr12:34.9-35.8 Mb | 9 aaneengesloten vensters, mediane ratio 1.334 | GC-gematchte mediaan | `artefact-prone` |
| chr7:61.2-62.1 Mb | 8 aaneengesloten vensters, mediane ratio 0.623 | GC-gematchte mediaan | `artefact-prone` |
| chr21:6.2-7.2 Mb | 8 aaneengesloten vensters, mediane ratio 0.413 | GC-gematchte mediaan | `artefact-prone` |
| chr9:40.7-41.4 Mb | 7 aaneengesloten vensters, mediane ratio 1.208 | GC-gematchte mediaan | `artefact-prone` |
| chr9:44.8-45.5 Mb | 7 aaneengesloten vensters, mediane ratio 0.600 | GC-gematchte mediaan | `artefact-prone` |
| chr9:60.9-61.6 Mb | 7 aaneengesloten vensters, mediane ratio 0.604 | GC-gematchte mediaan | `artefact-prone` |
| chr9:64.6-65.4 Mb | 7 aaneengesloten vensters, mediane ratio 0.668 | GC-gematchte mediaan | `artefact-prone` |
| chr15:20.0-20.7 Mb | 7 aaneengesloten vensters, mediane ratio 1.647 | GC-gematchte mediaan | `artefact-prone` |
| chr2:91.4-92.0 Mb | 6 aaneengesloten vensters, mediane ratio 1.263 | GC-gematchte mediaan | `artefact-prone` |
| chr7:62.4-63.0 Mb | 6 aaneengesloten vensters, mediane ratio 0.766 | GC-gematchte mediaan | `artefact-prone` |
| chr10:39.0-39.6 Mb | 6 aaneengesloten vensters, mediane ratio 0.799 | GC-gematchte mediaan | `artefact-prone` |
| chr10:46.4-47.0 Mb | 6 aaneengesloten vensters, mediane ratio 1.307 | GC-gematchte mediaan | `artefact-prone` |
| chr11:54.7-55.3 Mb | 6 aaneengesloten vensters, mediane ratio 0.791 | GC-gematchte mediaan | `artefact-prone` |
| chr14:21.9-22.5 Mb | 6 aaneengesloten vensters, mediane ratio 0.768 | GC-gematchte mediaan | `artefact-prone` |
| chr16:36.2-36.8 Mb | 6 aaneengesloten vensters, mediane ratio 0.742 | GC-gematchte mediaan | `artefact-prone` |
| chr1:120.5-121.0 Mb | 5 aaneengesloten vensters, mediane ratio 0.668 | GC-gematchte mediaan | `artefact-prone` |
| chr1:121.8-122.5 Mb | 5 aaneengesloten vensters, mediane ratio 0.580 | GC-gematchte mediaan | `artefact-prone` |
| chr5:45.9-46.4 Mb | 5 aaneengesloten vensters, mediane ratio 0.808 | GC-gematchte mediaan | `artefact-prone` |
| chr5:46.6-47.2 Mb | 5 aaneengesloten vensters, mediane ratio 0.396 | GC-gematchte mediaan | `artefact-prone` |
| chr8:43.6-44.1 Mb | 5 aaneengesloten vensters, mediane ratio 0.812 | GC-gematchte mediaan | `artefact-prone` |
| chr9:41.5-42.0 Mb | 5 aaneengesloten vensters, mediane ratio 1.304 | GC-gematchte mediaan | `artefact-prone` |
| chr15:21.7-22.2 Mb | 5 aaneengesloten vensters, mediane ratio 0.670 | GC-gematchte mediaan | `artefact-prone` |
| chr17:26.5-27.0 Mb | 5 aaneengesloten vensters, mediane ratio 1.422 | GC-gematchte mediaan | `artefact-prone` |
| chr21:5.3-6.0 Mb | 5 aaneengesloten vensters, mediane ratio 0.438 | GC-gematchte mediaan | `artefact-prone` |
| chr21:7.3-7.9 Mb | 5 aaneengesloten vensters, mediane ratio 0.447 | GC-gematchte mediaan | `artefact-prone` |

## `coverage-window` (600)

Dekkingsvensters van 100 kb die meer dan 3 sd van hun GC-gematchte mediaan afwijken

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chr1:143.2 Mb | ratio 48.936 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:32.9 Mb | ratio 34.814 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:125.1 Mb | ratio 27.794 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:49.1 Mb | ratio 25.894 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:93.4 Mb | ratio 25.215 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:49.6 Mb | ratio 14.865 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:41.8 Mb | ratio 11.855 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:0.1 Mb | ratio 8.942 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:18.2 Mb | ratio 8.283 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:49.6 Mb | ratio 7.692 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:31.0 Mb | ratio 6.941 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:46.4 Mb | ratio 6.782 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:133.6 Mb | ratio 6.082 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:26.6 Mb | ratio 5.691 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:21.9 Mb | ratio 5.585 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.7 Mb | ratio 5.266 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:49.7 Mb | ratio 5.187 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:190.1 Mb | ratio 4.806 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.1 Mb | ratio 4.663 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:49.0 Mb | ratio 4.560 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:10.4 Mb | ratio 4.458 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:85.7 Mb | ratio 4.405 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.6 Mb | ratio 4.215 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:10.3 Mb | ratio 4.173 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.4 Mb | ratio 4.048 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:90.3 Mb | ratio 3.981 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:89.8 Mb | ratio 3.857 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.5 Mb | ratio 3.736 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.3 Mb | ratio 3.622 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:10.7 Mb | ratio 3.593 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.5 Mb | ratio 3.522 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:10.6 Mb | ratio 3.402 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.6 Mb | ratio 3.400 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.1 Mb | ratio 3.355 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:8.3 Mb | ratio 3.343 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.1 Mb | ratio 3.340 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.2 Mb | ratio 3.316 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.3 Mb | ratio 3.309 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.5 Mb | ratio 3.299 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.8 Mb | ratio 3.203 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.2 Mb | ratio 3.123 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.3 Mb | ratio 3.110 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.1 Mb | ratio 3.018 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.0 Mb | ratio 3.004 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.6 Mb | ratio 2.960 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.9 Mb | ratio 2.939 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.6 Mb | ratio 2.906 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:11.0 Mb | ratio 2.856 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.7 Mb | ratio 2.843 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:62.8 Mb | ratio 2.760 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:9.8 Mb | ratio 2.691 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.2 Mb | ratio 2.690 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:12.5 Mb | ratio 2.687 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.8 Mb | ratio 2.593 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.4 Mb | ratio 2.581 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:9.9 Mb | ratio 2.549 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:49.2 Mb | ratio 2.524 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:91.4 Mb | ratio 2.484 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:40.9 Mb | ratio 2.481 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:16.6 Mb | ratio 2.463 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.4 Mb | ratio 2.450 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.3 Mb | ratio 2.430 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.9 Mb | ratio 2.424 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.6 Mb | ratio 2.407 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.8 Mb | ratio 2.403 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.2 Mb | ratio 2.365 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:56.3 Mb | ratio 2.360 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.8 Mb | ratio 2.354 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:85.8 Mb | ratio 2.341 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.7 Mb | ratio 2.336 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.9 Mb | ratio 2.319 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.4 Mb | ratio 2.308 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.0 Mb | ratio 2.307 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:15.8 Mb | ratio 2.304 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.2 Mb | ratio 2.299 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.7 Mb | ratio 2.296 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:10.7 Mb | ratio 2.286 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:91.5 Mb | ratio 2.264 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:37.2 Mb | ratio 2.259 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:9.7 Mb | ratio 2.251 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:18.6 Mb | ratio 2.243 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.0 Mb | ratio 2.230 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.2 Mb | ratio 2.229 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:11.3 Mb | ratio 2.222 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.8 Mb | ratio 2.207 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.9 Mb | ratio 2.204 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.9 Mb | ratio 2.194 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:30.8 Mb | ratio 2.187 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:9.0 Mb | ratio 2.167 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:29.0 Mb | ratio 2.156 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.1 Mb | ratio 2.151 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:85.6 Mb | ratio 2.136 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:121.7 Mb | ratio 2.114 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.8 Mb | ratio 2.104 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:123.3 Mb | ratio 2.087 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:12.5 Mb | ratio 2.086 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.5 Mb | ratio 2.085 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.5 Mb | ratio 2.052 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.7 Mb | ratio 2.041 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:161.4 Mb | ratio 2.038 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:28.5 Mb | ratio 2.037 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.7 Mb | ratio 2.035 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:40.5 Mb | ratio 2.028 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:75.6 Mb | ratio 2.017 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:190.0 Mb | ratio 2.006 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:50.1 Mb | ratio 1.993 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.6 Mb | ratio 1.987 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:17.4 Mb | ratio 1.982 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:16.7 Mb | ratio 1.982 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:0.0 Mb | ratio 1.975 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:22.6 Mb | ratio 1.971 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:41.2 Mb | ratio 1.966 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:44.0 Mb | ratio 1.959 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:94.2 Mb | ratio 1.935 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.5 Mb | ratio 1.926 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:10.5 Mb | ratio 1.925 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:18.7 Mb | ratio 1.925 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:9.3 Mb | ratio 1.918 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:28.8 Mb | ratio 1.911 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:15.7 Mb | ratio 1.904 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.7 Mb | ratio 1.888 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.9 Mb | ratio 1.879 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:18.9 Mb | ratio 1.875 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:15.6 Mb | ratio 1.872 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.0 Mb | ratio 1.870 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:12.1 Mb | ratio 1.862 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:12.3 Mb | ratio 1.843 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:41.0 Mb | ratio 1.838 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:46.5 Mb | ratio 1.827 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:21.5 Mb | ratio 1.820 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:39.0 Mb | ratio 1.810 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:15.5 Mb | ratio 1.804 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.3 Mb | ratio 1.797 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.2 Mb | ratio 1.795 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:31.2 Mb | ratio 1.791 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:29.8 Mb | ratio 1.774 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:14.9 Mb | ratio 1.763 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:43.2 Mb | ratio 1.758 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:49.5 Mb | ratio 1.738 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.8 Mb | ratio 1.725 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:5.2 Mb | ratio 1.721 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.1 Mb | ratio 1.708 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:22.2 Mb | ratio 1.705 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.7 Mb | ratio 0.300 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:34.1 Mb | ratio 1.697 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:25.0 Mb | ratio 0.306 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:5.8 Mb | ratio 0.306 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.1 Mb | ratio 0.311 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:5.9 Mb | ratio 0.313 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:0.3 Mb | ratio 1.686 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:34.0 Mb | ratio 1.686 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.0 Mb | ratio 0.315 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:26.1 Mb | ratio 0.317 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:60.6 Mb | ratio 0.318 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.0 Mb | ratio 0.318 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.7 Mb | ratio 0.322 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:30.2 Mb | ratio 1.676 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:60.7 Mb | ratio 0.326 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:46.6 Mb | ratio 0.327 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:16.5 Mb | ratio 1.672 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:61.0 Mb | ratio 0.328 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.3 Mb | ratio 0.331 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:67.7 Mb | ratio 1.669 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.3 Mb | ratio 0.333 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:89.6 Mb | ratio 1.666 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:19.4 Mb | ratio 0.337 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:94.0 Mb | ratio 0.337 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:33.4 Mb | ratio 0.340 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:61.4 Mb | ratio 0.346 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:39.2 Mb | ratio 0.347 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:24.1 Mb | ratio 0.347 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:6.4 Mb | ratio 0.349 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.8 Mb | ratio 0.350 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:143.6 Mb | ratio 0.351 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.4 Mb | ratio 1.647 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:19.0 Mb | ratio 0.354 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.3 Mb | ratio 0.354 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:61.3 Mb | ratio 0.355 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.2 Mb | ratio 0.356 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.9 Mb | ratio 0.357 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.1 Mb | ratio 0.362 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.4 Mb | ratio 0.363 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:19.3 Mb | ratio 0.366 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:40.9 Mb | ratio 1.633 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:121.8 Mb | ratio 0.367 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:6.8 Mb | ratio 0.367 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.1 Mb | ratio 0.368 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.5 Mb | ratio 0.372 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:60.4 Mb | ratio 0.372 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.6 Mb | ratio 0.373 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.8 Mb | ratio 0.375 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.4 Mb | ratio 0.377 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:46.9 Mb | ratio 0.377 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.9 Mb | ratio 0.379 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:61.6 Mb | ratio 0.380 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.7 Mb | ratio 0.380 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:36.2 Mb | ratio 1.618 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.4 Mb | ratio 0.382 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:44.1 Mb | ratio 1.617 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:0.5 Mb | ratio 0.384 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.0 Mb | ratio 0.384 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:19.5 Mb | ratio 0.385 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:60.5 Mb | ratio 0.386 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:60.3 Mb | ratio 0.387 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.9 Mb | ratio 0.389 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.5 Mb | ratio 0.389 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:65.1 Mb | ratio 0.390 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:38.9 Mb | ratio 1.609 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:46.8 Mb | ratio 0.396 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.6 Mb | ratio 0.396 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:86.2 Mb | ratio 0.397 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:7.6 Mb | ratio 0.398 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.6 Mb | ratio 0.399 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.4 Mb | ratio 0.399 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:47.0 Mb | ratio 0.400 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.8 Mb | ratio 0.400 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:18.4 Mb | ratio 0.401 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.7 Mb | ratio 0.402 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:61.2 Mb | ratio 0.402 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.9 Mb | ratio 0.405 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.1 Mb | ratio 0.406 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:6.6 Mb | ratio 0.409 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:21.4 Mb | ratio 1.590 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:21.6 Mb | ratio 1.590 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.8 Mb | ratio 0.410 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:9.2 Mb | ratio 1.590 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.6 Mb | ratio 1.587 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:62.2 Mb | ratio 0.414 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:11.9 Mb | ratio 0.414 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.2 Mb | ratio 0.416 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:19.1 Mb | ratio 0.416 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:62.7 Mb | ratio 0.416 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:6.5 Mb | ratio 0.417 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.3 Mb | ratio 0.418 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:18.5 Mb | ratio 0.419 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.1 Mb | ratio 0.420 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:58.4 Mb | ratio 0.421 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.3 Mb | ratio 0.421 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.5 Mb | ratio 0.423 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:6.2 Mb | ratio 0.425 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:57.1 Mb | ratio 1.574 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.8 Mb | ratio 0.426 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:64.1 Mb | ratio 0.427 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:60.0 Mb | ratio 0.429 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.9 Mb | ratio 0.429 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:97.4 Mb | ratio 0.429 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:47.9 Mb | ratio 1.571 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:19.9 Mb | ratio 1.568 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:42.3 Mb | ratio 1.564 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:19.6 Mb | ratio 0.437 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:5.5 Mb | ratio 0.438 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:21.8 Mb | ratio 0.441 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:40.4 Mb | ratio 1.558 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.2 Mb | ratio 0.442 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.8 Mb | ratio 0.443 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:17.6 Mb | ratio 0.444 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.3 Mb | ratio 0.447 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:181.4 Mb | ratio 0.448 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:58.7 Mb | ratio 1.550 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:13.7 Mb | ratio 0.451 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:93.0 Mb | ratio 0.456 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.0 Mb | ratio 0.457 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:27.2 Mb | ratio 0.463 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:11.5 Mb | ratio 1.536 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.4 Mb | ratio 0.465 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:20.1 Mb | ratio 0.466 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.2 Mb | ratio 0.467 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.7 Mb | ratio 0.467 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:41.0 Mb | ratio 0.467 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:22.0 Mb | ratio 0.468 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:38.2 Mb | ratio 0.469 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:19.2 Mb | ratio 0.471 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:41.8 Mb | ratio 1.528 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.1 Mb | ratio 0.476 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:22.5 Mb | ratio 1.524 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:64.6 Mb | ratio 0.478 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.7 Mb | ratio 0.479 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.0 Mb | ratio 0.481 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:69.7 Mb | ratio 0.483 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:34.4 Mb | ratio 0.485 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:84.2 Mb | ratio 0.485 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:16.0 Mb | ratio 0.486 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:58.6 Mb | ratio 0.492 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:27.3 Mb | ratio 1.507 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:20.2 Mb | ratio 0.493 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.1 Mb | ratio 1.506 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.6 Mb | ratio 1.505 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:42.2 Mb | ratio 1.504 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:41.9 Mb | ratio 1.503 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:45.3 Mb | ratio 0.498 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:25.9 Mb | ratio 0.498 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:37.2 Mb | ratio 0.499 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:41.3 Mb | ratio 0.502 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.4 Mb | ratio 1.497 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:38.1 Mb | ratio 0.504 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:51.6 Mb | ratio 0.504 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:113.0 Mb | ratio 1.495 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:9.6 Mb | ratio 1.493 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:60.2 Mb | ratio 0.507 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:59.0 Mb | ratio 1.492 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:93.5 Mb | ratio 0.508 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:29.3 Mb | ratio 1.492 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:0.0 Mb | ratio 0.511 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:93.1 Mb | ratio 0.512 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:26.9 Mb | ratio 1.486 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:59.3 Mb | ratio 1.483 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:20.5 Mb | ratio 0.517 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.2 Mb | ratio 0.519 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:30.1 Mb | ratio 0.519 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:13.0 Mb | ratio 1.479 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:34.4 Mb | ratio 0.522 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:12.9 Mb | ratio 0.524 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:90.8 Mb | ratio 1.473 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:106.7 Mb | ratio 0.528 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:61.9 Mb | ratio 0.529 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:47.6 Mb | ratio 1.470 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:90.1 Mb | ratio 1.470 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.8 Mb | ratio 0.532 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:111.8 Mb | ratio 0.532 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:59.5 Mb | ratio 0.532 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:28.4 Mb | ratio 1.467 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:45.2 Mb | ratio 0.535 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:36.3 Mb | ratio 0.536 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:93.3 Mb | ratio 0.536 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:92.8 Mb | ratio 0.538 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.0 Mb | ratio 1.461 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:43.9 Mb | ratio 0.539 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:45.4 Mb | ratio 0.541 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:160.6 Mb | ratio 1.456 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:36.2 Mb | ratio 0.544 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:54.3 Mb | ratio 0.545 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:20.0 Mb | ratio 0.546 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:20.3 Mb | ratio 0.548 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:20.4 Mb | ratio 0.552 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:0.4 Mb | ratio 0.555 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:55.6 Mb | ratio 0.556 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.8 Mb | ratio 0.556 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:40.8 Mb | ratio 1.443 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:40.6 Mb | ratio 1.442 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:62.0 Mb | ratio 0.558 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:9.1 Mb | ratio 0.558 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:7.6 Mb | ratio 0.559 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.9 Mb | ratio 0.559 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:53.0 Mb | ratio 1.440 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:43.1 Mb | ratio 0.563 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:93.2 Mb | ratio 0.564 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:51.4 Mb | ratio 0.565 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.9 Mb | ratio 0.565 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.7 Mb | ratio 1.434 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:223.5 Mb | ratio 0.567 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:26.8 Mb | ratio 1.432 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:168.0 Mb | ratio 1.432 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:92.9 Mb | ratio 0.569 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.9 Mb | ratio 0.570 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:167.6 Mb | ratio 0.571 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:38.0 Mb | ratio 0.573 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:61.7 Mb | ratio 0.575 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:26.6 Mb | ratio 1.424 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:70.9 Mb | ratio 0.578 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:26.8 Mb | ratio 1.422 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:29.4 Mb | ratio 1.422 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:39.3 Mb | ratio 0.579 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.4 Mb | ratio 0.580 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:145.3 Mb | ratio 1.420 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:59.1 Mb | ratio 1.420 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:53.9 Mb | ratio 0.580 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:26.9 Mb | ratio 1.420 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.7 Mb | ratio 0.581 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:67.3 Mb | ratio 1.419 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:120.7 Mb | ratio 0.582 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:148.5 Mb | ratio 1.418 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:35.4 Mb | ratio 1.417 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:47.1 Mb | ratio 0.583 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.2 Mb | ratio 0.584 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:23.2 Mb | ratio 0.584 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:61.3 Mb | ratio 0.586 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:35.1 Mb | ratio 1.412 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:75.7 Mb | ratio 1.408 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:7.4 Mb | ratio 1.407 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:42.1 Mb | ratio 1.407 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:12.6 Mb | ratio 1.406 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:35.3 Mb | ratio 1.406 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:61.4 Mb | ratio 0.594 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:58.6 Mb | ratio 1.406 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:93.0 Mb | ratio 0.595 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:35.0 Mb | ratio 0.595 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:12.2 Mb | ratio 0.595 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:25.3 Mb | ratio 0.596 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:45.9 Mb | ratio 0.597 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:168.1 Mb | ratio 1.403 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:20.6 Mb | ratio 0.598 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.7 Mb | ratio 0.598 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:7.5 Mb | ratio 1.402 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:45.1 Mb | ratio 0.600 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:0.2 Mb | ratio 1.400 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:228.5 Mb | ratio 0.600 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.3 Mb | ratio 0.600 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:69.8 Mb | ratio 0.602 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:124.9 Mb | ratio 0.602 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:106.4 Mb | ratio 0.602 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:181.3 Mb | ratio 0.603 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:0.4 Mb | ratio 0.603 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:71.0 Mb | ratio 0.603 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:15.7 Mb | ratio 0.603 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:60.9 Mb | ratio 0.604 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:11.7 Mb | ratio 0.604 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:58.9 Mb | ratio 1.395 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:39.5 Mb | ratio 0.606 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:22.7 Mb | ratio 0.607 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:38.0 Mb | ratio 0.607 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:80.2 Mb | ratio 0.607 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:9.3 Mb | ratio 1.391 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:29.1 Mb | ratio 0.610 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.5 Mb | ratio 0.612 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:41.2 Mb | ratio 0.613 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.8 Mb | ratio 0.613 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:41.5 Mb | ratio 1.386 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:34.9 Mb | ratio 1.383 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:26.3 Mb | ratio 0.618 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:0.0 Mb | ratio 1.381 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:46.7 Mb | ratio 1.380 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.7 Mb | ratio 0.622 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:70.1 Mb | ratio 0.622 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:100.9 Mb | ratio 1.377 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:51.3 Mb | ratio 0.623 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:22.3 Mb | ratio 0.624 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.5 Mb | ratio 0.625 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.3 Mb | ratio 0.625 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:17.9 Mb | ratio 0.625 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.0 Mb | ratio 0.626 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:59.7 Mb | ratio 1.374 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.2 Mb | ratio 1.372 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.3 Mb | ratio 0.630 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:45.8 Mb | ratio 0.630 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.6 Mb | ratio 0.630 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:51.0 Mb | ratio 0.631 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.5 Mb | ratio 1.368 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:66.0 Mb | ratio 1.368 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:91.6 Mb | ratio 0.634 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:90.7 Mb | ratio 0.634 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:12.7 Mb | ratio 0.636 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:70.6 Mb | ratio 0.637 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:44.9 Mb | ratio 0.638 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:18.0 Mb | ratio 1.361 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:12.0 Mb | ratio 0.639 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:22.4 Mb | ratio 0.640 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.6 Mb | ratio 0.640 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:39.9 Mb | ratio 0.640 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:38.1 Mb | ratio 0.640 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:43.5 Mb | ratio 0.641 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.8 Mb | ratio 0.641 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:5.3 Mb | ratio 0.643 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:18.5 Mb | ratio 0.644 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:40.4 Mb | ratio 0.645 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:61.8 Mb | ratio 1.354 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.4 Mb | ratio 0.646 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:84.3 Mb | ratio 0.646 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:35.6 Mb | ratio 1.354 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.0 Mb | ratio 1.353 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:17.5 Mb | ratio 1.353 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:35.0 Mb | ratio 1.353 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:10.2 Mb | ratio 0.648 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:26.7 Mb | ratio 1.351 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:51.2 Mb | ratio 0.649 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:40.2 Mb | ratio 1.351 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:30.7 Mb | ratio 0.652 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:58.8 Mb | ratio 1.347 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:39.8 Mb | ratio 1.346 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.1 Mb | ratio 0.654 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:44.2 Mb | ratio 1.346 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:120.6 Mb | ratio 0.654 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:40.5 Mb | ratio 0.654 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.5 Mb | ratio 1.344 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.8 Mb | ratio 0.656 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:152.4 Mb | ratio 1.343 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.4 Mb | ratio 0.657 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:65.3 Mb | ratio 0.657 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:53.0 Mb | ratio 0.658 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:5.7 Mb | ratio 0.658 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:34.8 Mb | ratio 0.660 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:51.5 Mb | ratio 0.661 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:106.0 Mb | ratio 0.662 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:15.8 Mb | ratio 0.662 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:8.0 Mb | ratio 0.662 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:46.9 Mb | ratio 1.338 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:65.8 Mb | ratio 0.662 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:101.9 Mb | ratio 1.338 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:21.4 Mb | ratio 1.337 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:18.3 Mb | ratio 0.664 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:42.4 Mb | ratio 1.336 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:0.1 Mb | ratio 0.665 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:39.3 Mb | ratio 0.665 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:7.2 Mb | ratio 0.665 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:35.2 Mb | ratio 1.334 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.6 Mb | ratio 1.334 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:37.1 Mb | ratio 0.666 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:63.4 Mb | ratio 0.666 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:38.9 Mb | ratio 1.334 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:42.6 Mb | ratio 0.666 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:36.4 Mb | ratio 0.667 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:120.8 Mb | ratio 0.668 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:64.7 Mb | ratio 0.668 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.2 Mb | ratio 0.668 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:91.2 Mb | ratio 0.669 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:54.5 Mb | ratio 0.670 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:21.9 Mb | ratio 0.670 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:64.9 Mb | ratio 0.671 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:16.0 Mb | ratio 0.672 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:91.9 Mb | ratio 0.673 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:8.1 Mb | ratio 1.327 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.7 Mb | ratio 0.674 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.1 Mb | ratio 0.674 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.0 Mb | ratio 0.676 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:22.0 Mb | ratio 0.676 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:11.8 Mb | ratio 0.678 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:21.7 Mb | ratio 0.678 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:15.0 Mb | ratio 1.322 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.9 Mb | ratio 0.678 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:122.2 Mb | ratio 0.680 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.5 Mb | ratio 0.680 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:30.3 Mb | ratio 1.319 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:97.2 Mb | ratio 1.318 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.6 Mb | ratio 0.682 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr22:16.4 Mb | ratio 1.317 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:45.0 Mb | ratio 0.683 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:22.3 Mb | ratio 0.683 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:70.1 Mb | ratio 1.316 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:92.1 Mb | ratio 0.684 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:97.5 Mb | ratio 0.685 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:23.1 Mb | ratio 1.315 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:61.3 Mb | ratio 0.686 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:234.7 Mb | ratio 1.314 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:39.6 Mb | ratio 0.687 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.0 Mb | ratio 0.687 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:61.7 Mb | ratio 0.689 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:44.0 Mb | ratio 0.689 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:35.2 Mb | ratio 1.310 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:92.7 Mb | ratio 0.690 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:21.7 Mb | ratio 1.309 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:35.4 Mb | ratio 1.309 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr13:18.3 Mb | ratio 0.691 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.2 Mb | ratio 0.693 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.7 Mb | ratio 1.307 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr14:41.1 Mb | ratio 0.693 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:22.4 Mb | ratio 1.305 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:59.2 Mb | ratio 1.305 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:35.5 Mb | ratio 1.305 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:41.5 Mb | ratio 1.304 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:46.3 Mb | ratio 0.697 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:20.9 Mb | ratio 0.697 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:43.2 Mb | ratio 0.698 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr12:36.5 Mb | ratio 0.698 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.3 Mb | ratio 1.302 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:22.1 Mb | ratio 0.698 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr1:16.8 Mb | ratio 0.699 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:43.0 Mb | ratio 0.701 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:65.9 Mb | ratio 1.299 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:36.3 Mb | ratio 0.702 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:42.7 Mb | ratio 0.702 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:170.6 Mb | ratio 0.703 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:70.4 Mb | ratio 0.704 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:22.4 Mb | ratio 1.296 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:24.3 Mb | ratio 1.296 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:54.1 Mb | ratio 0.705 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:13.6 Mb | ratio 0.707 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr19:36.3 Mb | ratio 1.292 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:36.9 Mb | ratio 0.709 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr6:32.5 Mb | ratio 0.709 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:41.7 Mb | ratio 1.290 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:91.8 Mb | ratio 0.711 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:28.2 Mb | ratio 1.289 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.5 Mb | ratio 0.711 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr15:21.1 Mb | ratio 1.288 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:87.3 Mb | ratio 1.287 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:54.0 Mb | ratio 0.713 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:90.6 Mb | ratio 1.286 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr9:40.6 Mb | ratio 0.715 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr2:94.1 Mb | ratio 0.715 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:41.4 Mb | ratio 0.716 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:53.5 Mb | ratio 0.716 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:70.3 Mb | ratio 0.717 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr7:62.4 Mb | ratio 0.717 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr3:91.7 Mb | ratio 0.718 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:21.7 Mb | ratio 1.282 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:37.3 Mb | ratio 0.718 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:29.7 Mb | ratio 1.281 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:27.9 Mb | ratio 1.281 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:45.2 Mb | ratio 0.721 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:70.9 Mb | ratio 0.721 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:70.2 Mb | ratio 0.722 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr16:32.5 Mb | ratio 0.723 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr18:19.4 Mb | ratio 0.723 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr10:46.8 Mb | ratio 1.276 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr17:38.2 Mb | ratio 0.724 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr20:28.6 Mb | ratio 1.275 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr11:53.4 Mb | ratio 0.725 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr8:45.7 Mb | ratio 0.725 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr5:49.9 Mb | ratio 1.274 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr4:77.2 Mb | ratio 0.726 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |
| chr21:6.3 Mb | ratio 0.726 | GC-gematchte mediaan, spreiding 0.0336 | `raw` |

## `mappability` (87)

Aaneengesloten gebieden onder 30 procent van de mediane dekking

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chrY:26.7-56.6 Mb | 299 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr1:125.2-143.1 Mb | 179 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr15:0.0-17.0 Mb | 170 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr13:0.0-16.0 Mb | 160 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr14:0.0-16.0 Mb | 160 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr9:45.5-60.5 Mb | 150 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr22:0.0-10.5 Mb | 105 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr16:38.3-46.3 Mb | 80 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr21:0.0-5.0 Mb | 50 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:59.5-62.5 Mb | 29 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr17:23.2-26.5 Mb | 28 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrY:0.0-2.8 Mb | 28 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr19:24.5-27.2 Mb | 27 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr22:12.9-15.2 Mb | 23 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr5:47.2-49.5 Mb | 23 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr14:16.2-18.2 Mb | 20 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr21:10.9-12.9 Mb | 20 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr2:90.4-91.4 Mb | 10 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:58.5-59.3 Mb | 6 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr22:18.2-18.7 Mb | 4 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrY:56.9-57.3 Mb | 4 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr10:39.6-39.9 Mb | 3 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr11:50.8-51.1 Mb | 3 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr5:46.4-46.8 Mb | 3 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr6:59.9-60.2 Mb | 3 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr9:67.9-68.2 Mb | 3 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrY:20.1-20.4 Mb | 3 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr1:121.9-122.2 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr14:106.9-107.1 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr18:20.7-20.9 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr2:89.3-89.5 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr2:94.3-94.5 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr20:29.9-30.1 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr21:5.4-5.7 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr21:6.7-7.0 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr6:170.7-170.9 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr9:60.7-60.9 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr9:66.4-66.6 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:0.0-0.2 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:37.1-37.3 Mb | 2 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr1:0.3-0.4 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr1:121.6-121.7 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr10:41.6-41.7 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr11:0.0-0.1 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr11:54.4-54.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr12:9.5-9.6 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr13:111.7-111.8 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr14:18.7-18.8 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr14:19.5-19.6 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr15:17.4-17.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr15:19.7-19.8 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr16:33.2-33.3 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr16:34.3-34.4 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr16:90.3-90.4 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr17:0.0-0.1 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr18:80.3-80.4 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr2:92.1-92.2 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr20:64.4-64.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr21:7.5-7.6 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr21:9.4-9.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr21:46.7-46.8 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr22:11.1-11.2 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr22:11.4-11.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr3:93.6-93.7 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr3:198.2-198.3 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr4:49.4-49.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr4:51.7-51.8 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr5:181.5-181.6 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr6:0.0-0.1 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr7:58.1-58.2 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr7:60.1-60.2 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr7:60.8-60.9 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr7:61.5-61.6 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr8:0.0-0.1 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr8:145.1-145.2 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr9:64.2-64.3 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr9:65.0-65.1 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chr9:138.3-138.4 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:2.0-2.1 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:49.4-49.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:50.2-50.3 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:116.5-116.6 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:120.9-121.0 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:144.4-144.5 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrX:154.2-154.3 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrY:9.0-9.1 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |
| chrY:21.7-21.8 Mb | 1 vensters onder 30% van mediaan | autosomale mediaan 51.0x | `artefact-prone` |

## `heterozygosity-window` (171)

Vensters van 1 Mb waarvan de heterozygote fractie afwijkt

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chrX:56-57 Mb | heterozygote fractie 0.000 bij 364 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:127-128 Mb | heterozygote fractie 0.001 bij 1397 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:143-144 Mb | heterozygote fractie 0.001 bij 1038 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:95-96 Mb | heterozygote fractie 0.001 bij 808 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:13-14 Mb | heterozygote fractie 0.001 bij 749 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:18-19 Mb | heterozygote fractie 0.002 bij 466 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:11-12 Mb | heterozygote fractie 0.003 bij 386 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:4-5 Mb | heterozygote fractie 0.003 bij 1142 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:33-34 Mb | heterozygote fractie 0.003 bij 1105 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:125-126 Mb | heterozygote fractie 0.003 bij 903 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:32-33 Mb | heterozygote fractie 0.003 bij 900 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:39-40 Mb | heterozygote fractie 0.004 bij 567 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:38-39 Mb | heterozygote fractie 0.004 bij 565 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:22-23 Mb | heterozygote fractie 0.004 bij 842 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:28-29 Mb | heterozygote fractie 0.004 bij 504 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:79-80 Mb | heterozygote fractie 0.004 bij 1482 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:82-83 Mb | heterozygote fractie 0.004 bij 946 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:67-68 Mb | heterozygote fractie 0.004 bij 703 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:134-135 Mb | heterozygote fractie 0.004 bij 459 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:34-35 Mb | heterozygote fractie 0.004 bij 676 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:87-88 Mb | heterozygote fractie 0.005 bij 1761 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:128-129 Mb | heterozygote fractie 0.005 bij 769 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:151-152 Mb | heterozygote fractie 0.005 bij 1091 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:31-32 Mb | heterozygote fractie 0.006 bij 890 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:147-148 Mb | heterozygote fractie 0.006 bij 796 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:146-147 Mb | heterozygote fractie 0.007 bij 908 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:47-48 Mb | heterozygote fractie 0.007 bij 881 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:93-94 Mb | heterozygote fractie 0.007 bij 1305 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:90-91 Mb | heterozygote fractie 0.007 bij 413 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:122-123 Mb | heterozygote fractie 0.008 bij 1018 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:92-93 Mb | heterozygote fractie 0.008 bij 875 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:116-117 Mb | heterozygote fractie 0.008 bij 1230 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:91-92 Mb | heterozygote fractie 0.008 bij 979 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:145-146 Mb | heterozygote fractie 0.008 bij 1199 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:78-79 Mb | heterozygote fractie 0.008 bij 712 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:121-122 Mb | heterozygote fractie 0.009 bij 337 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:105-106 Mb | heterozygote fractie 0.009 bij 222 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:57-58 Mb | heterozygote fractie 0.009 bij 745 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:27-28 Mb | heterozygote fractie 0.010 bij 401 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:35-36 Mb | heterozygote fractie 0.010 bij 789 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:81-82 Mb | heterozygote fractie 0.010 bij 970 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:84-85 Mb | heterozygote fractie 0.011 bij 1033 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:117-118 Mb | heterozygote fractie 0.011 bij 1362 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:99-100 Mb | heterozygote fractie 0.011 bij 544 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:75-76 Mb | heterozygote fractie 0.011 bij 1071 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:45-46 Mb | heterozygote fractie 0.011 bij 802 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:94-95 Mb | heterozygote fractie 0.012 bij 861 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:24-25 Mb | heterozygote fractie 0.012 bij 515 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:12-13 Mb | heterozygote fractie 0.012 bij 856 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:76-77 Mb | heterozygote fractie 0.012 bij 2034 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:77-78 Mb | heterozygote fractie 0.012 bij 921 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:138-139 Mb | heterozygote fractie 0.012 bij 575 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:26-27 Mb | heterozygote fractie 0.013 bij 397 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:83-84 Mb | heterozygote fractie 0.013 bij 549 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:66-67 Mb | heterozygote fractie 0.013 bij 1009 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:124-125 Mb | heterozygote fractie 0.013 bij 538 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:142-143 Mb | heterozygote fractie 0.013 bij 1074 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:114-115 Mb | heterozygote fractie 0.013 bij 1298 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:6-7 Mb | heterozygote fractie 0.013 bij 682 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:139-140 Mb | heterozygote fractie 0.013 bij 676 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:113-114 Mb | heterozygote fractie 0.014 bij 1015 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:110-111 Mb | heterozygote fractie 0.014 bij 795 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:98-99 Mb | heterozygote fractie 0.014 bij 711 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:123-124 Mb | heterozygote fractie 0.014 bij 774 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:74-75 Mb | heterozygote fractie 0.014 bij 562 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:5-6 Mb | heterozygote fractie 0.014 bij 1458 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:50-51 Mb | heterozygote fractie 0.014 bij 416 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:44-45 Mb | heterozygote fractie 0.015 bij 823 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:108-109 Mb | heterozygote fractie 0.015 bij 599 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:23-24 Mb | heterozygote fractie 0.016 bij 838 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:144-145 Mb | heterozygote fractie 0.016 bij 1276 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:41-42 Mb | heterozygote fractie 0.016 bij 572 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:88-89 Mb | heterozygote fractie 0.016 bij 699 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:86-87 Mb | heterozygote fractie 0.017 bij 1090 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:8-9 Mb | heterozygote fractie 0.017 bij 1021 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:96-97 Mb | heterozygote fractie 0.018 bij 685 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:109-110 Mb | heterozygote fractie 0.018 bij 784 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:7-8 Mb | heterozygote fractie 0.018 bij 882 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:51-52 Mb | heterozygote fractie 0.019 bij 755 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:103-104 Mb | heterozygote fractie 0.019 bij 677 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:69-70 Mb | heterozygote fractie 0.019 bij 776 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:43-44 Mb | heterozygote fractie 0.020 bij 648 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:54-55 Mb | heterozygote fractie 0.021 bij 675 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:25-26 Mb | heterozygote fractie 0.021 bij 720 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:16-17 Mb | heterozygote fractie 0.021 bij 334 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:17-18 Mb | heterozygote fractie 0.021 bij 285 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:111-112 Mb | heterozygote fractie 0.021 bij 332 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:19-20 Mb | heterozygote fractie 0.021 bij 377 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:150-151 Mb | heterozygote fractie 0.022 bij 883 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:73-74 Mb | heterozygote fractie 0.022 bij 412 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:137-138 Mb | heterozygote fractie 0.022 bij 914 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:104-105 Mb | heterozygote fractie 0.023 bij 349 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:68-69 Mb | heterozygote fractie 0.023 bij 646 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:153-154 Mb | heterozygote fractie 0.024 bij 749 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:20-21 Mb | heterozygote fractie 0.025 bij 366 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:29-30 Mb | heterozygote fractie 0.026 bij 817 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:97-98 Mb | heterozygote fractie 0.027 bij 521 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:152-153 Mb | heterozygote fractie 0.027 bij 920 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:154-155 Mb | heterozygote fractie 0.028 bij 361 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:130-131 Mb | heterozygote fractie 0.028 bij 469 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:136-137 Mb | heterozygote fractie 0.028 bij 713 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:149-150 Mb | heterozygote fractie 0.028 bij 748 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:100-101 Mb | heterozygote fractie 0.029 bij 834 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:148-149 Mb | heterozygote fractie 0.030 bij 740 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:55-56 Mb | heterozygote fractie 0.032 bij 967 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:46-47 Mb | heterozygote fractie 0.032 bij 530 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:70-71 Mb | heterozygote fractie 0.032 bij 803 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:129-130 Mb | heterozygote fractie 0.033 bij 610 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:140-141 Mb | heterozygote fractie 0.033 bij 813 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:80-81 Mb | heterozygote fractie 0.033 bij 420 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:85-86 Mb | heterozygote fractie 0.035 bij 1050 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:14-15 Mb | heterozygote fractie 0.037 bij 299 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:135-136 Mb | heterozygote fractie 0.037 bij 751 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:36-37 Mb | heterozygote fractie 0.039 bij 205 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:3-4 Mb | heterozygote fractie 0.040 bij 828 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:40-41 Mb | heterozygote fractie 0.042 bij 765 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chr7:125-126 Mb | heterozygote fractie 0.042 bij 1604 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chrX:131-132 Mb | heterozygote fractie 0.043 bij 533 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:126-127 Mb | heterozygote fractie 0.044 bij 639 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:53-54 Mb | heterozygote fractie 0.045 bij 762 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:48-49 Mb | heterozygote fractie 0.045 bij 784 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:52-53 Mb | heterozygote fractie 0.047 bij 338 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:120-121 Mb | heterozygote fractie 0.048 bij 484 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:89-90 Mb | heterozygote fractie 0.053 bij 1507 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:71-72 Mb | heterozygote fractie 0.059 bij 506 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:30-31 Mb | heterozygote fractie 0.060 bij 562 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:119-120 Mb | heterozygote fractie 0.064 bij 850 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:112-113 Mb | heterozygote fractie 0.066 bij 486 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chr4:19-20 Mb | heterozygote fractie 0.068 bij 1070 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chrX:118-119 Mb | heterozygote fractie 0.070 bij 704 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:15-16 Mb | heterozygote fractie 0.072 bij 568 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:115-116 Mb | heterozygote fractie 0.073 bij 898 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:107-108 Mb | heterozygote fractie 0.078 bij 245 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:72-73 Mb | heterozygote fractie 0.078 bij 523 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:102-103 Mb | heterozygote fractie 0.079 bij 381 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chr8:111-112 Mb | heterozygote fractie 0.083 bij 881 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chrX:42-43 Mb | heterozygote fractie 0.089 bij 393 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:101-102 Mb | heterozygote fractie 0.093 bij 875 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chr6:61-62 Mb | heterozygote fractie 0.100 bij 1675 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chrX:141-142 Mb | heterozygote fractie 0.101 bij 1121 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chr12:33-34 Mb | heterozygote fractie 0.105 bij 363 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr4:127-128 Mb | heterozygote fractie 0.107 bij 722 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr6:116-117 Mb | heterozygote fractie 0.108 bij 1030 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr2:209-210 Mb | heterozygote fractie 0.108 bij 1079 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr3:47-48 Mb | heterozygote fractie 0.110 bij 910 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr8:53-54 Mb | heterozygote fractie 0.114 bij 1321 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chrX:49-50 Mb | heterozygote fractie 0.133 bij 664 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chrX:9-10 Mb | heterozygote fractie 0.134 bij 1082 varianten | autosomale mediaan 0.633, spreiding 0.139 | `notable` |
| chr12:110-111 Mb | heterozygote fractie 0.145 bij 683 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr4:147-148 Mb | heterozygote fractie 0.145 bij 1382 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr13:19-20 Mb | heterozygote fractie 0.148 bij 2442 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr8:51-52 Mb | heterozygote fractie 0.149 bij 1067 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr12:38-39 Mb | heterozygote fractie 0.151 bij 1438 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr6:60-61 Mb | heterozygote fractie 0.155 bij 1006 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr4:73-74 Mb | heterozygote fractie 0.163 bij 1014 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr15:72-73 Mb | heterozygote fractie 0.166 bij 1163 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr13:58-59 Mb | heterozygote fractie 0.167 bij 1275 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr2:194-195 Mb | heterozygote fractie 0.177 bij 1530 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr22:41-42 Mb | heterozygote fractie 0.179 bij 969 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr2:39-40 Mb | heterozygote fractie 0.180 bij 1312 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr10:111-112 Mb | heterozygote fractie 0.185 bij 1438 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr3:99-100 Mb | heterozygote fractie 0.194 bij 1951 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr3:52-53 Mb | heterozygote fractie 0.197 bij 1004 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr15:64-65 Mb | heterozygote fractie 0.197 bij 1460 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr3:136-137 Mb | heterozygote fractie 0.205 bij 1023 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr4:86-87 Mb | heterozygote fractie 0.211 bij 900 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr2:186-187 Mb | heterozygote fractie 0.212 bij 1130 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr15:78-79 Mb | heterozygote fractie 0.213 bij 1895 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr3:51-52 Mb | heterozygote fractie 0.213 bij 923 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr11:46-47 Mb | heterozygote fractie 0.216 bij 751 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |
| chr2:169-170 Mb | heterozygote fractie 0.217 bij 1652 varianten | autosomale mediaan 0.633, spreiding 0.139 | `raw` |

## `roh` (3)

Aaneengesloten blokken onder 10 procent heterozygoot

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chr4:19-20 Mb | 1 Mb aaneengesloten onder 10% heterozygoot | autosomale mediaan 0.633 | `raw` |
| chr7:125-126 Mb | 1 Mb aaneengesloten onder 10% heterozygoot | autosomale mediaan 0.633 | `raw` |
| chr8:111-112 Mb | 1 Mb aaneengesloten onder 10% heterozygoot | autosomale mediaan 0.633 | `raw` |

## `gene-burden` (224)

Genen met 2 of meer coderende varianten buiten de gangbare catalogus

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| FCGBP | 52 coderende varianten buiten de gangbare catalogus, 9 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| MUC3A | 48 coderende varianten buiten de gangbare catalogus, 48 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| LILRB1 | 48 coderende varianten buiten de gangbare catalogus, 44 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| PRSS2 | 39 coderende varianten buiten de gangbare catalogus, 39 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LILRA2 | 26 coderende varianten buiten de gangbare catalogus, 26 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| KCNJ18 | 21 coderende varianten buiten de gangbare catalogus, 21 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV3-1 | 20 coderende varianten buiten de gangbare catalogus, 20 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| PRSS1 | 20 coderende varianten buiten de gangbare catalogus, 20 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| SERPINA1 | 19 coderende varianten buiten de gangbare catalogus, 19 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV7-6 | 19 coderende varianten buiten de gangbare catalogus, 19 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ZNF717 | 18 coderende varianten buiten de gangbare catalogus, 18 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| IGLV5-48 | 16 coderende varianten buiten de gangbare catalogus, 16 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| GSTT4 | 15 coderende varianten buiten de gangbare catalogus, 15 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| HLA-DRB1 | 14 coderende varianten buiten de gangbare catalogus, 13 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| MUC4 | 14 coderende varianten buiten de gangbare catalogus, 9 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TAS2R31 | 14 coderende varianten buiten de gangbare catalogus, 14 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| CCDC187 | 13 coderende varianten buiten de gangbare catalogus, 7 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV6-5 | 13 coderende varianten buiten de gangbare catalogus, 13 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| MUC6 | 13 coderende varianten buiten de gangbare catalogus, 13 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| IGHV4-31 | 12 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| OR8U1 | 12 coderende varianten buiten de gangbare catalogus, 12 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| SLC25A5 | 11 coderende varianten buiten de gangbare catalogus, 11 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LILRB2 | 11 coderende varianten buiten de gangbare catalogus, 11 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ASMTL | 11 coderende varianten buiten de gangbare catalogus, 11 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PRAMEF18 | 11 coderende varianten buiten de gangbare catalogus, 10 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TAS2R46 | 11 coderende varianten buiten de gangbare catalogus, 11 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| MUC5AC | 11 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| HLA-DQB2 | 10 coderende varianten buiten de gangbare catalogus, 9 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| LILRB3 | 10 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| SLC25A6 | 10 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TAS2R30 | 10 coderende varianten buiten de gangbare catalogus, 10 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| OR10G2 | 9 coderende varianten buiten de gangbare catalogus, 9 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| IGHV4-4 | 9 coderende varianten buiten de gangbare catalogus, 9 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRBV7-2 | 9 coderende varianten buiten de gangbare catalogus, 9 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| NBPF8 | 8 coderende varianten buiten de gangbare catalogus, 8 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| KIR3DL3 | 8 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| MUC2 | 8 coderende varianten buiten de gangbare catalogus, 7 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| AGAP3 | 8 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LILRA1 | 8 coderende varianten buiten de gangbare catalogus, 8 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| HLA-DQA1 | 8 coderende varianten buiten de gangbare catalogus, 8 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRBV5-6 | 8 coderende varianten buiten de gangbare catalogus, 8 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| IGHV3-48 | 8 coderende varianten buiten de gangbare catalogus, 8 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| IGHV1-3 | 7 coderende varianten buiten de gangbare catalogus, 7 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| MUC12 | 7 coderende varianten buiten de gangbare catalogus, 6 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TMC4 | 7 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| NBPF26 | 7 coderende varianten buiten de gangbare catalogus, 6 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ZNF418 | 7 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| NEU4 | 7 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ENSG00000206356 | 7 coderende varianten buiten de gangbare catalogus, 7 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGHV3-11 | 7 coderende varianten buiten de gangbare catalogus, 7 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| DHRSX | 7 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| HLA-DRB5 | 6 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| HMCN2 | 6 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LILRB5 | 6 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TAS2R19 | 6 coderende varianten buiten de gangbare catalogus, 6 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TAS2R43 | 6 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| CRLF2 | 6 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CYP2D7 | 6 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| FOXD4L4 | 5 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LAIR1 | 5 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| POU6F2 | 5 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGLV5-45 | 5 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRBV7-3 | 5 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| DSPP | 5 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| SPATA31A6 | 5 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CYP2D6 | 5 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| OR8G2P | 5 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ENSG00000289281 | 5 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| HLA-DQA2 | 5 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| CNTNAP3B | 5 coderende varianten buiten de gangbare catalogus, 5 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ZNF180 | 5 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TYW1B | 5 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRPV5 | 4 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ENSG00000293691 | 4 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGHV4-28 | 4 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRBV6-7 | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| IGKV1D-43 | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| CELA1 | 4 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GOLGA6L2 | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| HLA-A | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| HLA-B | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| CD99 | 4 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV5-4 | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| HTT | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| FAM136A | 4 coderende varianten buiten de gangbare catalogus, 4 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PLXNA3 | 4 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LBP | 4 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| EPHB6 | 4 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| KRTAP10-5 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| LILRB4 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| KLF14 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PRKRA | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CSAG1 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ECSCR | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CDSN | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV6-4 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| GAGE10 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LENG9 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV7-4 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRAV14DV4 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| LILRA4 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| MTCH2 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| MYOM2 | 3 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| RESF1 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ACTL9 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| FAM186A | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GOLGA8S | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| LENG8 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TNRC18 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CNTNAP3 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CRYBG2 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GOLGA6L9 | 3 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| RBM39 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV10-3 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ADCK5 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CEACAM7 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PCDHB8 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PRAME | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TUBB8B | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ADPRHL1 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PRSS3 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| AKAP17A | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GPR179 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| KANSL1 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CEP250 | 3 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| AADACL3 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV6-8 | 3 coderende varianten buiten de gangbare catalogus, 3 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| PDE4DIP | 3 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| AKR7L | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PIP5K1A | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| FANCD2 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PCDHA4 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| AKR1C8 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ESRRA | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| BLVRA | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGKV1D-8 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ZNF285 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ANKRD35 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GARRE1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CEACAM21 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ANKLE1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CD82 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| NCR1 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| HEG1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| DMRTC2 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GOLGA4 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TENT5A | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGHJ6 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ZAN | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PCLO | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| KRTAP10-1 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| FDXR | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CYP2C19 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| NBPF9 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TAS2R42 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TAF4B | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| LILRA6 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| PECAM1 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GRIPAP1 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ADGRA3 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGKJ2 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| MRPL45 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PRAMEF19 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ZSWIM6 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GOLGA6L1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ARID1B | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGHV3-7 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| FOLR3 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CACNA1F | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| G6PD | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGHM | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ADAMTS1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| MESP1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PKD1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| UBXN11 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| EPPK1 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGHV8-51-1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| BUB1B | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| KLF18 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRAV6 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| ZNF91 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRAV8-2 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRIM4 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| SLC2A8 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| STKLD1 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| UNC13B | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PDP1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PTPN20 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CEACAM5 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PPP2R3B | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV4-2 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| KRTAP10-4 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| KIF12 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| KCNJ12 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV5-3 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| TRBV12-4 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| SHANK3 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TSSK6 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| VPS28 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GTPBP6 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| CTAG2 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ENPP7 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| KRTAP5-1 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| VPS41 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| SMC4 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PWWP4 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| DNAH12 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PSMD3 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GADD45G | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| MROH1 | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| GDF5 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| ALMS1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PSG1 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| QRICH2 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PCDHB5 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| RCC1L | 2 coderende varianten buiten de gangbare catalogus, 1 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| IGHV3-53 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| PCDHB9 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PCDHB16 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| MUTYH | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| TRBV6-2 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| SLC39A4 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |
| PRAMEF10 | 2 coderende varianten buiten de gangbare catalogus, 2 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `artefact-prone` |
| DECR2 | 2 coderende varianten buiten de gangbare catalogus, 0 heterozygoot | genoombreed 1.694 zulke varianten in 704 genen | `raw` |

## `gene-frequency` (151)

Voor diezelfde genen: de gnomAD-frequenties van hun varianten

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| VPS41 | 2 varianten, laagste 0.0e+00, op een na laagste 0.0e+00 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| SERPINA1 | 19 varianten, laagste 0.0e+00, op een na laagste 0.0e+00 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| BUB1B | 2 varianten, laagste 6.8e-07, op een na laagste 7.9e-05 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| KIR3DL3 | 2 varianten, laagste 6.8e-07, op een na laagste 7.3e-05 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| TSSK6 | 1 varianten, laagste 2.1e-06, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| RESF1 | 1 varianten, laagste 4.1e-06, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| SMC4 | 1 varianten, laagste 6.6e-06, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| RBM39 | 2 varianten, laagste 6.6e-06, op een na laagste 1.3e-05 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| ARID1B | 2 varianten, laagste 9.4e-06, op een na laagste 1.5e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| UNC13B | 2 varianten, laagste 1.0e-05, op een na laagste 1.7e-04 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CD82 | 1 varianten, laagste 1.2e-05, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GOLGA4 | 1 varianten, laagste 1.3e-05, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TNRC18 | 3 varianten, laagste 2.1e-05, op een na laagste 2.0e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| BLVRA | 1 varianten, laagste 2.7e-05, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ADGRA3 | 2 varianten, laagste 3.3e-05, op een na laagste 7.9e-05 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| PSG1 | 2 varianten, laagste 3.3e-05, op een na laagste 4.5e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PDP1 | 1 varianten, laagste 3.9e-05, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TAF4B | 1 varianten, laagste 4.7e-05, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MUC4 | 9 varianten, laagste 5.1e-05, op een na laagste 8.5e-05 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| ADAMTS1 | 2 varianten, laagste 5.3e-05, op een na laagste 5.3e-05 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `notable` |
| QRICH2 | 2 varianten, laagste 5.3e-05, op een na laagste 3.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| FOXD4L4 | 5 varianten, laagste 5.6e-05, op een na laagste 2.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PKD1 | 2 varianten, laagste 2.6e-04, op een na laagste 1.7e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| SLC25A5 | 8 varianten, laagste 3.1e-04, op een na laagste 6.1e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGKV1D-43 | 4 varianten, laagste 3.7e-04, op een na laagste 4.6e-04 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PRKRA | 2 varianten, laagste 3.9e-04, op een na laagste 1.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TAS2R31 | 14 varianten, laagste 7.3e-04, op een na laagste 3.2e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| POU6F2 | 5 varianten, laagste 1.0e-03, op een na laagste 1.3e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MUC6 | 13 varianten, laagste 1.4e-03, op een na laagste 1.4e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRA2 | 24 varianten, laagste 2.1e-03, op een na laagste 2.2e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HLA-DQA1 | 8 varianten, laagste 2.4e-03, op een na laagste 4.0e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| FCGBP | 9 varianten, laagste 2.7e-03, op een na laagste 1.1e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| AKR7L | 2 varianten, laagste 3.7e-03, op een na laagste 3.9e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PRSS3 | 3 varianten, laagste 4.4e-03, op een na laagste 1.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ENSG00000206356 | 7 varianten, laagste 4.5e-03, op een na laagste 5.6e-03 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| KCNJ18 | 21 varianten, laagste 5.3e-03, op een na laagste 7.2e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GARRE1 | 2 varianten, laagste 6.8e-03, op een na laagste 4.3e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV7-6 | 19 varianten, laagste 8.4e-03, op een na laagste 4.7e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MUTYH | 2 varianten, laagste 8.5e-03, op een na laagste 1.1e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HLA-DQA2 | 5 varianten, laagste 8.8e-03, op een na laagste 1.1e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ADPRHL1 | 3 varianten, laagste 9.7e-03, op een na laagste 1.3e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ASMTL | 10 varianten, laagste 9.9e-03, op een na laagste 7.2e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MUC12 | 6 varianten, laagste 1.0e-02, op een na laagste 5.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| FAM136A | 4 varianten, laagste 1.4e-02, op een na laagste 2.5e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRB1 | 44 varianten, laagste 1.5e-02, op een na laagste 1.6e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRA4 | 3 varianten, laagste 2.0e-02, op een na laagste 8.1e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HMCN2 | 5 varianten, laagste 2.1e-02, op een na laagste 5.6e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| NBPF8 | 8 varianten, laagste 2.1e-02, op een na laagste 1.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV4-4 | 9 varianten, laagste 2.1e-02, op een na laagste 2.2e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TAS2R30 | 10 varianten, laagste 2.3e-02, op een na laagste 2.3e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TUBB8B | 3 varianten, laagste 2.5e-02, op een na laagste 4.1e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HLA-DRB5 | 4 varianten, laagste 2.5e-02, op een na laagste 7.0e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HLA-DRB1 | 10 varianten, laagste 2.7e-02, op een na laagste 3.0e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV5-4 | 4 varianten, laagste 2.9e-02, op een na laagste 8.0e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HLA-B | 4 varianten, laagste 3.0e-02, op een na laagste 3.1e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TAS2R19 | 6 varianten, laagste 3.3e-02, op een na laagste 5.1e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HTT | 4 varianten, laagste 3.4e-02, op een na laagste 6.7e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HLA-DQB2 | 9 varianten, laagste 3.5e-02, op een na laagste 6.3e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRB4 | 3 varianten, laagste 3.6e-02, op een na laagste 6.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRA1 | 8 varianten, laagste 4.8e-02, op een na laagste 5.8e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ZNF717 | 18 varianten, laagste 4.8e-02, op een na laagste 5.1e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ESRRA | 2 varianten, laagste 4.8e-02, op een na laagste 6.7e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PCLO | 2 varianten, laagste 5.2e-02, op een na laagste 5.3e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GADD45G | 2 varianten, laagste 5.7e-02, op een na laagste 5.7e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PRSS1 | 20 varianten, laagste 6.2e-02, op een na laagste 6.7e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ALMS1 | 2 varianten, laagste 6.3e-02, op een na laagste 4.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PRSS2 | 39 varianten, laagste 6.4e-02, op een na laagste 1.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| NEU4 | 5 varianten, laagste 6.8e-02, op een na laagste 7.8e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGLV5-45 | 4 varianten, laagste 6.9e-02, op een na laagste 2.4e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CRLF2 | 4 varianten, laagste 7.3e-02, op een na laagste 2.5e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV4-28 | 3 varianten, laagste 8.7e-02, op een na laagste 9.0e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| SLC2A8 | 2 varianten, laagste 9.2e-02, op een na laagste 9.3e-02 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PCDHB8 | 2 varianten, laagste 9.8e-02, op een na laagste 1.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HLA-A | 4 varianten, laagste 1.1e-01, op een na laagste 1.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CCDC187 | 7 varianten, laagste 1.1e-01, op een na laagste 1.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MUC3A | 48 varianten, laagste 1.1e-01, op een na laagste 1.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CYP2D6 | 2 varianten, laagste 1.3e-01, op een na laagste 3.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV10-3 | 3 varianten, laagste 1.3e-01, op een na laagste 1.4e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV6-7 | 4 varianten, laagste 1.3e-01, op een na laagste 1.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GOLGA6L9 | 2 varianten, laagste 1.4e-01, op een na laagste 2.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV5-6 | 8 varianten, laagste 1.4e-01, op een na laagste 2.4e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV12-4 | 2 varianten, laagste 1.5e-01, op een na laagste 4.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV6-5 | 13 varianten, laagste 1.6e-01, op een na laagste 4.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| SLC25A6 | 3 varianten, laagste 1.7e-01, op een na laagste 1.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| AADACL3 | 3 varianten, laagste 1.7e-01, op een na laagste 1.7e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRB5 | 5 varianten, laagste 1.7e-01, op een na laagste 1.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GOLGA6L2 | 4 varianten, laagste 1.7e-01, op een na laagste 4.4e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CEACAM5 | 1 varianten, laagste 1.7e-01, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PCDHB5 | 2 varianten, laagste 1.8e-01, op een na laagste 1.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| HEG1 | 2 varianten, laagste 1.8e-01, op een na laagste 2.1e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| SPATA31A6 | 5 varianten, laagste 1.9e-01, op een na laagste 3.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ANKLE1 | 2 varianten, laagste 1.9e-01, op een na laagste 2.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| KANSL1 | 2 varianten, laagste 1.9e-01, op een na laagste 1.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CYP2D7 | 3 varianten, laagste 2.2e-01, op een na laagste 3.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ZNF91 | 1 varianten, laagste 2.3e-01, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TENT5A | 1 varianten, laagste 2.3e-01, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PRAMEF18 | 10 varianten, laagste 2.3e-01, op een na laagste 3.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| NBPF26 | 6 varianten, laagste 2.4e-01, op een na laagste 3.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| KIF12 | 1 varianten, laagste 2.4e-01, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRB3 | 3 varianten, laagste 2.5e-01, op een na laagste 2.7e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MESP1 | 2 varianten, laagste 2.6e-01, op een na laagste 2.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TAS2R46 | 11 varianten, laagste 2.7e-01, op een na laagste 3.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CNTNAP3B | 5 varianten, laagste 2.7e-01, op een na laagste 2.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV3-48 | 8 varianten, laagste 2.9e-01, op een na laagste 4.5e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| FAM186A | 3 varianten, laagste 2.9e-01, op een na laagste 3.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PSMD3 | 2 varianten, laagste 3.0e-01, op een na laagste 3.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ACTL9 | 3 varianten, laagste 3.0e-01, op een na laagste 3.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| DSPP | 4 varianten, laagste 3.1e-01, op een na laagste 4.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV6-2 | 2 varianten, laagste 3.1e-01, op een na laagste 3.1e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV7-2 | 9 varianten, laagste 3.2e-01, op een na laagste 3.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GOLGA6L1 | 2 varianten, laagste 3.2e-01, op een na laagste 3.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| DHRSX | 5 varianten, laagste 3.2e-01, op een na laagste 3.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV3-1 | 20 varianten, laagste 3.3e-01, op een na laagste 3.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| NBPF9 | 2 varianten, laagste 3.4e-01, op een na laagste 4.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV7-4 | 3 varianten, laagste 3.5e-01, op een na laagste 4.1e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV4-2 | 2 varianten, laagste 3.5e-01, op een na laagste 3.5e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| OR8U1 | 12 varianten, laagste 3.5e-01, op een na laagste 3.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CEACAM21 | 2 varianten, laagste 3.5e-01, op een na laagste 4.2e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LBP | 3 varianten, laagste 3.5e-01, op een na laagste 3.7e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRIM4 | 2 varianten, laagste 3.6e-01, op een na laagste 3.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRB2 | 11 varianten, laagste 3.7e-01, op een na laagste 4.4e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GSTT4 | 15 varianten, laagste 3.8e-01, op een na laagste 3.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PCDHA4 | 2 varianten, laagste 3.8e-01, op een na laagste 3.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MUC2 | 7 varianten, laagste 3.8e-01, op een na laagste 3.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV1-3 | 7 varianten, laagste 4.1e-01, op een na laagste 4.2e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV8-51-1 | 2 varianten, laagste 4.3e-01, op een na laagste 8.4e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ZNF285 | 2 varianten, laagste 4.4e-01, op een na laagste 4.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| GTPBP6 | 2 varianten, laagste 4.4e-01, op een na laagste 5.1e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| FANCD2 | 2 varianten, laagste 4.5e-01, op een na laagste 4.5e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CNTNAP3 | 3 varianten, laagste 4.6e-01, op een na laagste 4.7e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| OR8G2P | 2 varianten, laagste 4.6e-01, op een na laagste 5.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV3-11 | 7 varianten, laagste 4.9e-01, op een na laagste 5.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| OR10G2 | 9 varianten, laagste 4.9e-01, op een na laagste 4.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRBV6-8 | 3 varianten, laagste 4.9e-01, op een na laagste 4.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PTPN20 | 2 varianten, laagste 4.9e-01, op een na laagste 4.9e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| PRAMEF10 | 2 varianten, laagste 4.9e-01, op een na laagste 6.7e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MTCH2 | 3 varianten, laagste 5.0e-01, op een na laagste 5.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| KCNJ12 | 2 varianten, laagste 5.0e-01, op een na laagste 5.0e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| DMRTC2 | 1 varianten, laagste 5.1e-01, op een na laagste n.v.t. | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| LILRA6 | 2 varianten, laagste 5.1e-01, op een na laagste 5.4e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CEACAM7 | 3 varianten, laagste 5.1e-01, op een na laagste 5.2e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ANKRD35 | 2 varianten, laagste 5.3e-01, op een na laagste 8.5e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV3-7 | 2 varianten, laagste 5.5e-01, op een na laagste 5.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGLV5-48 | 16 varianten, laagste 5.6e-01, op een na laagste 6.2e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TRAV14DV4 | 3 varianten, laagste 5.8e-01, op een na laagste 5.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| ENPP7 | 2 varianten, laagste 6.1e-01, op een na laagste 6.1e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| MYOM2 | 2 varianten, laagste 6.5e-01, op een na laagste 8.5e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| IGHV3-53 | 2 varianten, laagste 6.6e-01, op een na laagste 6.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| TAS2R42 | 2 varianten, laagste 7.6e-01, op een na laagste 7.6e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| CDSN | 3 varianten, laagste 7.8e-01, op een na laagste 7.8e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |
| FDXR | 2 varianten, laagste 8.3e-01, op een na laagste 8.3e-01 | gnomAD v4.1; drempel van de kandidaat is 1e-4 op beide | `raw` |

## `phase-set` (151)

Genen waarvan de varianten een fasegroep delen, met de cis- of trans-uitspraak

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| AADACL3 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PRAMEF10 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PRAMEF18 | 10 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| AKR7L | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| MUTYH | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| NBPF8 | 8 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| NBPF26 | 6 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| ANKRD35 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| NBPF9 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| FAM136A | 4 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ALMS1 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| IGKV1D-43 | 4 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| PRKRA | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| NEU4 | 5 heterozygote varianten, een op elke kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| FANCD2 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| GOLGA4 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ZNF717 | 18 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HEG1 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| SMC4 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| MUC4 | 9 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HTT | 4 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| ADGRA3 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| DSPP | 4 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| ENSG00000206356 | 7 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PCDHA4 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| PCDHB5 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PCDHB8 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| HLA-A | 4 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| CDSN | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HLA-B | 4 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HLA-DRB5 | 4 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HLA-DRB1 | 13 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HLA-DQA1 | 8 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HLA-DQA2 | 5 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| HLA-DQB2 | 9 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TENT5A | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ARID1B | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TNRC18 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| VPS41 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| POU6F2 | 5 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| BLVRA | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PCLO | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRIM4 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| MUC3A | 48 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| MUC12 | 6 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| TRBV3-1 | 20 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV4-2 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV6-2 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| TRBV7-2 | 9 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| TRBV6-5 | 13 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV7-4 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| TRBV5-4 | 4 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| TRBV6-7 | 4 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV7-6 | 19 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV5-6 | 8 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV6-8 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV10-3 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRBV12-4 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PRSS1 | 20 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PRSS2 | 39 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| MYOM2 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PDP1 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PRSS3 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| UNC13B | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CNTNAP3 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| CNTNAP3B | 5 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| SPATA31A6 | 5 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| FOXD4L4 | 5 heterozygote varianten, een op elke kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| GADD45G | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| KIF12 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| SLC2A8 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| HMCN2 | 5 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CCDC187 | 7 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| PTPN20 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| MUC6 | 13 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| MUC2 | 7 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CD82 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| MTCH2 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| OR8U1 | 12 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ESRRA | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| OR8G2P | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TAS2R19 | 6 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TAS2R31 | 14 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TAS2R46 | 11 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TAS2R30 | 10 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TAS2R42 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| RESF1 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| FAM186A | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| ADPRHL1 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| OR10G2 | 9 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TRAV14DV4 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| SERPINA1 | 19 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| IGHV1-3 | 7 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| IGHV4-4 | 9 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| IGHV3-7 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| IGHV3-11 | 7 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| IGHV4-28 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| IGHV3-48 | 8 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| IGHV8-51-1 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| IGHV3-53 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| GOLGA6L1 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| GOLGA6L2 | 4 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| BUB1B | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| GOLGA6L9 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| MESP1 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| PKD1 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| KCNJ12 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| KCNJ18 | 21 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PSMD3 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| KANSL1 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| FDXR | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| QRICH2 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ENPP7 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TUBB8B | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TAF4B | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ACTL9 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ANKLE1 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| TSSK6 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ZNF91 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| GARRE1 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| FCGBP | 9 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CEACAM21 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CEACAM7 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CEACAM5 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| DMRTC2 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| PSG1 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ZNF285 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRB3 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRA6 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRB5 | 5 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| LILRB2 | 11 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRA4 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRA2 | 26 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRA1 | 8 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRB1 | 44 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LILRB4 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| KIR3DL3 | 3 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| RBM39 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| LBP | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ADAMTS1 | 2 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| IGLV5-48 | 16 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| IGLV5-45 | 4 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| GSTT4 | 15 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CYP2D6 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CYP2D7 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| GTPBP6 | 2 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| CRLF2 | 4 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| SLC25A6 | 3 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| ASMTL | 11 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |
| DHRSX | 5 heterozygote varianten, beide op dezelfde kopie | GATK PGT/PID in het geleverde bestand | `notable` |
| SLC25A5 | 11 heterozygote varianten, geen gedeelde fasegroep | GATK PGT/PID in het geleverde bestand | `raw` |

## `clinvar` (7)

ClinVar-records als pathogeen of waarschijnlijk pathogeen aanwezig in dit genoom

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chr1:145927447 C>T (RBM8A) | genotype 0/1, diepte 36, kwaliteit 99 | ClinVar Pathogenic/Likely_pathogenic/Pathogenic,_low_penetrance|othe | `notable` |
| chr1:152307547 G>A (FLG) | genotype 0/1, diepte 38, kwaliteit 99 | ClinVar Pathogenic/Likely_pathogenic | `notable` |
| chr4:67753920 C>T (GNRHR) | genotype 0/1, diepte 60, kwaliteit 99 | ClinVar Pathogenic | `notable` |
| chr7:142750561 C>T (PRSS1) | genotype 0/1, diepte 34, kwaliteit 99 | ClinVar Pathogenic/Likely_pathogenic | `notable` |
| chr10:69315762 A>G (HK1) | genotype 0/1, diepte 48, kwaliteit 99 | ClinVar Pathogenic/Likely_pathogenic | `notable` |
| chr15:40209701 T>G (BUB1B) | genotype 0/1, diepte 46, kwaliteit 99 | ClinVar Pathogenic/Likely_pathogenic | `notable` |
| chr22:20996720 C>G (LZTR1) | genotype 0/1, diepte 48, kwaliteit 99 | ClinVar Pathogenic/Likely_pathogenic | `notable` |

## `variant-quality` (432)

Coderende varianten met allelbalans buiten 0,30 tot 0,70 of kwaliteit onder 90

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chr1:13150214 A>T (PRAMEF26) | allelbalans 0.25, diepte 36, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:13224919 T>A (PRAMEF18) | allelbalans 0.28, diepte 97, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:13225044 C>G (PRAMEF18) | allelbalans 0.30, diepte 105, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:13369246 T>C (PRAMEF19) | allelbalans 0.15, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:45330035 C>CCGGGCCGGGCGCGGTGGCT (MUTYH) | allelbalans 0.19, diepte 27, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:45330037 A>AC (MUTYH) | allelbalans 0.08, diepte 25, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:47994148 G>A (TRABD2B) | allelbalans 0.24, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:120449357 C>G (NBPF8) | allelbalans 0.12, diepte 66, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:120449388 G>A (NBPF8) | allelbalans 0.90, diepte 52, kwaliteit 68 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:120449389 A>G (NBPF8) | allelbalans 0.90, diepte 50, kwaliteit 68 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:120461263 G>A (NBPF8) | allelbalans 0.17, diepte 36, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:120461377 G>C (NBPF8) | allelbalans 0.24, diepte 29, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:120809853 A>C (NBPF26) | allelbalans 0.29, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:120809863 A>G (NBPF26) | allelbalans 0.20, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:120809865 T>G (NBPF26) | allelbalans 0.20, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:120809867 G>A (NBPF26) | allelbalans 0.19, diepte 36, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:120810541 C>T (NBPF26) | allelbalans 0.18, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr1:149005208 C>T (PDE4DIP) | allelbalans 0.24, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr1:154869723 G>GGCTGCTGCTGCT,GGCTGCTGCTGCTGCTGCTGCT (KCNN3) | allelbalans 1.00, diepte 24, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:20667362 G>GGGCGGCGGC,GGGCGGCGGCGGCGGCGGC (GDF7) | allelbalans 1.00, diepte 24, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:70297319 C>T (FAM136A) | allelbalans 0.12, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:70297345 G>C (FAM136A) | allelbalans 0.17, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:70297376 A>ACAGC (FAM136A) | allelbalans 0.15, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:70297379 ACTGT>A (FAM136A) | allelbalans 0.15, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:89085291 A>G (IGKV3-15) | allelbalans 0.22, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr2:90210392 T>G (IGKV1D-43) | allelbalans 0.06, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:90210393 A>C (IGKV1D-43) | allelbalans 0.06, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:90210403 T>A (IGKV1D-43) | allelbalans 0.17, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:90210407 C>G (IGKV1D-43) | allelbalans 0.17, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:119447863 C>T (TMEM37) | allelbalans 0.29, diepte 28, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr2:131263969 C>T (POTEE) | allelbalans 0.15, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:178450414 G>GAAGGTCCCACTGTCCTCGCGCTCCAGCGGCGGGGCCTCGGCGGTGCCTGCTCTGGGA (PRKRA) | allelbalans 0.16, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:178450414 G>GAAGGTCCCACTGTCCTCGCGCTCCAGCGGCGGGGCCTCGGCGGTGCCTGCTCTGGGA (PRKRA) | allelbalans 0.16, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr2:178451030 T>G (PRKRA) | allelbalans 0.18, diepte 22, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:197872 CT>C,CTTT (CHL1) | allelbalans 1.00, diepte 28, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:40462029 A>ACTGCTGCTGCTG,ACTGCTGCTGCTGCTGCTGCTGCTG (RPL14) | allelbalans 1.00, diepte 36, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:75738712 A>T (ZNF717) | allelbalans 0.20, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:75738713 T>A (ZNF717) | allelbalans 0.20, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:75739041 T>C (ZNF717) | allelbalans 0.14, diepte 63, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:75739044 A>T (ZNF717) | allelbalans 0.15, diepte 62, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:75739049 G>A (ZNF717) | allelbalans 0.14, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:75739225 G>GTT (ZNF717) | allelbalans 0.22, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:75739231 C>T (ZNF717) | allelbalans 0.25, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:75739239 A>C (ZNF717) | allelbalans 0.27, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:195779399 GACCTGTGGATAATGAGGAAGCATTGGTGACAGGAAGAGGGGTGGTGTC>G (MUC4) | allelbalans 0.88, diepte 17, kwaliteit 36 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:195779605 GAGGAAGTGTCGGTGACAGGAAGGGGGGTGGCGTGACCTGTGGATGCTGAGGAACGGCTGGTGACAGGAAGAGAGGTGGCGTGACCTGTGGATA>G (MUC4) | allelbalans 0.83, diepte 24, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:195780783 G>C (MUC4) | allelbalans 0.25, diepte 8, kwaliteit 66 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:195780795 T>G (MUC4) | allelbalans 0.22, diepte 9, kwaliteit 63 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:195784576 GTGGTGTCACCTGTGGATGCTGAGGAAAGGCTGGTGACAGGAAGAGGGGTGGCGTGACCTGTGGATGCTGAGGAAGCGTCGGTGACATGAAGAGGGGTGGCGTGACCTGTGGATGCTGAGGAAGGGCTAGTGACAGGAAGAGGA>G (MUC4) | allelbalans 0.81, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr3:195785343 G>C (MUC4) | allelbalans 0.24, diepte 41, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:195785361 T>C (MUC4) | allelbalans 0.26, diepte 31, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:195785362 G>A (MUC4) | allelbalans 0.26, diepte 27, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr3:195785375 T>C (MUC4) | allelbalans 0.09, diepte 22, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr5:99522854 C>G (ENSG00000206356) | allelbalans 0.26, diepte 35, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr5:99524057 G>T (ENSG00000206356) | allelbalans 0.18, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr5:140807399 GC>G (PCDHA4) | allelbalans 0.29, diepte 24, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr5:140807403 AGG>A (PCDHA4) | allelbalans 0.26, diepte 23, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr5:141178732 T>TCC (PCDHB8) | allelbalans 0.23, diepte 30, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr5:141178734 GTC>G (PCDHB8) | allelbalans 0.21, diepte 29, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr5:141180333 C>A,T (PCDHB8) | allelbalans 1.00, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:31741336 TACACACACACAC>T,TACACACACAC (MSH5) | allelbalans 1.00, diepte 15, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32519533 G>A (HLA-DRB5) | allelbalans 0.25, diepte 28, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32530180 C>CAG (HLA-DRB5) | allelbalans 0.16, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32530183 CTT>C (HLA-DRB5) | allelbalans 0.10, diepte 31, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32581704 C>T (HLA-DRB1) | allelbalans 0.24, diepte 94, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32581748 C>G (HLA-DRB1) | allelbalans 0.24, diepte 75, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32584393 A>ATG (HLA-DRB1) | allelbalans 0.20, diepte 15, kwaliteit 90 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32584393 A>ATG (HLA-DRB1) | allelbalans 0.20, diepte 15, kwaliteit 90 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32584394 CCA>C (HLA-DRB1) | allelbalans 0.20, diepte 15, kwaliteit 90 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32584394 CCA>C (HLA-DRB1) | allelbalans 0.20, diepte 15, kwaliteit 90 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32745298 T>C (HLA-DQA2) | allelbalans 0.13, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32745299 A>C (HLA-DQA2) | allelbalans 0.13, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32745303 A>G (HLA-DQA2) | allelbalans 0.14, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32745313 T>A (HLA-DQA2) | allelbalans 0.14, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32746011 T>G (HLA-DQA2) | allelbalans 0.21, diepte 34, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:32761203 C>T (HLA-DQB2) | allelbalans 0.15, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761225 T>C (HLA-DQB2) | allelbalans 0.15, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761226 G>A (HLA-DQB2) | allelbalans 0.15, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761228 G>T (HLA-DQB2) | allelbalans 0.15, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761231 G>A (HLA-DQB2) | allelbalans 0.15, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761232 C>T (HLA-DQB2) | allelbalans 0.15, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761237 T>A (HLA-DQB2) | allelbalans 0.16, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761241 C>T (HLA-DQB2) | allelbalans 0.16, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr6:32761248 G>A (HLA-DQB2) | allelbalans 0.25, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr6:170561961 G>GCAA (TBP) | allelbalans 0.21, diepte 24, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:5313004 T>G (TNRC18) | allelbalans 0.29, diepte 41, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:5313034 T>G (TNRC18) | allelbalans 0.24, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:100956382 A>G (MUC3A) | allelbalans 0.25, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:100956420 C>T (MUC3A) | allelbalans 0.24, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:100956476 C>G (MUC3A) | allelbalans 0.28, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:100956478 G>C (MUC3A) | allelbalans 0.29, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:100956480 G>C (MUC3A) | allelbalans 0.29, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:100956488 G>A (MUC3A) | allelbalans 0.25, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:100956513 T>C (MUC3A) | allelbalans 0.16, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:100956516 T>C (MUC3A) | allelbalans 0.16, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:100956528 C>T (MUC3A) | allelbalans 0.19, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:100956539 G>C (MUC3A) | allelbalans 0.18, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:100964820 T>C (MUC3A) | allelbalans 0.80, diepte 86, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:100966916 T>C (MUC3A) | allelbalans 0.78, diepte 83, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:101002450 G>A (MUC12) | allelbalans 0.20, diepte 79, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142308611 G>A (TRBV3-1) | allelbalans 0.26, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142308617 T>C (TRBV3-1) | allelbalans 0.25, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142308619 T>C (TRBV3-1) | allelbalans 0.25, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142308630 C>G (TRBV3-1) | allelbalans 0.23, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142345862 C>T (TRBV4-2) | allelbalans 0.27, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142349257 G>C (TRBV6-2) | allelbalans 0.21, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142349258 G>A (TRBV6-2) | allelbalans 0.20, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142353265 C>T (TRBV7-2) | allelbalans 0.29, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142353272 G>A (TRBV7-2) | allelbalans 0.29, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142451396 C>G (TRBV6-5) | allelbalans 0.25, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142451397 T>A (TRBV6-5) | allelbalans 0.26, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142451401 G>A (TRBV6-5) | allelbalans 0.26, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142451425 G>A (TRBV6-5) | allelbalans 0.27, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142455390 G>A (TRBV7-4) | allelbalans 0.28, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142455395 G>A (TRBV7-4) | allelbalans 0.25, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142463290 T>C (TRBV5-4) | allelbalans 0.16, diepte 31, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142463299 A>G (TRBV5-4) | allelbalans 0.16, diepte 31, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142488266 T>A (TRBV6-7) | allelbalans 0.13, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142488272 T>A (TRBV6-7) | allelbalans 0.13, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142488293 C>T (TRBV6-7) | allelbalans 0.16, diepte 43, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142492557 A>G (TRBV7-6) | allelbalans 0.29, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142492568 A>G (TRBV7-6) | allelbalans 0.27, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142492575 G>C (TRBV7-6) | allelbalans 0.26, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142492580 C>T (TRBV7-6) | allelbalans 0.21, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142492587 G>A (TRBV7-6) | allelbalans 0.17, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142492603 A>G (TRBV7-6) | allelbalans 0.11, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142500074 C>A (TRBV5-6) | allelbalans 0.18, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142500078 G>A (TRBV5-6) | allelbalans 0.20, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142500088 G>T (TRBV5-6) | allelbalans 0.26, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142500110 G>C (TRBV5-6) | allelbalans 0.29, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142500243 T>C (TRBV5-6) | allelbalans 0.16, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142500244 T>C (TRBV5-6) | allelbalans 0.16, diepte 44, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142500251 C>G (TRBV5-6) | allelbalans 0.14, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142507407 C>T (TRBV6-8) | allelbalans 0.14, diepte 35, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142749506 A>G (PRSS1) | allelbalans 0.15, diepte 27, kwaliteit 96 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142749516 C>G (PRSS1) | allelbalans 0.15, diepte 26, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142749524 C>G (PRSS1) | allelbalans 0.15, diepte 26, kwaliteit 96 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142751076 AAG>A (PRSS1) | allelbalans 0.14, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142751081 A>AG (PRSS1) | allelbalans 0.15, diepte 41, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142751082 A>G (PRSS1) | allelbalans 0.12, diepte 41, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142752476 G>C (PRSS1) | allelbalans 0.23, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142752490 G>A (PRSS1) | allelbalans 0.21, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142752505 G>T (PRSS1) | allelbalans 0.24, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142752506 G>T (PRSS1) | allelbalans 0.22, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142752522 C>G (PRSS1) | allelbalans 0.21, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142752561 A>C (PRSS1) | allelbalans 0.27, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142752564 T>C (PRSS1) | allelbalans 0.26, diepte 34, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142752947 A>G (PRSS1) | allelbalans 0.16, diepte 25, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142752948 C>A (PRSS1) | allelbalans 0.16, diepte 25, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142752950 A>G (PRSS1) | allelbalans 0.15, diepte 26, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142772055 C>T (PRSS2) | allelbalans 0.17, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142772080 C>T (PRSS2) | allelbalans 0.21, diepte 43, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142772094 T>A (PRSS2) | allelbalans 0.18, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142772129 T>C (PRSS2) | allelbalans 0.17, diepte 36, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142772154 G>T (PRSS2) | allelbalans 0.26, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142772166 T>A (PRSS2) | allelbalans 0.28, diepte 36, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142772170 C>G (PRSS2) | allelbalans 0.29, diepte 35, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773308 G>A (PRSS2) | allelbalans 0.24, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773330 A>T (PRSS2) | allelbalans 0.22, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773337 C>T (PRSS2) | allelbalans 0.26, diepte 31, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773369 C>T (PRSS2) | allelbalans 0.17, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142773408 T>A (PRSS2) | allelbalans 0.21, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773426 T>G (PRSS2) | allelbalans 0.20, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142773430 G>A (PRSS2) | allelbalans 0.20, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773431 C>T (PRSS2) | allelbalans 0.20, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773438 G>A (PRSS2) | allelbalans 0.17, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr7:142773481 C>G (PRSS2) | allelbalans 0.21, diepte 43, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773485 C>T (PRSS2) | allelbalans 0.21, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773503 C>T (PRSS2) | allelbalans 0.23, diepte 44, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773506 T>C (PRSS2) | allelbalans 0.22, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773512 T>C (PRSS2) | allelbalans 0.24, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773515 T>A (PRSS2) | allelbalans 0.24, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142773518 T>G (PRSS2) | allelbalans 0.23, diepte 43, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142774016 C>T (PRSS2) | allelbalans 0.29, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142774025 C>T (PRSS2) | allelbalans 0.30, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142774361 T>C (PRSS2) | allelbalans 0.24, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142774373 T>A (PRSS2) | allelbalans 0.21, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142774381 C>G (PRSS2) | allelbalans 0.24, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142774386 G>A (PRSS2) | allelbalans 0.26, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:142774389 G>C (PRSS2) | allelbalans 0.29, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr7:157009949 A>AGCGGCG,AGCGGCGGCG (MNX1) | allelbalans 1.00, diepte 9, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr8:12137930 G>A (USP17L2) | allelbalans 0.18, diepte 22, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr9:33794813 G>A (PRSS3) | allelbalans 0.13, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr9:33797919 T>C (PRSS3) | allelbalans 0.11, diepte 44, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr9:33798077 T>C (PRSS3) | allelbalans 0.14, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr9:39078736 G>A (CNTNAP3) | allelbalans 0.28, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr9:41923878 C>T (CNTNAP3B) | allelbalans 0.18, diepte 101, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr9:42187569 C>G (SPATA31A6) | allelbalans 0.75, diepte 20, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr9:42187574 C>T (SPATA31A6) | allelbalans 0.25, diepte 20, kwaliteit 83 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr9:127408233 C>CCACT (SLC2A8) | allelbalans 0.94, diepte 17, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr10:45826906 G>C (AGAP4) | allelbalans 0.21, diepte 28, kwaliteit 93 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr10:124021236 CGG>C,CGGGG (CHST15) | allelbalans 1.00, diepte 11, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1016887 G>A (MUC6) | allelbalans 0.14, diepte 173, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1016906 G>T (MUC6) | allelbalans 0.13, diepte 146, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1016912 G>A (MUC6) | allelbalans 0.13, diepte 138, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1016939 G>A (MUC6) | allelbalans 0.15, diepte 114, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1016950 C>T (MUC6) | allelbalans 0.09, diepte 108, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1016951 A>G (MUC6) | allelbalans 0.09, diepte 108, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1017035 A>AAT (MUC6) | allelbalans 0.27, diepte 102, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr11:1017040 GGT>G (MUC6) | allelbalans 0.26, diepte 108, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr11:1017135 G>A (MUC6) | allelbalans 0.15, diepte 125, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1017458 A>G (MUC6) | allelbalans 0.14, diepte 111, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1017935 A>C (MUC6) | allelbalans 0.12, diepte 84, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1017939 G>C (MUC6) | allelbalans 0.13, diepte 84, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:1018024 C>G (MUC6) | allelbalans 0.29, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr11:47638742 C>T (MTCH2) | allelbalans 0.19, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:47638743 A>G (MTCH2) | allelbalans 0.19, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:47638749 T>A (MTCH2) | allelbalans 0.19, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:56376427 G>T (OR8U1) | allelbalans 0.28, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr11:56376493 T>C (OR8U1) | allelbalans 0.14, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:56376496 C>T (OR8U1) | allelbalans 0.14, diepte 66, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:56376500 C>A (OR8U1) | allelbalans 0.14, diepte 63, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:56376505 T>C (OR8U1) | allelbalans 0.14, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:64315823 CGGG>C (ESRRA) | allelbalans 0.15, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:64315846 G>A (ESRRA) | allelbalans 0.15, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr11:90086720 C>CT (UBTFL1) | allelbalans 0.29, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11021868 A>C (TAS2R19) | allelbalans 0.30, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11021879 C>A (TAS2R19) | allelbalans 0.24, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11021935 T>C (TAS2R19) | allelbalans 0.14, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11021943 C>T (TAS2R19) | allelbalans 0.13, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11021949 T>A (TAS2R19) | allelbalans 0.13, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030508 T>C (TAS2R31) | allelbalans 0.20, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11030515 A>G (TAS2R31) | allelbalans 0.17, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030516 T>C (TAS2R31) | allelbalans 0.17, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030522 G>A (TAS2R31) | allelbalans 0.17, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030534 T>C (TAS2R31) | allelbalans 0.20, diepte 51, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030575 C>T (TAS2R31) | allelbalans 0.14, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030578 C>T (TAS2R31) | allelbalans 0.14, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030579 C>T (TAS2R31) | allelbalans 0.14, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030603 T>C (TAS2R31) | allelbalans 0.11, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030604 G>A (TAS2R31) | allelbalans 0.11, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030609 G>C (TAS2R31) | allelbalans 0.15, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030755 C>G (TAS2R31) | allelbalans 0.11, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11030885 C>G (TAS2R31) | allelbalans 0.24, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11030886 T>A (TAS2R31) | allelbalans 0.24, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11061467 T>C (TAS2R46) | allelbalans 0.18, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11061481 G>A (TAS2R46) | allelbalans 0.17, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11061483 T>C (TAS2R46) | allelbalans 0.18, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11061492 G>C (TAS2R46) | allelbalans 0.21, diepte 34, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11061502 C>G (TAS2R46) | allelbalans 0.22, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11061725 C>T (TAS2R46) | allelbalans 0.14, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11061727 G>C (TAS2R46) | allelbalans 0.14, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11061731 G>A (TAS2R46) | allelbalans 0.15, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11061752 G>C (TAS2R46) | allelbalans 0.20, diepte 35, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11061764 T>C (TAS2R46) | allelbalans 0.24, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11061769 T>C (TAS2R46) | allelbalans 0.23, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11133675 C>T (TAS2R30) | allelbalans 0.24, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11133677 G>C (TAS2R30) | allelbalans 0.23, diepte 35, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11133681 G>A (TAS2R30) | allelbalans 0.24, diepte 34, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11133683 G>A (TAS2R30) | allelbalans 0.24, diepte 34, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11133690 A>T (TAS2R30) | allelbalans 0.21, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:11133710 G>C (TAS2R30) | allelbalans 0.15, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11133715 A>G (TAS2R30) | allelbalans 0.15, diepte 27, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11133719 T>C (TAS2R30) | allelbalans 0.14, diepte 29, kwaliteit 90 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11134146 A>G (TAS2R30) | allelbalans 0.14, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11134147 A>G (TAS2R30) | allelbalans 0.14, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr12:11186063 T>C (TAS2R42) | allelbalans 0.72, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:50352038 T>A (FAM186A) | allelbalans 0.22, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:50352039 T>G (FAM186A) | allelbalans 0.22, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:50352044 C>G (FAM186A) | allelbalans 0.23, diepte 44, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr12:132776535 AGCGCCTCACACACAGGTACCCGCAGCAGCTGCTGTAGCCCCTCCAGCTCCTTCCTCCCTGCTGCTCCCG>A (GOLGA3) | allelbalans 0.27, diepte 30, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr13:63746826 C>CCTGTGGCTATGGCTCCAGCTATGG (ENSG00000237378) | allelbalans 0.30, diepte 27, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr13:113117611 CCCCTGTCCGACCGCGGTGCTGGGTGGGTGCCACTCTT>C (F7) | allelbalans 0.23, diepte 35, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr13:113404104 T>A (ADPRHL1) | allelbalans 0.17, diepte 18, kwaliteit 75 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr13:113404105 T>C (ADPRHL1) | allelbalans 0.17, diepte 18, kwaliteit 75 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr13:113404108 C>T (ADPRHL1) | allelbalans 0.12, diepte 17, kwaliteit 75 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:73263953 GGCCCCCCGACCTCCTCTGACAGGTGTGTGTGACA>G (PAPLN) | allelbalans 0.26, diepte 19, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:94379451 A>T (SERPINA1) | allelbalans 0.20, diepte 61, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379487 CCT>C (SERPINA1) | allelbalans 0.15, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379492 G>GAC (SERPINA1) | allelbalans 0.15, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379497 C>T (SERPINA1) | allelbalans 0.18, diepte 61, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379500 G>A (SERPINA1) | allelbalans 0.18, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379509 A>G (SERPINA1) | allelbalans 0.19, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379541 G>GA (SERPINA1) | allelbalans 0.18, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379543 TGAC>T (SERPINA1) | allelbalans 0.17, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379548 C>CTA (SERPINA1) | allelbalans 0.20, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:94379554 G>T (SERPINA1) | allelbalans 0.25, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:94379565 C>T (SERPINA1) | allelbalans 0.26, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:94379566 A>G (SERPINA1) | allelbalans 0.27, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:94379577 T>A (SERPINA1) | allelbalans 0.26, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:94379593 T>A (SERPINA1) | allelbalans 0.30, diepte 61, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:94379601 A>G (SERPINA1) | allelbalans 0.19, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379602 G>A (SERPINA1) | allelbalans 0.19, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379603 C>T (SERPINA1) | allelbalans 0.19, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379606 G>A (SERPINA1) | allelbalans 0.19, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:94379607 C>T (SERPINA1) | allelbalans 0.19, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:106012054 CTA>C (IGHV4-4) | allelbalans 0.21, diepte 14, kwaliteit 93 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:106012058 G>GGT (IGHV4-4) | allelbalans 0.21, diepte 14, kwaliteit 90 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:106012065 T>A (IGHV4-4) | allelbalans 0.15, diepte 13, kwaliteit 90 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:106012066 T>C (IGHV4-4) | allelbalans 0.15, diepte 13, kwaliteit 93 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:106012218 A>G (IGHV4-4) | allelbalans 0.20, diepte 20, kwaliteit 77 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:106116655 A>G (IGHV3-11) | allelbalans 0.27, diepte 15, kwaliteit 84 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:106116715 T>C (IGHV3-11) | allelbalans 0.25, diepte 12, kwaliteit 71 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr14:106268889 C>A (IGHV3-23) | allelbalans 0.82, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr14:106592950 T>A (IGHV3-53) | allelbalans 0.24, diepte 25, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr15:23129877 T>G (GOLGA6L1) | allelbalans 0.19, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr15:23129901 T>C (GOLGA6L1) | allelbalans 0.23, diepte 43, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr15:23440457 TC>T (GOLGA6L2) | allelbalans 0.26, diepte 27, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr15:23440459 TCTTCCTGCTCCCACATCTTCTCCTCCTGCTCCCGCATCTTC>T (GOLGA6L2) | allelbalans 0.24, diepte 29, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr15:30407965 C>CTTG (GOLGA8R) | allelbalans 0.19, diepte 75, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr15:82434465 C>T (GOLGA6L9) | allelbalans 0.22, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr16:30200833 A>G (SULT1A3) | allelbalans 0.87, diepte 15, kwaliteit 28 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:7846859 TACCACCACC>T,TACCACCACCACC (KDM6B) | allelbalans 1.00, diepte 26, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:21703044 C>A (KCNJ18) | allelbalans 0.20, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:21703050 G>A (KCNJ18) | allelbalans 0.19, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:21703080 C>T (KCNJ18) | allelbalans 0.25, diepte 51, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703083 C>T (KCNJ18) | allelbalans 0.25, diepte 51, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703101 C>T (KCNJ18) | allelbalans 0.25, diepte 51, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703113 C>T (KCNJ18) | allelbalans 0.26, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703139 A>G (KCNJ18) | allelbalans 0.22, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703340 C>T (KCNJ18) | allelbalans 0.16, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:21703362 G>C (KCNJ18) | allelbalans 0.84, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:21703383 C>T (KCNJ18) | allelbalans 0.25, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703501 G>A (KCNJ18) | allelbalans 0.24, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703524 G>A (KCNJ18) | allelbalans 0.21, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr17:21703539 C>T (KCNJ18) | allelbalans 0.15, diepte 39, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:21703782 CGAG>C (KCNJ18) | allelbalans 0.14, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:39175193 T>C (CACNB1) | allelbalans 0.19, diepte 26, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr17:41118174 T>A (KRTAP4-11) | allelbalans 0.17, diepte 46, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr18:47561 CATTGCTGTAAACTGCTCTGAG>C (TUBB8B) | allelbalans 0.17, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr18:47586 CAT>C (TUBB8B) | allelbalans 0.21, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr18:47809 G>A (TUBB8B) | allelbalans 0.14, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr18:11066140 T>G (PIEZO2) | allelbalans 0.29, diepte 38, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:1863292 C>T (KLF16) | allelbalans 0.30, diepte 10, kwaliteit 73 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:2015541 GGGC>G,GGGCGGC (BTBD2) | allelbalans 1.00, diepte 14, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:17286678 GTGTGTGTGTGTGTT>G (ANKLE1) | allelbalans 0.19, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:34352853 A>C (GARRE1) | allelbalans 0.17, diepte 23, kwaliteit 91 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:34352857 CAG>C (GARRE1) | allelbalans 0.17, diepte 24, kwaliteit 91 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:34684171 TAAAAAAAAAAAA>T (ZNF302) | allelbalans 0.62, diepte 12, kwaliteit 55 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:39885865 T>C (FCGBP) | allelbalans 0.14, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:45238745 A>G (EXOC3L2) | allelbalans 0.75, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54250956 G>T (LILRB5) | allelbalans 0.27, diepte 15, kwaliteit 93 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54251126 G>T (LILRB5) | allelbalans 0.25, diepte 32, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54251127 G>C (LILRB5) | allelbalans 0.24, diepte 33, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54278529 T>C (LILRB2) | allelbalans 0.14, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54278534 T>G (LILRB2) | allelbalans 0.14, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54278550 C>G (LILRB2) | allelbalans 0.14, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54278989 C>A (LILRB2) | allelbalans 0.13, diepte 52, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54279021 A>G (LILRB2) | allelbalans 0.18, diepte 44, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54279030 A>C (LILRB2) | allelbalans 0.20, diepte 44, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54279040 G>A (LILRB2) | allelbalans 0.23, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54279045 AG>A (LILRB2) | allelbalans 0.25, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54279050 T>TC (LILRB2) | allelbalans 0.26, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54336863 C>G (LILRA4) | allelbalans 0.12, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54574083 T>C (LILRA2) | allelbalans 0.19, diepte 63, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54574088 G>A (LILRA2) | allelbalans 0.19, diepte 62, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54574349 T>C (LILRA2) | allelbalans 0.22, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54574353 G>A (LILRA2) | allelbalans 0.20, diepte 49, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54574356 A>G (LILRA2) | allelbalans 0.20, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54574902 G>C (LILRA2) | allelbalans 0.27, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54574903 G>A (LILRA2) | allelbalans 0.24, diepte 70, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54574907 T>C (LILRA2) | allelbalans 0.25, diepte 68, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54574979 A>C (LILRA2) | allelbalans 0.22, diepte 85, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54574982 T>G (LILRA2) | allelbalans 0.21, diepte 85, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54575290 A>G (LILRA2) | allelbalans 0.14, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54575297 A>G (LILRA2) | allelbalans 0.13, diepte 61, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54575299 G>C (LILRA2) | allelbalans 0.13, diepte 63, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54575316 G>A (LILRA2) | allelbalans 0.14, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54575317 C>G (LILRA2) | allelbalans 0.14, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54575324 C>T (LILRA2) | allelbalans 0.14, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54575334 T>G (LILRA2) | allelbalans 0.15, diepte 54, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54575343 T>C (LILRA2) | allelbalans 0.15, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54576073 T>A (LILRA2) | allelbalans 0.26, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54576073 T>A (LILRA2) | allelbalans 0.26, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54576077 T>A (LILRA2) | allelbalans 0.28, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54576077 T>A (LILRA2) | allelbalans 0.28, diepte 47, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54594667 A>C (LILRA1) | allelbalans 0.14, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54594749 T>G (LILRA1) | allelbalans 0.14, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54594759 C>G (LILRA1) | allelbalans 0.12, diepte 51, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54595789 C>G (LILRA1) | allelbalans 0.21, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54595790 A>G (LILRA1) | allelbalans 0.21, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54595864 G>C (LILRA1) | allelbalans 0.27, diepte 86, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54630981 C>G (LILRB1) | allelbalans 0.19, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54630989 G>A (LILRB1) | allelbalans 0.20, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54630991 T>G (LILRB1) | allelbalans 0.20, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54630994 G>T (LILRB1) | allelbalans 0.20, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54631001 T>C (LILRB1) | allelbalans 0.20, diepte 61, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54631010 CT>C (LILRB1) | allelbalans 0.19, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54631016 A>G (LILRB1) | allelbalans 0.20, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54631055 G>T (LILRB1) | allelbalans 0.20, diepte 51, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54631975 C>T (LILRB1) | allelbalans 0.27, diepte 37, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54631983 A>C (LILRB1) | allelbalans 0.25, diepte 40, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632001 C>T (LILRB1) | allelbalans 0.79, diepte 42, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632003 C>A (LILRB1) | allelbalans 0.17, diepte 41, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54632040 T>G (LILRB1) | allelbalans 0.73, diepte 45, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632089 G>T (LILRB1) | allelbalans 0.24, diepte 63, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632090 C>T (LILRB1) | allelbalans 0.23, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632113 C>G (LILRB1) | allelbalans 0.22, diepte 65, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632143 G>A (LILRB1) | allelbalans 0.26, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632157 G>C (LILRB1) | allelbalans 0.22, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54632172 C>G (LILRB1) | allelbalans 0.19, diepte 59, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54632183 A>C (LILRB1) | allelbalans 0.16, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54632184 A>G (LILRB1) | allelbalans 0.16, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54632186 T>G (LILRB1) | allelbalans 0.15, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54632196 A>T (LILRB1) | allelbalans 0.13, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54633037 C>T (LILRB1) | allelbalans 0.08, diepte 48, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54633049 A>G (LILRB1) | allelbalans 0.19, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54633150 G>T (LILRB1) | allelbalans 0.26, diepte 53, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54633154 CAT>C (LILRB1) | allelbalans 0.25, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54633157 G>GCT (LILRB1) | allelbalans 0.25, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54633166 G>A (LILRB1) | allelbalans 0.24, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54633171 A>AAG (LILRB1) | allelbalans 0.24, diepte 55, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54633173 GTA>G (LILRB1) | allelbalans 0.23, diepte 56, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54633185 A>T (LILRB1) | allelbalans 0.22, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54633188 A>G (LILRB1) | allelbalans 0.22, diepte 50, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54667792 AG>A (LILRB4) | allelbalans 0.29, diepte 21, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr19:54726088 G>A (KIR3DL3) | allelbalans 0.14, diepte 58, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54726091 A>C (KIR3DL3) | allelbalans 0.12, diepte 57, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr19:54735264 A>C,T (KIR3DL3) | allelbalans 0.94, diepte 35, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr21:46334557 G>GTGGGATGTTCACAGTCAGTGACCACCCACCAGAACAGCA (PCNT) | allelbalans 0.24, diepte 29, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:22376226 T>A (IGLV5-45) | allelbalans 0.14, diepte 44, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:22376480 GTA>G (IGLV5-45) | allelbalans 0.23, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:22376484 G>GCC (IGLV5-45) | allelbalans 0.23, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:22904902 T>G (IGLJ3) | allelbalans 0.79, diepte 77, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:23998546 C>A (GSTT4) | allelbalans 0.21, diepte 62, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:23998547 T>A (GSTT4) | allelbalans 0.21, diepte 61, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:23998549 C>T (GSTT4) | allelbalans 0.21, diepte 62, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:23998550 T>A (GSTT4) | allelbalans 0.21, diepte 62, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:23998556 T>C (GSTT4) | allelbalans 0.18, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998558 A>C (GSTT4) | allelbalans 0.18, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998560 C>A (GSTT4) | allelbalans 0.18, diepte 60, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998567 G>C (GSTT4) | allelbalans 0.17, diepte 63, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998569 A>G (GSTT4) | allelbalans 0.16, diepte 63, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998571 TA>T (GSTT4) | allelbalans 0.16, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998574 TC>T (GSTT4) | allelbalans 0.16, diepte 64, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998579 T>TCG (GSTT4) | allelbalans 0.18, diepte 65, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chr22:23998589 A>G (GSTT4) | allelbalans 0.25, diepte 71, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:23998678 T>C (GSTT4) | allelbalans 0.28, diepte 74, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chr22:42130547 T>C (CYP2D6) | allelbalans 0.28, diepte 29, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chrX:2500656 C>A (DHRSX) | allelbalans 0.29, diepte 21, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `raw` |
| chrX:119470116 C>T (SLC25A5) | allelbalans 0.17, diepte 30, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |
| chrX:119470116 C>T (SLC25A5) | allelbalans 0.17, diepte 30, kwaliteit 99 | verwachting 0,50 bij heterozygoot; drempel GQ 90 | `artefact-prone` |

## `spectrum` (96)

De 96 trinucleotidecontexten met hun aandeel

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| A[C>T]G | 39553 voorvallen, 4.35% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>C]G | 37980 voorvallen, 4.18% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>C]A | 33100 voorvallen, 3.64% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>T]A | 32310 voorvallen, 3.55% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>T]G | 28445 voorvallen, 3.13% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>C]G | 26186 voorvallen, 2.88% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>C]T | 25808 voorvallen, 2.84% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>T]T | 24557 voorvallen, 2.70% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>T]G | 23312 voorvallen, 2.56% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>C]G | 21013 voorvallen, 2.31% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>T]G | 19621 voorvallen, 2.16% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>C]T | 17857 voorvallen, 1.96% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>C]G | 17723 voorvallen, 1.95% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>T]T | 17486 voorvallen, 1.92% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>T]T | 17219 voorvallen, 1.89% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>C]T | 16357 voorvallen, 1.80% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>T]A | 14562 voorvallen, 1.60% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>T]T | 14537 voorvallen, 1.60% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>T]A | 14448 voorvallen, 1.59% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>C]A | 14343 voorvallen, 1.58% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>T]C | 14090 voorvallen, 1.55% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>C]T | 13748 voorvallen, 1.51% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>C]A | 13359 voorvallen, 1.47% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>T]C | 13287 voorvallen, 1.46% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>T]A | 13151 voorvallen, 1.45% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>C]C | 12959 voorvallen, 1.43% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>T]C | 12632 voorvallen, 1.39% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>C]A | 12309 voorvallen, 1.35% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>C]C | 12250 voorvallen, 1.35% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>C]C | 11600 voorvallen, 1.28% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>T]C | 11204 voorvallen, 1.23% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>G]T | 10504 voorvallen, 1.16% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>A]A | 10240 voorvallen, 1.13% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>G]T | 10141 voorvallen, 1.12% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>C]C | 10141 voorvallen, 1.12% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>G]A | 9695 voorvallen, 1.07% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>G]T | 7519 voorvallen, 0.83% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>A]A | 7160 voorvallen, 0.79% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>A]T | 6982 voorvallen, 0.77% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>A]T | 6938 voorvallen, 0.76% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>A]C | 6900 voorvallen, 0.76% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>A]A | 6696 voorvallen, 0.74% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>G]A | 6473 voorvallen, 0.71% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>G]A | 6367 voorvallen, 0.70% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>A]T | 6303 voorvallen, 0.69% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>G]T | 6071 voorvallen, 0.67% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>A]A | 5919 voorvallen, 0.65% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>G]G | 5808 voorvallen, 0.64% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>A]A | 5595 voorvallen, 0.62% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>A]A | 5270 voorvallen, 0.58% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>G]G | 5202 voorvallen, 0.57% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>A]T | 5185 voorvallen, 0.57% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>G]T | 5180 voorvallen, 0.57% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>G]A | 5117 voorvallen, 0.56% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>G]C | 5097 voorvallen, 0.56% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>A]T | 5061 voorvallen, 0.56% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>A]G | 4989 voorvallen, 0.55% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>A]C | 4820 voorvallen, 0.53% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>G]C | 4735 voorvallen, 0.52% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>G]G | 4710 voorvallen, 0.52% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>G]T | 4591 voorvallen, 0.50% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>A]C | 4542 voorvallen, 0.50% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>A]T | 4524 voorvallen, 0.50% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>G]T | 4452 voorvallen, 0.49% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>G]C | 4416 voorvallen, 0.49% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>G]A | 4398 voorvallen, 0.48% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>A]T | 4130 voorvallen, 0.45% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>G]G | 3979 voorvallen, 0.44% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>G]C | 3948 voorvallen, 0.43% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>A]C | 3931 voorvallen, 0.43% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>A]C | 3903 voorvallen, 0.43% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>G]C | 3785 voorvallen, 0.42% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>G]G | 3676 voorvallen, 0.40% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>G]T | 3658 voorvallen, 0.40% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>A]G | 3616 voorvallen, 0.40% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[C>A]G | 3489 voorvallen, 0.38% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>G]A | 3409 voorvallen, 0.37% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>G]C | 3404 voorvallen, 0.37% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>G]A | 3358 voorvallen, 0.37% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>A]T | 3353 voorvallen, 0.37% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>A]G | 3249 voorvallen, 0.36% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>G]G | 3189 voorvallen, 0.35% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>A]G | 3146 voorvallen, 0.35% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| A[T>G]C | 3049 voorvallen, 0.34% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>G]C | 3024 voorvallen, 0.33% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[C>A]G | 3020 voorvallen, 0.33% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>A]C | 2980 voorvallen, 0.33% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>G]G | 2938 voorvallen, 0.32% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>A]C | 2574 voorvallen, 0.28% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>A]G | 2507 voorvallen, 0.28% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[T>A]C | 2473 voorvallen, 0.27% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>A]A | 2419 voorvallen, 0.27% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| G[T>A]A | 2304 voorvallen, 0.25% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[C>G]G | 2063 voorvallen, 0.23% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| C[T>G]A | 2024 voorvallen, 0.22% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |
| T[C>A]G | 1923 voorvallen, 0.21% van alle SNVs | kiembaanverwachting: transities overheersen, C>T op CpG hoogst | `raw` |

## `mitochondrial` (13)

chrM-varianten met hun heteroplasmiefractie

| Plaats | Meting | Waartegen afgezet | Status |
|---|---|---|---|
| chrM:263 A>G | fractie 1.000 bij diepte 2110 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:302 A>AC,ACC | fractie 0.988 bij diepte 1671 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:310 T>TC | fractie 0.999 bij diepte 1827 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:750 A>G | fractie 1.000 bij diepte 4321 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:1438 A>G | fractie 1.000 bij diepte 5212 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:4769 A>G | fractie 1.000 bij diepte 4177 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:8860 A>G | fractie 1.000 bij diepte 4026 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:13830 T>C | fractie 1.000 bij diepte 3689 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:14470 T>A | fractie 1.000 bij diepte 4939 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:15326 A>G | fractie 1.000 bij diepte 4572 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:16093 T>C | fractie 0.979 bij diepte 4219 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:16221 C>T | fractie 0.998 bij diepte 4546 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |
| chrM:16519 T>C | fractie 1.000 bij diepte 3401 | homoplasmie = 1,0; alles daaronder is heteroplasmie | `raw` |

## Wat deze opsomming niet kan zien

- Structurele varianten kleiner dan de vensterresolutie van 100 kb, en gebalanceerde herschikkingen in elke omvang.
- Alles waarvoor ouderdata nodig is, waaronder de fase van variantparen die verder dan een leesfragment uit elkaar liggen.
- Mozaieke gebeurtenissen onder de grens die per chromosoom in `chromosome-dosage` staat, en bij variegated aneuploidie ligt de per-chromosoomfractie daar structureel onder.
- Alles wat betekenis pas krijgt via het fenotype, want dat document is hier per regel uitgesloten.
- Insert-size-afwijkingen, omdat die klasse niet is gedraaid.
