#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric

def f1(xxoo):
    print(xxoo)
    return "ok"
while True:
    name = input("输入你的名字：")
    result = f1(name)
    if result == "ok":
         print("very good")
    else:
        print('error')