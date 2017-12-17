#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
# 打开文件
# 操作文件
# 关闭文件 f.close
# with open() as f:

# 只读 read
# f = open("db""r")
# 只写 write 先清空原文件
# f = open("db""w")
# 文件存在，报错；不存在，创建并写内容
# f = open("db""x")
# 追加
# f = open("db""a")
# tell()获取当前指针位置
#
f = open('db', 'r+', encoding='utf-8')
date = f.read()
print(date)
print(f.tell())
f.seek(f.tell())
f.write("888")

f.close()
