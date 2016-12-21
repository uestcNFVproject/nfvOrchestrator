#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午11:18
# @Author  : mengyuGuo
# @Site    : 
# @File    : NFVO.py
# @Software: PyCharm

class NFVO:
    def __init__(self,vim,vnfm,NSD_manager,VNFD_manager,vnf_instance_manager,nfvi_instance_manager,algorith_manager):
        self.vim_list=[vim]
        self.vnfm=vnfm
        self.NSD_manager=NSD_manager
        self.VNFD_manager=VNFD_manager
        self.vnf_instance_manager=vnf_instance_manager
        self.nfvi_instance_manager=nfvi_instance_manager
        self.algorith_manager=algorith_manager

    def register_vim(self,vim):
        self.vim_list.append(vim)



    def upload_vnfd(self,vnfd):
        return self.VNFD_manager.upload_vnfd(vnfd)

    def upload_nsd(self,nsd):
        return self.NSD_manager.upload_nsd(nsd)

    def deploy_ns(self,nsd_name):

        # step 1:get nsd
        nsd=self.NSD_manager.find_nsd_by_name(nsd_name)

        # step2 :compute solution
        solution=self.algorith_manager.get_solution(nsd,self.nfvi_instance_manager,self.vnf_instance_manager)

        # step 3:deploy new nets
        new_created_nets=solution.new_created_nets
        for net in new_created_nets:
            self.vim_list[net.vim_zone_number].create_net(net)

        # step 4:deploy new vms
        new_created_vms=solution.new_created_vms
        for vm in new_created_vms:
            self.vim_list[vm.vim_zone_number].create_vm(vm)

        # step 5:deploy sfc net path
        sfc_solution=solution.sfc_solution
        self.vim_list[sfc_solution.vim_zone_number].deploy_sfc(sfc_solution)

        # step 6:deply vnf
        vnf_list=solution.vnf_list
        for vnf in vnf_list:
            self.vnfm.create_vnf(vnf,vnf.vm)

        # step 7:check vnf state
        for vnf in solution.vnf_list:
            state=self.vnfm.check_vnf_state(vnf)
            if state!=0:
                print("vnf state wrong")
                for vm in new_created_vms:
                    self.vim_list[vm.vim_zone_number].delete_vm(vm)
                for net in new_created_nets:
                    self.vim_list[net.vim_zone_number].delete_net(net)
                return False
        # step 8 :check ns state
        pass



    def delete_ns(self):
        pass

    def destory_ns(self):
        pass
