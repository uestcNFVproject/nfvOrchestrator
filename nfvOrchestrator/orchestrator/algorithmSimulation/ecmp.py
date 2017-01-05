#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/29 22:08
# @Author  : mengyuGuo
# @Site    : 
# @File    : ecmp.py
# @Software: PyCharm



import copy

def get_dijstra(lj_size,lj,dist_matrix,prev_maxtrix):
    for i in range(lj_size):
        dist = []
        prev = []
        finded = []
        for tmp in range(lj_size):
            dist.append(-1)
            prev.append(-1)
            finded.append(-1)
        src = i
        dist_matrix.append(dist)
        prev_maxtrix.append(prev)
        dist[src] = 0
        finded[src] = 1
        if i == 4:
            pass
        for time in range(lj_size - 1):
            for node_id in range(lj_size):
                if finded[node_id] == 1:
                    continue
                if lj[src][node_id] == 1:
                    if dist[node_id] == -1:
                        dist[node_id] = dist[src] + 1
                        prev[node_id] = src
                    else:
                        tmp = dist[src] + 1
                        if dist[node_id] > tmp:
                            dist[node_id] = tmp
                            prev[node_id] = src

            # 从未确定距离的点中，选一个距离最近的确定距离
            min_dist = 1000
            min_node_id = -1
            for tmp in range(lj_size):
                if finded[tmp] != 1:
                    if dist[tmp] != -1 and dist[tmp] < min_dist:
                        min_dist = dist[tmp]
                        min_node_id = tmp
            finded[min_node_id] = 1
            src = min_node_id
    for i in range(lj_size):
        print(dist_matrix[i])
        print(prev_maxtrix[i])

# 寻找等价多路径


def find_ecmp(src, dst, dist_matrix,lj_size,ecmp_dic):
    # print(str(src)+"==>"+str(dst))
    if str(src)+' '+str(dst) in ecmp_dic:
        return ecmp_dic[str(src)+' '+str(dst)]
    if src==0 and dst==4:
        pass

    path_list=[]
    dist=dist_matrix[src][dst]
    if dist==1:
        path_list.append([src,dst])

    for i in range(lj_size):
        if i==src or i==dst:
            continue
        if dist_matrix[i][dst]==1 and dist_matrix[src][i]==dist-1:
            src_i_ecmp_list=find_ecmp(src,i,dist_matrix,lj_size,ecmp_dic)
            for path in src_i_ecmp_list:
                # print(path)
                new_path=copy.copy(path)
                new_path.append(dst)
                path_list.append(new_path)
    return path_list


def get_ecmp(lj_size,lj):
    # lj_size = 6
    # lj = []
    # lj.append([1, 1, 1, 1, 0, 0])
    # lj.append([1, 1, 1, 1, 1, 0])
    # lj.append([1, 1, 0, 0, 1, 0])
    # lj.append([1, 1, 0, 0, 1, 0])
    # lj.append([0, 1, 1, 1, 0, 1])
    # lj.append([0, 0, 0, 0, 1, 0])
    dist_matrix = []
    prev_maxtrix = []
    get_dijstra(lj_size,lj,dist_matrix,prev_maxtrix)
    ecmp_dic={}
    for src in range(lj_size):
        for dst in range(lj_size):
            if src == dst:
                continue
            ecmp_list = find_ecmp(src, dst, dist_matrix,lj_size,ecmp_dic)
            # print([src,dst])
            # print(ecmp_list)
            ecmp_dic[str(src)+' '+str(dst)]=ecmp_list
    #
    # for src_dst in ecmp_dic:
    #     print(src_dst)
    #     print(ecmp_dic[src_dst])
    return ecmp_dic