#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author
import urllib
import urllib.request
import re
def getpage(web):
    data = urllib.request.urlopen(web).read().decode("gbk")
    return data

web = "http://quote.eastmoney.com/stocklist.html"
date = getpage(web)
print(date)
print("afdasfas")



# <li><a target="_blank" href="http://quote.eastmoney.com/sh500016.html">基金裕元(500016)</a></li>