import os

from credentials import get_nova_credentials_v2
from novaclient.client import Client

def create_vnf():
    print(1)


def create_sfc():
    print(1)

def get_nova_credentials_v2():
    d = {}
    d['version'] = '2'
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_servers():
    credentials = get_nova_credentials_v2()
    nova_client = Client(**credentials)

    print(nova_client.servers.list())