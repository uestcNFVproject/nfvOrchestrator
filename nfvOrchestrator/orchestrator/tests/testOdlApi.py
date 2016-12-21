#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : testOdlApi.py
# @Software: PyCharm

from orchestrator.OpenDayLightApi import *
from  orchestrator.infoObjects import *
from django.test import TestCase


node0_ip = '192.168.1.204'
node1_ip = '192.168.1.208'
node2_ip = '192.168.1.211'
node3_ip = '192.168.1.215'
node4_ip = '192.168.1.214'
node5_ip = '192.168.1.210'
node0_url = "http://" + node0_ip + ":5000"
node1_url = "http://" + node1_ip + ":5000"
node2_url = "http://" + node2_ip + ":5000"
node3_url = "http://" + node3_ip + ":5000"
node4_url = "http://" + node4_ip + ":5000"
node5_url = "http://" + node5_ip + ":5000"
sf1_port = 10000
sf2_port = 10010
sf3_port = 10040

sff0_port = 10020
sff1_port = 10030
# sff2_port=10040
sff3_port = 10050
DEFAULT_PORT = '8181'

sf1_dpl_name = 'eth1'
sf2_dpl_name = 'eth1'
sf3_dpl_name = 'eth1'

sff0_dpl_name = 'eth1'
sff1_dpl_name = 'eth1'
# sff2_dpl_name='eth1'
sff3_dpl_name = 'eth1'

nodes_ip = [node0_ip, node1_ip, node2_ip, node3_ip, node4_ip, node5_ip]

vnf0 = vnfInfo(vm_name="dpi-1", vnf_name="dpi-1", ip_mgmt_address=node2_ip, rest_uri=node2_url,
                   sf_data_plane_locator_ip=node2_ip, type="dpi", service_function_forwarder_name="SFF1")
vnf1 = vnfInfo(vm_name="firewall-1", vnf_name="firewall-1", ip_mgmt_address=node3_ip, rest_uri=node3_url,
                   sf_data_plane_locator_ip=node3_ip, type="firewall", service_function_forwarder_name="SFF1")
vnf2 = vnfInfo(vm_name="firewall-2", vnf_name="firewall-2", ip_mgmt_address=node4_ip, rest_uri=node4_url,
                   sf_data_plane_locator_ip=node4_ip, type="firewall", service_function_forwarder_name="SFF1")
vnf_list = [vnf0, vnf1, vnf2]


sff0 = sffInfo(name="SFF0", node_name="node0", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                   data_plane_locator_ip=node0_ip, vnf_list=None)

sff1 = sffInfo(name="SFF1", node_name="node1", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                   data_plane_locator_ip=node1_ip, vnf_list=vnf_list)

sff2 = sffInfo(name="SFF3", node_name="node5", ovs_bridge_name="br-sfc", data_plane_locator_name="eth1",
                   data_plane_locator_ip=node5_ip, vnf_list=None)
sff_list = [sff0, sff1, sff2]

class myTest(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testNode(self):
        node_list = []
        sf_list_list=[None,None,[vnf0],[vnf1],[vnf2],None,None]
        for i in range(6):
            node = nodeInfo(name="node" + str(i), ip=nodes_ip[i],vnf_list=sf_list_list[i])
            node_list.append(node)
        res=get_service_nodes_data(node_list=node_list)
        expect={
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
                        "ip-mgmt-address": node5_ip
                    }
                ]
            }
        }
        self.assertEqual(res, expect)
    def testVnf(self):
        res = get_service_functions_data(vnf_list=vnf_list)
        expect = {
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
        self.assertEqual(res,expect)
    def testSff(self):
        res=get_service_function_forwarders_data(sff_list=sff_list)
        expect={
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
                        "service-function-forwarder-ovs:ovs-bridge": {"bridge-name": "br-sfc", },
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
        self.assertEqual(res,expect)

    def testSfc(self):
        sfc0_sf_list = [vnf0, vnf1]
        sfc1_sf_list = [vnf0, vnf2]
        sfc0 = sfcInfo(name="SFC1", isSymmetric="true", vnf_list=sfc0_sf_list)
        sfc1 = sfcInfo(name="SFC2", isSymmetric="true", vnf_list=sfc1_sf_list)
        sfc_list = [sfc0, sfc1]
        res=get_service_function_chains_data(sfc_list=sfc_list)
        expect={
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
        self.assertEqual(res,expect)

    def testSfMetaData(self):
        res=get_service_function_metadata_data()
        expect={
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
        self.assertEqual(res,expect)

    def testSfp(self):
        sfp0 = sfpInfo(sfp_name="SFP1", sfc_name="SFC1", classifier_name="Classifier1",
                       symmetric_classifier_name="Classifier2", is_symmetric="true")
        sfp1 = sfpInfo(sfp_name="SFP2", sfc_name="SFC2", classifier_name="Classifier3",
                       symmetric_classifier_name="Classifier4", is_symmetric="true")
        sfp_list = [sfp0, sfp1]
        res=get_service_function_paths_data(sfp_list=sfp_list)
        expect={
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
        self.assertEqual(res,expect)

    def testAcl(self):
        ace0 = aceInfo(rule_name="ACE1", rsp_name="nonoSchedule_1_RSP1", dst_ip="192.168.2.0/24",
                       src_ip="192.168.2.0/24",
                       ip_protocol="6", src_port_lower=0, src_port_upper=65535, dst_port_lower=80, dst_port_upper=80)
        acl0 = aclInfo(name="ACL1", ace_list=[ace0])

        ace1 = aceInfo(rule_name="ACE2", rsp_name="nonoSchedule_1_RSP1-Reverse", dst_ip="192.168.2.0/24",
                       src_ip="192.168.2.0/24",
                       ip_protocol="6", src_port_lower=80, src_port_upper=80, dst_port_lower=0, dst_port_upper=65535)
        acl1 = aclInfo(name="ACL2", ace_list=[ace1])

        ace2 = aceInfo(rule_name="ACE3", rsp_name="nonoSchedule_2_RSP2", dst_ip="192.168.2.0/24",
                       src_ip="192.168.2.0/24", ip_protocol="6", src_port_lower=0, src_port_upper=65535,
                       dst_port_lower=90,
                       dst_port_upper=90)
        acl2 = aclInfo(name="ACL3", ace_list=[ace2])

        ace3 = aceInfo(rule_name="ACE4", rsp_name="nonoSchedule_2_RSP2-Reverse", dst_ip="192.168.2.0/24",
                       src_ip="192.168.2.0/24", ip_protocol="6", src_port_lower=90, src_port_upper=90, dst_port_lower=0,
                       dst_port_upper=65535)
        acl3 = aclInfo(name="ACL4", ace_list=[ace3])

        acl_list = [acl0, acl1, acl2, acl3]
        res=get_service_function_acl_data(acl_list=acl_list)
        expect={
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
        self.assertEqual(res,expect)

    def testRsp(self):
        rsp0 = rspInfo(name="nonoSchedule_1_RSP1", sfp="SFP1", isSymmetric="true")
        res0=get_rendered_service_path_data(rsp=rsp0)
        expect0={
            "input": {
                # "name": "RSP1",
                "name": "nonoSchedule_1_RSP1",
                "parent-service-function-path": "SFP1",
                "symmetric": "true"
            }
        }
        self.assertEqual(res0,expect0)

        rsp1 = rspInfo(name="nonoSchedule_2_RSP2", sfp="SFP2", isSymmetric="true")
        res1 = get_rendered_service_path_data(rsp=rsp1)
        expect1 = {
            "input": {
                "name": "nonoSchedule_2_RSP2",
                "parent-service-function-path": "SFP2",
                "symmetric": "true"
            }
        }
        self.assertEqual(res1, expect1)

    def testClasdifier(self):
        classifier0 = classifierInfo(name="Classifier1", sff_name="SFF0", sff_interface="veth-br", ace_name="ACL1")
        classifier1 = classifierInfo(name="Classifier2", sff_name="SFF3", sff_interface="veth-br", ace_name="ACL2")
        classifier2 = classifierInfo(name="Classifier3", sff_name="SFF0", sff_interface="veth-br", ace_name="ACL3")
        classifier3 = classifierInfo(name="Classifier4", sff_name="SFF3", sff_interface="veth-br", ace_name="ACL4")
        classifier_list = [classifier0, classifier1, classifier2, classifier3]
        res=get_service_function_classifiers_data(classifier_list=classifier_list)
        expect={
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
        self.assertEqual(res,expect)

def testAll():

    # step1 node info
    node_list = []
    sf_list_list = [None, None, [vnf0], [vnf1], [vnf2], None, None]
    for i in range(6):
        node = nodeInfo(name="node" + str(i), ip=nodes_ip[i], vnf_list=sf_list_list[i])
        node_list.append(node)

    print("sending service nodes")
    register_nodes(node_list=node_list)

    # step2:vnf info

    print("sending service functions")
    register_vnfs(vnf_list=vnf_list)

    # step3:sff info

    print("sending service function forwarders")
    register_sffs(sff_list=sff_list)

    # step4:sfc info

    sfc0_sf_list = [vnf0, vnf1]
    sfc1_sf_list = [vnf0, vnf2]
    sfc0 = sfcInfo(name="SFC1", isSymmetric="true", vnf_list=sfc0_sf_list)
    sfc1 = sfcInfo(name="SFC2", isSymmetric="true", vnf_list=sfc1_sf_list)
    sfc_list = [sfc0, sfc1]
    print("sending service function chains")
    register_sfcs(sfc_list=sfc_list)


    # step5:sf metadata

    print("sending service function metadata")
    register_sf_metadata_data()


    # step6:sfp info
    sfp0 = sfpInfo(sfp_name="SFP1", sfc_name="SFC1", classifier_name="Classifier1",
                   symmetric_classifier_name="Classifier2", is_symmetric="true")
    sfp1 = sfpInfo(sfp_name="SFP2", sfc_name="SFC2", classifier_name="Classifier3",
                   symmetric_classifier_name="Classifier4", is_symmetric="true")
    sfp_list = [sfp0, sfp1]
    print("sending service function paths")
    register_sfps(sfp_list=sfp_list)


    # step7:ace info

    ace0 = aceInfo(rule_name="ACE1", rsp_name="nonoSchedule_1_RSP1", dst_ip="192.168.2.0/24", src_ip="192.168.2.0/24",
                   ip_protocol="6", src_port_lower=0, src_port_upper=65535, dst_port_lower=80, dst_port_upper=80)
    acl0 = aclInfo(name="ACL1", ace_list=[ace0])

    ace1 = aceInfo(rule_name="ACE2", rsp_name="nonoSchedule_1_RSP1-Reverse", dst_ip="192.168.2.0/24",
                   src_ip="192.168.2.0/24",
                   ip_protocol="6", src_port_lower=80, src_port_upper=80, dst_port_lower=0, dst_port_upper=65535)
    acl1 = aclInfo(name="ACL2", ace_list=[ace1])

    ace2 = aceInfo(rule_name="ACE3", rsp_name="nonoSchedule_2_RSP2", dst_ip="192.168.2.0/24",
                   src_ip="192.168.2.0/24", ip_protocol="6", src_port_lower=0, src_port_upper=65535, dst_port_lower=90,
                   dst_port_upper=90)
    acl2 = aclInfo(name="ACL3", ace_list=[ace2])

    ace3 = aceInfo(rule_name="ACE4", rsp_name="nonoSchedule_2_RSP2-Reverse", dst_ip="192.168.2.0/24",
                   src_ip="192.168.2.0/24", ip_protocol="6", src_port_lower=90, src_port_upper=90, dst_port_lower=0,
                   dst_port_upper=65535)
    acl3 = aclInfo(name="ACL4", ace_list=[ace3])

    acl_list = [acl0, acl1, acl2, acl3]
    print("sending service function acl")
    register_acls(acl_list=acl_list)

    # step8:rsp info
    rsp0 = rspInfo(name="nonoSchedule_1_RSP1", sfp="SFP1", isSymmetric="true")
    print("sending rendered service path0")
    register_rsp(rsp=rsp0)

    rsp1 = rspInfo(name="nonoSchedule_2_RSP2", sfp="SFP2", isSymmetric="true")
    print("sending rendered service path1")
    register_rsp(rsp=rsp1)

    # step9:classifier info
    classifier0=classifierInfo(name="Classifier1",sff_name="SFF0",sff_interface="veth-br",ace_name="ACL1")
    classifier1 = classifierInfo(name="Classifier2", sff_name="SFF3", sff_interface="veth-br", ace_name="ACL2")
    classifier2 = classifierInfo(name="Classifier3", sff_name="SFF30", sff_interface="veth-br", ace_name="ACL3")
    classifier3 = classifierInfo(name="Classifier4", sff_name="SFF3", sff_interface="veth-br", ace_name="ACL4")
    classifier_list=[classifier0,classifier1,classifier2,classifier3]
    print("sending service function classifiers")
    register_classifiers(classifier_list=classifier_list)
