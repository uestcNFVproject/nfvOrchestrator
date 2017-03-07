#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : AlgorithmManager.py
# @Software: PyCharm
import random
import sys
import os
import datetime
from orchestrator.infoObjects import *

class Default_ns_algorithm:
    @staticmethod
    def get_solution_for_ns(nsd, nfvo, ns_name):
        pass

class Default_vnf_algorithm:
    @staticmethod
    def get_solution_for_vnfd( vnfd, nfvo):
        vnfc_list = nfvo.get_all_vnfcs()
        random_server_index = random.randint(0, len(vnfc_list))
        vnfc = vnfc_list[random_server_index]
        vnf_solution = Vnf_solution(vnfd=vnfd, server_instance=vnfc, create_server=False, compute_node=None)
        solution = Solution()
        solution.vnf_solution_list.append(vnf_solution)
        return solution

class Default_vnffg_algorithm:
    # 现在只考虑只有一条sfp的vnffg
    @staticmethod
    def get_solution_for_vnffg(vnffgd, nfvo, vnffg_name):

        solution = Solution()
        # 为每一个sfp构造一个sfc solution
        vnf_index = 0
        for sfp in vnffgd.fp_vnfd_dic:
            sfp_name = list(sfp.keys())[0]
            sfp_content = sfp[sfp_name]
            # 为每一个vnf选择一个server
            vnfd_list = vnffgd.fp_vnfd_dic[sfp]
            vnf_list = []

            for vnfd in vnfd_list:
                vnf_index += 1
                vnf_instance_name = vnffg_name + str(vnf_index)
                server_list = nfvo.get_all_servers()
                random_server_index = random.randint(0, len(server_list))
                server = server_list[random_server_index]
                ip = nfvo.get_server_ip(server)
                vnf_type = vnfd.type
                # 寻找与该server连接的SFF，由于目前只有一个SFF用于连接SF，就默认SFF1
                SFF_NAME = nfvo.get_sff_name(ip)
                vnf_solution = Vnf_solution(vnfd=vnfd, server_instance=server, create_server=False, compute_node=None)
                solution.vnf_solution_list.append(vnf_solution)
                vnf = vnfInfo(vm_name=None, vnf_name=vnf_instance_name, ip_mgmt_address=ip,
                              rest_uri="http://" + ip + ":5000",
                              sf_data_plane_locator_ip=ip, type=vnf_type, service_function_forwarder_name=SFF_NAME)
                vnf_list.append(vnf)
            # 由solution.vnf_lostion执行
            solution.sfc_solution.vnf_solution = None
            in_classifier_ip = '192.168.1.204'
            in_classifier_sff_name = 'SFF0'
            in_classifier_name = 'Classifier1'
            out_classifier_ip = '192.168.1.210'
            out_classifier_sff_name = 'SFF0'
            out_classifier_name = 'Classifier2'
            sff_ip = '192.168.1.208'
            sff0 = sffInfo(name="SFF0", node_name="node0", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                           data_plane_locator_ip=in_classifier_ip, vnf_list=None)
            sff1 = sffInfo(name="SFF1", node_name="node1", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                           data_plane_locator_ip=sff_ip, vnf_list=vnf_list)
            sff2 = sffInfo(name="SFF3", node_name="node5", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                           data_plane_locator_ip=out_classifier_ip, vnf_list=None)
            sff_list = [sff0, sff1, sff2]
            solution.sfc_solution.sff_list = sff_list
            sfc_name = vnffg_name + sfp_name + "-chain"
            sfc_list = [sfcInfo(name=sfc_name, isSymmetric="true", vnf_list=vnf_list)]
            solution.sfc_solution.sfc_list = sfc_list
            sfp_full_name = vnffg_name + sfp_name + "-path"
            sfp_list = [sfpInfo(sfp_name=sfp_full_name, sfc_name=sfc_name, classifier_name="Classifier1",
                                symmetric_classifier_name="Classifier2", is_symmetric="true")]
            solution.sfc_solution.sfp_list = sfp_list
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
            policy_type = sfp_content["properties"]["policy"]["type"]
            policy_criteria = sfp_content["properties"]["policy"]["criteria"]
            for item in policy_criteria:
                if 'source_port_range' in item:
                    source_port_range = item['source_port_range']
                    source_port_low = source_port_range.split("-")[0]
                    source_port_high = source_port_range.split("-")[0]
                if 'ip_src_prefix' in item:
                    ip_src_prefix = item['ip_src_prefix']
                if 'destination_port_range' in item:
                    destination_port_range = item['destination_port_range']
                    destination_port_low = destination_port_range.split("-")[0]
                    destination_port_high = destination_port_range.split("-")[0]
                if 'ip_proto' in item:
                    ip_proto = item['ip_proto']
                if 'ip_dst_prefix' in item:
                    ip_dst_prefix = item['ip_dst_prefix']
            ace_name = vnffg_name + sfp_name + "-ace"
            # 这个值是odl查询的值
            rspId = 1
            rspName = vnffg_name + sfp_name + "-rsp"
            ace = aceInfo(rule_name=ace_name, rsp_name='nonoSchedule_' + rspId + rspName, dst_ip=ip_dst_prefix,
                          src_ip=ip_src_prefix,
                          ip_protocol=ip_proto, src_port_lower=source_port_low, src_port_upper=source_port_high,
                          dst_port_lower=destination_port_low,
                          dst_port_upper=destination_port_high)
            acl_name_in = vnffg_name + sfp_name + "-acl"
            acl = aclInfo(name=acl_name_in, ace_list=[ace])
            solution.sfc_solution.acl_list = [acl]

            rsp = rspInfo(name=rspName, sfp=sfp_full_name, isSymmetric="false")
            solution.sfc_solution.rsp = rsp

            # step9:classifier info
            classifier0 = classifierInfo(name=in_classifier_name, sff_name=in_classifier_sff_name,
                                         sff_interface="veth-br", ace_name=acl_name_in)
            # classifier1 = classifierInfo(name=out_classifier_name, sff_name=out_classifier_sff_name, sff_interface="veth-br", ace_name=acl_name_out)
            classifier_list = [classifier0]
            solution.sfc_solution.classifier_list = classifier_list

        return solution


class AlgorithmManager:

    default_ns_algorithm=Default_ns_algorithm
    ns_algorithm_list = [default_ns_algorithm]
    active_ns_algorithm=default_ns_algorithm

    default_vnffg_algorithm = Default_vnffg_algorithm
    active_vnffg_algorithm = default_vnffg_algorithm
    vnffg_algorithm_list = [default_vnffg_algorithm]

    default_vnf_algorithm = Default_vnf_algorithm
    active_vnf_algorithm = Default_vnf_algorithm
    vnf_algorithm_list = [default_vnf_algorithm]
    # ns
    def get_all_algorithm_for_ns(self):
        return AlgorithmManager.ns_algorithm_list

    def get_active_algorithm_for_ns(self):
        return AlgorithmManager.active_ns_algorithm

    def set_active_algorithm_for_ns(self,algorithm_name):
        for ns_algorithm in AlgorithmManager.ns_algorithm_list:
            if algorithm_name==ns_algorithm.__name__:
                AlgorithmManager.active_ns_algorithm=ns_algorithm
                return True
        raise Exception('algorithm not found')

    def add_algorithm_for_ns(self,algorithm_content,algorithm_name):
        # 检查是否重名
        list = os.listdir(os.getcwd())
        for line in list:
            if line == algorithm_name + '.py':
                raise Exception('name complict')
        # 创建algorithm_name.py文件
        file = open(algorithm_name + '.py', 'w')
        # 模板文件head信息
        head_str = '''#!/usr/bin/env python
        # -*- coding: utf-8 -*-
        # @Time    : time
        # @Author  : mengyuGuo
        # @Site    :
        # @File    : file_name
        # @Software: dynamic create
        '''
        head_str = head_str.replace('time', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        head_str = head_str.replace('file_name', algorithm_name + '.py')
        file.write(head_str)
        # 模板class信息
        class_str = '''
        class class_name:
            @staticmethod
            def get_solution_for_ns(nsd, nfvo, ns_name):
                func_content
            '''
        class_str = class_str.replace('class_name', algorithm_name)
        class_str = class_str.replace('func_content', algorithm_content)
        file.write(class_str)
        file.close()
        # 加载新创建的模块和类
        sys.path.append(sys.path[0])
        module = __import__(algorithm_name)
        print(module)
        alclass = getattr(module, algorithm_name)
        # 动态创建算法类
        algorithm = type(algorithm_name, (), {'get_solution_for_ns': alclass.get_solution_for_ns})
        # 更新数据结构
        AlgorithmManager.ns_algorithm_list.append(algorithm)

        # algorithm.get_solution_for_ns('arg0', 'arg1', 'arg2')


    # vnffg
    def get_all_algorithm_for_vnffg(self):
        return AlgorithmManager.vnffg_algorithm_list

    def get_active_algorithm_for_vnffg(self):
        return AlgorithmManager.active_vnffg_algorithm

    def set_active_algorithm_for_vnffg(self, algorithm_name):
        for vnffg_algorithm in AlgorithmManager.vnffg_algorithm_list:
            if algorithm_name == vnffg_algorithm.__name__:
                AlgorithmManager.active_vnffg_algorithm = vnffg_algorithm
                return True
        raise Exception('algorithm not found')

    def add_algorithm_for_vnffg(self, algorithm_content, algorithm_name):
        # 检查是否重名
        print(os.getcwd())
        list = os.listdir(os.getcwd())
        for line in list:
            if line == algorithm_name + '.py':
                raise Exception('name complict')
        # 创建algorithm_name.py文件
        file = open(algorithm_name + '.py', 'w')
        # 模板文件head信息
        head_str = '''#!/usr/bin/env python
            # -*- coding: utf-8 -*-
            # @Time    : time
            # @Author  : mengyuGuo
            # @Site    :
            # @File    : file_name
            # @Software: dynamic create
            '''
        head_str = head_str.replace('time', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        head_str = head_str.replace('file_name', algorithm_name + '.py')
        file.write(head_str)
        # 模板class信息
        class_str = '''
            class class_name:
                @staticmethod
                def get_solution_for_vnfd( vnfd, nfvo):
                    func_content
                '''
        class_str = class_str.replace('class_name', algorithm_name)
        class_str = class_str.replace('func_content', algorithm_content)
        file.write(class_str)
        file.close()
        # 加载新创建的模块和类
        sys.path.append(sys.path[0])
        module = __import__(algorithm_name)
        print(module)
        alclass = getattr(module, algorithm_name)
        # 动态创建算法类
        algorithm = type(algorithm_name, (), {'get_solution_for_vnffg': alclass.get_solution_for_vnffg})
        # 更新数据结构
        AlgorithmManager.vnffg_algorithm_list.append(algorithm)

        # algorithm.get_solution_for_vnf('arg0', 'arg1')


    # vnf
    def get_all_algorithm_for_vnf(self):
        return AlgorithmManager.vnf_algorithm_list

    def get_active_algorithm_for_vnf(self):
        return AlgorithmManager.active_vnf_algorithm

    def set_active_algorithm_for_vnf(self, algorithm_name):
        for vnf_algorithm in AlgorithmManager.vnf_algorithm_list:
            if algorithm_name == vnf_algorithm.__name__:
                AlgorithmManager.active_vnf_algorithm = vnf_algorithm
                return True
        raise Exception('algorithm not found')

    def add_algorithm_for_vnf(self, algorithm_content, algorithm_name):
        # 检查是否重名
        path=os.getcwd()+'/orchestrator/'
        print(path)
        list = os.listdir(path)
        for line in list:
            if line == algorithm_name + '.py':
                raise Exception('name complict')
        # 创建algorithm_name.py文件
        file = open(algorithm_name + '.py', 'w')
        # 模板文件head信息
        head_str = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : time1
# @Author  : mengyuGuo
# @Site    :
# @File    : file_name
# @Software: dynamic create
import random
import sys
import os
import datetime
from orchestrator.infoObjects import *
from orchestrator.AlgorithmManager import *
            '''
        head_str = head_str.replace('time1', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        head_str = head_str.replace('file_name', algorithm_name + '.py')
        file.write(head_str)
        # 模板class信息
        class_str = '''
class class_name:
    @staticmethod
    def get_solution_for_vnfd( vnfd, nfvo):
func_content
                '''
        class_str = class_str.replace('class_name', algorithm_name)
        class_str = class_str.replace('func_content', algorithm_content)
        file.write(class_str)
        file.close()
        # 加载新创建的模块和类
        sys.path.append(path)
        module = __import__(algorithm_name)
        print(module)
        alclass = getattr(module, algorithm_name)
        # 动态创建算法类
        algorithm = type(algorithm_name, (), {'get_solution_for_vnfd ': alclass.get_solution_for_vnfd})
        # 更新数据结构
        AlgorithmManager.vnf_algorithm_list.append(algorithm)

        # algorithm.get_solution_for_vnf('arg0', 'arg1')
        return 'ok'



    def get_solution_for_vnfd(self, vnfd, nfvo):
        if AlgorithmManager.active_vnf_algorithm is None:
            return AlgorithmManager.default_vnf_algorithm.get_solution_for_vnfd(vnfd,nfvo)
        else:
            return AlgorithmManager.active_vnf_algorithm.get_solution_for_vnfd(vnfd,nfvo)

    def get_solution_for_vnffg(self, vnffgd, nfvo, vnffg_name):
        if AlgorithmManager.active_vnffg_algorithm is None:
            return AlgorithmManager.default_vnffg_algorithm.get_solution_for_vnffgd(vnffgd,nfvo,vnffg_name)
        else:
            return AlgorithmManager.active_vnffg_algorithm.get_solution_for_vnffgd(vnffgd,nfvo,vnffg_name)



    def get_solution_for_ns(self,nsd, nfvo, ns_name):
        if AlgorithmManager.active_ns_algorithm is None:
            return AlgorithmManager.default_ns_algorithm.get_solution_for_nsd(nsd,nfvo,ns_name)
        else:
            return AlgorithmManager.active_ns_algorithm.get_solution_for_nsd(nsd,nfvo,ns_name)

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



