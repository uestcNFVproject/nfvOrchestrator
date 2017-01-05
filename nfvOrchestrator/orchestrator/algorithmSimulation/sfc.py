#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 22:45
# @Author  : mengyuGuo
# @Site    : 
# @File    : sfc.py
# @Software: PyCharm

class Sfc:
    def __init__(self,id):
        self.id=id
        self.sf_list=[]

    def append_sf(self,sf):
        self.sf_list.append(sf)


