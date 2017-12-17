#!/usr/bin/env/python
# _*_coding:utf-8_*_
# Author:Eric
from splinter.browser import Browser
import time

def main():
    browser = Browser()
    browser.visit('http://baidu.com')
    time.sleep(2)
    browser.fill('wd', 'python')
    button = browser.find_by_id("su")
    button.click()
    time.sleep(2)
    browser.driver.close()


if __name__ == '__main__':
    main()
