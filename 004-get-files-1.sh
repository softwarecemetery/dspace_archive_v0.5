set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

for p in $( find data1/ -maxdepth 1 -type d ! -path data1/ )
do
  echo -n "processing ${p}: "

  # aria2c -j16 --continue -l "log-full.txt" -i ${p}/dl.txt

  NPROC=0
  for f in $( find ${p}/ -maxdepth 1 -type d ! -path ${p}/ )
  do
    NPROC=$(($NPROC+1))
    handle=$( echo ${f} | cut -d'/' -f3 )
    # echo "  processing ${handle}"
    echo -n "${handle}, "
    scripts/write-dl.py ./${f} ${handle} >> ${p}/dl.txt
  done;
  echo ""
  echo "${NPROC} files processed!"
done;

