#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : infoObjects.py
# @Software: PyCharm

'''
these classes are for opendaylight operations
'''
class nodeInfo:
    def __init__(self,name,ip,vnf_list):
        self.name=name
        self.ip=ip
        self.vnf_list=vnf_list


class vnfInfo:
    def __init__(self, vm_name,vnf_name,ip_mgmt_address,rest_uri,sf_data_plane_locator_ip, type,service_function_forwarder_name,sf_data_plane_locator_port=6633,sf_data_plane_locator_name="eth1",image_name="ubuntu14.04", flavor_name="my3g", network_name="admin_internal_net",
                 keypair_name="mykey", security_group_name="my", compute_node_name='node-49.domain.tld', sf_dpl_name="eth1",
                 user_data='''
                #!/bin/sh
                passwd ubuntu<<EOF
                ubuntu
                ubuntu
                EOF
                sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
                service ssh restart
                '''):
        self.vm_name = vm_name
        self.vnf_name=vnf_name
        self.ip_mgmt_address=ip_mgmt_address
        self.rest_uri=rest_uri
        self.sf_data_plane_locator_ip=sf_data_plane_locator_ip
        self.sf_data_plane_locator_name=sf_data_plane_locator_name
        self.service_function_forwarder_name=service_function_forwarder_name
        self.sf_data_plane_locator_port=sf_data_plane_locator_port
        self.type=type
        self.image_name = image_name
        self.flavor_name = flavor_name
        self.network_name = network_name
        self.keypair_name = keypair_name
        self.security_group_name = security_group_name
        self.compute_node_name = compute_node_name
        self.sf_dpl_name=sf_dpl_name
        self.user_data=user_data

    def init_from_vnf(self,vnf):
        pass

class sffInfo:
    def __init__(self,name,node_name,ovs_bridge_name,data_plane_locator_name,data_plane_locator_ip,vnf_list):
        self.name=name
        self.node_name=node_name
        self.ovs_bridge_name=ovs_bridge_name
        self.data_plane_locator_name=data_plane_locator_name
        self.data_plane_locator_ip=data_plane_locator_ip
        self.vnf_list=vnf_list

class sfcInfo:
    def __init__(self,name,isSymmetric,vnf_list):
        self.name=name
        self.isSymmetric=isSymmetric
        self.vnf_list=vnf_list

class sfpInfo:
    def __init__(self,sfp_name,sfc_name,classifier_name,symmetric_classifier_name,is_symmetric):
        self.sfp_name=sfp_name
        self.sfc_name=sfc_name
        self.classifier_name=classifier_name
        self.symmetric_classifier_name=symmetric_classifier_name
        self.is_symmetric=is_symmetric



class aclInfo:
    def __init__(self,ace_list,name):
        self.name=name
        self.ace_list=ace_list

class aceInfo:
    def __init__(self,rule_name,rsp_name,dst_ip,src_ip,ip_protocol,src_port_lower,src_port_upper,dst_port_lower,dst_port_upper):
        self.rule_name=rule_name
        self.rsp_name=rsp_name
        self.dst_ip=dst_ip
        self.src_ip=src_ip
        self.ip_protocol=ip_protocol
        self.src_port_lower=src_port_lower
        self.src_port_upper=src_port_upper
        self.dst_port_lower=dst_port_lower
        self.dst_port_upper=dst_port_upper

class rspInfo:
    def __init__(self,name,sfp,isSymmetric):
        self.name=name
        self.sfp=sfp
        self.isSymmetric=isSymmetric

class classifierInfo:
    def __init__(self,name,sff_name,sff_interface,ace_name):
        self.name=name
        self.sff_name=sff_name
        self.sff_interface=sff_interface
        self.ace_name=ace_name
