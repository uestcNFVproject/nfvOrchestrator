#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFM.py
# @Software: PyCharm


from enum import Enum
from orchestrator import VIMProxy
from orchestrator.infoObjects import vnfInfo
# provider vnf life cycle management

class VNFM:
    vnf_list=[]

    # create a vm to work with this vnf
    def create_vnf(self,vnfd):
        # step1:from vfnd create a vnf object
        vnf=VNF.init_from_vnfd(vnfd)
        # step2:create new vm
        vm=VIMProxy.VIMProxy.create_vm(vm_name=vnf.vm_name)
        # step3:associate vnf with vm
        # for simplcy ,1 vnf only has 1 vm
        vnf.vm=vm
        # step4:register it to odl
        vnf_info=vnfInfo.init_from_vnf([vnf])
        VIMProxy.OpenDayLightApi.register_vnfs([vnf_info])

    # create a vnf without creating vm
    def create_vnf(self, vnfd,vm):
        # step1:from vfnd create a vnf object
        vnf = VNF.init_from_vnfd(vnfd)
        # step2:associate vnf with vm
        vnf.vm = vm
        # step3:register it to odl
        vnf_info = vnfInfo.init_from_vnf([vnf])
        VIMProxy.OpenDayLightApi.register_vnfs([vnf_info])

    def delete_vnf(self,vnf):
        vm=vnf.vm
        VIMProxy.VIMProxy.delete_vm(vm)

    # init with needed packet
    def init_vnf_function(self,vnfd,vnf,vm):
        pass


    def get_all_vnf(self):
        return VNFM.vnf_list

    def get_vnf_by_name(self,name):
        for vnf in VNFM.vnf_list:
            if name==vnf.vnf_name:
                return vnf
        return None


    def get_vnf_by_id(self,vnf_id):
        for vnf in VNFM.vnf_list:
            if vnf_id==vnf.vnf_id:
                return vnf
        return None

    def update_vnf_state(self,vnf):
        pass




class VNF:
    def __init__(self,vnf_id,name,state,vnfm,type,vnfd):
        self.vnf_id=vnf_id
        self.name=name
        self.state=state
        self.vnfm=vnfm
        self.type=type
        self.vnfd=vnfd
    # todo
    def init_from_vnfd(self,vnfd):
        pass


class vnf_life_state(Enum):
    created=1
    inited=2
    running=3
    free=4
    broken=5

