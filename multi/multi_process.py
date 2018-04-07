#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

@author: lenspace

@license: (C) Copyright 2017-2018.

@contact: ustbenspace@gmail.com

@file: multi_process.py

@time: 2018/4/7 下午9:26

@desc: multi processes test

'''

from multiprocessing import Process,Pool
import os,time,random

def run_proc(name):
    print('Run child process %s (%s).' %(name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name, end-start))

if __name__ == '__main__':
    print('Parent process id is %d' % os.getpid())
    p = Process(target=run_proc, args=('testchild',))
    print('child process will start')
    p.start()
    p.join()
    print('child process is end')

    print('ready to create processes with pool.')
    pool = Pool(200)
    for i in range(201):
        pool.apply_async(long_time_task, args=(i,))
    print('waiting for all subprocesses done...')
    pool.close()  # 调用close以后，就不能添加新的process了
    pool.join()     # join之前，必须先调用close
    print('all subprocesses end.')