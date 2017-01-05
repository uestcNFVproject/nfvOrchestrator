#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 21:21
# @Author  : mengyuGuo
# @Site    : 
# @File    : pod.py
# @Software: PyCharm


class Pod:

    pod_list=[]
    def __init__(self,id):
        self.id=id
        self.agg_switch_lis=[]
        self.edge_switch_list=[]
        self.compute_node_list=[]

        Pod.pod_list.append(self)

    def add_agg_switch(self,node):
        self.agg_switch_lis.append(node)

    def add_edge_switch_list(self,node):
        self.edge_switch_list.append(node)

    def add_compute_node_list(self,node):
        self.compute_node_list.append(node)
