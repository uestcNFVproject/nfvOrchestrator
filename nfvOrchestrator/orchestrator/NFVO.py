#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午11:18
# @Author  : mengyuGuo
# @Site    : 
# @File    : NFVO.py
# @Software: PyCharm
from orchestrator.NScatalogue import Ns_Instance
from orchestrator.NScatalogue import Vnf_instance
from orchestrator.NScatalogue import Vnffg_Instance
nfvo_instance=None

def init_NFVO(vim, vnfm, NSD_manager, VNFD_manager, NS_manager, NFVI_manager,algorith_manager,FG_manager):
    global nfvo_instance
    if nfvo_instance is None:
        nfvo_instance=NFVO(vim, vnfm, NSD_manager, VNFD_manager, NS_manager, NFVI_manager,algorith_manager,FG_manager,vim)
    return nfvo_instance

def get_NFVO():
    global nfvo_instance
    return nfvo_instance

class NFVO:
    def __init__(self, vim, vnfm, NSD_manager, VNFD_manager, NS_manager, NFVI_manager,algorith_manager,FG_manager,VIM):
        self.vim_list = [vim]
        self.vnfm = vnfm
        self.NSD_manager = NSD_manager
        self.VNFD_manager = VNFD_manager
        self.NS_manager = NS_manager
        self.NFVI_manager = NFVI_manager
        self.algorith_manager = algorith_manager
        self.FG_manager=FG_manager
        self.VIM=VIM

    def get_all_servers(self):
        return self.VIM.get_all_server()

    # vnfd vnffgd nsd catalogue
    def upload_vnfd(self, vnfd):
        return self.VNFD_manager.upload_vnfd(vnfd)

    def find_vnfd_by_name(self, name):
        return self.VNFD_manager.get_vnfd_by_name(name)

    def find_all_vnfd(self):
        return self.VNFD_manager.get_all_vnfd()

    def delete_vnfd_by_name(self,vnfd_name):
        return self.VNFD_manager.delete_vnfd(self.find_vnfd_by_name(vnfd_name))

    def upload_vnffgd(self, vnffgd):
        return self.NSD_manager.upload_vnffdg(vnffgd)

    def find_vnffgd_by_name(self,name):
        return self.NSD_manager.find_vnffgd_by_name(name)

    def delete_vnffgd_by_name(self,vnffgd_name):
        return self.NSD_manager.delete_vnffdg_by_name(vnffgd_name)

    def find_all_vnffgd(self):
        return  self.NSD_manager.get_all_vnffgd()

    def upload_nsd(self, nsd):
        return self.NSD_manager.upload_nsd(nsd)

    def delete_nsd_by_name(self, nsd_name):
        return self.NSD_manager.delete_nsd_by_name(nsd_name)

    def find_all_nsd(self):
        return self.NSD_manager.get_all_nsd()

    def find_nsd_by_id(self,nsd_id):
        return self.NSD_manager.find_nsd_by_id(nsd_id)

    def find_nsd_by_name(self,name):
        return self.NSD_manager.find_nsd_by_name(name)

    # vnf vnffg ns catalogue
    def deploy_vnf_instance_by_vnfd_name(self,vnfd_name,vnf_instance_name):
        vnfd=self.find_vnfd_by_name(vnfd_name)
        return self.deploy_vnf(vnfd,vnf_instance_name)



    def destory_vnf_instance_by_name(self, name):
        vnf_instance=self.get_vnf_install_by_name(name)
        return self.destory_vnf_instance(vnf_instance)


    def get_all_vnf_instances(self):
        return self.vnfm.get_all_vnf_instances()

    def get_vnf_install_by_name(self,vnf_instance_name):
        return self.vnfm.get_vnf_instane_by_name(vnf_instance_name)

    def delete_vnf_instanc_by_name(self,vnf_instance_name):
        vnf_instance=self.vnfm.get_vnf_instane_by_name(vnf_instance_name)
        return self.vnfm.delete_vnf(vnf_instance)

    def deploy_vnffg_instance_by_vnffgd_name(self,vnffgd_name,vnffg_instance_name):
        vnffgd=self.find_vnffgd_by_name(vnffgd_name)
        return self.deploy_vnffg(vnffgd,vnffg_instance_name)

    def destory_vnffg_instance_by_name(self,name):
        vnffg_instance=self.get_vnffg_instance_by_name(name)
        self.destory_vnffg(vnffg_instance)
        self.NS_manager.delete_vnffg_instance_by_name(name)

    def get_all_vnffg_instance(self):
        return self.NS_manager.get_all_vnffg_intances()

    def get_vnffg_instance_by_name(self,name):
        return self.NS_manager.get_vnffg_instance_by_name(name)

    def delete_vnffg_instance_by_name(self,name):
        return self.NS_manager.delete_vnffg_instance_by_name(name)


    def deploy_ns_instance_by_nsd_name(self,nsd_name):
        nsd=self.find_nsd_by_name(nsd_name)
        return self.deploy_ns(nsd)

    def get_all_ns_instance(self):
        return self.NS_manager.get_all_ns_intances()

    def get_ns_instance_by_name(self,name):
        return self.NS_manager.get_ns_instance_by_name(name)

    def destory_ns_instance_by_name(self,name):
        ns_instance=self.NS_manager.get_ns_instance_by_name(name)
        self.destory_ns_instance(ns_instance)
        self.NS_manager.delete_ns_instance_by_name(name)

    def delete_ns_instance_by_name(self,name):
        ns_instance=self.NS_manager.get_ns_instance_by_name(name)
        self.destory_ns(ns_instance)
        self.NS_manager.delete_ns_instance_by_name(name)

    # nfvi catalogue

    def get_all_compute_node(self):
        return self.NFVI_manager.get_all_compute_node()


    def get_all_switch_node(self):
        return self.NFVI_manager.get_all_switch_node()


    def get_server_ip(self,server):
        return self.vnfm.get_server_ip(server)
    def get_sff_name(self,sf_ip):
        return self.FG_manager.get_sff_name(sf_ip)

    # algorithm manager--ns
    def get_all_algorithm_for_ns(self):
        return self.algorith_manager.get_all_algorithm_for_ns()

    def get_active_algorithm_for_ns(self):
        return self.algorith_manager.get_active_algorithm_for_ns()

    def set_active_algorithm_for_ns(self, algorithm_name):
        return self.algorith_manager.set_active_algorithm_for_ns(algorithm_name)

    def add_algorithm_for_ns(self, algorithm_content, algorithm_name):
        return self.algorith_manager.add_algorithm_for_ns(algorithm_content, algorithm_name)


    # algorithm manager--vnffg
    def get_all_algorithm_for_vnffg(self):
        return self.algorith_manager.get_all_algorithm_for_vnffg()

    def get_active_algorithm_for_vnffg(self):
        return self.algorith_manager.get_active_algorithm_for_vnffg()

    def set_active_algorithm_for_vnffg(self, algorithm_name):
        return self.algorith_manager.set_active_algorithm_for_vnffg(algorithm_name)

    def add_algorithm_for_vnffg(self, algorithm_content, algorithm_name):
        return self.algorith_manager.add_algorithm_for_vnffg(algorithm_content, algorithm_name)

    # algorithm manager--vnf
    def get_all_algorithm_for_vnf(self):
        return self.algorith_manager.get_all_algorithm_for_vnf()

    def get_active_algorithm_for_vnf(self):
        return self.algorith_manager.get_active_algorithm_for_vnf()

    def set_active_algorithm_for_vnf(self, algorithm_name):
        return self.algorith_manager.set_active_algorithm_for_vnf(algorithm_name)

    def add_algorithm_for_vnf(self, algorithm_content, algorithm_name):
        return self.algorith_manager.add_algorithm_for_vnf(algorithm_content, algorithm_name)

    # settings
    def register_vim(self, vim):
        self.vim_list.append(vim)

    def get_all_vnfcs(self):
        return self.get_all_servers()

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

    def deploy_vnf(self,vnfd,vnf_instance_name):
        if self.NS_manager.check_vnf_instance_name_conflic(vnf_instance_name):
            raise Exception("name conflict")
        # 获取解决方案
        print('get solution')
        solution = self.algorith_manager.get_solution_for_vnfd(vnfd, self)
        print(solution)
        # 执行部署
        vnf_instance=None
        for vnf_solution in solution.vnf_solution_list:
            vnf_instance=self.vnfm.create_vnf(vnf_solution,vnf_instance_name)
        # 更新ns_catalogue
        self.NS_manager.add_vnf_instance(vnf_instance)
        return vnf_instance

    # todo
    def destory_vnf_instance(self,vnf_instance):
        pass

    def deploy_vnffg(self, vnffgd,vnffg_name):
        if self.NS_manager.check_vnffg_instance_name_conflic(vnffg_name):
            raise Exception("name conflict")
        # 获取解决方案
        solution = self.algorith_manager.get_solution_for_vnffg(vnffgd, self,vnffg_name)

        # 部署net
        # net are  considered in the future to satisfy net isolation and bandwith requirement
        net_instance_list=[]
        for net_solution in solution.net_solution_list:
            net_instance=self.vim_list[net_solution.vim_zone_number].create_net(net_solution)
            net_instance_list.append(net_instance)

        # 部署vnf
        vnf_instance_list=[]
        vnfd_list=[]
        vnf_index = 0
        for vnf_solution in solution.vnf_solution_list:
            vnf_index += 1
            vnf_instance_name = vnffg_name + str(vnf_index)
            vnf_instance=self.vnfm.create_vnf(vnf_solution,vnf_instance_name)
            vnf_instance_list.append(vnf_instance)
            # 0=>vnfd
            vnfd_list.append(vnf_solution.vnfd)

        # 部署fg
        sfc_instance_list=[]
        for sfc_solution in solution.sfc_solution_list:
            sfc_instance = self.FG_manager.deploy_sfc(sfc_solution)
            sfc_instance_list.append(sfc_instance)



        # 检测
        for vnf in solution.vnf_solution:
            state = self.vnfm.check_vnf_state(vnf)
            if state != 0:
                print("vnf state wrong")
                for vnf in vnf_solution:
                    self.vnfm.delete_vnf(vnf)
                for net in net_solution:
                    self.vim_list[net.vim_zone_number].delete_net(net)
                return False

        # 更新ns_catalogue
        for vnf_instance in vnf_instance_list:
            self.NS_manager.add_vnf_instance(vnf_instance)

        vnffg_instance=Vnffg_Instance(name=vnffg_name,vnffgd=vnffgd,vnf_instance_list=vnf_instance_list,fg_sfc_list=sfc_instance_list,net_list=net_instance_list)
        self.NS_manager.add_vnffg_instance(vnffg_instance)
        return vnffg_instance

    #  todo
    def destory_vnffg(self, vnffg_instance):
        pass


    def deploy_ns(self, nsd,ns_instance_name):
        if self.NS_manager.check_ns_instance_name_conflic(ns_instance_name):
            raise Exception("name conflict")
        # 获取解决方案
        solution = self.algorith_manager.get_solution_for_ns(nsd, self)

        # 部署net
        # net are  considered in the future to satisfy net isolation and bandwith requirement
        net_instance_list=[]
        for net_solution in solution.net_solution_list:
            net_instance=self.vim_list[net_solution.vim_zone_number].create_net(net_solution)
            net_instance_list.append(net_instance)

        # 部署vnf
        vnfm_vnf_instance_list=[]
        vnfd_list=[]
        vnf_solution = solution.vnf_solution
        for vnf_solution in solution.vnf_solution_list:
            vnfm_vnf_instance=self.vnfm.create_vnf(vnf_solution)
            vnfm_vnf_instance_list.append(vnfm_vnf_instance)
            # 0=>vnfd
            vnfd_list.append(vnf_solution.vnfd)

        # 部署fg
        sfc_instance_list=[]
        for sfc_solution in solution.sfc_solution_list:
            sfc_instance = self.FG_manager.deploy_sfc(sfc_solution)
            sfc_instance_list.append(sfc_instance)

        # 检测
        for vnf in solution.vnf_solution:
            state = self.vnfm.check_vnf_state(vnf)
            if state != 0:
                print("vnf state wrong")
                for vnf in vnf_solution:
                    self.vnfm.delete_vnf(vnf)
                for net in net_solution:
                    self.vim_list[net.vim_zone_number].delete_net(net)
                return False

        # 更新ns_catalogue
        vnf_instance_list=[]
        vnf_index=0
        for vnfm_vnf_instance in vnfm_vnf_instance_list:
            vnf_instance_name=ns_instance_name+str(vnf_index)
            vnfd=vnfd_list[vnf_index]
            vnf_index+=1
            vnf_instance = Vnf_instance( name=vnf_instance_name, vnfm_instance=vnfm_vnf_instance, vnfd=vnfd)
            self.NS_manager.add_vnf_instance(vnf_instance)
            vnf_instance_list.append(vnf_instance)
        ns_instance=Ns_Instance(name=ns_instance_name,nsd=nsd,vnf_instance_list=vnf_instance_list,fg_sfc_list=sfc_instance_list,net_list=net_instance_list)
        self.NS_manager.add_ns_instance(ns_instance)
        return ns_instance



    # todo
    def destory_ns(self,ns_instance):
        pass

