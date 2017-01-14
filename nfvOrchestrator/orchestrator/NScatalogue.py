#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : NScatalogue.py
# @Software: PyCharm



# 能够获取已经部署了的ns,vnffg,vnf的实例
class NS_manager:
    ns_instance_list = []
    vnffg_instance_list = []
    vnf_instance_list = []

    # ns
    def get_all_ns_intances(self):
        return NS_manager.ns_instance_list

    def add_ns_instance(self, ns_instance):
        for ns in NS_manager.ns_instance_list:
            if ns.name == ns_instance.name:
                raise Exception("confic name")
        NS_manager.ns_instance_list.append(ns_instance)

    def check_ns_instance_name_conflic(self, name):
        for ns in NS_manager.ns_instance_list:
            if ns.name == name:
                return True
        return False

    def delete_ns_instance_by_name(self, name):
        for ns in NS_manager.ns_instance_list:
            if ns.name == name:
                NS_manager.ns_instance_list.remove(ns)

    def get_ns_instance_by_name(self, name):
        for ns in NS_manager.ns_instance_list:
            if ns.name == name:
                return ns

    # vnffg
    def get_all_vnffg_intances(self):
        return NS_manager.vnffg_instance_list

    def add_vnffg_instance(self, vnffg_instance):
        for vnffg in NS_manager.vnffg_instance_list:
            if vnffg.name == vnffg_instance.name:
                raise Exception("confic name")
        NS_manager.vnffg_instance_list.append(vnffg_instance)

    def check_vnffg_instance_name_conflic(self, name):
        for vnffg in NS_manager.vnffg_instance_list:
            if vnffg.name == name:
                return True
        return False

    def delete_vnffg_instance_by_name(self, name):
        for vnffg in NS_manager.vnffg_instance_list:
            if vnffg.name == name:
                NS_manager.vnffg_instance_list.remove(vnffg)

    def get_vnffg_instance_by_name(self, name):
        for vnffg in NS_manager.vnffg_instance_list:
            if vnffg.name == name:
                return vnffg

    # vnf
    def get_all_vnf_intances(self):
        return NS_manager.vnf_instance_list

    def add_vnf_instance(self, vnf_instance):
        for vnf in NS_manager.vnf_instance_list:
            if vnf.name == vnf_instance.name:
                raise Exception("confic name")
        NS_manager.vnf_instance_list.append(vnf_instance)

    def check_vnf_instance_name_conflic(self, name):
        for vnf in NS_manager.vnf_instance_list:
            if vnf.name == name:
                return True
        return False

    def delete_vnffg_instance_by_name(self, name):
        for vnf in NS_manager.vnf_instance_list:
            if vnf.name == name:
                NS_manager.vnf_instance_list.remove(vnf)

    def get_vnffg_instance_by_name(self, name):
        for vnf in NS_manager.vnf_instance_list:
            if vnf.name == name:
                return vnf


class Ns_Instance:
    def __init__(self,name,nsd,vnf_instance_list,fg_sfc_list,net_list):
        self.name = name
        self.nsd = nsd
        self.vnf_instance_list = vnf_instance_list
        self.fg_sfc_list = fg_sfc_list
        self.net_list = net_list
    pass


class Vnffg_Instance:
    def __init__(self,name,vnffgd,vnf_instance_list,fg_sfc_list,net_list):
        self.name=name
        self.vnffgd=vnffgd
        self.vnf_instance_list=vnf_instance_list
        self.fg_sfc_list=fg_sfc_list
        self.net_list=net_list
    pass


class Vnf_instance:
    def __init__(self, name, vnfm_instance, vnfd):
        self.name = name
        self.vnfm_instance = vnfm_instance
        self.vnfd = vnfd


    pass
