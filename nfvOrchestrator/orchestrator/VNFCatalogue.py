#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFCatalogue.py
# @Software: PyCharm



# provider VNFD management,inlcuding vnfd curd
class VNFDManager:

    VNFD_list=[]

    def get_all_vnfd(self):
        return VNFDManager.VNFD_list

    def get_vnfd_by_name(self,name):
        for vnfd in VNFDManager.VNFD_list:
            if vnfd.name==name:
                return vnfd
        return None

    def upload_vnfd(self,vnfd_to_insert):
        for vnfd in VNFDManager.VNFD_list:
            if vnfd.name==vnfd_to_insert.name:
                return False
        return VNFDManager.VNFD_list.append(vnfd)

    def delete_vnfd(self,vnfd_to_delete):
        for vnfd in VNFDManager.VNFD_list:
            if(vnfd.name==vnfd_to_delete.name):
                VNFDManager.VNFD_list.remove(vnfd)
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