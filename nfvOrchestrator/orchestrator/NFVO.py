#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午11:18
# @Author  : mengyuGuo
# @Site    : 
# @File    : NFVO.py
# @Software: PyCharm
nfvo_instance=None

def init_NFVO(vim, vnfm, NSD_manager, VNFD_manager, NS_manager, NFVI_manager,algorith_manager,FG_manager):
    global nfvo_instance
    if nfvo_instance is None:
        nfvo_instance=NFVO(vim, vnfm, NSD_manager, VNFD_manager, NS_manager, NFVI_manager,algorith_manager,FG_manager)
    return nfvo_instance

def get_NFVO():
    global nfvo_instance
    return nfvo_instance

class NFVO:
    def __init__(self, vim, vnfm, NSD_manager, VNFD_manager, NS_manager, NFVI_manager,algorith_manager,FG_manager):
        self.vim_list = [vim]
        self.vnfm = vnfm
        self.NSD_manager = NSD_manager
        self.VNFD_manager = VNFD_manager
        self.NS_manager = NS_manager
        self.NFVI_manager = NFVI_manager
        self.algorith_manager = algorith_manager
        self.FG_manager=FG_manager

    def register_vim(self, vim):
        self.vim_list.append(vim)

    def upload_vnfd(self, vnfd):
        return self.VNFD_manager.upload_vnfd(vnfd)

    def find_vnfd_by_name(self, name):
        return self.VNFD_manager.get_vnfd_by_name(name)

    def find_all_vnfd(self):
        return self.VNFD_manager.get_all_vnfd()

    def delete_vnfd_by_name(self,vnfd_name):
        return self.VNFD_manager.delete_vnfd(self.find_vnffgd_by_name(vnfd_name))

    def upload_vnffgd(self, vnffgd):
        return self.NSD_manager.upload_vnffdg(vnffgd)

    def find_vnffgd_by_name(self,name):
        return self.NSD_manager.find_vnffgd_by_name(name)

    def upload_nsd(self, nsd):
        return self.NSD_manager.upload_nsd(nsd)

    def find_nsd_by_id(self,nsd_id):
        return self.NSD_manager.find_nsd_by_id(nsd_id)

    def find_nsd_by_name(self,name):
        return self.NSD_manager.find_nsd_by_name(name)

    def get_vim_by_name(self,vim_name):
        for vim in self.vim_list:
            if vim.name==vim_name:
                return vim
        return None



    # def deploy_vnffgd(self, vnffgd_name):
    #
    #     # Step 1: NFVO从NSD catalogue获取相关vnffgd
    #     vnffgd = self.NSD_manager.find_vnffgd_by_name()
    #
    #     # step2 :调用Algorithm Manager进行调度，Algorithm Manager根据NS catalogue和NFVI catalogue获取现有NS服务运行情况和底层NFVI资源情况，根据设定的算法计算出部署方案
    #     # todo:right now tacker will create a vm for a vnf,we should change it
    #     solution = self.algorith_manager.get_solution_for_vnffgd(vnffgd, self.NFVI_manager, self.NS_manager,self.NSD_manager,self.VNFD_manager)
    #
    #     # step 3:NFVO根据部署方案，调用VNFM创建网络和VNF，VNFM根据方案创建VNF实例：如果需要，调用VIM创建新VM来承载VNF实例，如果复用旧VM，在旧VM上部署相关VNF实例。
    #     # 创建好vm后，VNFM对VM进行初始化配置和检测
    #     # net are  considered in the future to satisfy net isolation and bandwith requirement
    #     net_solution = solution.net_solution
    #     for net in net_solution:
    #         self.vim_list[net.vim_zone_number].create_net(net)
    #
    #     vnf_solution = solution.vnf_solution
    #     for vnf_instance in vnf_solution.vnf_instance_list:
    #         self.vnfm.create_vnf(vnf_instance)
    #
    #     # step 4:NFVO根据部署方案，调用FG Manager创建NS所需的网络转发链路
    #     vnffgd_solution = solution.vnffgd_solution
    #     self.FG_manager.deploy_vnffgd(vnffgd_solution)
    #
    #     # step 5:创建好vm和ns的net后，NFVO根据部署方案，调用VNFM对VNF进行检测
    #     # step 6:NFVO对NS服务进行检测
    #     for vnf in solution.vnf_solution:
    #         state = self.vnfm.check_vnf_state(vnf)
    #         if state != 0:
    #             print("vnf state wrong")
    #             for vnf in vnf_solution:
    #                 self.vnfm.delete_vnf(vnf)
    #             for net in net_solution:
    #                 self.vim_list[net.vim_zone_number].delete_net(net)
    #             return False
    #
    #     return True

    def deploy_vnf(self,vnfd):
        # step1 :调用Algorithm Manager进行调度，Algorithm Manager根据NS catalogue和NFVI catalogue获取现有NS,VNFFG,VNF服务运行情况和底层NFVI资源情况，根据设定的算法计算出部署方案
        # todo:right now tacker will create a vm for a vnf,we should change it
        solution = self.algorith_manager.get_solution_for_vnf(vnfd, self.NFVI_manager, self.NS_manager,
                                                                self.NSD_manager, self.VNFD_manager)
        vnf_solution = solution.vnf_solution
        for vnf_instance in vnf_solution.vnf_instance_list:
            self.vnfm.create_vnf(vnf_instance)
        return


    def deploy_vnffg(self, vnffgd):

        # step1 :调用Algorithm Manager进行调度，Algorithm Manager根据NS catalogue和NFVI catalogue获取现有NS,VNFFG,VNF服务运行情况和底层NFVI资源情况，根据设定的算法计算出部署方案
        # todo:right now tacker will create a vm for a vnf,we should change it
        solution = self.algorith_manager.get_solution_for_vnffg(vnffgd, self.NFVI_manager, self.NS_manager,self.NSD_manager,self.VNFD_manager)

        # step 2:NFVO根据部署方案，调用VNFM创建网络和VNF，VNFM根据方案创建VNF实例：如果需要，调用VIM创建新VM来承载VNF实例，如果复用旧VM，在旧VM上部署相关VNF实例。
        # 创建好vm后，VNFM对VM进行初始化配置和检测
        # net are  considered in the future to satisfy net isolation and bandwith requirement
        net_solution = solution.net_solution
        for net in net_solution:
            self.vim_list[net.vim_zone_number].create_net(net)

        vnf_solution = solution.vnf_solution
        for vnf_instance in vnf_solution.vnf_instance_list:
            self.vnfm.create_vnf(vnf_instance)

        # step 4:NFVO根据部署方案，调用FG Manager创建NS所需的网络转发链路
        vnffg_solution = solution.vnffg_solution
        self.FG_manager.deploy_vnffg(vnffg_solution)

        # step 5:创建好vm和ns的net后，NFVO根据部署方案，调用VNFM对VNF进行检测
        # step 6:NFVO对NS服务进行检测
        for vnf in solution.vnf_solution:
            state = self.vnfm.check_vnf_state(vnf)
            if state != 0:
                print("vnf state wrong")
                for vnf in vnf_solution:
                    self.vnfm.delete_vnf(vnf)
                for net in net_solution:
                    self.vim_list[net.vim_zone_number].delete_net(net)
                return False

        return True


    def deploy_ns(self, nsd):

        # Step 1: 将nsd分解为多个vnffgd（由于底层还不支持nsd的部署，所以只能进行分解）


        # step2 :调用Algorithm Manager进行调度，Algorithm Manager根据NS catalogue和NFVI catalogue获取现有NS服务运行情况和底层NFVI资源情况，根据设定的算法计算出部署方案
        # simply,one vnf only contains one vnfc
        # algorith will consider the physical envirment (through nfvi_instance_manager),current ns envirment(through ns_instance_manager) to satisfied the nsd requirement
        # solution contains vnf and vm mapping relations,if one vm only support one vnfc,each vnf will create a new vm (current support)
        # if not,vm should contain not created flag
        # todo:right now tacker will create a vm for a vnf,we should change it
        solution = self.algorith_manager.get_solution_for_ns(nsd, self.NFVI_manager, self.NS_manager)

        # step 3:NFVO根据部署方案，调用VNFM创建网络和VNF，VNFM根据方案创建VNF实例：如果需要，调用VIM创建新VM来承载VNF实例，如果复用旧VM，在旧VM上部署相关VNF实例。
        # 创建好vm后，VNFM对VM进行初始化配置和检测
        # net are  considered in the future to satisfy net isolation and bandwith requirement
        net_solution = solution.net_solution
        for net in net_solution:
            self.vim_list[net.vim_zone_number].create_net(net)

        vnf_solution = solution.vnf_solution
        for vnf in vnf_solution:
            self.vnfm.create_vnf(vnf, vnf.vm)

        # step 4:NFVO根据部署方案，调用FG Manager创建NS所需的网络转发链路
        sfc_solution = solution.sfc_solution
        self.FG_manager.deploy_sfc(sfc_solution)

        # step 5:创建好vm和ns的net后，NFVO根据部署方案，调用VNFM对VNF进行检测
        # step 6:NFVO对NS服务进行检测
        for vnf in solution.vnf_solution:
            state = self.vnfm.check_vnf_state(vnf)
            if state != 0:
                print("vnf state wrong")
                for vnf in vnf_solution:
                    self.vnfm.delete_vnf(vnf)
                for net in net_solution:
                    self.vim_list[net.vim_zone_number].delete_net(net)
                return False

        return True



    def destory_ns(self):
        pass

class ns_instance:
    pass