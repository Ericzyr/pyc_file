#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
# li = [11, 22, 88, 11
# list(（11， 23， 11）) list_init_,内部执行for循环（11， 23， 11）[11， 23， 11]
# print(li)
# list = ["12", "23"] 创建一个列表
# tuple = (23, 12, 90, 23, [23, "国家", 40]) 创建一个元组
# dic ={"ki":124} 创建了一个字典
# set ={"123", "423"} 创建了一个集合
# print(type(se)) 如何知道是什么类型可以用这个方法
# dic = {"ki": 124, "name": "郑园"}
# se = {123, "你是", 230, 123}
# print(type(se))
# print(se)
# li = [23, 23, 30, 290, 90]
# # t = list(("hello", 12))
# s1 = set(li)
# print(s1)
s = set()
s.add("hello")
s.add("world")
print(s)

name = "java"
for i in range(10):
    if i >= 3:
        input_name = input("input you name:")
        if input_name == name:
            print('你输入的ok')
            break
        else:
            print('error')
            print(i)