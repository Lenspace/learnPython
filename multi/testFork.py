#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: testFork.py

@time: 2018/4/7 下午9:20

@desc: test fork

'''

import os

print('Process (%d) start...' % os.getpid())

pid = os.fork()

if pid == 0:
    print('I am a child process (%s), and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I am a parent process (%s), i created a child %s' % (os.getpid(), pid))
