#!/bin/bash
# Queries the whois ripe API looking for the terms given in an input file
# The file can only contain some special characters 
# 'TEST BEFORE ADDING NEW ONES'

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <input_file>" 
  exit 1
fi

input=$1

while read line; do

  curl "http://rest.db.ripe.net/search.json?source=ripe&sourc=apnic-grs&source=afrinic-grs&source=arin-grs&source=jpirr-grs&source=lacnic-grs&source=radb-grs&source=ripe-grs&type-filter=inetnum&query-string=$line" 2>/dev/null | grep inetnum -A 1 | grep value | cut -d'"' -f4 >> tmp_file

done <$input

cat tmp_file | sort | uniq > api_inetnums
rm tmp_file
