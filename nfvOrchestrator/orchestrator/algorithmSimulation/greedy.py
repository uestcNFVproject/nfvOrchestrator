#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-28 19:30
# @Author  : mengyuGuo
# @Site    :
# @File    : greedy.py
# @Software: PyCharm
from queue import PriorityQueue

from nfvOrchestrator.orchestrator.algorithmSimulation.common import *
from nfvOrchestrator.orchestrator.algorithmSimulation.node import Node
from nfvOrchestrator.orchestrator.algorithmSimulation.node import NoedType
from nfvOrchestrator.orchestrator.algorithmSimulation.pod import Pod
from nfvOrchestrator.orchestrator.algorithmSimulation.link import Link
from nfvOrchestrator.orchestrator.algorithmSimulation.topo import Topo
from nfvOrchestrator.orchestrator.algorithmSimulation.sfc import Sfc
from nfvOrchestrator.orchestrator.algorithmSimulation.sf import Sf
from nfvOrchestrator.orchestrator.algorithmSimulation.sf import SfType
from nfvOrchestrator.orchestrator.algorithmSimulation import ecmp
global pod_num
global next_id
global lj
pod_num = 4
next_id = 0
lj = []


# global next_id



def generate_id():
    next_id += 1
    return next_id - 1


def get_tempery_max_id():
    return next_id - 1


def init_topo():
    topo = Topo(pod_num=pod_num)

    # create core switch
    core_switch_num = pod_num
    for i in range(core_switch_num):
        core_switch = Node(id=generate_id(), type=NoedType['core_switch'], node_capacity=None, pod=None)
        topo.core_switch_list.append(core_switch)

    # create pod
    for i in range(core_switch_num):
        pod = Pod(id=generate_id())
        topo.pod_list.append(pod)

    # create agg_switch
    agg_switch_num = pod_num / 2
    for pod in topo.pod_list:
        for i in range(agg_switch_num):
            agg_switch = Node(id=generate_id(), type=NoedType['agg_switch'], node_capacity=0, pod=pod)
            topo.agg_switch_list.append(agg_switch)

    # create edge_switch
    edge_switch_num = pod_num / 2
    for pod in topo.pod_list:
        for i in range(edge_switch_num):
            edge_switch = Node(id=generate_id(), type=NoedType['edge_switch'], node_capacity=0, pod=pod)
            topo.edge_switch_list.append(edge_switch)

    # create compute_node
    compute_node_num = pod_num / 2
    for pod in topo.pod_list:
        for i in range(compute_node_num):
            compute_node = Node(id=generate_id(), type=NoedType['compute_node'],
                                node_capacity=common_compute_node_capacity, pod=pod)
            topo.compute_node_list.append(compute_node)

    # create link between core switch and agg switch
    for i in range(core_switch_num):
        core_switch = topo.core_switch_list[i]
        for pod in topo.pod_list:
            agg_switch_list = pod.agg_switch_lis
            agg_switch_index = i / 2
            agg_switch = agg_switch_list[agg_switch_index]
            link = Link(id=generate_id(), src_node=core_switch, dst_node=agg_switch,
                        bandwith_capacity=common_link_node_bandwith)
            topo.level1_link_list.append(link)
            core_switch.add_link(link)
            agg_switch.add_link(link)

    # create link between  agg switch and edge switch
    for pod in topo.pod_list:
        for agg_switch in pod.agg_switch_lis:
            for edge_switch in pod.edge_switch_list:
                link = Link(id=generate_id(), src_node=agg_switch, dst_node=edge_switch,
                            bandwith_capacity=common_link_node_bandwith)
                topo.level2_link_list.append(link)
                agg_switch.add_link(link)
                edge_switch.add_link(link)

    # create link between  agg switch and edge switch
    for pod in topo.pod_list:
        for i in range(edge_switch_num):
            edge_switch = pod.edge_switch_list[i]
            compute_node_start_index = i * edge_switch_num
            compute_node_end_index = compute_node_start_index + edge_switch_num
            for compute_node_index in range(compute_node_start_index, compute_node_end_index):
                compute_node = pod.compute_node_list[compute_node_index]
                link = Link(id=generate_id(), src_node=edge_switch, dst_node=compute_node,
                            bandwith_capacity=common_link_node_bandwith)
                topo.level3_link_list.append(link)
                compute_node.add_link(link)
                edge_switch.add_link(link)
    # change topo to lj[][]
    lj_size = get_tempery_max_id()
    for i in range(lj_size):
        arr = []
        for j in range(lj_size):
            arr.append(0)
        lj.append(arr)

    for link in topo.level1_link_list:
        lj[link.src_node.id][link.dst_node.id] = 1
        lj[link.dst_node.id][link.src_node.id] = 1

    for link in topo.level2_link_list:
        lj[link.src_node.id][link.dst_node.id] = 1
        lj[link.dst_node.id][link.src_node.id] = 1

    for link in topo.level3_link_list:
        lj[link.src_node.id][link.dst_node.id] = 1
        lj[link.dst_node.id][link.src_node.id] = 1

    # find all ecmp paths between nodes
    ecmp_dic=ecmp.get_ecmp(lj_size,lj)
    topo.ecmp_dic=ecmp_dic
    return topo


def create_common_sfc_demand(sfc_num, sfc_length):
    sfc_list = []
    type_list = ['firewall', 'dpi', 'ids']
    for i in range(sfc_num):
        sfc = Sfc(id=generate_id())
        for i in range(sfc_length):
            sf = Sf(id=generate_id(), weight=common_sf_weight, type=SfType(type_list[i]))
            sfc.append_sf(sf=sf)
    return sfc_list


def compute_solution_for_single_sfc(topo, sfc):
    # example for simplest greedy,find the lightest load  computed node
    # 先选sf，最后选inclassifier和outclassifier
    solution = []
    pq = PriorityQueue(pod_num * pod_num * pod_num / 4)
    for compute_node in topo.compute_node_list:
        pq.put(compute_node)
    last_sf = None
    node_list = []
    for sf in sfc:
        lightest_node = pq.get_nowait()
        lightest_node.add_sf(sf)
        node_list.append(lightest_node)
        # 改变链路状态
        path = path

    pass


def solve(topo, sfc_list):
    solution_list = []
    for sfc in sfc_list:
        solution = compute_solution_for_single_sfc(topo, sfc)
        solution_list.append(solution)
    return solution_list


if __name__ == '__main__':
    topo = init_topo()
    sfc_list = create_common_sfc_demand()
    solution = solve(topo, sfc_list)
