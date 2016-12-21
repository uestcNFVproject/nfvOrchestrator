#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : orchestrator.py
# @Software: PyCharm


from orchestrator import OpenStackOriApi
# orchestrator

class orchestrator:
    # create new vnf through openstack(nova or tacker) by python ori api
    def new_vnf(self,vnf_info):
        # boot a vm
        nova_client = OpenStackOriApi.get_nova_clint()
        vnf=OpenStackOriApi.create_server(nova_client=nova_client, image_name=vnf_info.image_name, flavor_name=vnf_info.flavor_name,
                                          network_name=vnf_info.network_name,
                                          vm_name=vnf_info.vm_name, keypair_name=vnf_info.keypair_name, security_group_name=vnf_info.security_group_name,
                                          compute_node_name=vnf_info.compute_node_name, user_data=vnf_info.user_data)
        # register vnf to odl

        return vnf
    def new_sfc(self):
        print(1)