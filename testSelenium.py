#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: testSelenium.py

@time: 2018/3/31 下午7:14

@desc:

'''

from selenium import webdriver

driver = webdriver.Chrome()
ph = webdriver.PhantomJS() # 无头浏览器，就是不会显现chrome
print(driver)

driver.get("https://www.taobao.com")

from selenium.webdriver.common.keys import Keys
elem = driver.find_element_by_xpath('//*[@id="q"]')
elem.send_keys('优衣库', Keys.ENTER)
print(driver.page_source)