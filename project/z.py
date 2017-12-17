#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
import os
import re
import sys
os.system("date")

t1 = re.compile(":(.*)").findall(time)
print(t1)


