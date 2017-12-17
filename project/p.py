#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
import os
import re
cod = os.popen("dir dir /od  D:\\驱动人生\\DTLSoft\\DriveTheLife").read()
print(cod)
# ipv4 = "IPv4.* (.*)"
# getip = re.compile(ipv4)
# ip = getip.findall(cod)
# print(ip[0])

