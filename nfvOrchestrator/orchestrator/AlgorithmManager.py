#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : AlgorithmManager.py
# @Software: PyCharm
import random

class AlgorithmManager:
    def get_solution_for_ns(self,nsd, NFVI_manager, NS_manager):
        pass

    #现在只考虑只有一条sfp的vnffg
    def get_solution_for_vnffg(self,vnffgd, NFVI_manager, NS_manager,NSD_manager,VNFD_manager):
        solution=Solution()
        solution.vnf_solution=Vnf_solution()
        # 获取sfp
        sfp_list=vnffgd.fp_list()
        for dic in sfp_list:
            vnf_name_list=[]
            for (k, v) in dic.items():
                print(v['properties']['path'])
                for vnf_info in v['properties']['path']:
                    vnf_name_list.append(vnf_info['forwarder'])
            vnfd_list=[]
            for vnf_name in vnf_name_list:
                vnfd=VNFD_manager.get_vnfd_by_name(vnf_name)
                vnfd_list.append(vnfd)
                solution.vnf_solution.require_vnfd_list.append(vnfd)
            # 实际上要做的，就是部署vnfd——list中的vnf
            # demo：随机选择compute节点
            for vnfd in vnfd_list:
                compute_node_list=NFVI_manager.get_all_compute_node();
                compute_node_index=random.randint(0, len(compute_node_list))
        #         生成server_instance信息
                vnf_instance=Vnf_solution()
                vnf_instance.vnfd=vnfd
                vnf_instance.create_server=True
                vnf_instance.compute_node=compute_node_list[compute_node_index]
                solution.vnf_instance_solution_list.append(vnf_instance)

        return solution

class Solution:
    def __init__(self):
        # 这个暂时不用管
        self.net_solution
        # 这个是重点
        self.vnf_solution
        # 这个是根据vnf_solution生成,odl
        self.sfc_solution
        # 这个是根据vnf_solution生成,tacker
        self.vnffg_solution



class Vnf_solution:

    def __init__(self):
        self.vnf_instance_solution_list=[]
        self.require_vnfd_list=[]


    def add_vnf_instance_list(self,vnf_instance):
        self.vnf_instance_list.append(vnf_instance)


class Vnfd_solution:
    def __init__(self):
        self.vnfd
        # 如果是新创建的实例，server_instance中的openstack_server为空
        # 如果是复用的实例，server_instance中的openstack_server为不为空
        self.server_instance
        self.create_server
        self.compute_node





class server_instance:
    def __init__(self,name,vnfd):
        self.name
        self.vnfd_list=[vnfd]
        self.flavor
        self.image
        # vnfm返回的server对象
        self.openstack_server


        pass

# 创建odl打通数据链路的相关数据结构
# todo
class sfc_solution:
    def __init__(self):
        self.node_list
        self.vnf_list
        self.sff_list
        self.sfc_list
        self.sfp_list
        self.acl_list
        self.rsp
        self.classifier_list



class net_solution:
    def __init__(self,net_list):
        self.new_created_net_list=net_list


class net:
    def __init__(self):
        self.project
        self.name
        self.create_subnet
        self.subnet_name
        self.dhcp
        self.is_share
        self.is_public



