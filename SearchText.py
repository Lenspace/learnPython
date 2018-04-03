#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
dstPath = 'E:\\CodeProject'
txt = 'getString'
fileExt = '.h'
def SearchText(dir, txt, fileExt):
    list = os.listdir(dir)
    for line in list:
        filepath = os.path.join(dir, line)
        if os.path.isdir(filepath):
            SearchText(filepath, txt, fileExt)

        if filepath.endswith(fileExt):
            try:
                with open(filepath, 'r', encoding='gbk') as f:
                    lines = f.readlines()
                    #print(lines)
                    if str(lines).find(txt) != -1:
                        print(filepath)
                        print('------')
            except:
                print("xxxxxxxxxxxxxxxxxxxxx:    %s" % filepath)


SearchText(dstPath, txt, fileExt)