set -euo pipefail

DSPACE_URL="10.1.32.112"

mkdir -p tmp

wget "http://${DSPACE_URL}/jspui/community-list" -O tmp/community-list

scripts/communities-and-collections.py tmp/community-list
