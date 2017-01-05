#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFM.py
# @Software: PyCharm


from enum import Enum
from orchestrator import VIMProxy
from orchestrator import NSDcatalogue
from orchestrator.infoObjects import vnfInfo
# provider vnf life cycle management
# 接受vnf_instance_solution来创建vnf
# 管理vnf 实体
class VNFM:
    vnf_list=[]

    def create_vnf(self,vnfd_solution):
        pass

    def delete_vnf(self,vnf_instance):
        pass

    def get_all_vnf_instances(self):
        return VNFM.vnf_list

    def get_vnf_instane_by_name(self,name):
        pass

    def get_vnf_by_id(self,vnf_id):
        pass

    def update_vnf_state(self,vnf_instances):
        pass

    def check_vnf_state(self,vnf_instances):
        pass



class VNFM_simple(VNFM):
    vnf_list=[]
    vm_dic={}
    def __init__(self):
        self.nsd_catalogue=NSDcatalogue.NSD_manager()

    def create_vnf(self,vnfd_solution):
        # step1:from vnfd_solution create a vnf object
        vnf_instance=Vnf_instance(vnfd_solution)

        # step2:create new vm，simply use defalut settings
        if vnf_instance.create_new_vm:
            vnf_instance.vm=VIMProxy.VIMProxy.create_vm(vm_name=vnfd_solution.vm_name)
            VNFM_simple.vm_dic[vnfd_solution.vm]=[vnf_instance]
        else:
            VNFM_simple.vm_dic[vnfd_solution.vm].append = vnf_instance

        # step3:update vnf instance in ns catalogue
        self.nsd_catalogue.add_vnf_instance(vnf_instance)

        # setp4:init vnf function
        self.init_vnf_function(self, vnf_instance)

        return vnf_instance

    def delete_vnf(self,vnf_instance):
        VNFM_simple.vnf_list.remove(vnf_instance)
        VNFM_simple.vm_dic[vnf_instance.vm].remove(vnf_instance)
        count=len(VNFM_simple.vm_dic[vnf_instance.vm])
        if count==0:
            VIMProxy.VIMProxy.delete_vm(vnf_instance.vm)


    # # init with needed software
    def init_vnf_function(self,vnf_instance):
        pass


    def get_all_vnf_instances(self):
        return VNFM.vnf_list

    def get_vnf_instane_by_name(self,name):
        for vnf in VNFM.vnf_list:
            if name==vnf.vnf_name:
                return vnf
        return None


    def get_vnf_by_id(self,vnf_id):
        for vnf in VNFM.vnf_list:
            if vnf_id==vnf.vnf_id:
                return vnf
        return None

    def update_vnf_state(self,vnf_instances):
        pass

    def check_vnf_state(self,vnf_instances):
        pass

class VNFM_tacker(VNFM):
    pass



class Vnf_instance:
    def __init__(self,vnfd_solution):
        self.name=vnfd_solution.name
        self.vnfd_solution=vnfd_solution
        self.vnfd=vnfd_solution.vnfd
        self.vm=vnfd_solution.vm
        self.create_new_vm=vnfd_solution.create_new_vm


    # todo
    def init_from_vnfd(self,vnfd):
        pass




class vnf_life_state(Enum):
    created=1
    inited=2
    running=3
    free=4
    broken=5

