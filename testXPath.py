#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree

html = '''
<?xml version="1.0" encoding="utf-8"?>

<bookstore>

<book>
  <title lang="en" very="cn">Harry Potter</title>
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
text = s1.xpath('./@lang')
very = s1.xpath('./@very')
print(text)
print(very)