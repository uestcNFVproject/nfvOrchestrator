import argparse
import requests, json
from requests.auth import HTTPBasicAuth
from subprocess import call
import time
import sys
import os

USERNAME = 'admin'
PASSWORD = 'admin'
controller = '192.168.1.225'
DEFAULT_PORT = '8181'


def register_nodes(node_list):
    put(controller, DEFAULT_PORT, get_service_nodes_uri(), get_service_nodes_data(node_list=node_list), True)

def register_vnfs(vnf_list):
    put(controller, DEFAULT_PORT, get_service_functions_uri(),
        get_service_functions_data(vnf_list=vnf_list), True)


def register_sffs(sff_list):
    put(controller, DEFAULT_PORT, get_service_function_forwarders_uri(),
        get_service_function_forwarders_data(sff_list=sff_list), True)


def register_sfcs(sfc_list):
    put(controller, DEFAULT_PORT, get_service_function_chains_uri(),
        get_service_function_chains_data(sfc_list=sfc_list), True)


def register_sf_metadata_data():
    put(controller, DEFAULT_PORT, get_service_function_metadata_uri(), get_service_function_metadata_data(), True)


def register_sfps(sfp_list):
    put(controller, DEFAULT_PORT, get_service_function_paths_uri(), get_service_function_paths_data(sfp_list=sfp_list),
        True)


def register_acls(acl_list):
    put(controller, DEFAULT_PORT, get_service_function_acl_uri(), get_service_function_acl_data(acl_list=acl_list),
        True)


def register_rsp(rsp):
    post(controller, DEFAULT_PORT, get_rendered_service_path_uri(), get_rendered_service_path_data(rsp=rsp), True)


def register_classifiers(classifier_list):
    put(controller, DEFAULT_PORT, get_service_function_classifiers_uri(),
        get_service_function_classifiers_data(classifier_list=classifier_list), True)


def get(host, port, uri):
    url = 'http://' + host + ":" + port + uri
    r = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    jsondata = json.loads(r.text)
    return jsondata


def put(host, port, uri, data, debug=False):
    '''Perform a PUT rest operation, using the URL and data provided'''

    url = 'http://' + host + ":" + port + uri

    headers = {'Content-type': 'application/yang.data+json',
               'Accept': 'application/yang.data+json'}
    if debug == True:
        print("PUT %s" % url)
        print(json.dumps(data, indent=4, sort_keys=True))
    r = requests.put(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if debug == True:
        print(r.text)
    r.raise_for_status()
    time.sleep(5)


def post(host, port, uri, data, debug=False):
    '''Perform a POST rest operation, using the URL and data provided'''

    url = 'http://' + host + ":" + port + uri
    headers = {'Content-type': 'application/yang.data+json',
               'Accept': 'application/yang.data+json'}
    if debug == True:
        print("POST %s" % url)
        print(json.dumps(data, indent=4, sort_keys=True))
    r = requests.post(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if debug == True:
        print(r.text)
    r.raise_for_status()
    time.sleep(5)

def get_service_nodes_uri():
    return "/restconf/config/service-node:service-nodes"

def get_service_nodes_data(node_list):
    service_nodes=[]
    for node in node_list:
        dic= {
            "name": node.name,
            "service-function": [
            ],
            "ip-mgmt-address": node.ip
        }
        service_nodes.append(dic)
    return service_nodes


def get_service_functions_uri():
    return "/restconf/config/service-function:service-functions"


def get_service_functions_data(vnf_list):
    service_function_list = []
    for vnf in vnf_list:
        dic = {
            "name": vnf.vnf_name,
            "ip-mgmt-address": vnf.ip_mgmt_address,
            "rest-uri": vnf.rest_uri,
            "type": "dpi",
            "nsh-aware": "true",
            "sf-data-plane-locator": [
                {
                    "name": vnf.sf_data_plane_locator_name,
                    "port": vnf.sf_data_plane_locator_port,
                    "ip": vnf.sf_data_plane_locator_ip,
                    "transport": "service-locator:vxlan-gpe",
                    "service-function-forwarder": vnf.service_function_forwarder_name
                }
            ]
        }
        service_function_list.append(dic)
    return {
        "service-functions": {
            "service-function": service_function_list
        }
    }


def get_service_function_forwarders_uri():
    return "/restconf/config/service-function-forwarder:service-function-forwarders"


def get_service_function_forwarders_data(node_name, sff_name, data_plane_locator_ip, vnf_list, ovs_bridge_name="br-sfc",
                                         sff_data_plane_locator_name='eth1'):
    return {
        "service-function-forwarders": {
            "service-function-forwarder": [
                {
                    "name": sff_name,
                    "service-node": node_name,
                    "service-function-forwarder-ovs:ovs-bridge": {"bridge-name": ovs_bridge_name, },
                    "sff-data-plane-locator": [
                        {
                            "name": sff_data_plane_locator_name,
                            "data-plane-locator": {
                                "transport": "service-locator:vxlan-gpe",
                                "port": 6633,
                                "ip": data_plane_locator_ip
                            },
                            "service-function-forwarder-ovs:ovs-options": {
                                "remote-ip": "flow",
                                "dst-port": "6633",
                                "key": "flow",
                                "nsp": "flow",
                                "nsi": "flow",
                                "nshc1": "flow",
                                "nshc2": "flow",
                                "nshc3": "flow",
                                "nshc4": "flow"
                            }
                        }
                    ],
                    "service-function-dictionary": convert_vnf_list_to_sf_dic(vnf_list, sff_data_plane_locator_name),
                }
            ]
        }
    }


def convert_vnf_list_to_sf_dic(vnf_list, sff_data_plane_locator_name):
    res = []
    for vnf in vnf_list:
        name = vnf.name
        sf_dpl_name = vnf.sf_dpl_name
        dic = {
            "name": vnf.name,
            "sff-sf-data-plane-locator": {
                "sf-dpl-name": vnf.sf_dpl_name,
                "sff-dpl-name": sff_data_plane_locator_name
            }
        }
        res.append(dic)
    return res


def get_service_function_chains_uri():
    return "/restconf/config/service-function-chain:service-function-chains/"


def get_service_function_chains_data(sfc_list):
    service_function_chains = []
    for sfc in sfc_list:
        dic = {
            "name": sfc.name,
            "symmetric": sfc.isSymmetric,
            "sfc-service-function": sfc.vnf_list
        }
        service_function_chains.append(dic)
    return {
        "service-function-chains": {
            "service-function-chain": service_function_chains
        }
    }


def convert_vnf_list_to_sfc_service_function(vnf_list):
    res = []
    for index, vnf in vnf_list:
        dic = {
            "name": vnf.type + "-" + index,
            "type": vnf.type
        }
        res.append(dic)
    return res


def get_service_function_metadata_uri():
    return "/restconf/config/service-function-path-metadata:service-function-metadata/"


def get_service_function_metadata_data():
    return {
        "service-function-metadata": {
            "context-metadata": [
                {
                    "name": "NSH1",
                    "context-header1": "1",
                    "context-header2": "2",
                    "context-header3": "3",
                    "context-header4": "4"
                }
            ]
        }
    }


def get_service_function_paths_uri():
    return "/restconf/config/service-function-path:service-function-paths/"


def get_service_function_paths_data(sfp_list):
    service_function_path = []
    for sfp in sfp_list:
        dic = {
            "name": sfp.sfp_name,
            "service-chain-name": sfp.sfc_name,
            "classifier": sfp.in_classifier_name,
            "symmetric-classifier": sfp.out_classifier_name,
            "context-metadata": "NSH1",
            "symmetric": sfp.is_symmetric
        }
    service_function_path.append(dic)
    return {
        "service-function-paths": {
            "service-function-path": service_function_path
        }
    }


def get_service_function_acl_uri():
    return "/restconf/config/ietf-access-control-list:access-lists/"


def get_service_function_acl_data(acl_list):
    acls = []
    for acl in acl_list:
        aces=[]
        for ace in acl.ace_list:
            ace_dic = {
                "rule-name": ace.rule_name,
                "actions": {
                    "service-function-acl:rendered-service-path":ace.rsp_name
                },
                "matches": {
                    "destination-ipv4-network":ace.dst_ip,
                    "source-ipv4-network": ace.src_ip,
                    "protocol": ace.ip_protocol,
                    "source-port-range": {
                        "lower-port": ace.src_port_lower,
                        "upper-port": ace.src_port_upper
                    },
                    "destination-port-range": {
                        "lower-port":ace.dst_port_lower,
                        "upper-port": ace.dst_port_upper
                    }
                }
            }
            aces.append(ace_dic)
        dic = {
            "acl-name": acl.name,
            "access-list-entries": {
                "ace": aces
            }
        }
        acls.append(dic)
    return acls



def get_service_function_classifiers_uri():
    return "/restconf/config/service-function-classifier:service-function-classifiers/"


def get_service_function_classifiers_data(classifier_list):
    service_function_classifiers=[]
    for classifier in classifier_list:
        dic={
            "name": classifier.classifier,
            "scl-service-function-forwarder": [
                {
                    "name": classifier.sff_name,
                    "interface": classifier.sff_interface
                }
            ],
            "access-list": classifier.ace_name
        }
        service_function_classifiers.append(dic)
    return {
        "service-function-classifiers": {
            "service-function-classifier": service_function_classifiers
        }
    }


def get_rendered_service_path_uri():
    return "/restconf/operations/rendered-service-path:create-rendered-path/"


# nonoSchedule_123456_oriPathName
def get_rendered_service_path_data(rsp):
    return {
        "input": {
            "name": rsp.name,
            "parent-service-function-path": rsp.sfp,
            "symmetric": rsp.isSymmetric
        }
    }


