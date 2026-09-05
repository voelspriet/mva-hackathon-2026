#!/usr/bin/env bash
# Stream AlphaMissense's protein-level substitution table and keep UniProt O60566 (BubR1) only.
# Protein-level public lookup; no patient coordinates involved.
set -uo pipefail
OUT=${1:-work/track2/alphamissense_O60566_aa.tsv}
curl -sSL "https://storage.googleapis.com/dm_alphamissense/AlphaMissense_aa_substitutions.tsv.gz" \
 | gzip -dc | awk -F'\t' '$1=="O60566"{print; f=1; next} f && $1!="O60566"{exit}' > "$OUT"
wc -l < "$OUT"
