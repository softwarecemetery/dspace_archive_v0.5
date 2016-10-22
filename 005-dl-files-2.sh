set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

for p in $( find data2/ -maxdepth 1 -type d ! -path data2/ )
do
  echo -n "processing ${p}: "

  aria2c -j16 --continue -l "aria-log2.txt" -i ${p}/dl.txt

done;
