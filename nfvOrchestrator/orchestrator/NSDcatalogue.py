#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : NSDcatalogue.py
# @Software: PyCharm

import yaml
import re
from orchestrator import VNFDcatalogue


# provider nsd management ,including nsd curd
class NSD_manager:
    def __init__(self):
        self.vnfd_manager=VNFDcatalogue.VNFD_manager()

    NSD_list=[]

    def get_all_nsd(self):
        return NSD_manager.NSD_list

    def find_nsd_by_id(self,id):
        for nsd in NSD_manager.NSD_list:
            if nsd.id==id:
                return nsd
        return None

    def find_nsd_by_name(self,name):
        for nsd in NSD_manager.NSD_list:
            if nsd.name==name:
                return nsd
        return None

    def upload_nsd(self,NSD):
        for nsd in NSD_manager.NSD_list:
            if nsd.nsd_id==NSD.nsd_id or nsd.name==NSD.name :
                return False
        # self.refine_nsd(NSD)
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


    # def refine_nsd(self,NSD):
    #     # 有些nsd包含新的nfd信息，需要提取出来进行注册
    #     self.register_vnfd(NSD)
    #
    #     # 根据其余的vnfd——name，提取vnfd
    #     self.search_vnfd_in_nsd(NSD)
    #
    #     # 提取fgd的信息
    #     self.search_fgd_in_nsd(NSD)
    #
    #     # 提取vld的信息
    #     self.search_vld_in_nsd(NSD)
    #
    # def register_vnfd(self,NSD):
    #     content = json.loads(NSD.content)
    #     if "vnfd" in content:
    #         vnfd__list = content["vnfd"]
    #         for vnfd in vnfd__list:
    #             self.vnfd_manager.upload_vnfd(vnfd)
    #             NSD.vnfd_list.append(vnfd)
    #
    # # 搜索标准是vnfd.*:name
    # def search_vnfd_in_nsd(self,NSD):
    #     vnfd_name_list = []
    #     for m in NSD.vnfd_pattern.finditer(NSD.content):
    #         vnfd_name_list.append(m.group(1))
    #     for vnfd_name in vnfd_name_list:
    #         vnfd = self.vnfd_manager.get_vnfd_by_name(vnfd_name)
    #         NSD.vnfd_list.append(vnfd)
    #     return NSD.vnfd_list
    #
    #
    # def search_fgd_in_nsd(self,NSD):
    #     content = json.loads(NSD.content)
    #     if "vnffgd" in content:
    #         vnffgd_list = content["vnffgd"]
    #         for vnffgd in vnffgd_list:
    #             NSD.vnffgd_list.append(vnffgd)
    #
    # def search_vld_in_nsd(self,NSD):
    #     content = json.loads(NSD.content)
    #     if "vld" in content:
    #         vld_list = content["vld"]
    #         for vld in vld_list:
    #             NSD.vld_list.append(vld)



    vnffgd_list=[]
    def get_all_vnffgd(self):
        return NSD_manager.NSD_list

    def find_vnffgd_by_name(self,name):
        for vnffgd in NSD_manager.vnffgd_list:
            if vnffgd.name==name:
                return vnffgd
        return None

    def upload_vnffdg(self,vnffgd):
        for tmp in NSD_manager.vnffdg_list:
            if tmp.name==vnffgd.name :
                raise Exception("invalid vnffgd ,name conflict")
        return NSD_manager.vnffdg_list.append(vnffgd)

    def delete_vnffdg_by_name(self,name):
        for tmp in NSD_manager.vnffdg_list:
            if(tmp.name==name):
                NSD_manager.vnffdg_list.remove(tmp)
                return True
        return False

    def delete_all_vnffdg(self):
        NSD_manager.NSD_list.clear()



class NSD:
    def __init__(self,content):
        self.yaml_content=content
        self.dic_content = yaml.load(self.yaml_content)

        if 'metadata' not in self.dic_content or 'ID' not in self.dic_content['metadata']:
            raise Exception("invalid nsd ,no metadata or  ID infomation")
        self.id = self.dic_content['metadata']['ID']

        if 'metadata' not in self.dic_content or 'name' not in self.dic_content['metadata']:
            raise Exception("invalid nsd ,no metadata or  name infomation")
        self.name = self.dic_content['metadata']['name']

        if 'topology_template' not in self.dic_content :
            raise Exception("invalid nsd ,no topology_template ")

        self.vnf_list = []
        for (k, v) in self.dic_content['topology_template'].items():
            if k.startswith('VNF'):
                tmp = {}
                tmp[k] = v
                self.vnf_list.append(tmp)

        self.cp_list = []
        for (k, v) in self.dic_content['topology_template'].items():
            if k.startswith('CP'):
                tmp = {}
                tmp[k] = v
                self.cp_list.append(tmp)

        self.vl_list = []
        for (k, v) in self.dic_content['topology_template'].items():
            if k.startswith('VL'):
                tmp = {}
                tmp[k] = v
                self.vl_list.append(tmp)

        self.fp_list = []
        for (k, v) in self.dic_content['topology_template'].items():
            if k.startswith('Forwarding path'):
                tmp = {}
                tmp[k] = v
                self.fp_list.append(tmp)

        if 'topology_template' not in self.dic_content or 'Groups' not in self.dic_content['topology_template']:
            raise Exception("invalid nsd ,no topology_template  or Groups ")

        self.fp_list = []
        for (k, v) in self.dic_content['topology_template']['Groups'].items():
            if k.startswith('VNFFG'):
                tmp = {}
                tmp[k] = v
                self.fp_list.append(tmp)



class VLD:
    def __init__(self,name,content):
        self.name=name
        self.content=content


class VNFFGD:
    def __init__(self, yaml_content):
        self.yaml_content = yaml_content
        self.dic_content = yaml.load(yaml_content)

        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid vnfd ,no metadata or  name infomation")
        self.name = self.dic_content['metadata']['template_name']

        if 'topology_template' not in self.dic_content or 'node_templates' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  node_templates infomation")

        self.fp_list = []
        for (k, v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('Forwarding_path'):
                tmp = {}
                tmp[k] = v
                self.fp_list.append(tmp)

        self.vnffg_list = []

        if 'topology_template' not in self.dic_content or 'groups' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  groups infomation")

        for (k, v) in self.dic_content['topology_template']['groups'].items():
            if k.startswith('VNFFG'):
                tmp = {}
                tmp[k] = v
                self.vdu_list.append(tmp)
