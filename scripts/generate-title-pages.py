#! /usr/bin/env python3

import sys

from bs4 import BeautifulSoup

if len(sys.argv) < 2:
  print("missing dspace param")
  quit()


def fetchtitles(n, href):


  n = int(n) // 1000 + 1
  for _ in range(0, n):
    print ("%s?type=title&sort_by=2&order=ASC&rpp=1000&offset=%d %s" % (href, (_ * 1000), 'browse-' + str(_ * 1000).zfill(5)   ))

fetchtitles(sys.argv[1], sys.argv[2])
