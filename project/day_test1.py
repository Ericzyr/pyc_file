#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
user = 'c'
password = '123'
print('用户只能输入3次')
for i in range(10):
    if i >= 1:
        user_name = input('请输入用户名：')
        user_password = input('输入你的密码：')
        if user == user_name:
            if password == user_password:
                print("输入用户和密码正确：ok")
                break
        else:
            print('你输入的误：error')
        print('你输入了', i, '次')