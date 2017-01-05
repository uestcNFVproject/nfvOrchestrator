#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-28 19:30
# @Author  : mengyuGuo
# @Site    :
# @File    : node.py
# @Software: PyCharm

from enum import Enum


class Node:
    node_list = []

    def __init__(self, id, type, node_capacity,pod):
        self.id = id
        self.type = type
        self.linklist = []

        # for compute_node
        self.node_capacity = node_capacity
        self.used_capacity = 0
        self.load_percent = 0.0
        self.sf_list = []

        # for compute_node & agg switch & edge switch
        self.pod = pod

        Node.node_list.append(self)

    def add_link(self, link):
        self.linklist.append(link)

    def del_link(self, link):
        self.linklist.remove(link)

    def add_sf(self, sf):
        self.sf_list.append(sf)
        self.used_capacity += sf.weight
        self.load_percent = self.used_capacity / self.node_capacity

    def del_sf(self, sf):
        self.sf_list.remove(sf)
        self.used_capacity -= sf.weight
        self.load_percent = self.used_capacity / self.node_capacity

    def __lt__(self, other):
        if not isinstance(other,Node):
            raise TypeError("can't cmp other type to Node")
        if self.load_percent<other.load_percent:
            return True
        else:
            return False


class NoedType(Enum):
    core_switch = 1
    agg_switch = 2
    edge_switch = 3
    compute_node = 4
