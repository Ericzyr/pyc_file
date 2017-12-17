#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author
import os
# if not (os.path.exists(r"F:\download\20171029")):
#     os.makedirs(r"F:\download\20171029")
code="sh201003"
# print(code[0:2])
# print(code[2:])

inshorsz = 10
if code[0:2] == "sh":
    inshorsz = 0
else:
    inshorsz = 1
if inshorsz != 10:
    t="adf"+str(inshorsz)+code[2:]+"asdfadf"
    print(t)
# http://quotes.money.163.com/service/chddata.html?code=1300133&end=20170523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP
# http://quotes.money.163.com/service/chddata.html?code=1300133&end=20170523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP