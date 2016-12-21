#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : odl_demo_v1.py
# @Software: PyCharm


import argparse
import requests,json
from requests.auth import HTTPBasicAuth
from subprocess import call
import time
import sys
import os

# 6 node,2 classifier,4 sff,2 sf,1 sfc,1 sfp ,2 rsp,sdn network
# my-odl
controller='192.168.1.1'

node0_ip='192.168.1.204'
node1_ip='192.168.1.208'
node2_ip='192.168.1.211'
node3_ip='192.168.1.215'
node4_ip='192.168.1.214'
node5_ip='192.168.1.210'

node0_url="http://"+node0_ip+":5000"
node1_url="http://"+node1_ip+":5000"
node2_url="http://"+node2_ip+":5000"
node3_url="http://"+node3_ip+":5000"
node4_url="http://"+node4_ip+":5000"
node5_url="http://"+node5_ip+":5000"

sf1_port=10000
sf2_port=10010
sf3_port=10040

sff0_port=10020
sff1_port=10030
# sff2_port=10040
sff3_port=10050
DEFAULT_PORT='8181'

sf1_dpl_name='eth1'
sf2_dpl_name='eth1'
sf3_dpl_name='eth1'

sff0_dpl_name='eth1'
sff1_dpl_name='eth1'
# sff2_dpl_name='eth1'
sff3_dpl_name='eth1'

USERNAME='admin'
PASSWORD='admin'

def get(host, port, uri):
    url='http://'+host+":"+port+uri
    r = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    jsondata=json.loads(r.text)
    return jsondata

def put(host, port, uri, data, debug=False):
    '''Perform a PUT rest operation, using the URL and data provided'''

    url='http://'+host+":"+port+uri

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

    url='http://'+host+":"+port+uri
    headers = {'Content-type': 'application/yang.data+json',
               'Accept': 'application/yang.data+json'}
    if debug == True:
        print("POST %s" % url)
        print (json.dumps(data, indent=4, sort_keys=True))
    r = requests.post(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if debug == True:
        print (r.text)
    r.raise_for_status()
    time.sleep(5)

def get_service_nodes_uri():
    return "/restconf/config/service-node:service-nodes"

def get_service_nodes_data():
    return {
    "service-nodes": {
        "service-node": [
            {
                "name": "node0",
                "service-function": [
                ],
                "ip-mgmt-address": node0_ip
            },
            {
                "name": "node1",
                "service-function": [
                ],
                "ip-mgmt-address": node1_ip
            },
            {
                "name": "node2",
                "service-function": [
                    "dpi-1"
                ],
                "ip-mgmt-address": node2_ip
            },
            {
                "name": "node3",
                "service-function": [
                    "firewall-1"
                ],
                "ip-mgmt-address": node3_ip
            },
            {
                "name": "node4",
                "service-function": [
                    "firewall-2"
                ],
                "ip-mgmt-address": node4_ip
            },
            {
                "name": "node5",
                "service-function": [
                ],
                "ip-mgmt-address":node5_ip
            }
        ]
    }
}

def get_service_functions_uri():
    return "/restconf/config/service-function:service-functions"

def get_service_functions_data():
    return {
    "service-functions": {
        "service-function": [
           {
                "name": "dpi-1",
                "ip-mgmt-address": node2_ip,
                "rest-uri": node2_url,
                "type": "dpi",
                "nsh-aware": "true",
                "sf-data-plane-locator": [
                    {
                        "name": sf1_dpl_name,
                        "port": 6633,
                        "ip": node2_ip,
                        "transport": "service-locator:vxlan-gpe",
                        "service-function-forwarder": "SFF1"
                    }
                ]
            },
            {
                "name": "firewall-1",
                "ip-mgmt-address": node3_ip,
                "rest-uri": node3_url,
                "type": "firewall",
                "nsh-aware": "true",
                "sf-data-plane-locator": [
                    {
                        "name": sf2_dpl_name,
                        "port": 6633,
                        "ip": node3_ip,
                        "transport": "service-locator:vxlan-gpe",
                        "service-function-forwarder": "SFF1"
                    }
                ]
            },
            {
                "name": "firewall-2",
                "ip-mgmt-address": node4_ip,
                "rest-uri": node4_url,
                "type": "firewall",
                "nsh-aware": "true",
                "sf-data-plane-locator": [
                    {
                        "name": sf3_dpl_name,
                        "port": 6633,
                        "ip": node4_ip,
                        "transport": "service-locator:vxlan-gpe",
                        "service-function-forwarder": "SFF1"
                    }
                ]
            }
        ]
    }
}

def get_service_function_forwarders_uri():
    return "/restconf/config/service-function-forwarder:service-function-forwarders"

def get_service_function_forwarders_data():
    return {
    "service-function-forwarders": {
        "service-function-forwarder": [
           {
                "name": "SFF0",
                "service-node": "node0",
                "service-function-forwarder-ovs:ovs-bridge": {
                    "bridge-name": "br-sfc",
                },
                "sff-data-plane-locator": [
                    {
                        "name": sff0_dpl_name,
                        "data-plane-locator": {
                            "transport": "service-locator:vxlan-gpe",
                            "port": 6633,
                            "ip": node0_ip
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
            },
            {
                "name": "SFF1",
                "service-node": "node1",
                "service-function-forwarder-ovs:ovs-bridge": {"bridge-name": "br-sfc",},
                "sff-data-plane-locator": [
                    {
                        "name": sff1_dpl_name,
                        "data-plane-locator": {
                            "transport": "service-locator:vxlan-gpe",
                            "port": 6633,
                            "ip": node1_ip
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
                "service-function-dictionary": [
                    {
                        "name": "dpi-1",
                        "sff-sf-data-plane-locator": {
                             "sf-dpl-name": sf1_dpl_name,
                             "sff-dpl-name": sff1_dpl_name
                        }
                    },
                    {
                        "name": "firewall-1",
                        "sff-sf-data-plane-locator": {
                            "sf-dpl-name": sf2_dpl_name,
                            "sff-dpl-name": sff1_dpl_name
                        }
                    },
                    {
                        "name": "firewall-2",
                        "sff-sf-data-plane-locator": {
                            "sf-dpl-name": sf3_dpl_name,
                            "sff-dpl-name": sff1_dpl_name
                        }
                    }
                ],
            },
            # {
            #     "name": "SFF2",
            #     "service-node": "node4",
            #     "service-function-forwarder-ovs:ovs-bridge": {
            #         "bridge-name": "br-sfc",
            #     },
            #     "sff-data-plane-locator": [
            #         {
            #             "name": sff2_dpl_name,
            #             "data-plane-locator": {
            #                 "transport": "service-locator:vxlan-gpe",
            #                 "port": 6633,
            #                 "ip":node4_ip
            #             },
            #             "service-function-forwarder-ovs:ovs-options": {
            #                 "remote-ip": "flow",
            #                 "dst-port": "6633",
            #                 "key": "flow",
            #                 "nsp": "flow",
            #                 "nsi": "flow",
            #                 "nshc1": "flow",
            #                 "nshc2": "flow",
            #                 "nshc3": "flow",
            #                 "nshc4": "flow"
            #             }
            #         }
            #     ],
            #     "service-function-dictionary": [
            #
            #     ]
            # },
            {
                "name": "SFF3",
                "service-node": "node5",
                "service-function-forwarder-ovs:ovs-bridge": {
                    "bridge-name": "br-sfc",
                },
                "sff-data-plane-locator": [
                    {
                        "name": sff3_dpl_name,
                        "data-plane-locator": {
                            "transport": "service-locator:vxlan-gpe",
                            "port": 6633,
                            "ip": node5_ip
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
            }
        ]
    }
}

def get_service_function_chains_uri():
    return "/restconf/config/service-function-chain:service-function-chains/"

def get_service_function_chains_data():
    return {
    "service-function-chains": {
        "service-function-chain": [
            {
                "name": "SFC1",
                "symmetric": "true",
                "sfc-service-function": [
                    {
                        "name": "dpi-abstract1",
                        "type": "dpi"
                    },
                    {
                        "name": "firewall-abstract1",
                        "type": "firewall"
                    }
                ]
            },
            {
                "name": "SFC2",
                "symmetric": "true",
                "sfc-service-function": [
                    {
                        "name": "dpi-abstract1",
                        "type": "dpi"
                    },
                    {
                        "name": "firewall-abstract1",
                        "type": "firewall"
                    }
                ]
            }
        ]
    }
}
# def get_service_function_chains_data2():
#     return {
#     "service-function-chains": {
#         "service-function-chain": [
#             {
#                 "name": "SFC2",
#                 "symmetric": "true",
#                 "sfc-service-function": [
#                     {
#                         "name": "dpi-abstract1",
#                         "type": "dpi"
#                     },
#                     {
#                         "name": "firewall-abstract1",
#                         "type": "firewall"
#                     }
#                 ]
#             }
#         ]
#     }
# }

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

def get_service_function_paths_data():
    return {
  "service-function-paths": {
    "service-function-path": [
      {
        "name": "SFP1",
        "service-chain-name": "SFC1",
        "classifier": "Classifier1",
        "symmetric-classifier": "Classifier2",
        "context-metadata": "NSH1",
        "symmetric": "true"
      },
        {
            "name": "SFP2",
            "service-chain-name": "SFC2",
            "classifier": "Classifier3",
            "symmetric-classifier": "Classifier4",
            "context-metadata": "NSH1",
            "symmetric": "true"
        }
    ]
  }
}
# def get_service_function_paths_data2():
#     return {
#   "service-function-paths": {
#     "service-function-path": [
#       {
#         "name": "SFP2",
#         "service-chain-name": "SFC2",
#         "classifier": "Classifier3",
#         "symmetric-classifier": "Classifier4",
#         "context-metadata": "NSH1",
#         "symmetric": "true"
#       }
#     ]
#   }
# }

def get_rendered_service_path_uri():
    return "/restconf/operations/rendered-service-path:create-rendered-path/"
# nonoSchedule_123456_oriPathName
def get_rendered_service_path_data():
    return {
    "input": {
        # "name": "RSP1",
        "name": "nonoSchedule_1_RSP1",
        "parent-service-function-path": "SFP1",
        "symmetric": "true"
    }
}
def get_rendered_service_path_data2():
    return {
    "input": {
        "name": "nonoSchedule_2_RSP2",
        "parent-service-function-path": "SFP2",
        "symmetric": "true"
    }
}

def get_service_function_acl_uri():
    return "/restconf/config/ietf-access-control-list:access-lists/"

def get_service_function_acl_data():
    return  {
  "access-lists": {
    "acl": [
      {
        "acl-name": "ACL1",
        "access-list-entries": {
          "ace": [
            {
              "rule-name": "ACE1",
              "actions": {
                "service-function-acl:rendered-service-path": "nonoSchedule_1_RSP1"
              },
              "matches": {
                "destination-ipv4-network": "192.168.2.0/24",
                "source-ipv4-network": "192.168.2.0/24",
                "protocol": "6",
                "source-port-range": {
                    "lower-port": 0,
                    "upper-port": 65535
                },
                "destination-port-range": {
                    "lower-port": 80,
                    "upper-port": 80
                }
              }
            }
          ]
        }
      },
      {
        "acl-name": "ACL2",
        "access-list-entries": {
          "ace": [
            {
              "rule-name": "ACE2",
              "actions": {
                "service-function-acl:rendered-service-path": "nonoSchedule_1_RSP1-Reverse"
              },
              "matches": {
                "destination-ipv4-network": "192.168.2.0/24",
                "source-ipv4-network": "192.168.2.0/24",
                "protocol": "6",
                "source-port-range": {
                    "lower-port": 80,
                    "upper-port": 80
                },
                "destination-port-range": {
                    "lower-port": 0,
                    "upper-port": 65535
                }
              }
            }
          ]
        }
      },
        {
            "acl-name": "ACL3",
            "access-list-entries": {
                "ace": [
                    {
                        "rule-name": "ACE3",
                        "actions": {
                            "service-function-acl:rendered-service-path": "nonoSchedule_2_RSP2"
                        },
                        "matches": {
                            "destination-ipv4-network": "192.168.2.0/24",
                            "source-ipv4-network": "192.168.2.0/24",
                            "protocol": "6",
                            "source-port-range": {
                                "lower-port": 0,
                                "upper-port": 65535
                            },
                            "destination-port-range": {
                                "lower-port": 90,
                                "upper-port": 90
                            }
                        }
                    }
                ]
            }
        },
        {
            "acl-name": "ACL4",
            "access-list-entries": {
                "ace": [
                    {
                        "rule-name": "ACE4",
                        "actions": {
                            "service-function-acl:rendered-service-path": "nonoSchedule_2_RSP2-Reverse"
                        },
                        "matches": {
                            "destination-ipv4-network": "192.168.2.0/24",
                            "source-ipv4-network": "192.168.2.0/24",
                            "protocol": "6",
                            "source-port-range": {
                                "lower-port": 90,
                                "upper-port": 90
                            },
                            "destination-port-range": {
                                "lower-port": 0,
                                "upper-port": 65535
                            }
                        }
                    }
                ]
            }
        }
    ]
  }
}
# def get_service_function_acl_data2():
#     return  {
#   "access-lists": {
#     "acl": [
#       {
#         "acl-name": "ACL3",
#         "access-list-entries": {
#           "ace": [
#             {
#               "rule-name": "ACE3",
#               "actions": {
#                 "service-function-acl:rendered-service-path": "RSP2"
#               },
#               "matches": {
#                 "destination-ipv4-network": "192.168.2.0/24",
#                 "source-ipv4-network": "192.168.2.0/24",
#                 "protocol": "6",
#                 "source-port-range": {
#                     "lower-port": 0,
#                     "upper-port": 65535
#                 },
#                 "destination-port-range": {
#                     "lower-port": 90,
#                     "upper-port": 90
#                 }
#               }
#             }
#           ]
#         }
#       },
#       {
#         "acl-name": "ACL4",
#         "access-list-entries": {
#           "ace": [
#             {
#               "rule-name": "ACE4",
#               "actions": {
#                 "service-function-acl:rendered-service-path": "RSP2-Reverse"
#               },
#               "matches": {
#                 "destination-ipv4-network": "192.168.2.0/24",
#                 "source-ipv4-network": "192.168.2.0/24",
#                 "protocol": "6",
#                 "source-port-range": {
#                     "lower-port": 90,
#                     "upper-port": 90
#                 },
#                 "destination-port-range": {
#                     "lower-port": 0,
#                     "upper-port": 65535
#                 }
#               }
#             }
#           ]
#         }
#       }
#     ]
#   }
# }
def get_service_function_classifiers_uri():
    return "/restconf/config/service-function-classifier:service-function-classifiers/"

def get_service_function_classifiers_data():
    return  {
  "service-function-classifiers": {
    "service-function-classifier": [
      {
        "name": "Classifier1",
        "scl-service-function-forwarder": [
          {
            "name": "SFF0",
            "interface": "veth-br"
          }
        ],
        "access-list": "ACL1"
      },
      {
        "name": "Classifier2",
        "scl-service-function-forwarder": [
          {
            "name": "SFF3",
            "interface": "veth-br"
          }
        ],
        "access-list": "ACL2"
      },
        {
            "name": "Classifier3",
            "scl-service-function-forwarder": [
                {
                    "name": "SFF0",
                    "interface": "veth-br"
                }
            ],
            "access-list": "ACL3"
        },
        {
            "name": "Classifier4",
            "scl-service-function-forwarder": [
                {
                    "name": "SFF3",
                    "interface": "veth-br"
                }
            ],
            "access-list": "ACL4"
        }
    ]
  }
}
# def get_service_function_classifiers_data2():
#     return  {
#   "service-function-classifiers": {
#     "service-function-classifier": [
#       {
#         "name": "Classifier3",
#         "scl-service-function-forwarder": [
#           {
#             "name": "SFF0",
#             "interface": "veth-br"
#           }
#         ],
#         "access-list": "ACL3"
#       },
#       {
#         "name": "Classifier4",
#         "scl-service-function-forwarder": [
#           {
#             "name": "SFF3",
#             "interface": "veth-br"
#           }
#         ],
#         "access-list": "ACL4"
#       }
#     ]
#   }
# }
if __name__ == "__main__":

    print ("sending service nodes")
    put(controller, DEFAULT_PORT, get_service_nodes_uri(), get_service_nodes_data(), True)
    print ("sending service functions")
    put(controller, DEFAULT_PORT, get_service_functions_uri(), get_service_functions_data(), True)
    print ("sending service function forwarders")
    put(controller, DEFAULT_PORT, get_service_function_forwarders_uri(), get_service_function_forwarders_data(), True)
    # sfc0
    print ("sending service function chains")
    put(controller, DEFAULT_PORT, get_service_function_chains_uri(), get_service_function_chains_data(), True)
    print ("sending service function metadata")
    put(controller, DEFAULT_PORT, get_service_function_metadata_uri(), get_service_function_metadata_data(), True)
    print ("sending service function paths")
    put(controller, DEFAULT_PORT, get_service_function_paths_uri(), get_service_function_paths_data(), True)
    print ("sending service function acl")
    put(controller, DEFAULT_PORT, get_service_function_acl_uri(), get_service_function_acl_data(), True)
    print ("sending rendered service path")
    post(controller, DEFAULT_PORT, get_rendered_service_path_uri(), get_rendered_service_path_data(), True)
    print ("sending rendered service path2")
    post(controller, DEFAULT_PORT, get_rendered_service_path_uri(), get_rendered_service_path_data2(), True)
    print ("sending service function classifiers")
    put(controller, DEFAULT_PORT, get_service_function_classifiers_uri(), get_service_function_classifiers_data(), True)


