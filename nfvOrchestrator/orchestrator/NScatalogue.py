#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : NScatalogue.py
# @Software: PyCharm



# 能够获取已经部署了的ns的解决方案
class NS_manager:
    ns_list=[]
    vnf_list=[]
    vnffg_list=[]
    def get_all_ns(self):
        return NS_manager.ns_list

    def add_ns(self,ns):
        NS_manager.ns_list.append(ns)

    def del_ns(self,ns):
        NS_manager.ns_list.remove(ns)



    def get_all_vnf_instance(self,vnf_instance):
        return NS_manager.vnf_list

    def add_vnf_instance(self,vnf_instance):
        return NS_manager.vnf_list.append(vnf_instance)

    def del_vnf(self,vnf_instance):
        return NS_manager.vnf_list.remove(vnf_instance)

    def del_vnf_by_name(self,vnf_instance):
        return NS_manager.vnf_list.remove(vnf_instance)

class NS:
    def __init__(self,nsd,solution):
        self.nsd=nsd
        self.solution=solution

