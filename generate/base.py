#!/usr/bin/env python

import sys
import urllib


def genUrls(url, start, end):
    x = start; y = end
    list = []
    while x < y:
        list.append(url + str(x))
        x += 1
    return list

print genUrls('http://www.bilibili.com/video/av', 1, 100)
