#!/usr/bin/env bash
# MVA Hackathon 2026, Track 1 pipeline. VCF in, ranked CSV + evidence out. No patient data leaves the machine
# except HTTP range reads of public gnomAD sites files (static hosting, no query is sent).
# Usage: pipeline/run.sh data/<sample>.vcf.gz work/
set -euo pipefail
VCF=$(cd "$(dirname "$1")" && pwd)/$(basename "$1"); W=$2; P=$(cd "$(dirname "$0")" && pwd); mkdir -p "$W/ref"; cd "$W"
T0=$(date +%s); step(){ echo "[$(( $(date +%s)-T0 ))s] $*"; }
step "tool versions"; bcftools --version | head -1; python3 --version
ENS=116
step "references (skipped if present)"
[ -f ref/Homo_sapiens.GRCh38.$ENS.chr.gff3.gz ] || curl -sS -o ref/Homo_sapiens.GRCh38.$ENS.chr.gff3.gz https://ftp.ensembl.org/pub/release-$ENS/gff3/homo_sapiens/Homo_sapiens.GRCh38.$ENS.chr.gff3.gz
for c in 5 11 15; do [ -f ref/Homo_sapiens.GRCh38.dna.chromosome.$c.fa.gz ] || curl -sS -o ref/Homo_sapiens.GRCh38.dna.chromosome.$c.fa.gz https://ftp.ensembl.org/pub/release-$ENS/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.$c.fa.gz; done
[ -f ref/ref_5_11_15.fa.gz.fai ] || { (for c in 5 11 15; do gzip -dc ref/Homo_sapiens.GRCh38.dna.chromosome.$c.fa.gz; done) | bgzip > ref/ref_5_11_15.fa.gz; python3 -c "import pysam;pysam.faidx('ref/ref_5_11_15.fa.gz')"; }
[ -f ref/clinvar.vcf.gz ] || { curl -sS -o ref/clinvar.vcf.gz https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz; curl -sS -o ref/clinvar.vcf.gz.tbi https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz.tbi; }
step "1. VCF header facts"; bcftools view -h "$VCF" | grep -E "^##reference|^##source" | cut -c1-160; bcftools query -l "$VCF"
step "2. known MVA genes (BUB1B, CEP57, TRIP13): PASS variants, consequences, ClinVar"
printf '5\t892849\t919357\n11\t95789965\t95837070\n15\t40160984\t40221137\n' > core_regions.txt
bcftools view -R core_regions.txt -i 'FILTER="PASS"' -Oz -o core.vcf.gz "$VCF"; bcftools index -tf core.vcf.gz
bcftools csq --force -f ref/ref_5_11_15.fa.gz -g ref/Homo_sapiens.GRCh38.$ENS.chr.gff3.gz -p a -l core.vcf.gz -Oz -o core.csq.vcf.gz 2>/dev/null; bcftools index -tf core.csq.vcf.gz
bcftools annotate -a ref/clinvar.vcf.gz -c INFO/CLNSIG,INFO/CLNDN,INFO/CLNREVSTAT core.csq.vcf.gz -Oz -o core.annot.vcf.gz; bcftools index -tf core.annot.vcf.gz
bcftools query -i 'INFO/BCSQ~"missense" || INFO/BCSQ~"stop" || INFO/BCSQ~"frameshift" || INFO/BCSQ~"splice" || INFO/CLNSIG~"athogenic"' \
  -f '%CHROM\t%POS\t%REF\t%ALT\t[%GT]\t[%AD]\t%INFO/CLNSIG\t%INFO/BCSQ\n' core.annot.vcf.gz | cut -c1-200 | tee coding_candidates.tsv
step "3. gnomAD v4.1 frequencies for coding candidates (HTTP range reads)"
awk -F'\t' '{print "chr"$1":"$2"-"$2}' coding_candidates.tsv | paste -sd, - > gnomad_regions.txt
for t in exomes genomes; do bcftools query -r "$(cat gnomad_regions.txt)" -f "$t\t%CHROM\t%POS\t%REF\t%ALT\tAC=%INFO/AC\tAN=%INFO/AN\tnhomalt=%INFO/nhomalt\n" \
  "https://storage.googleapis.com/gcp-public-data--gnomad/release/4.1/vcf/$t/gnomad.$t.v4.1.sites.chr15.vcf.bgz" 2>/dev/null; done | tee gnomad_candidates.tsv
step "4. genome-wide recessive-compatible scan (PASS, CDS, not dbSNP, GQ>=50, DP>=10)"
[ -f cds_all.sorted.bed.gz ] || python3 "$P/make_cds_bed.py" ref/Homo_sapiens.GRCh38.$ENS.chr.gff3.gz cds_all.sorted.bed.gz
bcftools view -R cds_all.sorted.bed.gz -i 'FILTER="PASS" && INFO/DB=0' "$VCF" -Ou 2>/dev/null | bcftools sort -Oz -o coding_nodbsnp.vcf.gz 2>/dev/null; bcftools index -tf coding_nodbsnp.vcf.gz
printf '##INFO=<ID=GENE,Number=1,Type=String,Description="gene">\n' > gene.hdr
bcftools annotate -a cds_all.sorted.bed.gz -c CHROM,FROM,TO,GENE -h gene.hdr coding_nodbsnp.vcf.gz -Oz -o coding_nodbsnp.gene.vcf.gz 2>/dev/null
bcftools query -i 'GQ>=50 && FMT/DP>=10' -f '%INFO/GENE\t[%GT]\t%CHROM:%POS:%REF:%ALT\n' coding_nodbsnp.gene.vcf.gz | python3 "$P/recessive_scan.py" > recessive_compatible_genes.txt
head -3 recessive_compatible_genes.txt; echo "  ... $(wc -l < recessive_compatible_genes.txt) genes; BUB1B line: $(grep -c '^BUB1B' recessive_compatible_genes.txt)"
step "5. mosaic aneuploidy profile"
bcftools query -i 'FILTER="PASS" && TYPE="snp"' -f '%CHROM\t%POS\t[%GT\t%AD\t%DP]\n' "$VCF" | python3 "$P/mosaic_baf.py" mosaic > mosaic_raw.txt
bcftools query -i 'FILTER="PASS" && TYPE="snp"' -f '%CHROM\t%POS\t[%GT\t%AD\t%DP]\n' "$VCF" | python3 "$P/mosaic_robust.py" | tee mosaic_robust.txt | tail -2
python3 "$P/plot_mosaic.py" mosaic_robust.json mosaic.hist.json mosaic_profile.png
step "6. ACMG SF v3.2 secondary-findings screen"
python3 "$P/acmg_bed.py" ref/Homo_sapiens.GRCh38.$ENS.chr.gff3.gz "$P/acmg_sf32_genes.txt" acmg.bed
bcftools view -R acmg.bed -i 'FILTER="PASS"' "$VCF" -Ou 2>/dev/null | bcftools sort -Oz -o acmg.vcf.gz 2>/dev/null; bcftools index -tf acmg.vcf.gz
bcftools annotate -a ref/clinvar.vcf.gz -c INFO/CLNSIG,INFO/CLNDN,INFO/CLNREVSTAT,INFO/GENEINFO acmg.vcf.gz -Oz -o acmg.clinvar.vcf.gz; bcftools index -tf acmg.clinvar.vcf.gz
bcftools query -i 'INFO/CLNSIG~"athogenic"' -f '%CHROM:%POS\t%REF>%ALT\t[%GT]\t%INFO/GENEINFO\t%INFO/CLNSIG\n' acmg.clinvar.vcf.gz | tee acmg_hits.tsv | awk -F'\t' '{c[$5]++} END{for(k in c) print "   "c[k], k}'
step "7. submission CSV"
python3 "$P/make_csv.py" coding_candidates.tsv gnomad_candidates.tsv track1_submission.csv
python3 "$P/../scoring/score_local.py" track1_submission.csv
step "done"
