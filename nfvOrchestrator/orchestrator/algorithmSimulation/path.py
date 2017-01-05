#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 19:43
# @Author  : mengyuGuo
# @Site    : 
# @File    : path.py
# @Software: PyCharm
from nfvOrchestrator.orchestrator.algorithmSimulation.common import *


class Path:
    path_list = []

    def __init__(self, id, src_node, dst_node):
        self.id = id
        self.src_node = src_node
        self.dst_node = dst_node
        self.link_list = []
        self.flow_list = []

        Path.path_list.append(self)

    def get_free_bandwith(self):
        min = -1
        for link in self.link_list:
            if min == -1 or link.get_free_bandwith() < min:
                min = link.get_free_bandwith()
        return min

    def deploy_flow(self, flow):

        if self.get_free_bandwith() < flow.demand:
            raise Exception("demand larger than path free bandwith")
        for link in self.link_list:
            link.deploy_flow(flow)

    def get_min_load_percent(self):
        min = 1
        for link in self.link_list:
            if link.load_percent < min:
                min = link.load_percent
        return min

    def get_max_load_percent(self):
        max = 0
        for link in self.link_list:
            if link.load_percent > max:
                max = link.load_percent
        return max
