set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

for f in $( ls data/browse-*.json )
do
  x=$( echo ${f} | cut -d'-' -f2 | sed s/json/list/g )
  # scripts/create-download-links.py "${f}" > data/aria-${x}
  aria2c -j16 --continue -l "log-full.txt" -i data/aria-${x}
  # scripts/create-download-links.py data/browse-00000.json
done;
