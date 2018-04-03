#!/usr/bin/env python
# -*- coding:utf-8 -*-

i = 12
str = 'http://www.baidu.com/index={0}'.format(i)
print(str)

str = str + '/123/'
print(str)

import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' 时间')

'''
from fake_useragent import UserAgent
ua = UserAgent()
print(ua.random)
print(ua.random)
'''

for i in range(6,31,6):
    print(i)

l1 = [1,2,3,4,5]
l2 = ['a', 'b', 'c', 'd', 'e']

for l in l2:
    if l is 'c':
        print(l1[l2.index(l)])
for i in range(len(l2)):
    if l2[i] is 'c':
        print(l1[i])


zipper = zip(l1, l2)
print(zipper)
for ite in zipper:
    print(ite)

    i1 = ite[1]
    print(i1)

dict1 = { 'abc': 1, 'bbb' : 1}
if dict1.get('abc') == 1:
    print('has abc')
    print(dict1)
if dict1.get('mm') != 1:
    print('has not mm')
    print(dict1)
    dict1['mm'] = 12
    print(dict1)

def toString(c):
    return c*2
l3 = map(toString, l1)
print(list(l3))

sx = 'hello'
print(len(sx))
sx2 = ''
print(len(sx2))

with open('error.txt', 'a', encoding='utf-8') as f:
    f.write('hello')
    f.write('\r\n')