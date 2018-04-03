#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree  #这里是xpath
import pandas as pd

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return url+' 产生异常'

if __name__ == '__main__':
    url = 'http://book.douban.com/subject/1084336/comments'
    #print(getHTMLText(url))
    html = getHTMLText(url)
    s = etree.HTML(html)
    href = s.xpath('//*[@id="comments"]/ul/li[1]/div[1]/a/@href')
    print(href)
    print(s.xpath('//*[@id="comments"]/ul/li[1]/div[1]/a/@title'))
    print(s.xpath('//*[@id="comments"]/ul/li[1]/div[1]/a/text()'))
    imgs = s.xpath('//*[@id="comments"]/ul/li/div[1]/a/img/@src')
    print(imgs)

    df = pd.DataFrame(imgs)
    df.to_csv('doubanimgs.csv')
'''
    with open('douban.txt', 'w', encoding='utf-8') as f:
        for j in href:
            print(j)
            f.write(j)
        for i in imgs:
            print(i)
            f.write(i)
'''








#print(r.encoding)   # 优选编码，没有的话，才使用下面的
#print(r.apparent_encoding) # 明显编码
#print(r.headers)
#print(r.text)