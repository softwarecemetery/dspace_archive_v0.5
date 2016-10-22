set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

for p in $( find data3/ -maxdepth 1 -type d ! -path data3/ )
do
  echo -n "processing ${p}: "

  aria2c -j16 --continue -l "aria-log3.txt" -i ${p}/dl.txt

done;
