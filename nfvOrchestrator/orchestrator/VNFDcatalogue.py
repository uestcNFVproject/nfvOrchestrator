#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFDcatalogue.py
# @Software: PyCharm
import json


# provider VNFD management,inlcuding vnfd curd
class VNFD_manager:

    def __init__(self):
        pass

    VNFD_list=[]

    def get_all_vnfd(self):
        return VNFD_manager.VNFD_list

    def get_vnfd_by_name(self,name):
        for vnfd in VNFD_manager.VNFD_list:
            if vnfd.name==name:
                return vnfd
        return None

    def find_relative_vnfd(self,nsd):
        name_list=nsd.vnf_name_list
        res=[]
        for targer_name in name_list:
            for vnfd in VNFD_manager.VNFD_list:
                if vnfd.name ==targer_name:
                    res.append(vnfd)
        return res

    def upload_vnfd(self,vnfd_to_insert):
        for vnfd in VNFD_manager.VNFD_list:
            if vnfd.name==vnfd_to_insert.name:
                return False
        self.refine_vnfd(vnfd_to_insert)
        VNFD_manager.VNFD_list.append(vnfd)
        return vnfd

    def delete_vnfd(self,vnfd_to_delete):
        for vnfd in VNFD_manager.VNFD_list:
            if(vnfd.name==vnfd_to_delete.name):
                VNFD_manager.VNFD_list.remove(vnfd)
                return True
        return False

    def refine_vnfd(self,vnfd):
        vnfd.vdu_list=self.search_vduin_vnfd(vnfd)
        vnfd.vl_list=self.search_vl_vnfd(vnfd)
        vnfd.flavor_list = self.search_flavor_list_vnfd(vnfd)
        vnfd.cp_list = self.search_cp_list_vnfd(vnfd)

    def search_vdu_in_vnfd(self, vnfd):
        content = json.loads(vnfd.content)
        if "vdu" in content:
            vdu_list = content["vdu"]
            for vdu in vdu_list:
                vnfd.vdu_list.append(vdu)

    def search_vl_in_vnfd(self, vnfd):
        content = json.loads(vnfd.content)
        if "vl" in content:
            vl_list = content["vl"]
            for vl in vl_list:
                vnfd.vl_list.append(vl)

    def search_flavor_in_vnfd(self, vnfd):
        content = json.loads(vnfd.content)
        if "flavor" in content:
            flavor_list = content["flavor"]
            for flavor in flavor_list:
                vnfd.flavor_list.append(flavor)

    def search_cp_in_vnfd(self, vnfd):
        content = json.loads(vnfd.content)
        if "connection-point" in content:
            cp_list = content["connection-point"]
            for cp in cp_list:
                vnfd.cp_list.append(cp)

class VNFD:
    def __init__(self):
        self.name
        self.vnfd_id
        self.type
        self.cpu_request
        self.mem_request
        self.link_request


    pass