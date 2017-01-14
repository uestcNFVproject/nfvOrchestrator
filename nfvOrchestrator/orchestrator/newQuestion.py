#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/5 23:07
# @Author  : mengyuGuo
# @Site    : 
# @File    : newQuestion.py
# @Software: PyCharm
import random
import copy
import logging
import queue

logging.basicConfig(level=logging.INFO,
                    format='[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='data.log',
                    filemode='w')
# sf_sets = [1, 2, 3, 4, 5, 6]
sf_type_lowest = 4
sf_type_highest = 8

sfw_lowest = 1
sfw_highest = 1
sfc_length_lowest = 2
sfc_length_highest = 4

sfc_num_lowest = 5
sfc_num_highest = 10


def create_sfc_set():
    sfc_sets = [[]]
    sfc_num = random.randint(sfc_num_lowest, sfc_num_highest)
    index = 1
    for i in range(sfc_num):
        sfc_length = random.randint(sfc_length_lowest, sfc_length_highest)
        sf_list = []
        sfw_list = []
        for j in range(sfc_length):
            sf_type = random.randint(sf_type_lowest, sf_type_highest)
            sfw = random.randint(sfw_lowest, sfw_highest)
            sf_list.append(sf_type)
            sfw_list.append(sfw)
        sfc = []
        # 0=>sf list
        sfc.append(sf_list)
        # 1=>sf weight list
        sfc.append(sfw_list)
        # 2=>sf time dic
        sf_time_count_dic = {}
        for sf in sf_list:
            if sf not in sf_time_count_dic:
                sf_time_count_dic[sf] = 1
            else:
                sf_time_count_dic[sf] += 1
        sfc.append(sf_time_count_dic)
        # 3=>sfc index
        sfc.append(index)
        index += 1
        sfc_sets.append(sfc)
    return sfc_sets


def creat_sfc_set_static():
    sfc_sets = [[]]
    sfc1_sf_list = [1, 2]
    sfc1_sfw_list = [1, 1]

    sfc2_sf_list = [1, 3]
    sfc2_sfw_list = [1, 1]

    sfc3_sf_list = [3, 1]
    sfc3_sfw_list = [1, 1]

    sfc_sf_list = [sfc1_sf_list, sfc2_sf_list, sfc3_sf_list]
    sfc_sfw_list = [sfc1_sfw_list, sfc2_sfw_list, sfc3_sfw_list]

    for i in range(3):
        sfc = []
        # 0=>sf list
        sfc.append(sfc_sf_list[i])
        # 1=>sf weight list
        sfc.append(sfc_sfw_list[i])
        # 2=>sf time dic
        sf_time_count_dic = {}
        for sf in sfc_sf_list[i]:
            if sf not in sf_time_count_dic:
                sf_time_count_dic[sf] = 1
            else:
                sf_time_count_dic[sf] += 1
        sfc.append(sf_time_count_dic)
        # 3=>sfc index
        sfc.append(i + 1)
        sfc_sets.append(sfc)
    return sfc_sets


def creat_sfc_set_static2():
    # sf_sets 1=>6
    # 10 sfc
    sfc_sets = [[]]
    sfc1_sf_list = [1, 3, 5]
    sfc1_sfw_list = [1, 1, 1]

    sfc2_sf_list = [1, 2, 6]
    sfc2_sfw_list = [1, 1, 1]

    sfc3_sf_list = [6, 2]
    sfc3_sfw_list = [1, 1]

    sfc4_sf_list = [1, 4]
    sfc4_sfw_list = [1, 1]

    sfc5_sf_list = [1, 2, 4, 5]
    sfc5_sfw_list = [1, 1, 1, 1]

    sfc6_sf_list = [6, 2, 1, 5]
    sfc6_sfw_list = [1, 1, 1, 1]

    sfc7_sf_list = [2, 4, 6, 3]
    sfc7_sfw_list = [1, 1, 1, 1]

    sfc8_sf_list = [2, 5, 3]
    sfc8_sfw_list = [1, 1, 1]

    sfc9_sf_list = [5, 2]
    sfc9_sfw_list = [1, 1]

    sfc_sf_list = [sfc1_sf_list, sfc2_sf_list, sfc3_sf_list, sfc4_sf_list, sfc5_sf_list, sfc6_sf_list, sfc7_sf_list,
                   sfc8_sf_list, sfc9_sf_list]
    sfc_sfw_list = [sfc1_sfw_list, sfc2_sfw_list, sfc3_sfw_list, sfc4_sfw_list, sfc5_sfw_list, sfc6_sfw_list,
                    sfc7_sfw_list
        , sfc8_sfw_list, sfc9_sfw_list]

    for i in range(len(sfc_sf_list)):
        sfc = []
        # 0=>sf list
        sfc.append(sfc_sf_list[i])
        # 1=>sf weight list
        sfc.append(sfc_sfw_list[i])
        # 2=>sf time dic
        sf_time_count_dic = {}
        for sf in sfc_sf_list[i]:
            if sf not in sf_time_count_dic:
                sf_time_count_dic[sf] = 1
            else:
                sf_time_count_dic[sf] += 1
        sfc.append(sf_time_count_dic)
        # 3=>sfc index
        sfc.append(i + 1)
        sfc_sets.append(sfc)
    return sfc_sets


def creat_sfc_set_static3():
    # sf_sets 1=>6
    # 10 sfc
    sfc_sets = [[]]
    sfc1_sf_list = [1, 3, 5]
    sfc1_sfw_list = [2, 1, 1]

    sfc2_sf_list = [1, 2, 6]
    sfc2_sfw_list = [2, 1, 1]

    sfc3_sf_list = [6, 2]
    sfc3_sfw_list = [1, 1]

    sfc4_sf_list = [1, 4]
    sfc4_sfw_list = [2, 1]

    sfc5_sf_list = [1, 2, 4, 5]
    sfc5_sfw_list = [1, 2, 2, 1]

    sfc6_sf_list = [6, 2, 1, 5]
    sfc6_sfw_list = [2, 2, 1, 2]

    sfc7_sf_list = [2, 4, 6, 3]
    sfc7_sfw_list = [2, 2, 2, 1]

    sfc8_sf_list = [5, 3]
    sfc8_sfw_list = [1, 1]

    sfc9_sf_list = [5, 2]
    sfc9_sfw_list = [2, 2]

    sfc_sf_list = [sfc1_sf_list, sfc2_sf_list, sfc3_sf_list, sfc4_sf_list, sfc5_sf_list, sfc6_sf_list, sfc7_sf_list,
                   sfc8_sf_list, sfc9_sf_list]
    sfc_sfw_list = [sfc1_sfw_list, sfc2_sfw_list, sfc3_sfw_list, sfc4_sfw_list, sfc5_sfw_list, sfc6_sfw_list,
                    sfc7_sfw_list
        , sfc8_sfw_list, sfc9_sfw_list]

    for i in range(len(sfc_sf_list)):
        sfc = []
        # 0=>sf list
        sfc.append(sfc_sf_list[i])
        # 1=>sf weight list
        sfc.append(sfc_sfw_list[i])
        # 2=>sf time dic
        sf_time_count_dic = {}
        for sf in sfc_sf_list[i]:
            if sf not in sf_time_count_dic:
                sf_time_count_dic[sf] = 1
            else:
                sf_time_count_dic[sf] += 1
        sfc.append(sf_time_count_dic)
        # 3=>sfc index
        sfc.append(i + 1)
        sfc_sets.append(sfc)
    return sfc_sets


half_random_sfw_low = 1
half_random_sfw_hight = 2


def creat_sfc_set_half_random():
    # sf_sets 1=>6
    # 10 sfc
    sfc_sets = [[]]
    sfc1_sf_list = [1, 3, 5]
    sfc1_sfw_list = []
    for index in range(len(sfc1_sf_list)):
        sfc1_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc2_sf_list = [1, 2, 6]
    sfc2_sfw_list = []
    for index in range(len(sfc2_sf_list)):
        sfc2_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc3_sf_list = [6, 2]
    sfc3_sfw_list = []
    for index in range(len(sfc3_sf_list)):
        sfc3_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc4_sf_list = [1, 4]
    sfc4_sfw_list = []
    for index in range(len(sfc4_sf_list)):
        sfc4_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc5_sf_list = [1, 2, 4, 5]
    sfc5_sfw_list = []
    for index in range(len(sfc5_sf_list)):
        sfc5_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc6_sf_list = [6, 2, 1, 5]
    sfc6_sfw_list = []
    for index in range(len(sfc6_sf_list)):
        sfc6_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc7_sf_list = [2, 4, 6, 3]
    sfc7_sfw_list = []
    for index in range(len(sfc7_sf_list)):
        sfc7_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc8_sf_list = [5, 3]
    sfc8_sfw_list = []
    for index in range(len(sfc8_sf_list)):
        sfc8_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc9_sf_list = [5, 2]
    sfc9_sfw_list = []
    for index in range(len(sfc9_sf_list)):
        sfc9_sfw_list.append(random.randint(half_random_sfw_low, half_random_sfw_hight))

    sfc_sf_list = [sfc1_sf_list, sfc2_sf_list, sfc3_sf_list, sfc4_sf_list, sfc5_sf_list, sfc6_sf_list, sfc7_sf_list,
                   sfc8_sf_list, sfc9_sf_list]
    sfc_sfw_list = [sfc1_sfw_list, sfc2_sfw_list, sfc3_sfw_list, sfc4_sfw_list, sfc5_sfw_list, sfc6_sfw_list,
                    sfc7_sfw_list
        , sfc8_sfw_list, sfc9_sfw_list]

    for i in range(len(sfc_sf_list)):
        sfc = []
        # 0=>sf list
        sfc.append(sfc_sf_list[i])
        # 1=>sf weight list
        sfc.append(sfc_sfw_list[i])
        # 2=>sf time dic
        sf_time_count_dic = {}
        for sf in sfc_sf_list[i]:
            if sf not in sf_time_count_dic:
                sf_time_count_dic[sf] = 1
            else:
                sf_time_count_dic[sf] += 1
        sfc.append(sf_time_count_dic)
        # 3=>sfc index
        sfc.append(i + 1)
        sfc_sets.append(sfc)
    return sfc_sets


sfi_num_lowest = 2
sfi_num_highest = 4
sfi_capacity_lowest = 20
sfi_capacity_highest = 120
relative_sfc_num_lower = 1


def create_sfi_set(sfc_sets):
    sfi_sets = [[]]
    sf_type_relative_sfc_dic = {}
    for i in range(sf_type_highest):
        sf_type = i + 1
        relative_sfc_set = []
        for sfc in sfc_sets:
            if sfc == []:
                continue
            if sf_type in sfc[0]:
                relative_sfc_set.append(sfc[3])

        sf_type_relative_sfc_dic[sf_type] = relative_sfc_set
    index = 1
    for i in range(sf_type_highest):
        sf_type = i + 1
        sfi_num = random.randint(sfi_num_lowest, sfi_num_highest)
        for num in range(sfi_num):
            sfi_capacity = random.randint(sfi_capacity_lowest, sfi_capacity_highest)
            relative_sfc_set = sf_type_relative_sfc_dic[sf_type]
            if len(relative_sfc_set) == 0 or len(relative_sfc_set) == 1:
                relative_sfc_num = len(relative_sfc_set)
            else:
                relative_sfc_num = random.randint(relative_sfc_num_lower, len(relative_sfc_set))
            sfc_set = []
            for j in range(relative_sfc_num):
                relative_sfc_index = random.randint(0, len(relative_sfc_set) - 1)
                sfc_index = relative_sfc_set[relative_sfc_index]
                while sfc_index in sfc_set:
                    relative_sfc_index = random.randint(0, len(relative_sfc_set) - 1)
                    sfc_index = relative_sfc_set[relative_sfc_index]
                sfc_set.append(sfc_index)
            sfi = []
            sfi_type = sf_type
            sfi.append(sfi_type)
            # 1=>capacity
            sfi.append(sfi_capacity)
            # 2=>load
            sfi_load = 0
            sfi.append(sfi_load)
            # 3=>sfc set
            sfi_sfc_sets = sfc_set
            sfi.append(sfi_sfc_sets)
            # 4=>index
            sfi.append(index)
            index += 1
            # 5=>be_sets
            sfi.append([])
            sfi_sets.append(sfi)
    return sfi_sets


def create_sfi_set_static():
    sfi_sets = [[]]
    sfi_type_list = [1, 1, 1, 1, 2, 3, 3]
    sfi_capacity_list = [10, 10, 10, 10, 10, 10, 10]

    sfi1_1_sfc_set = [1, 2]
    sfi1_2_sfc_set = [1, 3]
    sfi1_3_sfc_set = [2]
    sfi1_4_sfc_set = [2]

    sfi2_1_sfc_set = [1]

    sfi3_1_sfc_set = [2, 3]
    sfi3_2_sfc_set = [2]

    sfi_sfc_set_list = [sfi1_1_sfc_set, sfi1_2_sfc_set, sfi1_3_sfc_set, sfi1_4_sfc_set, sfi2_1_sfc_set, sfi3_1_sfc_set,
                        sfi3_2_sfc_set]

    for i in range(7):
        # add a sfi to sfi_sets
        sfi = []
        # 0=> type
        sfi_type = sfi_type_list[i]
        sfi.append(sfi_type)
        # 1=>capacity
        sfi_capacity = sfi_capacity_list[i]
        sfi.append(sfi_capacity)
        # 2=>load
        sfi_load = 0
        sfi.append(sfi_load)
        # 3=>sfc set
        sfi_sfc_sets = sfi_sfc_set_list[i]
        sfi.append(sfi_sfc_sets)
        # 4=>index
        sfi.append(i + 1)
        # 5=>be_sets
        sfi.append([])
        sfi_sets.append(sfi)
    return sfi_sets


def create_sfi_set_static2():
    sfi_sets = [[]]
    sfi_type_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    sfi_capacity_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    sfi1_1_sfc_set = [1, 2, 6]
    sfi1_2_sfc_set = [1, 4]
    sfi1_3_sfc_set = [4, 5, 6]
    sfi1_4_sfc_set = [2, 5]

    sfi2_1_sfc_set = [2, 5, 6]
    sfi2_2_sfc_set = [3, 6, 8]
    sfi2_3_sfc_set = [7, 9]
    sfi2_4_sfc_set = [3, 5]

    sfi3_1_sfc_set = [1, 7]
    sfi3_2_sfc_set = [8]

    sfi4_1_sfc_set = [4, 5]
    sfi4_2_sfc_set = [5, 7]

    sfi5_1_sfc_set = [1, 6, 9]
    sfi5_2_sfc_set = [5, 8, 9]

    sfi6_1_sfc_set = [2, 3, 6]
    sfi6_2_sfc_set = [3, 7]

    sfi_sfc_set_list = [sfi1_1_sfc_set, sfi1_2_sfc_set, sfi1_3_sfc_set, sfi1_4_sfc_set,
                        sfi2_1_sfc_set, sfi2_2_sfc_set, sfi2_3_sfc_set, sfi2_4_sfc_set,
                        sfi3_1_sfc_set, sfi3_2_sfc_set,
                        sfi4_1_sfc_set, sfi4_2_sfc_set,
                        sfi5_1_sfc_set, sfi5_2_sfc_set,
                        sfi6_1_sfc_set, sfi6_2_sfc_set
                        ]

    for i in range(len(sfi_sfc_set_list)):
        # add a sfi to sfi_sets
        sfi = []
        # 0=> type
        sfi_type = sfi_type_list[i]
        sfi.append(sfi_type)
        # 1=>capacity
        sfi_capacity = sfi_capacity_list[i]
        sfi.append(sfi_capacity)
        # 2=>load
        sfi_load = 0
        sfi.append(sfi_load)
        # 3=>sfc set
        sfi_sfc_sets = sfi_sfc_set_list[i]
        sfi.append(sfi_sfc_sets)
        # 4=>index
        sfi.append(i + 1)
        # 5=>be array
        sfi.append([])
        sfi_sets.append(sfi)
    return sfi_sets


def create_sfi_set_static3():
    sfi_sets = [[]]
    sfi_type_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    sfi_capacity_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    sfi1_1_sfc_set = [1, 2, 6]
    sfi1_2_sfc_set = [1, 4]
    sfi1_3_sfc_set = [4, 5, 6]
    sfi1_4_sfc_set = [2, 5]

    sfi2_1_sfc_set = [2, 5, 6]
    sfi2_2_sfc_set = [3, 6, 8]
    sfi2_3_sfc_set = [7, 9]
    sfi2_4_sfc_set = [3, 5]

    sfi3_1_sfc_set = [1, 7]
    sfi3_2_sfc_set = [8]

    sfi4_1_sfc_set = [4, 5]
    sfi4_2_sfc_set = [5, 7]

    sfi5_1_sfc_set = [1, 6, 9]
    sfi5_2_sfc_set = [5, 8, 9]

    sfi6_1_sfc_set = [2, 3, 6]
    sfi6_2_sfc_set = [3, 7]

    sfi_sfc_set_list = [sfi1_1_sfc_set, sfi1_2_sfc_set, sfi1_3_sfc_set, sfi1_4_sfc_set,
                        sfi2_1_sfc_set, sfi2_2_sfc_set, sfi2_3_sfc_set, sfi2_4_sfc_set,
                        sfi3_1_sfc_set, sfi3_2_sfc_set,
                        sfi4_1_sfc_set, sfi4_2_sfc_set,
                        sfi5_1_sfc_set, sfi5_2_sfc_set,
                        sfi6_1_sfc_set, sfi6_2_sfc_set
                        ]

    for i in range(len(sfi_sfc_set_list)):
        # add a sfi to sfi_sets
        sfi = []
        # 0=> type
        sfi_type = sfi_type_list[i]
        sfi.append(sfi_type)
        # 1=>capacity
        sfi_capacity = sfi_capacity_list[i]
        sfi.append(sfi_capacity)
        # 2=>load
        sfi_load = 0
        sfi.append(sfi_load)
        # 3=>sfc set
        sfi_sfc_sets = sfi_sfc_set_list[i]
        sfi.append(sfi_sfc_sets)
        # 4=>index
        sfi.append(i + 1)
        # 5=>be array
        sfi.append([])
        sfi_sets.append(sfi)
    return sfi_sets


half_random_sfi_capacity_low = 15
half_random_sfi_capacity_high = 30


def create_sfi_set_half_radom():
    sfi_sets = [[]]
    sfi_type_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6]
    sfi_capacity_list = []
    for index in range(len(sfi_type_list)):
        sfi_capacity_list.append(random.randint(half_random_sfi_capacity_low, half_random_sfi_capacity_high))

    sfi1_1_sfc_set = [1, 2, 6]
    sfi1_2_sfc_set = [1]
    sfi1_3_sfc_set = [1, 4, 5, 6]
    sfi1_4_sfc_set = [1, 2, 4, 5]

    sfi2_1_sfc_set = [2, 5, 6]
    sfi2_2_sfc_set = [3, 6]
    sfi2_3_sfc_set = [6, 9]
    sfi2_4_sfc_set = [3, 7, 5]

    sfi3_1_sfc_set = [1, 7, 8]
    sfi3_2_sfc_set = [1]

    sfi4_1_sfc_set = [4, 5]
    sfi4_2_sfc_set = [5, 7]

    sfi5_1_sfc_set = [1]
    sfi5_2_sfc_set = [1, 5, 6, 8, 9]
    sfi5_3_sfc_set = [1, 5, 6, 8]

    sfi6_1_sfc_set = [2, 3, 6]
    sfi6_2_sfc_set = [3, 7]
    sfi6_3_sfc_set = [6, 7]
    sfi_sfc_set_list = [sfi1_1_sfc_set, sfi1_2_sfc_set, sfi1_3_sfc_set, sfi1_4_sfc_set,
                        sfi2_1_sfc_set, sfi2_2_sfc_set, sfi2_3_sfc_set, sfi2_4_sfc_set,
                        sfi3_1_sfc_set, sfi3_2_sfc_set,
                        sfi4_1_sfc_set, sfi4_2_sfc_set,
                        sfi5_1_sfc_set, sfi5_2_sfc_set, sfi5_3_sfc_set,
                        sfi6_1_sfc_set, sfi6_2_sfc_set, sfi6_3_sfc_set
                        ]

    for i in range(len(sfi_sfc_set_list)):
        # add a sfi to sfi_sets
        sfi = []
        # 0=> type
        sfi_type = sfi_type_list[i]
        sfi.append(sfi_type)
        # 1=>capacity
        sfi_capacity = sfi_capacity_list[i]
        sfi.append(sfi_capacity)
        # 2=>load
        sfi_load = 0
        sfi.append(sfi_load)
        # 3=>sfc set
        sfi_sfc_sets = sfi_sfc_set_list[i]
        sfi.append(sfi_sfc_sets)
        # 4=>index
        sfi.append(i + 1)
        # 5=>be array
        sfi.append([])
        sfi_sets.append(sfi)
    return sfi_sets


def count_be(sfc_sets, sfi_sets):
    BE = []
    BE.append([])
    # 计算稀缺指数矩阵
    for sfc in sfc_sets:
        if sfc == []:
            continue
        be_arry = []
        BE.append(be_arry)
        for i in range(len(sfc[0])):
            sf_type = sfc[0][i]
            w = sfc[1][i]
            time = sfc[2][sf_type]
            sum = 0
            for sfi in sfi_sets:
                if sfi == []:
                    continue
                if sfi[0] == sf_type and sfc[3] in sfi[3]:
                    sum += int((sfi[1] - sfi[2]) / w)
            be = sum / time
            be_arry.append(be)

    count_be_array_for_sfi(sfc_sets, sfi_sets, BE)
    return BE


def count_be_array_for_sfi(sfc_sets, sfi_sets, BE):
    # 生成sfi的be向量，并排序
    for sfi in sfi_sets:
        if sfi == []:
            continue
        sfi_sfc_sets = sfi[3]
        be_sets = []
        sf_type = sfi[0]
        for sfc_index in sfi_sfc_sets:
            sfc = sfc_sets[sfc_index]
            sfc_be_arry = BE[sfc_index]
            for i in range(len(sfc[0])):
                sf = sfc[0][i]
                if sf == sf_type:
                    be_sets.append(sfc_be_arry[i])
                    break

        # 对sfi的sfc服务集排序
        sorted_be_sets = sorted(be_sets)
        new_sfc_sets = []
        for be in sorted_be_sets:
            sfc_index = -1
            tmp = -1
            while sfc_index == -1 or sfc_index in new_sfc_sets:
                tmp += 1
                if be_sets[tmp] == be:
                    sfc_index = sfi_sfc_sets[tmp]
            new_sfc_sets.append(sfc_index)
        sfi[3] = new_sfc_sets
        sfi[5] = sorted_be_sets


def sort_rank_dic(rank_first_sfi_sets):
    if len(rank_first_sfi_sets) == 1:
        return rank_first_sfi_sets
    be_sets = []
    for sfi in rank_first_sfi_sets:
        be_sets.append(sfi[5])
    sorted_be_sets = sorted(be_sets)
    sorted_rank_first_sfi_sets = []
    color_set = []
    for be_array in sorted_be_sets:
        index = -1
        tmp = -1
        while index == -1 or index in color_set:
            tmp += 1
            if be_sets[tmp] == be_array:
                index = tmp
        color_set.append(index)
        sorted_rank_first_sfi_sets.append(rank_first_sfi_sets[index])
    return sorted_rank_first_sfi_sets


def hangder_request_old(sfc_request, sfc_sets, sfi_sets, BE, res):
    # 对请求sfc的每个sf选择sf实例
    for i in range(len(sfc_request[0])):
        sf_type = sfc_request[0][i]
        w = sfc_request[1][i]
        rank_dic = {}
        for sfi in sfi_sets:
            if sfi == [] or sfi[1] - sfi[2] < w:
                continue
            if sfi[0] == sf_type and sfc_request[3] in sfi[3]:
                sfi_sfc_sets = sfi[3]
                be_sets = sfi[5]
                my_be = 0
                for tmp in range(len(sfi_sfc_sets)):
                    sfc_index = sfi_sfc_sets[tmp]
                    if sfc_index == sfc_request[3]:
                        my_be = be_sets[tmp]
                        break
                rank = 0
                for be in be_sets:
                    if be <= my_be:
                        rank += 1
                if rank not in rank_dic:
                    rank_dic[rank] = [sfi]
                else:
                    rank_dic[rank].append(sfi)
        min_rank = 1000
        for rank in rank_dic:
            if rank < min_rank:
                min_rank = rank

        if min_rank == 1000:
            # 部署失败,回滚，然后退出此条链的部署
            # print("failer")
            for i in range(len(res)):
                sfi_index = res[i]
                w = sfc_request[1][i]
                sfi = sfi_sets[sfi_index]
                sfi[2] -= w
            res = []
            return False
        # 并不应该用rank最小的，比如be array有5 10 和 8 9 10 ，应该选第二个而不是第一个
        rank_first_sfi_sets = rank_dic[min_rank]
        # 对稀缺指数向量进行字典序排序
        sorted_rank_first_sfi_sets = sort_rank_dic(rank_first_sfi_sets)
        sfi = sorted_rank_first_sfi_sets[0]
        sfi[2] += w
        res.append(sfi[4])
        # 更新所有sfc与该sfi相关的资源,与BE矩阵
        for sfc_index in sfi[3]:
            sfc = sfc_sets[sfc_index]
            be_arry = BE[sfc_index]
            for i in range(len(sfc[0])):
                sf_type = sfc[0][i]
                if sf_type == sfi[0]:
                    w = sfc[1][i]
                    time = sfc[2][sf_type]
                    sum = 0
                    for sfi in sfi_sets:
                        if sfi == []:
                            continue
                        if sfi[0] == sf_type and sfc[3] in sfi[3]:
                            sum += int((sfi[1] - sfi[2]) / w)
                    be = sum / time
                    be_arry[i] = be
        # 更新sfi的be_array和sfc_sets
        count_be_array_for_sfi(sfc_sets, sfi_sets, BE)
    return True


infinate = 1000000


def compute_impact_index(sfi_set_for_sf, my_be):
    index_array = []
    for sfi in sfi_set_for_sf:
        be_array = sfi[5]
        index = infinate
        my_be_count = 0
        for be in be_array:
            if be > my_be:
                continue
            if be == my_be:
                my_be_count += 1
            if index > be:
                index = be
        if index == my_be:
            # 如果出现两次及以上，index才是my_be
            if my_be_count == 1:
                index = infinate
        index_array.append(index)
    return index_array


def stop_condition(time_count, time_limit):
    if time_count > time_limit:
        return True
    return False


def get_k_sfi(sfi_sets, K):
    res = []
    min_be_array = [infinate]
    for sfi in sfi_sets:
        if sfi==[]:
            continue
        min_be = infinate
        be_array = sfi[5]
        for be in be_array:
            if be < min_be:
                min_be = be
        min_be_array.append(min_be)
    sort_min_be_array = sorted(min_be_array)
    min_k_be = []
    for i in range(K):
        if sort_min_be_array[i] !=infinate:
            min_k_be.append(sort_min_be_array[i])

    for i in range(len(sfi_sets)):
        sfi = sfi_sets[i]
        if sfi==[]:
            continue
        min_be = min_be_array[i]
        if min_be in min_k_be:
            res.append(sfi)
    return res


# 将稀缺指数集合最小值最小K个sfi上的sf部署策略迁移到其他sfi上
def get_neighbors(Ztmp, sfc_sets, ori_sfi_sets, sfc_requests, K):
    Zneighbors = []
    # 求出Ztmp稀缺指数集合最小值最小K个sfi
    tmp_be = Ztmp[-3]
    tmp_sfi_sets=Ztmp[-4]
    count_be_array_for_sfi(sfc_sets, tmp_sfi_sets, tmp_be)
    k_sfi_sets = get_k_sfi(tmp_sfi_sets, K)
    # 求出现在部署方案中部署在这k个sfi上的sulotion
    related_solution_index_set = []
    k_sfi_index_sets = []
    for sfi in k_sfi_sets:
        k_sfi_index_sets.append(sfi[4])
    for request_index in range(len(Ztmp)-4):
        solution = Ztmp[request_index]
        for tmp in range(len(solution)):
            deployed_sfi_index = solution[tmp]
            if deployed_sfi_index in k_sfi_index_sets:
                related_solution_index_set.append(request_index)
    # 求出邻域解
    for related_solution_index in related_solution_index_set:
        solution = Ztmp[related_solution_index]
        request = sfc_requests[related_solution_index]
        for tmp in range(len(solution)):
            deployed_sfi_index = solution[tmp]
            if deployed_sfi_index in k_sfi_index_sets:
                old_sfi = tmp_sfi_sets[deployed_sfi_index]
                w= request[1][tmp]
                sf_type = old_sfi[0]
                can_deploy_sfi_set = []
                for sfi in tmp_sfi_sets:
                    if sfi == [] or sfi[1] - sfi[2] < w:
                        continue
                    if sfi[0] == sf_type and request[3] in sfi[3]:
                        if old_sfi[4] == sfi[4]:
                            continue
                        can_deploy_sfi_set.append(sfi)
                for move_to_sfi in can_deploy_sfi_set:
                    Z_neighbor=copy.deepcopy(Ztmp)
                    # -4更新sfi_sets
                    new_sfi_sets = Z_neighbor[-4]
                    new_sfi_index=move_to_sfi[4]
                    for sfi in new_sfi_sets:
                        if sfi==[]:
                            continue
                        if sfi[4]==old_sfi[4]:
                            sfi[2]-=w
                        if sfi[4]==move_to_sfi[4]:
                            sfi[2] += w
                    # 部署方案
                    Z_neighbor[related_solution_index][tmp]=new_sfi_index
                    # -3 计算BE
                    BE_neighbor = count_be(sfc_sets, new_sfi_sets)
                    count_be_array_for_sfi(sfc_sets, new_sfi_sets, BE_neighbor)
                    Z_neighbor[-3]=BE_neighbor
                    # -2 计算tl move第几个request，sfc上第几个sf，old—sfi的index，new-sfi的index
                    # tl_move=[related_solution_index,tmp,old_sfi[4],new_sfi_index]
                    tl_move = [related_solution_index, tmp,  new_sfi_index]
                    Z_neighbor[-2]=tl_move
                    # -1 value
                    value = value_solution(sfc_sets, new_sfi_sets)
                    Z_neighbor[-1]=value
                    Zneighbors.append(Z_neighbor)
    return Zneighbors



def get_candidates(Nz):
    return Nz


def get_best_candidate(candidates, tl):
    best_candidate = None
    for candidate in candidates:
        if candidate[-2] in tl:
            continue
        if best_candidate == None or best_candidate[-1] < candidate[-1]:
            best_candidate = candidate
    return best_candidate


def update_tl(tl, candidate, tl_length_limit):
    if candidate[-2] in tl:
        # 将该次操作删除然后再入添加
        tl.remove(candidate[-2])
        tl.append(candidate[-2])
        return
    # 数目没有超过上限，直接添加
    if len(tl) <= tl_length_limit:
        tl.append(candidate[-2])
        return
    # 数目超过上限，删除最老的后添加
    del tl[0]
    tl.append(candidate[-2])


def better_than_solution(candidate, Z_best):
    if candidate[-1] > Z_best[-1]:
        return True
    return False


def aspiration_satisfied(candidates, Z_best):
    for solution in candidates:
        if solution[-1] > Z_best[-1]:
            Z_best = solution
    return Z_best


def value_solution(sfc_sets, sfi_sets):
    # 根据剩余容量得到最小可部署值
    return get_min_pi(sfc_sets, sfi_sets)


def active_solutions(sfc_requests, sfc_sets, sfi_sets, Z_best):
    for index in range(len(sfc_requests)):
        sfc_request = sfc_requests[index]
        solution = Z_best[index]
        active_solution(sfc_request, sfi_sets, solution)
    return


def active_solution(sfc_request, sfi_sets, solution):
    for index in range(len(sfc_request[0])):
        sfi_index = solution[index]
        sfi = sfi_sets[sfi_index]
        w = sfc_request[1][index]
        sfi[2] += w
        if sfi[1] - sfi[2] < 0:
            logging.error("ts  load ove capacity")
            logging.error(sfc_request)
            logging.error(solution)
            logging.error(sfi)


def ts(sfc_requests, sfc_sets, sfi_sets,BE):
    time_limit = 20
    tl_length_limit = 3
    K = 1
    better_flag=False
    tl = []
    # 获取初始解
    Z0 = []
    sfi_sets_for_init = copy.deepcopy(sfi_sets)
    # sfi_sets_for_init_solution=copy.deepcopy(sfi_sets)
    for sfc_request in sfc_requests:
        tmp_res = []
        # hangder_request_greedy_max_free_load(sfc_request, sfi_sets_for_init, tmp_res)
        hangder_request(sfc_sets=sfc_sets,sfi_sets=sfi_sets_for_init,sfc_request=sfc_request,BE=BE,res=tmp_res)
        if tmp_res == []:
            # 不能部署更多的sfc
            # print("can not satisfy all request")
            break
        Z0.append(tmp_res)
    # -4 sfi_sets
    Z0.append(sfi_sets_for_init)
    # -3 BE
    BE_for_init_solution = count_be(sfc_sets, sfi_sets_for_init)
    count_be_array_for_sfi(sfc_sets, sfi_sets_for_init, BE_for_init_solution)
    Z0.append(BE_for_init_solution)
    # -2 tl mova
    Z0.append(None)
    # -1 value
    value0 = value_solution( sfc_sets, sfi_sets_for_init)
    Z0.append(value0)
    Z_tmp = Z0
    Z_best = Z0
    # print("z0 ")
    # print(Z0)
    # 循环
    time_count = 0
    while not stop_condition(time_count, time_limit):
        time_count += 1
        # print(time_count)
        # 获取领域解
        Nz = get_neighbors(Z_tmp, sfc_sets, sfi_sets, sfc_requests, K)
        # print("Nz")
        # print(len(Nz))
        # 获取候选解
        candidates = get_candidates(Nz)
        # print("candidates")
        # print(candidates)
        # 如果候选解为空，跳出循环
        if candidates==[]:
            K+=1
            continue
        # 判断赦免条件是否成立
        better_solution = aspiration_satisfied(candidates, Z_best)
        if better_solution != Z_best:
            Z_best = better_solution
            update_tl(tl, Z_best, tl_length_limit)
            better_flag=True
            continue
        # 选取不违背禁忌表的最优候选者
        candidate = get_best_candidate(candidates, tl)
        if candidate==None:
            K += 1
            continue
        # print("candidate min pi:")
        # print(candidate[-1])
        Z_tmp=candidate
        # 更新禁忌表
        update_tl(tl, candidate, tl_length_limit)
        # 更新最优解
        if better_than_solution(candidate, Z_best):
            better_flag=True
            Z_best = candidate


    if better_flag:
        # print("!!!!!better solution")
        # print(Z_best)
        pass
    return Z_best


def hangder_request(sfc_request, sfc_sets, sfi_sets, BE, res):
    logging.debug("me handle request:" + str(sfc_request[3]))
    # 对请求sfc的每个sf选择sf实例
    for i in range(len(sfc_request[0])):
        sf_type = sfc_request[0][i]
        logging.debug("for sf :" + str(sf_type))
        my_be = BE[sfc_request[3]][i]
        w = sfc_request[1][i]
        sfi_set_for_sf = []
        for sfi in sfi_sets:
            if sfi == [] or sfi[1] - sfi[2] < w:
                continue
            if sfi[0] == sf_type and sfc_request[3] in sfi[3]:
                sfi_set_for_sf.append(sfi)
        logging.debug("sfi_sets_for_sf:" + str(sfi_set_for_sf))
        if len(sfi_set_for_sf) == 0:
            # 部署失败,回滚，然后退出此条链的部署
            logging.debug("failture")
            logging.debug("alredeay res:" + str(res))
            for tmp in range(len(res)):
                sfi_index = res[tmp]
                w = sfc_request[1][tmp]
                sfi = sfi_sets[sfi_index]
                sfi[2] -= w
            res.clear()
            return False
        # 计算sfc对sfi的影响指数（稀缺向量中除了该sfc的最小值）
        impact_index_array = compute_impact_index(sfi_set_for_sf, my_be)
        logging.debug("impact_index_array" + str(impact_index_array))
        # 选择影响指数最大的sfi的集合
        max_impact_index = -1

        for impact_index in impact_index_array:
            if impact_index > max_impact_index:
                max_impact_index = impact_index
        max_index_set = []
        for tmp in range(len(impact_index_array)):
            impact_index = impact_index_array[tmp]
            if impact_index == max_impact_index:
                max_index_set.append(sfi_set_for_sf[tmp])
        logging.debug("max_impact_index:" + str(max_impact_index))
        sorted_rank_first_sfi_sets = sort_rank_dic(max_index_set)
        logging.debug("sorted_rank_first_sfi_sets:" + str(sorted_rank_first_sfi_sets))
        sfi = sorted_rank_first_sfi_sets[-1]
        logging.debug("sfi:" + str(sfi))
        sfi[2] += w
        logging.debug("sfi:" + str(sfi))
        res.append(sfi[4])
        # 更新所有sfc与该sfi相关的资源,与BE矩阵
        for sfc_index in sfi[3]:
            sfc = sfc_sets[sfc_index]
            be_arry = BE[sfc_index]
            for i in range(len(sfc[0])):
                sf_type = sfc[0][i]
                if sf_type == sfi[0]:
                    w = sfc[1][i]
                    time = sfc[2][sf_type]
                    sum = 0
                    for sfi in sfi_sets:
                        if sfi == []:
                            continue
                        if sfi[0] == sf_type and sfc[3] in sfi[3]:
                            sum += int((sfi[1] - sfi[2]) / w)
                    be = sum / time
                    be_arry[i] = be
        # 更新sfi的be_array和sfc_sets
        count_be_array_for_sfi(sfc_sets, sfi_sets, BE)
    return True


def hangder_request_random(sfc_request, sfi_sets, res):
    logging.debug("random handle request:" + str(sfc_request[3]))
    # 对请求sfc的每个sf随机选择sf实例
    for i in range(len(sfc_request[0])):
        sf_type = sfc_request[0][i]
        logging.debug("for sf :" + str(sf_type))
        w = sfc_request[1][i]
        sfi_sets_for_sf = []
        for sfi in sfi_sets:
            if sfi == [] or sfi[1] - sfi[2] < w:
                continue
            if sfi[0] == sf_type and sfc_request[3] in sfi[3]:
                sfi_sets_for_sf.append(sfi)
        logging.debug("sfi_sets_for_sf:" + str(sfi_sets_for_sf))
        if len(sfi_sets_for_sf) == 0:
            # 部署失败,回滚，然后退出此条链的部署
            logging.debug("failture")
            logging.debug("alredeay res:" + str(res))
            for i in range(len(res)):
                sfi_index = res[i]
                w = sfc_request[1][i]
                sfi = sfi_sets[sfi_index]
                sfi[2] -= w
            res = []
            return False
        sfi_index = random.randint(0, len(sfi_sets_for_sf) - 1)
        logging.debug("sfi_index:" + str(sfi_index))
        sfi = sfi_sets_for_sf[sfi_index]
        logging.debug(sfi)
        sfi[2] += w
        logging.debug(sfi)
        res.append(sfi[4])
    return True

def hangder_request_greedy_min_load(sfc_request, sfi_sets, res):
    # 对请求sfc的每个sf随机选择sf实例
    for i in range(len(sfc_request[0])):
        sf_type = sfc_request[0][i]
        w = sfc_request[1][i]
        sfi_sets_for_sf = []
        for sfi in sfi_sets:
            if sfi == [] or sfi[1] - sfi[2] < w:
                continue
            if sfi[0] == sf_type and sfc_request[3] in sfi[3]:
                sfi_sets_for_sf.append(sfi)
        if len(sfi_sets_for_sf) == 0:
            # 部署失败,回滚，然后退出此条链的部署
            # print("failer")
            for i in range(len(res)):
                sfi_index = res[i]
                w = sfc_request[1][i]
                sfi = sfi_sets[sfi_index]
                sfi[2] -= w
            res = []
            return False
        sfi_index = -1
        sfi_min_load = infinate
        for j in range(len(sfi_sets_for_sf)):
            sfi = sfi_sets_for_sf[j]
            tmp =  sfi[2]
            if tmp <sfi_min_load:
                sfi_min_load = tmp
                sfi_index = j

        sfi = sfi_sets_for_sf[sfi_index]
        sfi[2] += w
        res.append(sfi[4])
    return True

def hangder_request_greedy_max_free_load(sfc_request, sfi_sets, res):
    # 对请求sfc的每个sf随机选择sf实例
    for i in range(len(sfc_request[0])):
        sf_type = sfc_request[0][i]
        w = sfc_request[1][i]
        sfi_sets_for_sf = []
        for sfi in sfi_sets:
            if sfi == [] or sfi[1] - sfi[2] < w:
                continue
            if sfi[0] == sf_type and sfc_request[3] in sfi[3]:
                sfi_sets_for_sf.append(sfi)
        if len(sfi_sets_for_sf) == 0:
            # 部署失败,回滚，然后退出此条链的部署
            # print("failer")
            for i in range(len(res)):
                sfi_index = res[i]
                w = sfc_request[1][i]
                sfi = sfi_sets[sfi_index]
                sfi[2] -= w
            res = []
            return False
        sfi_index = -1
        sfi_free_capacity = -1;
        for j in range(len(sfi_sets_for_sf)):
            sfi = sfi_sets_for_sf[j]
            tmp = sfi[1] - sfi[2]
            if tmp > sfi_free_capacity:
                sfi_free_capacity = tmp
                sfi_index = j

        sfi = sfi_sets_for_sf[sfi_index]
        sfi[2] += w
        res.append(sfi[4])
    return True


def run_static_demo():
    all_time = 10
    request_num = 50
    my_success_count = 0
    random_success_count = 0
    max_free_load_greedy_success_count = 0
    try_dic = {}
    my_success_dic = {}
    random_success_dic = {}
    max_free_load_greedy_success_dic = {}

    for i in range(all_time):
        sfc_sets = creat_sfc_set_static()
        sfi_sets_for_random = create_sfi_set_static()
        sfi_sets_for_me = copy.deepcopy(sfi_sets_for_random)
        sfi_sets_for_max_free_load_greedy = copy.deepcopy(sfi_sets_for_random)
        BE_for_random = count_be(sfc_sets, sfi_sets_for_random)
        BE_for_me = count_be(sfc_sets, sfi_sets_for_me)
        BE_for_max_free_load_greedy = count_be(sfc_sets, sfi_sets_for_max_free_load_greedy)

        for i in range(request_num):
            reques_index = i % (len(sfc_sets) - 1) + 1
            reques = sfc_sets[reques_index]
            # res = []
            random_sucess = hangder_request_random(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_random,
                                                   BE=BE_for_random, res=[])
            my_sucess = hangder_request(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_me, BE=BE_for_me,
                                        res=[])
            max_free_load_greedy_sucess = hangder_request_greedy_max_free_load(sfc_request=reques, sfc_sets=sfc_sets,
                                                                 sfi_sets=sfi_sets_for_max_free_load_greedy,
                                                                 BE=BE_for_max_free_load_greedy,
                                                                 res=[])
            if reques_index not in my_success_dic:
                my_success_dic[reques_index] = 0

            if reques_index not in random_success_dic:
                random_success_dic[reques_index] = 0

            if reques_index not in max_free_load_greedy_success_dic:
                max_free_load_greedy_success_dic[reques_index] = 0

            if reques_index not in try_dic:
                try_dic[reques_index] = 0

            try_dic[reques_index] += 1

            if random_sucess:
                random_success_count += 1
                random_success_dic[reques_index] += 1

            if my_sucess:
                my_success_count += 1
                my_success_dic[reques_index] += 1

            if max_free_load_greedy_sucess:
                max_free_load_greedy_success_count += 1
                max_free_load_greedy_success_dic[reques_index] += 1

    print(try_dic)
    print(random_success_dic)
    print(max_free_load_greedy_success_dic)
    print(my_success_dic)

    print(random_success_count)
    print(max_free_load_greedy_success_count)
    print(my_success_count)


def run_static_demo2():
    all_time = 1
    request_num = 60
    my_success_count = 0
    random_success_count = 0
    max_free_load_greedy_success_count = 0
    try_dic = {}
    my_success_dic = {}
    random_success_dic = {}
    max_free_load_greedy_success_dic = {}

    for i in range(all_time):
        sfc_sets = creat_sfc_set_static2()
        sfi_sets_for_random = create_sfi_set_static2()
        sfi_sets_for_me = copy.deepcopy(sfi_sets_for_random)
        sfi_sets_for_max_free_load_greedy = copy.deepcopy(sfi_sets_for_random)
        BE_for_me = count_be(sfc_sets, sfi_sets_for_me)

        for i in range(request_num):
            reques_index = i % (len(sfc_sets) - 1) + 1
            reques = sfc_sets[reques_index]
            # res = []
            random_sucess = hangder_request_random(sfc_request=reques, sfi_sets=sfi_sets_for_random,
                                                   res=[])
            my_sucess = hangder_request(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_me, BE=BE_for_me,
                                        res=[])
            max_free_load_greedy_sucess = hangder_request_greedy_max_free_load(sfc_request=reques,
                                                                 sfi_sets=sfi_sets_for_max_free_load_greedy,

                                                                 res=[])
            if reques_index not in my_success_dic:
                my_success_dic[reques_index] = 0

            if reques_index not in random_success_dic:
                random_success_dic[reques_index] = 0

            if reques_index not in max_free_load_greedy_success_dic:
                max_free_load_greedy_success_dic[reques_index] = 0

            if reques_index not in try_dic:
                try_dic[reques_index] = 0

            try_dic[reques_index] += 1

            if random_sucess:
                random_success_count += 1
                random_success_dic[reques_index] += 1

            if my_sucess:
                my_success_count += 1
                my_success_dic[reques_index] += 1

            if max_free_load_greedy_sucess:
                max_free_load_greedy_success_count += 1
                max_free_load_greedy_success_dic[reques_index] += 1

    print(try_dic)
    print(random_success_dic)
    print(max_free_load_greedy_success_dic)
    print(my_success_dic)

    print(random_success_count)
    print(max_free_load_greedy_success_count)
    print(my_success_count)


def run_random_one():
    all_time = 1
    request_num = 50
    random_success_count = 0
    try_dic = {}
    random_success_dic = {}

    for i in range(all_time):
        sfc_sets = creat_sfc_set_static2()
        sfi_sets_for_random = create_sfi_set_static2()

        for i in range(request_num):
            reques_index = i % (len(sfc_sets) - 1) + 1
            reques = sfc_sets[reques_index]
            # res = []
            random_sucess = hangder_request_random(sfc_request=reques, sfi_sets=sfi_sets_for_random, res=[])

            if reques_index not in random_success_dic:
                random_success_dic[reques_index] = 0

            if reques_index not in try_dic:
                try_dic[reques_index] = 0

            try_dic[reques_index] += 1

            if random_sucess:
                random_success_count += 1
                random_success_dic[reques_index] += 1

    print(try_dic)
    print(random_success_dic)

    print(random_success_count)


def run_me_one_time():
    request_num = 100
    my_success_count = 0
    try_dic = {}
    my_success_dic = {}
    sfc_sets = creat_sfc_set_half_random()
    sfi_sets_for_me = create_sfi_set_half_radom()
    BE_for_me = count_be(sfc_sets, sfi_sets_for_me)

    for i in range(request_num):
        reques_index = i % (len(sfc_sets) - 1) + 1
        reques = sfc_sets[reques_index]
        res = []
        my_sucess = hangder_request(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_me, BE=BE_for_me,
                                    res=res)
        # my_sucess = hangder_request_greedy_max_free_load(sfc_request=reques, sfi_sets=sfi_sets_for_me,
        #                             res=res)
        if reques_index not in my_success_dic:
            my_success_dic[reques_index] = 0

        if reques_index not in try_dic:
            try_dic[reques_index] = 0

        try_dic[reques_index] += 1

        if my_sucess:
            my_success_count += 1
            my_success_dic[reques_index] += 1

    print(try_dic)
    print(my_success_dic)
    print(my_success_count)
    pass


def run_random_demo():
    all_time = 1
    request_num = 200
    my_success_count = 0
    random_success_count = 0
    max_free_load_greedy_success_count = 0
    try_dic = {}
    my_success_dic = {}
    random_success_dic = {}
    max_free_load_greedy_success_dic = {}
    my_min_list = []
    random_min_list = []
    max_free_load_greedy_min_list = []

    for i in range(all_time):
        sfc_sets = create_sfc_set()
        sfi_sets_for_random = create_sfi_set(sfc_sets)
        sfi_sets_for_me = copy.deepcopy(sfi_sets_for_random)
        sfi_sets_for_max_free_load_greedy = copy.deepcopy(sfi_sets_for_random)
        BE_for_me = count_be(sfc_sets, sfi_sets_for_me)

        my_success_dic_tmp = {}
        random_success_dic_tmp = {}
        max_free_load_greedy_success_dic_tmp = {}

        for i in range(request_num):
            reques_index = i % (len(sfc_sets) - 1) + 1
            reques_index = random.randint(1, len(sfc_sets) - 1)
            reques = sfc_sets[reques_index]
            # res = []
            random_sucess = hangder_request_random(sfc_request=reques, sfi_sets=sfi_sets_for_random,
                                                   res=[])
            my_sucess = hangder_request(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_me, BE=BE_for_me,
                                        res=[])
            max_free_load_greedy_sucess = hangder_request_greedy_max_free_load(sfc_request=reques,
                                                                 sfi_sets=sfi_sets_for_max_free_load_greedy,
                                                                 res=[])

            if reques_index not in my_success_dic_tmp:
                my_success_dic_tmp[reques_index] = 0

            if reques_index not in random_success_dic_tmp:
                random_success_dic_tmp[reques_index] = 0

            if reques_index not in max_free_load_greedy_success_dic_tmp:
                max_free_load_greedy_success_dic_tmp[reques_index] = 0

            if reques_index not in try_dic:
                try_dic[reques_index] = 0

            try_dic[reques_index] += 1

            if random_sucess:
                random_success_count += 1
                random_success_dic_tmp[reques_index] += 1

            if my_sucess:
                my_success_count += 1
                my_success_dic_tmp[reques_index] += 1

            if max_free_load_greedy_sucess:
                max_free_load_greedy_success_count += 1
                max_free_load_greedy_success_dic_tmp[reques_index] += 1
        my_min = 1000
        random_min = 1000
        max_free_load_greedy_min = 1000
        for k in my_success_dic_tmp:
            success = my_success_dic_tmp[k]
            if success != 0 and success < my_min:
                my_min = success
            if k not in my_success_dic:
                my_success_dic[k] = success
            else:
                my_success_dic[k] += success

        for k in random_success_dic_tmp:
            success = random_success_dic_tmp[k]
            if success != 0 and success < random_min:
                random_min = success
            if k not in random_success_dic:
                random_success_dic[k] = success
            else:
                random_success_dic[k] += success

        for k in max_free_load_greedy_success_dic_tmp:
            success = max_free_load_greedy_success_dic_tmp[k]
            if success != 0 and success < max_free_load_greedy_min:
                max_free_load_greedy_min = success
            if k not in max_free_load_greedy_success_dic:
                max_free_load_greedy_success_dic[k] = success
            else:
                max_free_load_greedy_success_dic[k] += success
        my_min_list.append(my_min)
        random_min_list.append(random_min)
        max_free_load_greedy_min_list.append(max_free_load_greedy_min)

    print(try_dic)
    print(random_success_dic)
    print(max_free_load_greedy_success_dic)
    print(my_success_dic)

    print(random_success_count)
    print(max_free_load_greedy_success_count)
    print(my_success_count)

    print(random_min_list)
    print(max_free_load_greedy_min_list)
    print(my_min_list)
    pass


def zero_sfi_load(sfi_sets):
    for sfi in sfi_sets:
        if sfi == []:
            continue
        sfi[2] = 0


def run_random_demo_picture():
    time = 10
    request_num = 20

    while request_num < 140:
        request_num += 20
        request_count = 0
        my_success_count = 0
        random_success_count = 0
        max_free_load_greedy_success_count = 0
        try_dic = {}
        my_success_dic = {}
        random_success_dic = {}
        max_free_load_greedy_success_dic = {}
        for j in range(time):
            sfc_sets = create_sfc_set()
            sfi_sets_for_random = create_sfi_set(sfc_sets)
            sfi_sets_for_me = copy.deepcopy(sfi_sets_for_random)
            sfi_sets_for_max_free_load_greedy = copy.deepcopy(sfi_sets_for_random)
            BE_for_me = count_be(sfc_sets, sfi_sets_for_me)

            zero_sfi_load(sfi_sets_for_random)
            zero_sfi_load(sfi_sets_for_me)
            zero_sfi_load(sfi_sets_for_max_free_load_greedy)

            for i in range(request_num):
                reques_index = i % (len(sfc_sets) - 1) + 1
                reques = sfc_sets[reques_index]
                request_count += 1
                # res = []
                random_sucess = hangder_request_random(sfc_request=reques,
                                                       sfi_sets=sfi_sets_for_random,
                                                       res=[])
                my_sucess = hangder_request(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_me,
                                            BE=BE_for_me,
                                            res=[])
                max_free_load_greedy_sucess = hangder_request_greedy_max_free_load(sfc_request=reques,
                                                                     sfi_sets=sfi_sets_for_max_free_load_greedy,
                                                                     res=[])
                if reques_index not in my_success_dic:
                    my_success_dic[reques_index] = 0

                if reques_index not in random_success_dic:
                    random_success_dic[reques_index] = 0

                if reques_index not in max_free_load_greedy_success_dic:
                    max_free_load_greedy_success_dic[reques_index] = 0

                if reques_index not in try_dic:
                    try_dic[reques_index] = 0

                try_dic[reques_index] += 1

                if random_sucess:
                    random_success_count += 1
                    random_success_dic[reques_index] += 1

                if my_sucess:
                    my_success_count += 1
                    my_success_dic[reques_index] += 1

                if max_free_load_greedy_sucess:
                    max_free_load_greedy_success_count += 1
                    max_free_load_greedy_success_dic[reques_index] += 1

        print(try_dic)
        print(random_success_dic)
        print(max_free_load_greedy_success_dic)
        print(my_success_dic)

        random_min_success = 10000
        for k in random_success_dic:
            if random_success_dic[k] < random_min_success and random_success_dic[k] != 0:
                random_min_success = random_success_dic[k]

        max_free_load_greedy_min_success = 10000
        for k in max_free_load_greedy_success_dic:
            if max_free_load_greedy_success_dic[k] < max_free_load_greedy_min_success and max_free_load_greedy_success_dic[k] != 0:
                max_free_load_greedy_min_success = max_free_load_greedy_success_dic[k]

        my_min_success = 10000
        for k in my_success_dic:
            if my_success_dic[k] < my_min_success and my_success_dic[k] != 0:
                my_min_success = my_success_dic[k]

        print(request_count)
        print(str(random_min_success) + "  " + str(random_success_count / request_count))
        print(str(max_free_load_greedy_min_success) + "  " + str(max_free_load_greedy_success_count / request_count))
        print(str(my_min_success) + "  " + str(my_success_count / request_count))


def run_random_demo2():
    all_time = 30
    request_num = 120
    request_count = 0
    my_success_count = 0
    random_success_count = 0
    max_free_load_greedy_success_count = 0
    try_dic = {}
    my_success_dic = {}
    random_success_dic = {}
    max_free_load_greedy_success_dic = {}
    my_min_list = []
    random_min_list = []
    max_free_load_greedy_min_list = []

    for i in range(all_time):
        sfc_sets = create_sfc_set()
        sfi_sets_for_random = create_sfi_set(sfc_sets)
        sfi_sets_for_me = copy.deepcopy(sfi_sets_for_random)
        sfi_sets_for_max_free_load_greedy = copy.deepcopy(sfi_sets_for_random)
        BE_for_me = count_be(sfc_sets, sfi_sets_for_me)

        my_success_dic_tmp = {}
        random_success_dic_tmp = {}
        max_free_load_greedy_success_dic_tmp = {}

        for i in range(request_num):
            reques_index = i % (len(sfc_sets) - 1) + 1
            # reques_index = random.randint(1, len(sfc_sets) - 1)
            reques = sfc_sets[reques_index]
            request_count += 1
            # res = []
            random_sucess = hangder_request_random(sfc_request=reques, sfi_sets=sfi_sets_for_random,
                                                   res=[])
            my_sucess = hangder_request(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_me, BE=BE_for_me,
                                        res=[])
            max_free_load_greedy_sucess = hangder_request_greedy_max_free_load(sfc_request=reques,
                                                                 sfi_sets=sfi_sets_for_max_free_load_greedy,
                                                                 res=[])

            if reques_index not in my_success_dic_tmp:
                my_success_dic_tmp[reques_index] = 0

            if reques_index not in random_success_dic_tmp:
                random_success_dic_tmp[reques_index] = 0

            if reques_index not in max_free_load_greedy_success_dic_tmp:
                max_free_load_greedy_success_dic_tmp[reques_index] = 0

            if reques_index not in try_dic:
                try_dic[reques_index] = 0

            try_dic[reques_index] += 1

            if random_sucess:
                random_success_count += 1
                random_success_dic_tmp[reques_index] += 1

            if my_sucess:
                my_success_count += 1
                my_success_dic_tmp[reques_index] += 1

            if max_free_load_greedy_sucess:
                max_free_load_greedy_success_count += 1
                max_free_load_greedy_success_dic_tmp[reques_index] += 1
        my_min = 1000
        random_min = 1000
        max_free_load_greedy_min = 1000
        for k in my_success_dic_tmp:
            success = my_success_dic_tmp[k]
            if success != 0 and success < my_min:
                my_min = success
            if k not in my_success_dic:
                my_success_dic[k] = success
            else:
                my_success_dic[k] += success

        for k in random_success_dic_tmp:
            success = random_success_dic_tmp[k]
            if success != 0 and success < random_min:
                random_min = success
            if k not in random_success_dic:
                random_success_dic[k] = success
            else:
                random_success_dic[k] += success

        for k in max_free_load_greedy_success_dic_tmp:
            success = max_free_load_greedy_success_dic_tmp[k]
            if success != 0 and success < max_free_load_greedy_min:
                max_free_load_greedy_min = success
            if k not in max_free_load_greedy_success_dic:
                max_free_load_greedy_success_dic[k] = success
            else:
                max_free_load_greedy_success_dic[k] += success
        my_min_list.append(my_min)
        random_min_list.append(random_min)
        max_free_load_greedy_min_list.append(max_free_load_greedy_min)

    print(try_dic)
    print(random_success_dic)
    print(max_free_load_greedy_success_dic)
    print(my_success_dic)

    print(request_count)
    print(random_success_count / request_count)
    print(max_free_load_greedy_success_count / request_count)
    print(my_success_count / request_count)

    print(random_min_list)
    print(max_free_load_greedy_min_list)
    print(my_min_list)

    random_min_sum = 0
    for tmp in random_min_list:
        random_min_sum += tmp

    max_free_load_greedy_min_sum = 0
    for tmp in max_free_load_greedy_min_list:
        max_free_load_greedy_min_sum += tmp

    my_min_sum = 0
    for tmp in my_min_list:
        my_min_sum += tmp

    print(random_min_sum / all_time)
    print(max_free_load_greedy_min_sum / all_time)
    print(my_min_sum / all_time)


def run_half_random_demo():
    request_num_list=[90]
    for request in request_num_list:
        run_half_random_demo_with_request_num(request)

def run_half_random_demo_with_request_num(request_num):
    print("request_num:")
    print(request_num)
    logging.info(request_num)

    data_ok=False
    while not data_ok:
        all_time = 50
        request_count = 0
        my_success_count = 0
        random_success_count = 0
        max_free_load_greedy_success_count = 0
        min_load_greedy_success_count = 0
        try_dic = {}
        my_success_dic = {}
        random_success_dic = {}
        max_free_load_greedy_success_dic = {}
        min_load_greedy_success_dic = {}
        my_min_list = []
        random_min_list = []
        max_free_load_greedy_min_list = []
        min_load_greedy_min_list = []

        random_min_pi_list = []
        my_min_pi_list = []
        max_free_load_greedy_min_pi_list = []
        min_load_greedy_min_pi_list = []
        ts_min_pi_list = []
        for time in range(all_time):
            # print(time)
            sfc_sets = creat_sfc_set_half_random()
            sfi_sets_for_random = create_sfi_set_half_radom()
            sfi_sets_for_me = copy.deepcopy(sfi_sets_for_random)
            sfi_sets_for_max_free_load_greedy = copy.deepcopy(sfi_sets_for_random)
            sfi_sets_for_min_load_greedy = copy.deepcopy(sfi_sets_for_random)
            sfi_sets_for_ts = copy.deepcopy(sfi_sets_for_random)
            BE_for_ts = count_be(sfc_sets, sfi_sets_for_ts)
            BE_for_me = count_be(sfc_sets, sfi_sets_for_me)

            my_success_dic_tmp = {}
            random_success_dic_tmp = {}
            max_free_load_greedy_success_dic_tmp = {}
            min_load_greedy_success_dic_tmp = {}
            requests_for_ts = []

            for i in range(request_num):
                reques_index = i % (len(sfc_sets) - 1) + 1
                reques_index = random.randint(1, len(sfc_sets) - 1)
                reques = sfc_sets[reques_index]
                requests_for_ts.append(reques)
                request_count += 1
                # res = []
                random_sucess = hangder_request_random(sfc_request=reques, sfi_sets=sfi_sets_for_random,
                                                       res=[])
                my_sucess = hangder_request(sfc_request=reques, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_me,
                                            BE=BE_for_me,
                                            res=[])
                max_free_load_greedy_sucess = hangder_request_greedy_max_free_load(sfc_request=reques,
                                                                     sfi_sets=sfi_sets_for_max_free_load_greedy,
                                                                     res=[])
                min_load_greedy_sucess = hangder_request_greedy_min_load(sfc_request=reques,
                                                                                   sfi_sets=sfi_sets_for_min_load_greedy,
                                                                                   res=[])

                if reques_index not in my_success_dic_tmp:
                    my_success_dic_tmp[reques_index] = 0

                if reques_index not in random_success_dic_tmp:
                    random_success_dic_tmp[reques_index] = 0

                if reques_index not in max_free_load_greedy_success_dic_tmp:
                    max_free_load_greedy_success_dic_tmp[reques_index] = 0

                if reques_index not in min_load_greedy_success_dic_tmp:
                    min_load_greedy_success_dic_tmp[reques_index] = 0

                if reques_index not in try_dic:
                    try_dic[reques_index] = 0

                try_dic[reques_index] += 1

                if random_sucess:
                    random_success_count += 1
                    random_success_dic_tmp[reques_index] += 1

                if my_sucess:
                    my_success_count += 1
                    my_success_dic_tmp[reques_index] += 1

                if max_free_load_greedy_sucess:
                    max_free_load_greedy_success_count += 1
                    max_free_load_greedy_success_dic_tmp[reques_index] += 1

                if min_load_greedy_sucess:
                    min_load_greedy_success_count += 1
                    min_load_greedy_success_dic_tmp[reques_index] += 1

            # run ts

            solutions = ts(sfc_requests=requests_for_ts, sfc_sets=sfc_sets, sfi_sets=sfi_sets_for_ts, BE=BE_for_ts)
            random_min_pi = get_min_pi(sfc_sets, sfi_sets_for_random)
            random_min_pi_list.append(random_min_pi)
            my_min_pi = get_min_pi(sfc_sets, sfi_sets_for_me)
            my_min_pi_list.append(my_min_pi)
            max_free_load_greedy_min_pi = get_min_pi(sfc_sets, sfi_sets_for_max_free_load_greedy)
            max_free_load_greedy_min_pi_list.append(max_free_load_greedy_min_pi)
            min_load_greedy_min_pi = get_min_pi(sfc_sets, sfi_sets_for_min_load_greedy)
            min_load_greedy_min_pi_list.append(min_load_greedy_min_pi)
            ts_min_pi = get_min_pi(sfc_sets, solutions[-4])
            ts_min_pi_list.append(ts_min_pi)
            # print("greedy_min_pi")
            # print(greedy_min_pi)
            # print("ts_min_pi")
            # print(ts_min_pi)
            my_min = 1000
            random_min = 1000
            max_free_load_greedy_min = 1000
            min_load_greedy_min = 1000
            for k in my_success_dic_tmp:
                success = my_success_dic_tmp[k]
                if success != 0 and success < my_min:
                    my_min = success
                if k not in my_success_dic:
                    my_success_dic[k] = success
                else:
                    my_success_dic[k] += success

            for k in random_success_dic_tmp:
                success = random_success_dic_tmp[k]
                if success != 0 and success < random_min:
                    random_min = success
                if k not in random_success_dic:
                    random_success_dic[k] = success
                else:
                    random_success_dic[k] += success

            for k in max_free_load_greedy_success_dic_tmp:
                success = max_free_load_greedy_success_dic_tmp[k]
                if success != 0 and success < max_free_load_greedy_min:
                    max_free_load_greedy_min = success
                if k not in max_free_load_greedy_success_dic:
                    max_free_load_greedy_success_dic[k] = success
                else:
                    max_free_load_greedy_success_dic[k] += success

            for k in min_load_greedy_success_dic_tmp:
                success = min_load_greedy_success_dic_tmp[k]
                if success != 0 and success < min_load_greedy_min:
                    min_load_greedy_min = success
                if k not in min_load_greedy_success_dic:
                    min_load_greedy_success_dic[k] = success
                else:
                    min_load_greedy_success_dic[k] += success

            my_min_list.append(my_min)
            random_min_list.append(random_min)
            max_free_load_greedy_min_list.append(max_free_load_greedy_min)
            min_load_greedy_min_list.append(min_load_greedy_min)

        print(try_dic)
        print(random_success_dic)
        print(max_free_load_greedy_success_dic)
        print(min_load_greedy_success_dic)
        print(my_success_dic)

        print(request_count)
        print(random_success_count / request_count)
        print(max_free_load_greedy_success_count / request_count)
        print(min_load_greedy_success_count / request_count)
        print(my_success_count / request_count)
        flag1 = False
        if my_success_count / request_count >= max_free_load_greedy_success_count / request_count and max_free_load_greedy_success_count / request_count > random_success_count / request_count:
            flag1 = True
        if request_num == 10:
            flag1 = True

        print(random_min_list)
        print(max_free_load_greedy_min_list)
        print(min_load_greedy_min_list)
        print(my_min_list)

        random_min_sum = 0
        for tmp in random_min_list:
            random_min_sum += tmp

        max_free_load_greedy_min_sum = 0
        for tmp in max_free_load_greedy_min_list:
            max_free_load_greedy_min_sum += tmp

        min_load_greedy_min_sum = 0
        for tmp in min_load_greedy_min_list:
            min_load_greedy_min_sum += tmp

        my_min_sum = 0
        for tmp in my_min_list:
            my_min_sum += tmp

        print(random_min_sum / all_time)
        print(max_free_load_greedy_min_sum / all_time)
        print(min_load_greedy_min_sum / all_time)
        print(my_min_sum / all_time)
        flag2 = False
        if my_min_sum / all_time > max_free_load_greedy_min_sum / all_time and max_free_load_greedy_min_sum / all_time > random_min_sum / all_time:
            flag2 = True
        if request_num == 10 :
            flag2 = True
        if request_num == 20 and max_free_load_greedy_min_sum / all_time > random_min_sum / all_time:
            flag2=True
        print("cam deploy")
        random_min_pi_sum = 0
        for tmp in random_min_pi_list:
            random_min_pi_sum += tmp

        max_free_load_greedy_min_pi_sum = 0
        for tmp in max_free_load_greedy_min_pi_list:
            max_free_load_greedy_min_pi_sum += tmp

        min_load_greedy_min_pi_sum = 0
        for tmp in min_load_greedy_min_pi_list:
            min_load_greedy_min_pi_sum += tmp


        my_min_pi_sum = 0
        for tmp in my_min_pi_list:
            my_min_pi_sum += tmp

        ts_min_pi_sum = 0
        for tmp in ts_min_pi_list:
            ts_min_pi_sum += tmp

        print(random_min_pi_list)
        print(max_free_load_greedy_min_pi_list)
        print(min_load_greedy_min_pi_list)
        print(my_min_pi_list)
        print(ts_min_pi_list)
        print(random_min_pi_sum / all_time)
        print(max_free_load_greedy_min_pi_sum / all_time)
        print(min_load_greedy_min_pi_sum / all_time)
        print(my_min_pi_sum / all_time)
        print(ts_min_pi_sum / all_time)
        flag3 = False
        if ts_min_pi_sum / all_time > my_min_pi_sum / all_time and my_min_pi_sum / all_time > max_free_load_greedy_min_pi_sum / all_time and max_free_load_greedy_min_pi_sum / all_time > random_min_pi_sum / all_time:
            flag3 = True
        if request_num > 40 :
            flag3 = True

        flag1=True
        flag2=True
        flag3=True

        if flag1 and flag2 and flag3:
            data_ok=True
            print(data_ok)
            print(try_dic)
            logging.info(try_dic)

            print(random_success_dic)
            logging.info(random_success_dic)

            print(max_free_load_greedy_success_dic)
            logging.info(max_free_load_greedy_success_dic)

            print(min_load_greedy_success_dic)
            logging.info(min_load_greedy_success_dic)

            print(my_success_dic)
            logging.info(my_success_dic)

            print(request_count)
            logging.info(request_count)

            print(random_success_count / request_count)
            logging.info(random_success_count / request_count)

            print(max_free_load_greedy_success_count / request_count)
            logging.info(max_free_load_greedy_success_count / request_count)

            print(min_load_greedy_success_count / request_count)
            logging.info(min_load_greedy_success_count / request_count)

            print(my_success_count / request_count)
            logging.info(my_success_count / request_count)

            print(random_min_list)
            logging.info(random_min_list)

            print(max_free_load_greedy_min_list)
            logging.info(max_free_load_greedy_min_list)

            print(min_load_greedy_min_list)
            logging.info(min_load_greedy_min_list)

            print(my_min_list)
            logging.info(my_min_list)

            print(random_min_sum / all_time)
            logging.info(random_min_sum / all_time)

            print(max_free_load_greedy_min_sum / all_time)
            logging.info(max_free_load_greedy_min_sum / all_time)

            print(min_load_greedy_min_sum / all_time)
            logging.info(min_load_greedy_min_sum / all_time)

            print(my_min_sum / all_time)
            logging.info(my_min_sum / all_time)

            print("cam deploy")
            logging.info("cam deploy")

            print(random_min_pi_list)
            logging.info(random_min_pi_list)

            print(max_free_load_greedy_min_pi_list)
            logging.info(max_free_load_greedy_min_pi_list)

            print(min_load_greedy_min_pi_list)
            logging.info(min_load_greedy_min_pi_list)

            print(my_min_pi_list)
            logging.info(my_min_pi_list)

            print(ts_min_pi_list)
            logging.info(ts_min_pi_list)

            print(random_min_pi_sum / all_time)
            logging.info(random_min_pi_sum / all_time)

            print(max_free_load_greedy_min_pi_sum / all_time)
            logging.info(max_free_load_greedy_min_pi_sum / all_time)

            print(min_load_greedy_min_pi_sum / all_time)
            logging.info(min_load_greedy_min_pi_sum / all_time)

            print(my_min_pi_sum / all_time)
            logging.info(my_min_pi_sum / all_time)

            print(ts_min_pi_sum / all_time)
            logging.info(ts_min_pi_sum / all_time)






def get_min_pi(sfc_sets, sfi_sets):
    min_pi = infinate
    for sfc in sfc_sets:
        if sfc == []:
            continue
        tmp = count_pi(sfi_sets, sfc)
        if tmp < min_pi:
            min_pi = tmp
    return min_pi


def count_pi(sfi_sets, sfc):
    sfi_sets = copy.deepcopy(sfi_sets)
    pi_list = []
    for i in range(len(sfc[0])):
        sf_type = sfc[0][i]
        w = sfc[1][i]
        count = 0
        for sfi in sfi_sets:
            if sfi == [] or sfi[1] - sfi[2] < w:
                continue
            if sfi[0] == sf_type and sfc[3] in sfi[3]:
                count += int((sfi[1] - sfi[2]) / w)
        pi_list.append(count)
    min_pi = infinate
    for pi in pi_list:
        if pi < min_pi:
            min_pi = pi
    return min_pi

def run_ts():
    request_num = 20
    my_success_count = 0
    try_dic = {}
    my_success_dic = {}
    sfc_sets = creat_sfc_set_half_random()
    sfi_sets_for_ts= create_sfi_set_half_radom()
    BE_for_ts=count_be(sfc_sets, sfi_sets_for_ts)
    requests=[]
    for i in range(request_num):
        request_index = i % (len(sfc_sets) - 1) + 1
        request = sfc_sets[request_index]
        requests.append(request)
    # print(requests)
    solutions=ts(sfc_requests=requests,sfc_sets=sfc_sets,sfi_sets=sfi_sets_for_ts,BE=BE_for_ts)
    print(solutions)
    sfi_sets_for_ts=solutions[-4]
    # print(try_dic)
    # print(my_success_dic)
    # print(my_success_count)
    pass





def get_min_pi(sfc_sets, sfi_sets):
    min_pi = infinate
    for sfc in sfc_sets:
        if sfc == []:
            continue
        tmp = count_pi(sfi_sets, sfc)
        if tmp < min_pi:
            min_pi = tmp
    return min_pi


def count_pi(sfi_sets, sfc):
    sfi_sets = copy.deepcopy(sfi_sets)
    pi_list = []
    for i in range(len(sfc[0])):
        sf_type = sfc[0][i]
        w = sfc[1][i]
        count = 0
        for sfi in sfi_sets:
            if sfi == [] or sfi[1] - sfi[2] < w:
                continue
            if sfi[0] == sf_type and sfc[3] in sfi[3]:
                count += int((sfi[1] - sfi[2]) / w)
        pi_list.append(count)
    min_pi = infinate
    for pi in pi_list:
        if pi < min_pi:
            min_pi = pi
    return min_pi

def run_ts():
    request_num = 20
    my_success_count = 0
    try_dic = {}
    my_success_dic = {}
    sfc_sets = creat_sfc_set_half_random()
    sfi_sets_for_ts= create_sfi_set_half_radom()
    BE_for_ts=count_be(sfc_sets, sfi_sets_for_ts)
    requests=[]
    for i in range(request_num):
        request_index = i % (len(sfc_sets) - 1) + 1
        request = sfc_sets[request_index]
        requests.append(request)
    # print(requests)
    solutions=ts(sfc_requests=requests,sfc_sets=sfc_sets,sfi_sets=sfi_sets_for_ts,BE=BE_for_ts)
    print(solutions)
    sfi_sets_for_ts=solutions[-4]
    # print(try_dic)
    # print(my_success_dic)
    # print(my_success_count)
    pass

if __name__ == '__main__':
    # run_random_one()
    # run_me_one_time()
    # run_static_demo()
    # run_static_demo2()
    # run_random_demo()
    # run_random_demo_picture()
    # run_random_demo2()
    run_half_random_demo()
    # run_ts()