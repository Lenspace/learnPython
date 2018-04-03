#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree

html = '''
<?xml version="1.0" encoding="utf-8"?>

<bookstore>

<book>
  <title lang="en" very="cn">Harry Potter</title>
  <title lang="en" very="cn">Harry Potter1212</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
'''

s = etree.HTML(html)

#text,very = s.xpath('//title[@lang]/@lang | //title/@very')
s1 = s.xpath('//title')
print(s1)
s2 = s.xpath('//title[position()!=1]/text()')
print(s2)


html2 = '''
<p class="mt12"><span class="note subInfor">距5号线<a href='http://zu.fang.com/house1-j011-k0228/'>和平西桥站</a>约798米。</span></p>
'''

s2 = etree.HTML(html2)
str22 = s2.xpath('//p/span')[0].xpath('string()')
print(str22)
str23 = s2.xpath('string()')
#str23 = s23.xpath('string()')
print(str23)
