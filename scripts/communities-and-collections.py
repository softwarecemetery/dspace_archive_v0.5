#! /usr/bin/env python3

import sys

from bs4 import BeautifulSoup

if len(sys.argv) < 2:
  print("filename missing!")
  quit()


import json
import io


def recurse_lookahead(bs):
  t = bs.find_all('li');

  if t[0]['class'][0] == "communityLink":
    return 1
  return 0

def recurse_communities(book, dictionary, bs, depth):

  # get all li
  t = bs.find_all('li', recursive=False)

  # er?
  assert len(t) != 0

  # community
  community = False # "collectionListItem"
  if t[0]['class'][0] == "communityLink":
    community = True

  for it in t:
    if community: # communityLink
      c = it.find('strong', recursive=False).find('a')
      # c_name = c.contents[0]
      c_name = c['href'].split('/')[-1]

      # indent print community name
      # print( (' ' * (2 * depth)) + c_name)
      # print( (' ' * (2 * depth)) + c['href'].split('/')[-1] )

      c_bs   = it.find('ul', recursive=False)

      if c_bs != None:
        book[c['href'].split('/')[-1]] = c.contents[0]

        if recurse_lookahead(it):
          dictionary[c_name] = {}
        else:
          dictionary[c_name] = []

        recurse_communities(book, dictionary[c_name], c_bs, depth+1)
    else: # collectionListItem
      c = it.find('a')

      # indent print community name
      # print( (' ' * (2 * depth)) + c.contents[0])
      # print( (' ' * (2 * depth)) + c['href'].split('/')[-1])

      book[c['href'].split('/')[-1]] = c.contents[0]

      dictionary.append(c['href'].split('/')[-1])

def parsecommunities(bs):

  b = {}
  d = {}

  # first li communityLink tag.
  t = bs.find('li', attrs={"class":"communityLink"})
  # find it's parent
  p = t.parent

  recurse_communities(b, d, p, 0);

  # print(b)

  # print(json.dumps(d, indent=2, ensure_ascii=False))

  return b, d


with open(sys.argv[1]) as f:
  bs = BeautifulSoup(f, "html.parser")

  communities, hierarchy = parsecommunities(bs);

  # todo: fixup utf-8 encoding for non-ascii characters encoding
  cfpath = 'data/communities.json';
  with io.open(cfpath, 'w', encoding='utf8') as f:
    data = json.dumps(communities, ensure_ascii=False)
    f.write(data)

  hfpath = 'data/hierarchy.json';
  with io.open(hfpath, 'w', encoding='utf8') as f:
    data = json.dumps(hierarchy, ensure_ascii=False)
    f.write(data)

  quit()
