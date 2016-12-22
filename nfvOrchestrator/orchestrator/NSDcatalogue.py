#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : NSDcatalogue.py
# @Software: PyCharm

import json
import re
from orchestrator import VNFDcatalogue

# provider ns life cycle management
# !!!每一家的nsd都长的不一样，我该怎么办！！！

# provider nsd management ,including nsd curd
class NSD_manager:
    def __init__(self):
        self.vnfd_manager=VNFDcatalogue.VNFD_manager()

    NSD_list=[]

    def get_all_nsd(self):
        return NSD_manager.NSD_list

    def find_nsd_by_name(self,name):
        for nsd in NSD_manager.NSD_list:
            if nsd.name==name:
                return nsd
        return None

    def upload_nsd(self,NSD):
        for nsd in NSD_manager.NSD_list:
            if nsd.nsd_id==NSD.nsd_id or nsd.name==NSD.name :
                return False
        self.refine_nsd(NSD)
        return NSD_manager.NSD_list.append(NSD)

    def delete_nsd_by_name(self,name):
        for nsd in NSD_manager.NSD_list:
            if(nsd.name==name):
                NSD_manager.NSD_list.remove(nsd)
                return True
        return False

    def delete_all_nsd(self):
        NSD_manager.NSD_list.clear()


    def update_nsd(self,old_nsd,new_nsd):
        pass


    def refine_nsd(self,NSD):
        # 有些nsd包含新的nfd信息，需要提取出来进行注册
        self.register_vnfd(NSD)

        # 根据其余的vnfd——name，提取vnfd
        self.search_vnfd_in_nsd(NSD)

        # 提取fgd的信息
        self.search_fgd_in_nsd(NSD)

        # 提取vld的信息
        self.search_vld_in_nsd(NSD)

    def register_vnfd(self,NSD):
        content = json.loads(NSD.content)
        if "vnfd" in content:
            vnfd__list = content["vnfd"]
            for vnfd in vnfd__list:
                self.vnfd_manager.upload_vnfd(vnfd)
                NSD.vnfd_list.append(vnfd)

    # 搜索标准是vnfd.*:name
    def search_vnfd_in_nsd(self,NSD):
        vnfd_name_list = []
        for m in NSD.vnfd_pattern.finditer(NSD.content):
            vnfd_name_list.append(m.group(1))
        for vnfd_name in vnfd_name_list:
            vnfd = self.vnfd_manager.get_vnfd_by_name(vnfd_name)
            NSD.vnfd_list.append(vnfd)
        return NSD.vnfd_list


    def search_fgd_in_nsd(self,NSD):
        content = json.loads(NSD.content)
        if "vnffgd" in content:
            vnffgd_list = content["vnffgd"]
            for vnffgd in vnffgd_list:
                NSD.vnffgd_list.append(vnffgd)

    def search_vld_in_nsd(self,NSD):
        content = json.loads(NSD.content)
        if "vld" in content:
            vld_list = content["vld"]
            for vld in vld_list:
                NSD.vld_list.append(vld)


class NSD:
    def __init__(self,name,content):
        self.name=name
        self.content=content
        self.vnfd_pattern = re.compile(r'vnfd.*?: \s*(\w*)')


        # 从NSD提取相关信息 todo




class VLD:
    def __init__(self,name,content):
        self.name=name
        self.content=content


class VNFFGD:
    def __init__(self,name,content):
        self.name=name
        self.content=content

    # 从NSD提取相关信息 todo
    def refine(self):
        self.vnf_list
        self.sfc

