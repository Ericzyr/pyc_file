#!/usr/bin/env/python
# _*_coding:utf-8_*_

from splinter.browser import Browser

def f1():
    browser = Browser()
    url = 'https://train.qunar.com/'
    browser.visit(url)
    # browser.fill('password', 'zyrarter')
    # browser.fill('mainPassword', 'zyrarter')
    #
    # browser.find_by_name('stsSearch').click()
    # browser.find_by_id('dologin').click()

if __name__ == '__main__':
    f1()