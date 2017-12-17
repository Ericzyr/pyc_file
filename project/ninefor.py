#!/usr/bin/env/python
#_*_coding:utf-8_*_
# Author
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(j, "*", i, "=", i*j, end="")
        else:
            break
    print("\t")



