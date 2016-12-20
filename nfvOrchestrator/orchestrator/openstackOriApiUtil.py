import os_client_config

nova = os_client_config.make_client(
    'compute',
    auth_url='https://example.com',
    username='example-openstack-user',
    password='example-password',
    project_name='example-project-name',
    region_name='example-region-name')


import glanceclient.v2.client as glclient
glance = glclient.Client(...)
images = glance.images.list()


import glanceclient.v2.client as glclient
image_id = 'c002c82e-2cfa-4952-8461-2095b69c18a6'
glance = glclient.Client(...)
image = glance.images.get(image_id)

import novaclient.v2.client as nvclient
name = "cirros"
nova = nvclient.Client(...)
image = nova.images.find(name=name)

import glanceclient.v2.client as glclient
imagefile = "/tmp/myimage.img"
glance = glclient.Client(...)
with open(imagefile) as fimage:
  glance.images.create(name="myimage", is_public=False, disk_format="qcow2",
                       container_format="bare", data=fimage)


import novaclient.v2.client as nvclient
nova = nvclient.Client(...)
keypairs = nova.keypairs.list()

import novaclient.v2.client as nvclient
nova = nvclient.Client(...)
security_groups = nova.security_groups.list()

export OS_USERNAME="admin"
export OS_PASSWORD="password"
export OS_TENANT_NAME="admin"
export OS_AUTH_URL="http://IPADDRESS/v2.0"
def get_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d
credentials = get_credentials()
def get_nova_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d
nova_credentials = get_nova_credentials()

def print_values(val, type):
    if type == 'ports':
        val_list = val['ports']
    if type == 'networks':
        val_list = val['networks']
    if type == 'routers':
        val_list = val['routers']
    for p in val_list:
        for k, v in p.items():
            print("%s : %s" % (k, v))
        print('\n')


def print_values_server(val, server_id, type):
    if type == 'ports':
        val_list = val['ports']

    if type == 'networks':
        val_list = val['networks']
    for p in val_list:
        bool = False
        for k, v in p.items():
            if k == 'device_id' and v == server_id:
                bool = True
        if bool:
            for k, v in p.items():
                print("%s : %s" % (k, v))
            print('\n')

#!/usr/bin/env python
from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values

credentials = get_credentials()
neutron = client.Client(**credentials)
netw = neutron.list_networks()

print_values(netw, 'networks')


Create ports
#!/usr/bin/env python
from neutronclient.v2_0 import client
import novaclient.v2.client as nvclient
from credentials import get_credentials
from credentials import get_nova_credentials

credentials = get_nova_credentials()
nova_client = nvclient.Client(**credentials)

# Replace with server_id and network_id from your environment

server_id = '9a52795a-a70d-49a8-a5d0-5b38d78bd12d'
network_id = 'ce5d204a-93f5-43ef-bd89-3ab99ad09a9a'
server_detail = nova_client.servers.get(server_id)
print(server_detail.id)

if server_detail != None:
    credentials = get_credentials()
    neutron = client.Client(**credentials)

    body_value = {
                     "port": {
                             "admin_state_up": True,
                             "device_id": server_id,
                             "name": "port1",
                             "network_id": network_id
                      }
                 }
    response = neutron.create_port(body=body_value)
    print(response)


List ports
#!/usr/bin/env python
from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values

credentials = get_credentials()
neutron = client.Client(**credentials)
ports = neutron.list_ports()
print_values(ports, 'ports')


