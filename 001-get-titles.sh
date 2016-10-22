set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

wget --quiet "http://${DSPACE_URL}/jspui/browse" -O tmp/dspace-browse

x=$(cat tmp/dspace-browse  | grep -i "Showing results" | cut -d' ' -f7 | head -n1)

scripts/generate-title-pages.py "${x}" "http://${DSPACE_URL}/jspui/browse" > tmp/titles.list

mkdir -p tmp/browse/

err=0
while read -r url filename tail; do
  wget -O "tmp/browse/${filename}" "$url" || err=1
  scripts/parse-titles.py "tmp/browse/${filename}"
done <tmp/titles.list
