#! /usr/bin/env python3

import sys
import os

from bs4 import BeautifulSoup

if len(sys.argv) < 2:
  print("missing file url")
  quit()


import json
import io

def handlefetch(handle, bs):

  table = bs.find('table', {'class' : 'itemDisplayTable'});
  meta_s = table.find_all('tr')
  data = {}

  for meta in meta_s[1:]:
    label = meta.find('td', {'class' : 'metadataFieldLabel'}).text
    value = meta.find('td', {'class' : 'metadataFieldValue'}).text

    if label in data:
      if (type(data[label]) != 'list'):
        data[label] = [data[label]]
      data[label].append(value)
    else:
      data[label] = value

    try:
      if label == "Appears in Collections:":
        a = meta.find('a')
        data["Appears in Collections:"] = a['href'].split('/')[-1]
    except:
      pass

  urlhref = []
  files = []
  for td in bs.find_all('td', {'class' : 'standard', 'headers' : 't1'}):
    if (td.find('a') is not None):
      text = td.find('a').text
      url = td.find('a').get('href')
      if url in urlhref:
        continue
      urlhref.append(url)
      files.append(text)

  data['href'] = urlhref
  data['files'] = files

  return data

with open(sys.argv[1] + '/' + sys.argv[2]) as f:
  bs = BeautifulSoup(f, "html.parser")

  data = handlefetch(sys.argv[2], bs)

  abspath = os.path.abspath(sys.argv[1])
  for href in data['href']:
    print("http://10.1.32.112" +href)
    print("  dir=" + abspath)
    print("  out=/" + href.split('/' + sys.argv[2] + '/')[1])
    print

  jpath = sys.argv[1] + '/info.json'
  with io.open(jpath, 'w', encoding='utf8') as f:
    d_string = json.dumps(data, ensure_ascii=False, indent=2)
    f.write(d_string)


  # titles = parsetitles(bs)

  # write_dl(sys.argv[1])
