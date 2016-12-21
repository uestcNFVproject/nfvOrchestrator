#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : testOpenStackOriApi.py
# @Software: PyCharm

import json
from orchestrator.OpenStackOriApi import *
from django.test import TestCase

def test_openstasck_ori_api():
    nova_client = get_nova_client()
    print(get_flavors_list(nova_client))
    print(get_flavor_by_name(nova_client, 'my3g'))

    print(get_servers_list(nova_client))
    print(get_server_by_name(nova_client, 'test6'))

    print(get_images_list(nova_client))
    print(get_image_by_name(nova_client, 'TestVM'))

    print(get_networks_list(nova_client))
    print(get_network_by_name(nova_client, 'admin_internal_net'))

    print(get_keypairs_list(nova_client))
    print(get_keypair_by_name(nova_client, 'mykey'))

    print(get_security_groups_list(nova_client))
    print(get_security_group_by_name(nova_client, 'my'))

    # create cirros
    image_name = 'TestVM'
    flavor_name = 'm1.micro'
    network_name = 'admin_internal_net'
    vm_name = 'testcirros'
    keypair_name = 'mykey'
    security_group_name = 'my'
    compute_node_name = 'node-49.domain.tld'
    user_data = '''
    #!/bin/sh
    passwd ubuntu<<EOF
    ubuntu
    ubuntu
    EOF
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
    service ssh restart
    '''

    print(create_server(nova_client=nova_client, image_name=image_name, flavor_name=flavor_name,
                        network_name=network_name,
                        vm_name=vm_name, keypair_name=keypair_name, security_group_name=security_group_name,
                        compute_node_name=compute_node_name, user_data=user_data))


# nova_client = get_nova_client()
# print(get_hypervisors_list(nova_client))
class myTest(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_get_hosts(self):
        hosts=get_hosts_list(get_nova_client())
        print(hosts[-1])

    def test_get_hypervisors(self):
        hypervisors=get_hypervisors_list(get_nova_client())
        print(hypervisors)

    def test_get_all_servers(self):
        print(get_servers_list(get_nova_client()))
