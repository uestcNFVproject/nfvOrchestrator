#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/28 19:38
# @Author  : mengyuGuo
# @Site    : 
# @File    : link.py
# @Software: PyCharm



class Link:
    link_list = []

    def __init__(self, id, src_node, dst_node, bandwith_capacity):
        self.id = id
        self.src_node = src_node
        self.dst_node = dst_node
        self.bandwith_capacity = bandwith_capacity
        self.used_bandwith = 0
        self.load_percent = 0.0
        self.flow_list = []
        Link.link_list.append(self)

    def get_free_bandwith(self):
        return self.bandwith_capacity - self.used_bandwith

    def get_other_node(self, node):
        if self.src_node.id == node.id:
            return self.dst_node
        return self.src_node

    def check_exceed_capacity(self, flow):
        if self.used_bandwith + flow.weight > self.bandwith_capacity:
            return False
        return True

    def deploy_flow(self, flow):
        self.flow_list.append(flow)
        self.used_bandwith += flow.weight
        self.load_percent = self.used_bandwith / self.bandwith_capacity
