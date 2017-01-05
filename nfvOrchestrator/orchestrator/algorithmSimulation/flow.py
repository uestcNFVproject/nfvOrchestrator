#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 19:43
# @Author  : mengyuGuo
# @Site    :
# @File    : flow.py
# @Software: PyCharm


class Flow:
    flow_list = []

    def __init__(self, id, demand, src_node, dst_node):
        self.id = id
        self.demand = demand
        self.deplyed_demand = 0
        self.sub_flow_list = []
        self.parent_flow = None
        self.src_node = src_node
        self.dst_node = dst_node
        self.path = None

    def add_parent_flow(self, flow):
        self.parent_flow = flow

    def add_sub_flow(self, flow):
        self.sub_flow_list.append(flow)

    def deploy_on_path(self, path):
        if path.get_free_bandwith() < self.demand:
            raise Exception("demand larger than path free bandwith")
        if self.parent_flow != None:
            self.parent_flow.deplyed_demand += self.demand

        self.deplyed_demand += self.demand
        path.deploy_flow(self)
