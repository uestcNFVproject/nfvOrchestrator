import time

from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client


def get_nova_clint():
    auth = v3.Password(auth_url='http://192.168.1.3:5000/v3',
                       username='admin',
                       password='admin',
                       project_name='admin',
                       user_domain_id='default',
                       project_domain_id='default')
    sess = session.Session(auth=auth)
    nova_client = client.Client("2.1", session=sess)
    return nova_client


def get_flavors_list(nova_client):
    return nova_client.flavors.list()


def get_flavor_by_name(nova_client, name):
    return nova_client.flavors.find(name=name)


def get_servers_list(nova_client):
    return nova_client.servers.list()


def get_server_by_name(nova_client, name):
    return nova_client.servers.find(name=name)


def get_images_list(nova_client):
    return nova_client.images.list()


def get_image_by_name(nova_client, name):
    return nova_client.images.find(name=name)


def get_networks_list(nova_client):
    return nova_client.networks.list()


def get_network_by_name(nova_client, name):
    return nova_client.networks.find(label=name)


def get_keypairs_list(nova_client):
    return nova_client.keypairs.list()


def get_keypair_by_name(nova_client, name):
    return nova_client.keypairs.find(name=name)


def get_security_groups_list(nova_client):
    return nova_client.security_groups.list()


def get_security_group_by_name(nova_client, name):
    return nova_client.security_groups.find(name=name)


def create_server(nova_client, image_name, flavor_name, network_name, vm_name, keypair_name, security_group_name,
                  compute_node_name, user_data):
    image = get_image_by_name(nova_client, image_name)
    flavor = get_flavor_by_name(nova_client, flavor_name)
    net = get_network_by_name(nova_client, network_name)
    security_group = get_security_group_by_name(nova_client, security_group_name)
    nics = [{'net-id': net.id}]
    instance = nova_client.servers.create(name=vm_name, image=image, security_group=security_group,
                                          availability_zone='nova:' + compute_node_name,
                                          flavor=flavor, key_name=keypair_name, nics=nics, userdata=user_data)
    print("Sleeping for 5s after create command")
    time.sleep(5)
    return instance



