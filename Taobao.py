#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from fake_useragent import UserAgent


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

url = "https://uniqlo.tmall.com"

if __name__ == '__main__':

    text = getHTMLText(url)
    print(text)
