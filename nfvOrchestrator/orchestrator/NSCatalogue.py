#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : NSCatalogue.py
# @Software: PyCharm

# provider ns life cycle management
class NSManager:
    pass


# provider nsd management ,including nsd curd
class NSDManager:

    NSD_list=[]

    def get_all_nsd(self):
        return NSDManager.NSD_list

    def find_nsd_by_name(self,name):
        for nsd in NSDManager.NSD_list:
            if nsd.name==name:
                return nsd
        return None

    def find_nsd_by_id(self,nsd_id):
        for nsd in NSDManager.NSD_list:
            if nsd.nsd_id==nsd_id:
                return nsd
        return None

    def upload_nsd(self,NSD):
        for nsd in NSDManager.NSD_list:
            if nsd.nsd_id==NSD.nsd_id or nsd.name==NSD.name :
                return False
        return NSDManager.NSD_list.append(NSD)

    def delete_nsd_by_name(self,name):
        for nsd in NSDManager.NSD_list:
            if(nsd.name==name):
                NSDManager.NSD_list.remove(nsd)
                return True
        return False

    def delete_nsd_by_id(self,nsd_id):
        for nsd in NSDManager.NSD_list:
            if(nsd.nsd_id==nsd_id):
                NSDManager.NSD_list.remove(nsd)
                return True
        return False

    def delete_all_nsd(self):
        NSDManager.NSD_list.clear()

    # todo
    def update_nsd(self,old_nsd,new_nsd):
        pass



class NSD:
    def __init__(self,nsd_id,name):
        self.nsd_id=nsd_id
        self.name=name
        self.vnf_list
        self.sfc
        self.fg



class VLD:
    pass

class VNFFGD:
    pass

