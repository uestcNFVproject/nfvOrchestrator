#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-25 下午7:21
# @Author  : mengyuGuo
# @Site    : 
# @File    : countLIne.py
# @Software: PyCharm


import os
s = os.sep
lines=0
for rt, dirs, files in os.walk('.'):
    for f in files:
        if str(f).endswith('py') or str(f).endswith('html') or str(f).endswith('yaml'):
            count = len(open(os.path.join(rt, f), 'rU').readlines())
            lines=lines+count
print(lines)
