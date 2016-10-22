set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

for p in $( find data1/ -maxdepth 1 -type d ! -path data1/ )
do
  echo -n "processing ${p}: "

  aria2c -j16 --continue -l "aria-log1.txt" -i ${p}/dl.txt

done;
