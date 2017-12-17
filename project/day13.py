#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
import os
import sys
for i in range(3):
    try:
        name = int(input("输入一个数字："))
        print("打印处理的是：", name, "米")
    except:
        print("你输入的有误系统自动退出了")
        t = os.system("ipconfig")
        sys.exit()
