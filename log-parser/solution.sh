#!/bin/bash
set -e

BASE_DIR="$(pwd)"  # Current working directory
LOG_FILE="${BASE_DIR}/data/server.log"
OUTPUT_DIR="${BASE_DIR}/reports"
OUTPUT_FILE="${OUTPUT_DIR}/error_summary.csv"

mkdir -p "$OUTPUT_DIR"

# Write header first
echo "ip_address,error_count" > "$OUTPUT_FILE"

grep "ERROR" "$LOG_FILE" | \
    awk '{print $NF}' | \
    sort | \
    uniq -c | \
    awk '{print $2 "," $1}' | \
    sort --field-separator=',' --key=2,2nr --key=1,1 >> "$OUTPUT_FILE"

echo "Log analysis complete. Report generated at ${OUTPUT_FILE}"
