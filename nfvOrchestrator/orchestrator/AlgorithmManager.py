#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : AlgorithmManager.py
# @Software: PyCharm
import random

from orchestrator.infoObjects import *

class AlgorithmManager:
    # ns_algorithm_list=[]
    # ns_active_algorithm=None
    #
    # vnffg_algorithm_list = []
    # vnffg_active_algorithm = None
    #
    # vnf_algorithm_list = []
    # vnf_active_algorithm = None
    # # ns
    # # todo
    # def reflush_algorithm_for_ns(self):
    #     return AlgorithmManager.ns_algorithm_list
    #
    # def get_all_algorithm_for_ns(self):
    #     return AlgorithmManager.ns_algorithm_list
    #
    # def get_active_algorithm_for_ns(self):
    #     return AlgorithmManager.ns_active_algorithm
    # # todo
    # def add_algorithm_for_ns(self):
    #     pass
    # # vnffg
    # # todo
    # def reflush_algorithm_for_vnffg(self):
    #     return AlgorithmManager.vnffg_algorithm_list
    #
    # def get_all_algorithm_for_vnffg(self):
    #     return AlgorithmManager.vnffg_algorithm_list
    #
    # def get_active_algorithm_for_vnffg(self):
    #     return AlgorithmManager.vnffg_algorithm_list
    #
    # # todo
    # def add_algorithm_for_vnffg(self):
    #     pass
    # # vnf
    # # todo
    # def reflush_algorithm_for_vnf(self):
    #     return AlgorithmManager.vnf_algorithm_list
    #
    # def get_all_algorithm_for_vnf(self):
    #     return AlgorithmManager.vnf_algorithm_list
    #
    # def get_active_algorithm_for_vnf(self):
    #     return AlgorithmManager.vnf_algorithm_list
    #
    # # todo
    # def add_algorithm_for_vnffg(self):
    #     pass

    def  get_solution_for_vnfd(self,vnfd,nfvo):
        # 寻找一个server，将vnfd部署在上面
        # 获取所有server
        server_list=nfvo.get_all_servers()
        random_server_index=random.randint(0,len(server_list))
        server=server_list[random_server_index]
        vnf_solution=Vnf_solution(vnfd=vnfd,server_instance=server,create_server=False,compute_node=None)
        solution=Solution
        solution.vnf_solution_list.append(vnf_solution)
        return solution

    #现在只考虑只有一条sfp的vnffg
    def get_solution_for_vnffg(self,vnffgd, nfvo,vnffg_name):

        solution = Solution
        # 为每一个sfp构造一个sfc solution
        vnf_index = 0
        for sfp in vnffgd.fp_vnfd_dic:
            sfp_name=list(sfp.keys())[0]
            sfp_content=sfp[sfp_name]
            # 为每一个vnf选择一个server
            vnfd_list=vnffgd.fp_vnfd_dic[sfp]
            vnf_list=[]

            for vnfd in vnfd_list:
                vnf_index+=1
                vnf_instance_name = vnffg_name + str(vnf_index)
                server_list = nfvo.get_all_servers()
                random_server_index = random.randint(0, len(server_list))
                server = server_list[random_server_index]
                ip=nfvo.get_server_ip(server)
                vnf_type = vnfd.type
                # 寻找与该server连接的SFF，由于目前只有一个SFF用于连接SF，就默认SFF1
                SFF_NAME=nfvo.get_sff_name(ip)
                vnf_solution = Vnf_solution(vnfd=vnfd, server_instance=server, create_server=False, compute_node=None)
                solution.vnf_solution_list.append(vnf_solution)
                vnf = vnfInfo(vm_name=None, vnf_name=vnf_instance_name, ip_mgmt_address=ip, rest_uri= "http://" +ip + ":5000",
                               sf_data_plane_locator_ip=ip, type=vnf_type, service_function_forwarder_name=SFF_NAME)
                vnf_list.append(vnf)
            # 由solution.vnf_lostion执行
            solution.sfc_solution.vnf_solution=None
            in_classifier_ip = '192.168.1.204'
            in_classifier_sff_name='SFF0'
            in_classifier_name='Classifier1'
            out_classifier_ip = '192.168.1.210'
            out_classifier_sff_name = 'SFF0'
            out_classifier_name='Classifier2'
            sff_ip = '192.168.1.208'
            sff0 = sffInfo(name="SFF0", node_name="node0", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                           data_plane_locator_ip=in_classifier_ip, vnf_list=None)
            sff1 = sffInfo(name="SFF1", node_name="node1", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                           data_plane_locator_ip=sff_ip, vnf_list=vnf_list)
            sff2 = sffInfo(name="SFF3", node_name="node5", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                           data_plane_locator_ip=out_classifier_ip, vnf_list=None)
            sff_list = [sff0, sff1, sff2]
            solution.sfc_solution.sff_list=sff_list
            sfc_name=vnffg_name+sfp_name+"-chain"
            sfc_list = [sfcInfo(name=sfc_name, isSymmetric="true", vnf_list=vnf_list)]
            solution.sfc_solution.sfc_list = sfc_list
            sfp_full_name=vnffg_name+sfp_name+"-path"
            sfp_list = [sfpInfo(sfp_name=sfp_full_name, sfc_name=sfc_name, classifier_name="Classifier1",
                                symmetric_classifier_name="Classifier2", is_symmetric="true")]
            solution.sfc_solution.sfp_list=sfp_list
            # acl信息从vnfgd中获取
            '''
            policy:
            type: ACL
            criteria:
              - network_src_port_id: 640dfd77-c92b-45a3-b8fc-22712de480e1
              - destination_port_range: 80-1024
              - ip_proto: 6
              - ip_dst_prefix: 192.168.1.2/24
            '''
            policy_type=sfp_content["properties"]["policy"]["type"]
            policy_criteria=sfp_content["properties"]["policy"]["criteria"]
            for item in policy_criteria:
                if 'source_port_range' in item:
                    source_port_range=item['source_port_range']
                    source_port_low=source_port_range.split("-")[0]
                    source_port_high = source_port_range.split("-")[0]
                if 'ip_src_prefix' in item:
                    ip_src_prefix=item['ip_src_prefix']
                if 'destination_port_range' in item:
                    destination_port_range=item['destination_port_range']
                    destination_port_low = destination_port_range.split("-")[0]
                    destination_port_high = destination_port_range.split("-")[0]
                if 'ip_proto' in item:
                    ip_proto=item['ip_proto']
                if 'ip_dst_prefix' in item:
                    ip_dst_prefix=item['ip_dst_prefix']
            ace_name=vnffg_name+sfp_name+"-ace"
            # 这个值是odl查询的值
            rspId=1
            rspName=vnffg_name+sfp_name+"-rsp"
            ace = aceInfo(rule_name=ace_name, rsp_name='nonoSchedule_'+rspId+rspName, dst_ip=ip_dst_prefix,
                           src_ip=ip_src_prefix,
                           ip_protocol=ip_proto, src_port_lower=source_port_low, src_port_upper=source_port_high, dst_port_lower=destination_port_low,
                           dst_port_upper=destination_port_high)
            acl_name_in=vnffg_name+sfp_name+"-acl"
            acl = aclInfo(name=acl_name_in, ace_list=[ace])
            solution.sfc_solution.acl_list = [acl]

            rsp = rspInfo(name=rspName, sfp=sfp_full_name, isSymmetric="false")
            solution.sfc_solution.rsp=rsp

            # step9:classifier info
            classifier0 = classifierInfo(name=in_classifier_name, sff_name=in_classifier_sff_name, sff_interface="veth-br", ace_name=acl_name_in)
            # classifier1 = classifierInfo(name=out_classifier_name, sff_name=out_classifier_sff_name, sff_interface="veth-br", ace_name=acl_name_out)
            classifier_list = [classifier0]
            solution.sfc_solution.classifier_list=classifier_list

        return solution

    def get_solution_for_ns(self,nsd, NFVI_manager, NS_manager):
        pass

class Solution:
    def __init__(self):
        # 这个暂时不用管
        self.net_solution_list=[]
        # 所有vnf部署方案都在这
        self.vnf_solution_list=[]
        # vnf_solution = solution.vnf_solution
        # for vnf_instance in solution.vnf_solution_list:
        #     vnfm_vnf_instance=self.vnfm.create_vnf(vnf_instance)

        # 包含多个sfc及vnf
        self.sfc_solution_list=[]
        # vnffg_solution = solution.vnffg_solution
        # for sfc in solution.sfc_solution_list:
        #     sfc_instance = self.FG_manager.deploy_sfc(sfc)


class  Net_solution:
    def __init__(self):
        pass




class Vnf_solution:
    def __init__(self,vnfd,server_instance,create_server,compute_node):
        self.vnfd=vnfd
        # 如果是新创建的实例，server_instance中的openstack_server为空
        # 如果是复用的实例，server_instance中的openstack_server为不为空
        self.server_instance=server_instance
        self.create_server=create_server
        self.compute_node=compute_node





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
class Sfc_solution:
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



