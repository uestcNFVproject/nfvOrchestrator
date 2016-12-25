#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFDcatalogue.py
# @Software: PyCharm
import yaml


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
                raise Exception("invalid vnfd ,name conflict")
        VNFD_manager.VNFD_list.append(vnfd)
        return vnfd

    def delete_vnfd(self,vnfd_to_delete):
        for vnfd in VNFD_manager.VNFD_list:
            if(vnfd.name==vnfd_to_delete.name):
                VNFD_manager.VNFD_list.remove(vnfd)
                return True
        return False


class VNFD:
    def __init__(self,yaml_content):
        self.yaml_content = yaml_content
        self.dic_content = yaml.load(yaml_content)

        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid vnfd ,no metadata or  name infomation")
        self.name=self.dic_content['metadata']['template_name']

        if 'types' not in self.dic_content :
            raise Exception("invalid vnfd ,no type infomation")
        self.type=self.dic_content['node types']


        if 'topology_template' not in self.dic_content or 'node_templates' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  node_templates infomation")

        self.vdu_list = []
        for (k,v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('VDU'):
                tmp={}
                tmp[k]=v
                self.vdu_list.append(tmp)

        self.cp_list=[]

        for (k,v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('CP'):
                tmp={}
                tmp[k]=v
                self.vdu_list.append(tmp)

        self.vl_list = []
        for (k,v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('VL'):
                tmp={}
                tmp[k]=v
                self.vdu_list.append(tmp)
