#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: fang1.py

@time: 2018/3/31 下午11:11

@desc:

'''

from pymongo import MongoClient
import requests
from fake_useragent import UserAgent
from lxml import etree
import time


client = MongoClient()
db = client.fang
table_one = db.one
tb_two = db.two

ua = UserAgent()
host = 'http://zu.fang.com'

def mylog(str):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ': ' + str)

def getHTMLText(url):
    try:
        headers = {
            'User-Agent' : ua.random,
        }

        r = requests.get(url, headers=headers, timeout=20)
        sc = r.status_code
        print(sc)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return url+" 产生异常"

if __name__ == '__main__' :
    i = 1
    datas = table_one.find()
    for data in datas:
        mylog('正在爬取第{0}页'.format(i))
        i += 1

        area = data['area']
        url = data['url']
        mylog('url is ' + url)
        data.pop('_id')

        html = getHTMLText(url)
        s = etree.HTML(html)
        subareas = s.xpath('//*[@id="rentid_D04_08"]/a[position()!=1]/text()')
        subhrefs = s.xpath('//*[@id="rentid_D04_08"]/a[position()!=1]/@href')

        length = len(subareas)
        mylog('当前页面共有元素{0}'.format(length))

        j = 0
        while j < length:
            newData = {}
            newData['area'] = area
            newData['subarea'] = subareas[j]
            newData['url'] = host + subhrefs[j]
            tb_two.insert(newData)
            j += 1

        time.sleep(5)
