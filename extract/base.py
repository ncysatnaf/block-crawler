#!/usr/bin/env python

import re
import sys
import urllib2
from BeautifulSoup import BeautifulSoup

def getLinks(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        print link.get('href')


def main():
    for url in sys.argv[1:]:
        getLinks(url)


if __name__ == "__main__":
    main()
