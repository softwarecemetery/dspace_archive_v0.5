#! /usr/bin/env python3

import sys
import os

from bs4 import BeautifulSoup

if len(sys.argv) < 2:
  print("missing file url")
  quit()


import json
import io


def parsetitles(bs):
  titles = {}

  for table in bs.find_all('table', {'class' : 'miscTable'}):
    data = table.find_all('tr')

    for record in data[1:]: # first table is th
      a = record.find('td', attrs={"headers":"t2"}).find('a')
      titles[a['href'].split('/')[-1]] = a.contents[0]

  return titles

with open(sys.argv[1]) as f:
  bs = BeautifulSoup(f, "html.parser")

  titles = parsetitles(bs)

  hfpath = 'data/' + os.path.basename(sys.argv[1]) + '.json';
  print(hfpath)
  with io.open(hfpath, 'w', encoding='utf8') as f:
    data = json.dumps(titles, ensure_ascii=False)
    f.write(data)
