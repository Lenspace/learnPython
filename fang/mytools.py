#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: mytools.py

@time: 2018/4/1 下午1:00

@desc:

'''

import time
import requests
from fake_useragent import UserAgent

ua = UserAgent()
host = 'http://zu.fang.com'

def mylog(str):
    if isinstance(str, list):
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ': 数量{0} list:{1}'.format(len(str), str))
    else:
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

