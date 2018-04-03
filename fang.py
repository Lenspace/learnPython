#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 房天下 fang.com
import requests
from lxml import etree
import pandas
from pyquery import PyQuery
from fake_useragent import UserAgent
import time
import random

ua = UserAgent()
def getHTMLText(url):
    try:
        headers = {
            'User-Agent' : ua.random,
        }
        print(headers)
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

url = "http://zu.fang.com/"
#//*[@id="rentid_D04_01"]/dd/a[2]
#//*[@id="rentid_D04_01"]/dd/a[3]
if __name__ == '__main__':
    text = getHTMLText(url)
    s = etree.HTML(text)
    age = s.xpath('//*[@id="rentid_D04_01"]/dd/a/text()')
    print(text)
    print(age)