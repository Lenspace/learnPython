#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: task_worker.py

@time: 2018/4/8 上午12:03

@desc: distributed system this is master

'''

import sys, time, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
port = 5000
authkey = b'abc'

print('connect to server:port is %s:%s' % (server_addr, port))

m = QueueManager(address=(server_addr, port), authkey=authkey)
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列中读取数据，运算，并把结果写回到result中
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except:
        print('task queue is empty')

print('worker exit.')
