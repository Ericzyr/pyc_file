#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric

# 三元运算，三目运算 ，是对用于简单的if....else...
i = input("输入一个数字")
if i == 1:
    name = "Eric"
else:
    name = "ales"
print(name)

# name = "Eric" if i == 1 else "alex"
# print(name)

def f1(a):
    return a + 100


f2 = lambda a1: a1+100 #lambda 运算，是对用于简单的函数运算
ret1 = f1(9)
ret2 = f2(12)
print(ret1)
print(ret2)

