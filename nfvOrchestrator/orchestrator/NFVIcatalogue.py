#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : NFVIcatalogue.py
# @Software: PyCharm


# hold all physical resources,including computing,storage,networking
# and vm level
class NFVI_manager:
    def __init__(self):
        self.cpu_intotal=0
        self.mem_intotal=0
        self.disk_intotal=0
        self.bind_with_intotal=0

        self.used_vcpu_intotal=0
        self.used_mem_intotal=0
        self.used_disk_intotal = 0
        self.used_bind_with_intotal = 0
        
        self.compute_node_list=[]
        
        self.core_layer_switch_list = []
        self.agg_layer_switch_list = []
        self.edge_layer_switch_list = []

        # 从OpenStack获取计算节点信息，todo
        # 目前硬件平台固定，采用人工配置，todo

        pass

    def get_all_compute_node(self):
        return self.compute_node_list

    def get_all_vm(self):
        pass

    def get_all_switch_node(self):
        res=[]
        for node in self.core_layer_switch_list:
            res.append(node)
        for node in self.agg_layer_switch_list:
            res.append(node)
        for node in self.edge_layer_switch_list:
            res.append(node)
        return res

class compute_node:
    def __init__(self,zone,name,type,state,cpu_intotal,mem_intotal,disk_intotal,bandwith,switch):

        self.zone=zone
        self.name=name
        self.type=type
        self.state=state

        self.cpu_intotal = cpu_intotal
        self.mem_intotal = mem_intotal
        self.disk_intotal = disk_intotal

        self.vcpu_in_use=0
        self.mem_in_use=0
        self.disk_in_use=0
        
        self.bandwith_intotal=bandwith

        self.vm_nums=0
        self.vm_list=[]

        self.linked_switch_list=[switch]
        self.bandwith_dic[switch.name] = {bandwith}


    def add_linked_switch_list(self,switch,bandwith):
        self.linked_switch_list.append(switch)
        self.bandwith_dic[switch.name] = bandwith


    def add_server(self,server):
        self.vm_nums = self.vm_nums+1
        self.vm_list.append(server)
        self.vcpu_in_use = self.vcpu_in_use+server.vcpu
        self.mem_in_use = self.mem_in_use+server.mem
        self.disk_in_use = self.disk_in_use+server.disk

class server:

    def __init__(self,name,flavor,image,net):
        self.name=name
        self.cpu=flavor.cpu
        self.mem=flavor.mem
        self.disk=flavor.disk
        self.image=image
        self.net_list=[net]
        self.ip_list=[]


class switch:
    def __init__(self,level,name):
        self.level=level
        self.name=name
        self.compute_node_list=[]
        self.lower_level_switch_list = []
        self.upper_level_switch_list = []
        self.bandwith_dic = {}


    def add_compute_node(self,compute_node):
        self.compute_node_list.append(compute_node)
        self.bandwith_dic[compute_node.name]=compute_node.bandwith_intotal

    def add_lower_level_switch_list(self,switch,bandwith):
        self.lower_level_switch_list.append(switch)
        self.bandwith_dic[switch.name] = bandwith

    def add_upper_compute_node(self,switch,bandwith):
        self.upper_level_switch_list.append(switch)
        self.bandwith_dic[switch.name] = bandwith


    def del_compute_node(self,compute_node):
        for tmp in self.compute_node_list:
            if tmp.name ==compute_node.name:
                self.compute_node_list.remove(tmp)
        if compute_node.name in self.bandwith_dic:
            self.bandwith_dic.pop(compute_node.name)


    def del_lower_level_switch_list(self,switch):
        for tmp in self.lower_level_switch_list:
            if tmp.name ==switch.name:
                self.lower_level_switch_list.remove(tmp)
        if switch.name in self.bandwith_dic:
            self.bandwith_dic.pop(switch.name)

    def del_upper_compute_node(self,switch):
        for tmp in self.lower_level_switch_list:
            if tmp.name ==switch.name:
                self.lower_level_switch_list.remove(tmp)
        if switch.name in self.bandwith_dic:
            self.bandwith_dic.pop(switch.name)



