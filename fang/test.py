#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: test.py

@time: 2018/4/2 下午4:04

@desc:

'''

from pymongo import MongoClient

client = MongoClient()
db = client.fang
table_two = db.two
table_three = db.three

datas = table_two.find()
for data in datas:
    print('area: %s \tsubarea: %s \turl: %s' % (data['area'], data['subarea'], data['url']))


print(table_three.count())