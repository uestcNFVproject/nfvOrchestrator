#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFM.py
# @Software: PyCharm

import random
from enum import Enum
from orchestrator import VIMProxy
from orchestrator.NScatalogue import Vnf_instance
from orchestrator import OpenDayLightApi
from orchestrator import infoObjects


# provider vnf life cycle management
# 接受vnf_solution来创建vnf_instance
# 管理vnf 实体


class VNFS:
    pass




class VNFM:
    vnfi_list=[]
    vnfc_list = []
    vnfs_list = []
    vnfc_vnfs_dic={}

    def get_vnf_instance_list(self):
        return self.vnfi_list

    def get_vnf_c_list(self):
        return self.vnfc_list

    def get_vnf_s_list(self):
        return self.vnfs_list

    def get_vnfc_vnfs_dic(self):
        return self.vnfc_vnfs_dic

    def create_vnf(self,vnf_solution,vnf_instance_name):
        pass

    def del_vnf(self,vnf_instance_name):
        pass




    def create_vnf(self,vnf_solution,vnf_instance_name):
        if vnf_solution.create_vnfc:
            # 创建新的vm（vnfc）
            vm_instance =TackerProxy.create_vm(vm_name=vnf_solution.vm_name,vnf_solution=vnf_solution)
            #  绑定floating ip
            ip = self.get_new_floating_ip()
            address = Address(ip)
            vm_instance.add_floating_ip(address)
            self.vm_ip_dic[vm_instance] = ip
            self.vnfc_list.append(vm_instance)
        else:
            # 复用vm（vnfc）
            vm_instance = vnf_solution.vm_instance
        # 部署功能
        self.init_function(vm_instance, vnf_solution.vnfd, vnf_instance_name)
        vnfc=VNFS(vnf_solution.vnfd.type,vm_instance)
        self.vnfs_list.append()
        # 更新数据结构
        vnf_instance = Vnf_instance(name=vnf_instance_name, vm_instance=vm_instance, vnfd=vnf_solution.vnfd,sf=vnfc)
        if vm_instance not in self.vnfc_vnfs_dic.keys():
            self.vnfc_vnfs_dic[vm_instance]=[vnfc]
        else:
            self.vnfc_vnfs_dic[vm_instance].append(vnfc)
        return vnf_instance

    def delete_vnf(self, vnf_instance):
        pass

    def get_all_vnf_instances(self):
        return VNFM.vnf_list

    def get_vnf_instane_by_name(self, name):
        pass

    def get_vnf_by_id(self, vnf_id):
        pass

    def update_vnf_state(self, vnf_instances):
        pass

    def check_vnf_state(self, vnf_instances):
        pass


class Address:
    def __init__(self, ip):
        self.ip = ip


class VNFM_simple(VNFM):
    vnf_list = []
    vm_list = []
    vm_vnf_dic = {}
    vm_ip_dic = {}
    vm_interface_dic={}
    floating_ip_free_pool = ["192.168.1.203"]
    floating_ip_used_pool = []
    # 6个vm
    # todo 迁移到vim
    interfaceId_ip_dic={}
    interfaceId_ip_dic["0784ac37-1b50-4866-ada9-b295f308df5a"]="192.168.1.215"
    interfaceId_ip_dic["675d1415-201e-4f31-97f7-4d83a7eeba2f"]= "192.168.1.214"
    interfaceId_ip_dic['eacafe8d-e373-4d9f-a0ab-c6aac07bdf25']="192.168.1.211"
    interfaceId_ip_dic['e3be7a34-2c2b-4e4a-9f12-e38148354cd2'] = "192.168.1.210"
    interfaceId_ip_dic['380e1fd6-7697-4c65-82f7-13a5a4badf35'] = "192.168.1.208"
    interfaceId_ip_dic['947c1c2a-aa5c-4e2e-be92-937d534a815f'] = "192.168.1.204"
    def get_new_floating_ip(self):
        if len(VNFM_simple.floating_ip_free_pool) == 0:
            return None
        ip = VNFM_simple.floating_ip_free_pool[random.randint(0, len(VNFM_simple.floating_ip_free_pool) - 1)]
        VNFM_simple.floating_ip_used_pool.append(ip)
        VNFM_simple.floating_ip_free_pool.remove(ip)

    def free_floating_ip(self, ip):
        VNFM_simple.floating_ip_used_pool.remove(ip)
        VNFM_simple.floating_ip_free_pool.append(ip)

    def __init__(self):
        # 获取已有的vm，填充数据结构,这里只能获取server的interface_list
        VNFM_simple.vm_list=VIMProxy.VIMProxy.get_all_server()
        for vm in VNFM_simple.vm_list:
            interface_list=vm.interface_list()
            for interface in interface_list:
                id =interface.id
                if id in VNFM_simple.interfaceId_ip_dic:
                    ip=VNFM_simple.interfaceId_ip_dic[id]
                    if ip.startwith("192.168.1."):
                        VNFM_simple.vm_ip_dic[vm]=ip
        pass

        # self.vnfd=vnfd
        # # 如果是新创建的实例，server_instance为空
        # # 如果是复用的实例，server_instance不为空
        # self.server_instance=server_instance
        # self.create_server=create_server
        # self.compute_node=compute_node
    # todo 迁移到vim
    def get_server_ip(self,server):
        return VNFM_simple.vm_ip_dic[server]
    def create_vnf(self, vnf_solution, vnf_instance_name):
        if vnf_solution.create_server:
            # 创建新的vm，暂时不管flvor，都使用默认的m3g flavor（物理资源紧张）
            floavor = list(vnf_solution.vnfd.vdu_list[0].values())[0]["properties"]["flavor"]
            vm_instance = VIMProxy.VIMProxy.create_vm(vm_name=vnf_solution.vm_name,
                                                      compute_node_name=vnf_solution.compute_node.name)
            VNFM_simple.vm_list.append(vm_instance)
            #  添加一个floating ip
            ip = self.get_new_floating_ip()
            address = Address(ip)
            vm_instance.add_floating_ip(address)
            VNFM_simple.vm_ip_dic[vm_instance] = ip
        else:
            # 复用vm
            vm_instance = vnf_solution.server_instance
        # 部署功能
        self.init_function(vm_instance, vnf_solution.vnfd, vnf_instance_name)
        # 更新数据结构
        vnf_instance = Vnf_instance(name=vnf_instance_name, vnfm_instance=vm_instance, vnfd=vnf_solution.vnfd)
        VNFM_simple.vm_dic[vm_instance] = [vnf_instance]
        return vnf_instance

    def init_function(self, vm_instance, vnfd, vnf_instance_name):
        vnf_type = vnfd.type
        ip = VNFM_simple.vm_ip_dic[vm_instance]
        vnf = infoObjects.vnfInfo(vm_name=None, vnf_name=vnf_instance_name, ip_mgmt_address=ip,
                                  rest_uri="http://" + ip + ":5000", sf_data_plane_locator_ip=ip, type=vnf_type,
                                  service_function_forwarder_name="SFF1")
        vnf_list = [vnf]
        OpenDayLightApi.register_vnfs(vnf_list)

    def delete_vnf(self, vnf_instance):
        VNFM_simple.vnf_list.remove(vnf_instance)
        VNFM_simple.vm_dic[vnf_instance.vm].remove(vnf_instance)
        count = len(VNFM_simple.vm_dic[vnf_instance.vm])
        if count == 0:
            VIMProxy.VIMProxy.delete_vm(vnf_instance.vm)

    # # init with needed software该功能暂时由FG manager实现
    def init_vnf_function(self, vnf_instance):
        pass

    def get_all_vnf_instances(self):
        return VNFM.vnf_list

    def get_vnf_instane_by_name(self, name):
        for vnf in VNFM.vnf_list:
            if name == vnf.vnf_name:
                return vnf
        return None

    def get_vnf_by_id(self, vnf_id):
        for vnf in VNFM.vnf_list:
            if vnf_id == vnf.vnf_id:
                return vnf
        return None

    def update_vnf_state(self, vnf_instances):
        pass

    def check_vnf_state(self, vnf_instances):
        pass


class VNFM_tacker(VNFM):

    pass

    # todo
    def init_from_vnfd(self, vnfd):
        pass


class vnf_life_state(Enum):
    created = 1
    inited = 2
    running = 3
    free = 4
    broken = 5
