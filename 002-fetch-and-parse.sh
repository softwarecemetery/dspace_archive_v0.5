set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

for f in $( ls data/browse-*.json )
do
  scripts/create-dirs.py "${f}"
done;
