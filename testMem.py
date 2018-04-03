#!/usr/bin/env python
# -*- coding:utf-8 -*-
import resource

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
l = []
for i in range(50000):
    l.append(object())
mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
del l
print('Class: {}:\n'.format(getattr(cls, '__name__')))
print('Initial RAM usage: {:14,}'.format(mem_init))
print('  Final RAM usage: {:14,}'.format(mem_final))
