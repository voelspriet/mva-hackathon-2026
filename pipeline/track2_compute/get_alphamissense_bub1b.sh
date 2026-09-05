#!/usr/bin/env bash
# Stream the public AlphaMissense hg38 bulk TSV and keep only the BUB1B locus (chr15:40160984-40221137).
# The whole gene span is requested, so no patient-specific coordinate is disclosed; the file is static
# public hosting and nothing is uploaded. Output: work/track2/alphamissense_BUB1B.tsv
set -euo pipefail
OUT=${1:-work/track2/alphamissense_BUB1B.tsv}
URL=https://storage.googleapis.com/dm_alphamissense/AlphaMissense_hg38.tsv.gz
curl -sSL "$URL" | gzip -dc | awk -F'\t' -v OFS='\t' '
  /^#/ {next}
  $1=="chr15" && $2>=40160984 && $2<=40221137 {print; found=1; next}
  found && $1=="chr15" && $2>40221137 {exit}
' > "$OUT"
wc -l < "$OUT"
