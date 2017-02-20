#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-2-20 上午10:09
# @Author  : mengyuGuo
# @Site    : 
# @File    : testStr.py
# @Software: PyCharm


class A:
    def __init__(self):
        self.i=10

a=A()
def str_obj(obj):
 return str('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))