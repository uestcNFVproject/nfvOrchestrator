#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 22:38
# @Author  : mengyuGuo
# @Site    : 
# @File    : topo.py
# @Software: PyCharm

class Topo:

    def __init__(self,pod_num):
        self.pod_num=pod_num

        self.pod_list=[]

        self.core_switch_list=[]
        self.agg_switch_list=[]
        self.edge_switch_list=[]

        self.level1_link_list=[]
        self.level2_link_list = []
        self.level3_link_list = []

        self.path_list=[]
        self.path_dic={}

