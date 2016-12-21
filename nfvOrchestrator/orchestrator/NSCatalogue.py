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

    def get_all_nsd(self):
        pass

    def get_nsd_by_name(self,name):
        pass

    def get_nsd_by_id(self,nsd_id):
        pass

    def add_nsd(self,NSD):
        pass

    def delete_nsd_by_name(self,name):
        pass

    def delete_nsd_by_id(self,nsd_id):
        pass

    def delete_all_nsd(self):
        pass

    def update_nsd(self,old_nsd,new_nsd):
        pass



class NSD:
    def __init__(self,nsd_id,name):
        pass

class VLD:
    pass

class VNFFGD:
    pass

