#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: fang2.py

@time: 2018/4/1 下午12:57

@desc:

'''



from pymongo import MongoClient
from lxml import etree
import time

from mytools import mylog
from mytools import getHTMLText
from mytools import host

client = MongoClient()
db = client.fang
table_two = db.two
table_three = db.three

def getNextUrl(texts, hrefs):
    for text in texts:
        if text == '下一页':
            return host + hrefs[texts.index(text)]


if __name__ == '__main__' :
    i = 1
    datas = table_two.find()
    error = 1
    for data in datas:

        if error < 101:
            error += 1
            continue  # 意外中断后的恢复

        curUrl = data['url']
        area = data['area']
        subarea = data['subarea']

        page = 1
        while True:
            if len(curUrl) == 0:
                break

            time.sleep(5)
            mylog('正在进行第{0}次爬取'.format(i))
            i += 1
            mylog('正在爬取{0}-{1}-第{2}页: {3}'.format(area, subarea, page, curUrl))
            page += 1

            html = getHTMLText(curUrl)
            s = etree.HTML(html)

            # 解析当前页面数据
            '//*[@id="listBox"]/div[2]/dl[1]/dd'
            '//*[@id="rentid_D09_01_02"]'
            #titles = s.xpath('//*[@id="listBox"]/div[3]/dl/dd/p[1]/a/text()')
            titles = s.xpath('//*[@class="info rel"]/p[1]/a/text()')
            subUrls = s.xpath('//*[@id="listBox"]/div/dl/dd/p[1]/a/@href')
            '''
            数据不完整，屏蔽掉后面从子页面中直接获取
            refers = s.xpath('//*[@id="listBox"]/div[3]/dl/dd/p[2]') #/text()')
            referlist = list(map(lambda refer : refer.xpath('string()'), refers))
            #refer0 = refers[0].xpath('string()')
            print(len(refers))

            addrs = s.xpath('//*[@id="listBox"]/div[3]/dl/dd/div[1]/p/span')#[0].xpath('string()')
            addrlist = list(map(lambda addr : addr.xpath('string()'), addrs))
            '''
            prices = s.xpath('//*[@id="listBox"]/div/dl/dd/div[2]/p/span/text()')

            mylog(titles)
            mylog(subUrls)
            mylog(prices)

            if (len(titles) == len(subUrls)) and (len(titles)==len(prices)):
                length = len(subUrls)
                j = 0
                while j < length:
                    newData = {}
                    newData['area'] = area
                    newData['subarea'] = subarea
                    newData['url'] = host + subUrls[j]
                    newData['title'] = titles[j]
                    newData['prices'] = prices[j]
                    table_three.insert(newData)
                    j += 1
            else:
                with open('errorUrl.txt', 'a', encoding='utf-8') as f:
                    f.write(curUrl)
                    f.write('\r\n')


            # 获取下一页url
            texts = s.xpath('//*[@id="rentid_D10_01"]/a/text()')
            hrefs = s.xpath('//*[@id="rentid_D10_01"]/a/@href')

            nexturl = getNextUrl(texts, hrefs)
            if nexturl != None:
                curUrl = nexturl
            else:
                curUrl = ''
