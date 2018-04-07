#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: task_master.py

@time: 2018/4/7 下午11:24

@desc: distributed system this is master

'''

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda : result_queue)

# 绑定端口，设置密码为'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# 从result队列读取结果
print('Try get result....')
for i in range(10):
    r = result.get(timeout=10)
    print('result: %s' % r)

# 关闭
manager.shutdown()
print('master end.')
