#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
'''age = 9
name_list = ['Eric', 'Town', 'wqt', 22, age]
print(name_list)
print(name_list.index(22))
'''
ad_dict = {
    1239098809: dict(name='jack', age=22, job='IT'),
    123902349: dict(mane="jacon", age=32, job="Rasdfr"),
}
# print(ad_dict[1239098809]['name'])
ad_dict[1239098809]['person'] = 'green' #在字典里插入数据
print(ad_dict)
print(type(ad_dict))

