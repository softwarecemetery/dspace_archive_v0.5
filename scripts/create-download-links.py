#! /usr/bin/env python3

import sys
import os

from bs4 import BeautifulSoup

if len(sys.argv) < 2:
  print("missing file url")
  quit()


import json
import io

def create_dirs(fname):

  with io.open(fname, 'r', encoding='utf8') as f:
    data = json.load(f)

  for handle in data.keys():
    sh = str(int(handle) // 1000).zfill(2)

    href = './data/' + sh + '/' + handle

    fhref = os.path.abspath(href)

    print ('http://10.1.32.112/jspui/handle/123456789/' + handle + "/?mode=full\n" + "  " + 'dir=' + fhref + "\n  out=" + handle)

create_dirs(sys.argv[1])
