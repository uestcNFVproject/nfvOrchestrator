#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VIMProxy.py
# @Software: PyCharm


'''
provider api to manage physical resources
including   create vm ,destory vm,init vm,
            create net,destory net, get net.
            create sfc,destory sfc,get sfc

supported by openstack ,opendaylight

'''
from orchestrator import OpenStackOriApi
from orchestrator import OpenDayLightApi


class VIMProxy:
    # by opensatck api util
    # VM
    def create_vm(self,vm_name,image_name= 'TestVM',flavor_name = 'my3g',network_name = 'admin_internal_net',
                  keypair_name='mykey',security_group_name = 'my',compute_node_name = 'node-49.domain.tld'
                  , user_data = '''
            #!/bin/sh
            passwd ubuntu<<EOF
            ubuntu
            ubuntu
            EOF
            sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
            service ssh restart
            '''):
        nova_client=OpenStackOriApi.get_nova_client()
        # create normal vnf-based vm
        server = OpenStackOriApi.create_server(nova_client=nova_client, image_name=image_name, flavor_name=flavor_name,
                            network_name=network_name,
                            vm_name=vm_name, keypair_name=keypair_name, security_group_name=security_group_name,
                            compute_node_name=compute_node_name, user_data=user_data)
        return server

    def get_all_server(self):
        nova_client = OpenStackOriApi.get_nova_client()
        return OpenStackOriApi.get_servers_list(nova_client)

    def delete_vm(self,name):
        nova_client = OpenStackOriApi.get_nova_client()
        return OpenStackOriApi.delete_server(nova_client,name)

    # NET
    def create_net(self,**kwargs):
        nova_client = OpenStackOriApi.get_nova_client()
        return OpenStackOriApi.create_net(kwargs)


    def delete_net(self,name):
        nova_client = OpenStackOriApi.get_nova_client()
        return OpenStackOriApi.delete_net(nova_client,name)


    def get_all_hosts(self):
        nova_client = OpenStackOriApi.get_nova_client()
        return OpenStackOriApi.get_hosts_list(nova_client)


    def get_all_hypervisors_list(self):
        nova_client = OpenStackOriApi.get_nova_client()
        return OpenStackOriApi.get_hypervisors_list(nova_client)

    # todo
    def attach_vm_to_net(self):
        pass




    # physical resource info update
    def update_nfvi_info(self):
        pass


























