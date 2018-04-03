#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 房天下 zu.fang.com
import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random
from pymongo import MongoClient

ua = UserAgent()

def mylog(str):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ': ' + str)

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
        return url+" 产生异常"

url = "http://zu.fang.com"

if __name__ == '__main__':
    text = getHTMLText(url)
    s = etree.HTML(text)
    areas = s.xpath('//*[@id="rentid_D04_01"]/dd/a[position()!=1]/text()')
    hrefs = s.xpath('//*[@id="rentid_D04_01"]/dd/a[position()!=1]/@href')
    print(areas)
    print(hrefs)


    length = len(areas)
    length -= 1
    mylog('当前页面共有元素{0}'.format(length))

    client = MongoClient()
    db = client.fang
    table = db.one

    i = 0
    while i < length:
        dict = {}
        dict['area'] = areas[i]
        dict['url'] = url+hrefs[i]
        table.insert(dict)
        i += 1

