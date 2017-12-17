#!/usr/bin/env/python
# _*_ coding:utf-8 _*_
# Author:Eric
def outer(func):
    def inner():
        #print('before')
        func()
        #print('after')
    return inner

@outer
def f1():
    print("F1")
s = f1()
print(s)
