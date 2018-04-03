#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree
from pymongo import MongoClient
import time
from fake_useragent import UserAgent
ua = UserAgent()

# 拉勾连续访问，第六页就有问题
# 明天试一下，如果速度慢一些可以么---->可以，一分钟5次是可以的
# 不知道带上Refer能否突破这个限制
# 是不是有个Refer的问题？那个会带着上一次的url的


def mylog(str):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ': ' + str)

def getHTMLText(url):
    try:
        header = {
            'Host': 'www.lagou.com',
            'User-Agent': ua.random,
            # 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        }
        mylog(header['User-Agent'])
        r = requests.get(url, headers=header, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return url+' 产生异常'

def scanPages(url, page):
    client = MongoClient()
    db = client.newLagou  # 连接test数据库，没有则自动创建
    mg_job_table = db.job  # 使用set集合，没有则自动创建

    for j in range(page):
        mylog('正在爬取第{0}页'.format(j+1))
        newUrl = url + '{0}/'.format(j+1)
        mylog(newUrl)
        html = getHTMLText(newUrl)

        s = etree.HTML(html)
        dpnames = s.xpath('//*[@id="s_position_list"]/ul/li/@data-positionname')
        comps = s.xpath('//*[@id="s_position_list"]/ul/li/@data-company')
        salarys = s.xpath('//*[@id="s_position_list"]/ul/li/@data-salary')
        positionids = s.xpath('//*[@id="s_position_list"]/ul/li/@data-positionid')
        compids = s.xpath('//*[@id="s_position_list"]/ul/li/@data-companyid')
        brs = s.xpath('//*[@id="s_position_list"]/ul/li/div[2]/div[2]/text()')  # 简介
        adds = s.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/span/em/text()') #地址


        length = len(positionids)
        mylog('当前页面共有元素{0}'.format(length))
        if length == 0:
            print(html)
            continue
        i = 0
        while i < length:
            dict = {}
            dict['positionid'] = positionids[i]
            dict['name'] = dpnames[i]
            dict['company'] = comps[i]
            dict['salary'] = salarys[i]
            dict['companyUrl'] = 'https://www.lagou.com/gongsi/{0}.html'.format(compids[i])
            dict['positionUrl'] = 'https://www.lagou.com/jobs/{0}.html'.format(positionids[i])
            dict['profile'] = brs[i]
            dict['address'] = adds[i]
            mg_job_table.insert(dict)
            i += 1
        mylog('开始等待')
        time.sleep(12)
        mylog('等待结束')

if __name__ == '__main__':
    url = 'https://www.lagou.com/zhaopin/C++/'
    scanPages(url, 10)
