#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : NFVIcatalogue.py
# @Software: PyCharm


# hold all physical resources,including computing,storage,networking
# and vm level
class Compute_node:
    def __init__(self, zone, name, type, state, cpu_intotal, mem_intotal, disk_intotal, bandwith, switch):
        self.zone = zone
        self.name = name
        self.type = type
        self.state = state

        self.cpu_intotal = cpu_intotal
        self.mem_intotal = mem_intotal
        self.disk_intotal = disk_intotal

        self.vcpu_in_use = 0
        self.mem_in_use = 0
        self.disk_in_use = 0

        self.bandwith_intotal = bandwith

        self.vm_nums = 0
        self.vm_list = []

        self.linked_switch_list = [switch]
        self.bandwith_dic={}
        self.bandwith_dic[switch.name] = {bandwith}

    def add_linked_switch_list(self, switch, bandwith):
        self.linked_switch_list.append(switch)
        self.bandwith_dic[switch.name] = bandwith

    def add_server(self, server):
        self.vm_nums = self.vm_nums + 1
        self.vm_list.append(server)
        self.vcpu_in_use = self.vcpu_in_use + server.cpu
        self.mem_in_use = self.mem_in_use + server.mem
        self.disk_in_use = self.disk_in_use + server.disk


class Server:
    def __init__(self, name, flavor, image, net):
        self.name = name
        self.cpu = flavor.cpu
        self.mem = flavor.mem
        self.disk = flavor.disk
        self.image = image
        self.net_list = [net]
        self.ip_list = []

class Flavor:
    def __init__(self, cpu, mem, disk):
        self.cpu = cpu
        self.mem = mem
        self.disk = disk


class Switch:
    def __init__(self, level, name):
        # 0=>core
        # 1=>agg
        # 2=>edg
        self.level = level
        self.name = name
        self.compute_node_list = []
        self.lower_level_switch_list = []
        self.upper_level_switch_list = []
        self.bandwith_dic = {}

    def add_compute_node(self, compute_node):
        self.compute_node_list.append(compute_node)
        self.bandwith_dic[compute_node.name] = compute_node.bandwith_intotal

    def add_lower_level_switch(self, switch, bandwith):
        self.lower_level_switch_list.append(switch)
        self.bandwith_dic[switch.name] = bandwith

    def add_upper_level_switch(self, switch, bandwith):
        self.upper_level_switch_list.append(switch)
        self.bandwith_dic[switch.name] = bandwith

    def del_compute_node(self, compute_node):
        for tmp in self.compute_node_list:
            if tmp.name == compute_node.name:
                self.compute_node_list.remove(tmp)
        if compute_node.name in self.bandwith_dic:
            self.bandwith_dic.pop(compute_node.name)

    def del_lower_level_switch_list(self, switch):
        for tmp in self.lower_level_switch_list:
            if tmp.name == switch.name:
                self.lower_level_switch_list.remove(tmp)
        if switch.name in self.bandwith_dic:
            self.bandwith_dic.pop(switch.name)

    def del_upper_compute_node(self, switch):
        for tmp in self.lower_level_switch_list:
            if tmp.name == switch.name:
                self.lower_level_switch_list.remove(tmp)
        if switch.name in self.bandwith_dic:
            self.bandwith_dic.pop(switch.name)


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


        # 网络采用人工配置
        switch=Switch(2,'Vswitch0')
        self.edge_layer_switch_list.append(switch)


        core_switch = Switch(0, 'kb-310gateway')
        self.core_layer_switch_list.append(core_switch)
        core_switch.add_lower_level_switch(switch,1000)
        switch.add_upper_level_switch(core_switch,1000)

        # 从OpenStack获取计算节点信息，由于nova接口获取信息过少,现在采取人工配置
        compute_node1=Compute_node('nova', 'node-50', 'active', 'up', 6, 3, 18, '1000', switch)
        self.compute_node_list.append(compute_node1)

        switch.add_compute_node(compute_node1)

        my3g=Flavor(1,0.5,3)
        server=Server('test6',my3g,'ubuntu14.04','inner_net')
        server.net_list.append('admin_internal_net')
        server.net_list.append('admin_floating_net')
        server.ip_list.append('192.168.123.6')
        server.ip_list.append('192.168.111.20')
        server.ip_list.append('192.168.1.215')
        compute_node1.add_server(server)

        server = Server('test5', my3g, 'ubuntu14.04', 'inner_net')
        server.net_list.append('admin_internal_net')
        server.net_list.append('admin_floating_net')
        server.ip_list.append('192.168.123.5')
        server.ip_list.append('192.168.111.19')
        server.ip_list.append('192.168.1.214')
        compute_node1.add_server(server)

        server = Server('test4', my3g, 'ubuntu14.04', 'inner_net')
        server.net_list.append('admin_internal_net')
        server.net_list.append('admin_floating_net')
        server.ip_list.append('192.168.123.4')
        server.ip_list.append('192.168.111.18')
        server.ip_list.append('192.168.1.211')
        compute_node1.add_server(server)

        server = Server('test3', my3g, 'ubuntu14.04', 'inner_net')
        server.net_list.append('admin_internal_net')
        server.net_list.append('admin_floating_net')
        server.ip_list.append('192.168.123.1')
        server.ip_list.append('192.168.111.17')
        server.ip_list.append('192.168.1.210')
        compute_node1.add_server(server)

        server = Server('test2', my3g, 'ubuntu14.04', 'inner_net')
        server.net_list.append('admin_internal_net')
        server.net_list.append('admin_floating_net')
        server.ip_list.append('192.168.123.3')
        server.ip_list.append('192.168.111.16')
        server.ip_list.append('192.168.1.208')
        compute_node1.add_server(server)

        server = Server('test1', my3g, 'ubuntu14.04', 'inner_net')
        server.net_list.append('admin_internal_net')
        server.net_list.append('admin_floating_net')
        server.ip_list.append('192.168.123.2')
        server.ip_list.append('192.168.111.15')
        server.ip_list.append('192.168.1.204')
        compute_node1.add_server(server)

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
