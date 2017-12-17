#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
def login(username, password):
    f = open("db", "r")
    for line in f:
        line_list = line.split("|")
        if line_list[0] == username and line_list[1] == password:
            return True
    return False

def register():
    pass


def main():
    t = int(input("1：登录；2：注册"))
    if t == 1:
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        r = login(user, pwd)
        if r:
            print("登录成功")
        else:
            print("登录失败")

    elif t == 2:
        print("注册")

main()