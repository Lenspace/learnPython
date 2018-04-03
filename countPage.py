#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 网页访问统计
# https://cc.amazingcounters.com/counter.php?i=3214508&c=9643837
import requests
from lxml import etree
from pyquery import PyQuery
from fake_useragent import UserAgent
import time
import random

ua = UserAgent()
def getHTMLText(url):
    try:
        headers = {
            'User-Agent' : ua.random,
            'Host' : 'cc.amazingcounters.com',
            'Referer' : 'http://www.cnblogs.com/chengxiao/p/6103002.html'
        }
        print(headers)
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

url = "https://cc.amazingcounters.com/counter.php?i=3214508&c=9643837"

if __name__ == '__main__':
    text = getHTMLText(url)
    print(text)