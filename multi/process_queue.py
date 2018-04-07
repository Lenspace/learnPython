#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: process_queue.py

@time: 2018/4/7 下午10:05

@desc: multi process with queue
        multiprocessing中的Queue是线程安全的，可以放心使用

'''

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write %s' % os.getpid())
    for i in range(10):
        print('Put %d in queue' % i)
        q.put(i)
        time.sleep(random.random())
        time.sleep(3)

def read(q):
    while True:
        value = q.get(True)
        print('Process to read %s, Get %d from queue' % (os.getpid(), value))

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr1 = Process(target=read, args=(q,))
    pr2 = Process(target=read, args=(q,))
    pw.start()
    pr1.start()
    pr2.start()
    pw.join()
    pr1.terminate()
    pr2.terminate()

