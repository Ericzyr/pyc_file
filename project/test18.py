#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric

name = "java"

for i in range(4):
    if i >= 1:
        input_name = input("input you name:")
        if input_name == name:
            print('你输入的ok')
            break
        else:
            print('error')
            print("输入", i, "次")




