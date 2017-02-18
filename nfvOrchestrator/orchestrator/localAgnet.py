#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:15
# @Author  : mengyuGuo
# @Site    : 
# @File    : localAgnet.py
# @Software: PyCharm
import os
import time
import re
import json
import requests
monitor_ip='127.0.0.1'
monitor_PORT='8181'
monitor_url='/node_info/details/'
# monitor_url='/test/'
def get(host, port, uri):
    url='http://'+host+":"+port+uri
    r = requests.get(url)
    print(r)
    jsondata=json.loads(r.text)
    return jsondata

def put(host, port, uri, data, debug=False):
    '''Perform a PUT rest operation, using the URL and data provided'''

    url='http://'+host+":"+port+uri
    if debug == True:
        print("PUT %s" % url)
        print(json.dumps(data, indent=4, sort_keys=True))
    r = requests.put(url, data=json.dumps(data))
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
        print(json.dumps(data, indent=4, sort_keys=True))
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r)
    if debug == True:
        print(r.text)
    r.raise_for_status()
    time.sleep(5)


def get_node_info():
    res=get(monitor_ip,monitor_PORT,monitor_url)
    print(res)

# 无限循环，调用命令收集信息，发送给指定web接口
def post_node_info():
    time2sleep = 5
    while True:
        top_res = os.popen('top -bi -n 2').read()
        io_res = os.popen('iostat').read()
        df_res = os.popen('df -hl').read()
        # 处理top_res
        NodeName = 'node-50'
        top_res_spilt = top_res.split('top - ')[2].split('\n')
        first_line = top_res_spilt[0]

        first_line_split = re.split(' +', first_line)
        BaseInfo = {}
        Time = first_line_split[0]

        RunTime = first_line_split[2].rstrip(',')+first_line_split[3].rstrip(',')
        BaseInfo['Time'] = Time
        BaseInfo['RunTime'] = RunTime
        BaseInfo['NodeName'] = NodeName

        LoadInfo = {}
        Load1 = first_line_split[8].rstrip(',')
        Load5 = first_line_split[9].rstrip(',')
        Load15 = first_line_split[10].rstrip(',')
        LoadInfo['Load1'] = Load1
        LoadInfo['Load5'] = Load5
        LoadInfo['Load15'] = Load15

        second_line = top_res_spilt[1].rstrip(',')
        second_line_split = re.split(' +', second_line)

        TaskInfo = {}
        Taskstotal = second_line_split[1].rstrip(',')
        TaskRunning = second_line_split[3].rstrip(',')
        TaskSleeping = second_line_split[5].rstrip(',')
        TaskStopped = second_line_split[7].rstrip(',')
        Taskzombie = second_line_split[9].rstrip(',')
        TaskInfo['Taskstotal'] = Taskstotal
        TaskInfo['TaskRunning'] = TaskRunning
        TaskInfo['TaskSleeping'] = TaskSleeping
        TaskInfo['TaskStopped'] = TaskStopped
        TaskInfo['Taskzombie'] = Taskzombie

        third_line = top_res_spilt[2]
        third_line_split = re.split(' +', third_line)

        CpuInfo = {}
        Us = third_line_split[1].rstrip(',')
        Sy = third_line_split[3].rstrip(',')
        Ni = third_line_split[5].rstrip(',')
        Idle = third_line_split[7].rstrip(',')
        Wa = third_line_split[9].rstrip(',')
        Hi = third_line_split[11].rstrip(',')
        Si = third_line_split[13].rstrip(',')
        CpuInfo['Us'] = Us
        CpuInfo['Sy'] = Sy
        CpuInfo['Ni'] = Ni
        CpuInfo['Idle'] = Idle
        CpuInfo['Wa'] = Wa
        CpuInfo['Hi'] = Hi
        CpuInfo['Si'] = Si

        fourth_line = top_res_spilt[3]
        fourth_line_split = re.split(' +', fourth_line)

        MemInfo = {}
        Memtotal = fourth_line_split[2].rstrip(',')
        Memused = fourth_line_split[4].rstrip(',')
        Memfree = fourth_line_split[6].rstrip(',')
        Membuffer = fourth_line_split[8].rstrip(',')
        MemInfo['Memtotal'] = Memtotal
        MemInfo['Memused'] = Memused
        MemInfo['Memfree'] = Memfree
        MemInfo['Membuffer'] = Membuffer

        # 处理df_res

        DiskInfo = {}
        df_res_spilt = df_res.split('\n')
        for i in range(1, len(df_res_spilt) - 1):
            line = re.split(' +', df_res_spilt[i])
            # print(line)
            FileSysName = line[0]
            FileSysTotal = line[1]
            FileSysFree = line[2]
            MountPoint = line[3]
            DiskInfo[FileSysName] = {'FileSysTotal': FileSysTotal, 'FileSysFree': FileSysFree, 'MountPoint': MountPoint}
        # 处理io_res
        io_res_spilt = io_res.split('\n')

        IOinfo = {}
        first_line = re.split(' +', io_res_spilt[6])
        DeviceName = first_line[0]
        Tps = first_line[1]
        ReadSpeed = first_line[2]
        ReadToral = first_line[3]
        WriteSpeed = first_line[4]
        WriteTotal = first_line[5]
        IOinfo[DeviceName] = {'Tps': Tps, 'ReadSpeed': ReadSpeed, 'ReadToral': ReadToral, 'WriteSpeed': WriteSpeed,
                              'WriteTotal': WriteTotal}

        second_line = re.split(' +', io_res_spilt[7])
        DeviceName = second_line[0]
        Tps = second_line[1]
        ReadSpeed = second_line[2]
        ReadToral = second_line[3]
        WriteSpeed = second_line[4]
        WriteTotal = second_line[5]
        IOinfo[DeviceName] = {'Tps': Tps, 'ReadSpeed': ReadSpeed, 'ReadToral': ReadToral, 'WriteSpeed': WriteSpeed,
                              'WriteTotal': WriteTotal}

        info_dic = {'BaseInfo': BaseInfo, 'LoadInfo': LoadInfo, 'TaskInfo': TaskInfo, 'CpuInfo': CpuInfo,
                    'MemInfo': MemInfo, 'DiskInfo': DiskInfo, 'IOinfo': IOinfo}
        # json_info=json.dumps(info_dic)
        post(monitor_ip, monitor_PORT, monitor_url, info_dic)
        print(Time + ' send node info：')
        print(json.dumps(info_dic))
        time.sleep(time2sleep)


if __name__ == '__main__':
    get_node_info()