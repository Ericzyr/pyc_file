#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
import os
name = 'Eric'
age = 16
job = 'IT'
msg = '''
Information of belwoe person %s:
name:%s
age:%s
jop:%s
''' % (name, name, age, job)
print(msg)
print(os.popen("ipconfig").read())