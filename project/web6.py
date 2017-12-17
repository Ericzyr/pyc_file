#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author


import os
import urllib
import urllib.request
import re


def getweballcode(web):
    webcode = urllib.request.urlopen(web).read().decode("utf-8")
    return webcode


def getwebselfcode(pcode):
    r = re.compile(pcode).findall(allgetcode)
    return r


web = "http://www.oneplusbbs.com/thread-573719-1-1.html"
allgetcode=getweballcode(web)

pcode = "<img id=\".*\" aid=\".*\" src=.*zoomfile=\".*\" file=\"(.*)\" class=\"zoom\" onclick=\"zoom.*"
getself = getwebselfcode(pcode)


for url in range(len(getself)):
    print(url)
    # path = "F:\\download1\\a.jpg"
    # urllib.request.urlretrieve(url, path)

