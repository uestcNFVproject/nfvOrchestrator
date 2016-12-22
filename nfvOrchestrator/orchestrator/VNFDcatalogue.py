#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFDcatalogue.py
# @Software: PyCharm



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
        return VNFD_manager.VNFD_list.append(vnfd)

    def delete_vnfd(self,vnfd_to_delete):
        for vnfd in VNFD_manager.VNFD_list:
            if(vnfd.name==vnfd_to_delete.name):
                VNFD_manager.VNFD_list.remove(vnfd)
                return True
        return False

#
class VNFD:
    def __init__(self):
        self.name
        self.vnfd_id
        self.type
        self.cpu_request
        self.mem_request
        self.link_request


    pass