# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 16-12-21 下午4:30
# # @Author  : mengyuGuo
# # @Site    :
# # @File    : OpenStackOriApi.py
# # @Software: PyCharm
#
# import time
#
# from keystoneauth1.identity import v3
# from keystoneauth1 import session
# from novaclient import client
#
#
# def get_nova_client():
#     auth = v3.Password(auth_url='http://192.168.1.3:5000/v3',
#                        username='admin',
#                        password='admin',
#                        project_name='admin',
#                        user_domain_id='default',
#                        project_domain_id='default')
#     sess = session.Session(auth=auth)
#     nova_client = client.Client("2.1", session=sess)
#     return nova_client
#
#
# def get_flavors_list(nova_client):
#     return nova_client.flavors.list()
#
#
# def get_flavor_by_name(nova_client, name):
#     return nova_client.flavors.find(name=name)
#
#
# def get_servers_list(nova_client):
#     return nova_client.servers.list()
#
#
# def get_server_by_name(nova_client, name):
#     return nova_client.servers.find(name=name)
#
#
# def get_images_list(nova_client):
#     return nova_client.images.list()
#
#
# def get_image_by_name(nova_client, name):
#     return nova_client.images.find(name=name)
#
#
# def get_networks_list(nova_client):
#     return nova_client.networks.list()
#
#
# def get_network_by_name(nova_client, name):
#     return nova_client.networks.find(label=name)
#
#
# def get_keypairs_list(nova_client):
#     return nova_client.keypairs.list()
#
#
# def get_keypair_by_name(nova_client, name):
#     return nova_client.keypairs.find(name=name)
#
#
# def get_security_groups_list(nova_client):
#     return nova_client.security_groups.list()
#
#
# def get_security_group_by_name(nova_client, name):
#     return nova_client.security_groups.find(name=name)
#
# def get_ports_list(nova_client):
#     return nova_client.security_groups.list()
#
#
# def get_security_group_by_name(nova_client, name):
#     return nova_client.security_groups.find(name=name)
#
#
# def create_server(nova_client, image_name, flavor_name, network_name, vm_name, keypair_name, security_group_name,
#                   compute_node_name, user_data):
#     image = get_image_by_name(nova_client, image_name)
#     flavor = get_flavor_by_name(nova_client, flavor_name)
#     net = get_network_by_name(nova_client, network_name)
#     security_group = get_security_group_by_name(nova_client, security_group_name)
#     nics = [{'net-id': net.id}]
#     instance = nova_client.servers.create(name=vm_name, image=image, security_group=security_group,
#                                           availability_zone='nova:' + compute_node_name,
#                                           flavor=flavor, key_name=keypair_name, nics=nics, userdata=user_data)
#     print("Sleeping for 5s after create command")
#     time.sleep(5)
#     return instance
#
#
#
# def delete_server(nova_client,name):
#     server = nova_client.servers.find(name=name)
#     return server.delete()
#
# def add_floatin_ip(nova_client,server_name):
#     floating_ip = nova_client.floating_ips.create()
#     instance = get_server_by_name(nova_client=nova_client,name=server_name)
#     return instance.add_floating_ip(floating_ip)
#
#
# def del_floatin_ip(nova_client,server_name):
#     instance = get_server_by_name(nova_client=nova_client,name=server_name)
#     floating_ip=instance.get_floating_ip()
#     return instance.remove_floating_ip(address=floating_ip)
#
#
# def get_interface_list(nova_client,name):
#     instance = get_server_by_name(nova_client=nova_client, name=name)
#     return instance.interface_list()
#
# def attach_interface(nova_client,name,port_id):
#     instance = get_server_by_name(nova_client=nova_client, name=name)
#     return instance.interface_attach(port_id=port_id)
#
#
# def detach_interface(nova_client,name,port_id):
#     instance = get_server_by_name(nova_client=nova_client, name=name)
#     return instance.interface_detach(port_id=port_id)
#
#
# def create_net(nova_client, **kwargs):
#     return nova_client.networks.create(kwargs)
#
#
# def delete_net(nova_client, name):
#     network=get_network_by_name(nova_client,name)
#     return nova_client.networks.delete(network)
#
#
# def get_hosts_list(nova_client):
#     return nova_client.hosts.list()
#
#
#
# def get_hypervisors_list(nova_client):
#     return nova_client.hypervisors.list()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
