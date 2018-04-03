#!/usr/bin/env python
# -*- coding:utf-8 -*-

i = 12
str = 'http://www.baidu.com/index={0}'.format(i)
print(str)

str = str + '/123/'
print(str)

import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' 时间')


from fake_useragent import UserAgent
ua = UserAgent()
print(ua.random)
print(ua.random)

for i in range(6,31,6):
    print(i)