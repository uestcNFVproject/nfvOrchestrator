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
from orchestrator.models import Descriptor
next_nsd_id=0
def get_next_nsd_id():
    global next_nsd_id
    next_nsd_id+=1
    return next_nsd_id

def set_next_nsd_id(next_id):
    global next_nsd_id
    next_nsd_id=next_id

next_vnffgd_id=0
def get_next_vnffgd_id():
    global next_vnffgd_id
    next_vnffgd_id+=1
    return next_vnffgd_id

def set_next_vnffgd_id(next_id):
    global next_vnffgd_id
    next_vnffgd_id=next_id



# provider nsd management ,including nsd curd
class NSD_manager:
    def __init__(self):
        # 从数据库中读取已有NSD和VNFFGD
        # 0==》nsd
        # 2==>vnffgd
        max_assigned_id = -1
        nsd_in_db = Descriptor.objects.filter(type=0).values_list('assigned_id', 'yaml_content')
        for e in nsd_in_db:
            nsd_to_insert = NSD()
            nsd_to_insert.init_from_db(e[1], e[0])
            if (int(e[0]) > max_assigned_id):
                max_assigned_id = int(e[0])
            NSD_manager.NSD_list.append(nsd_to_insert)
        if max_assigned_id != -1:
            set_next_nsd_id(max_assigned_id + 1)

        max_assigned_id = -1
        vnffgd_in_db = Descriptor.objects.filter(type=2).values_list('assigned_id', 'yaml_content')
        for e in vnffgd_in_db:
            vnffgd_to_insert = VNFFGD()
            vnffgd_to_insert.init_from_db(e[1], e[0])
            if (int(e[0]) > max_assigned_id):
                max_assigned_id = int(e[0])
            NSD_manager.VNFFGD_list.append(vnffgd_to_insert)
        if max_assigned_id != -1:
            set_next_vnffgd_id(max_assigned_id + 1)

        print('nsd manager init over ')

    def set_vnfd_catalogue(self,vnfd_manager):
        self.vnfd_manager = vnfd_manager


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

    def upload_nsd(self,nsd_content):
        nsd_to_insert=NSD()
        nsd_to_insert.init_from_web(nsd_content)
        for nsd in NSD_manager.NSD_list:
            if nsd.name==nsd_to_insert.name :
                raise Exception("invalid nsd ,name conflict")
        NSD_manager.NSD_list.append(nsd_to_insert)
        # 生成模型，存储到数据库
        descriptor = Descriptor()
        descriptor.type = 0
        descriptor.yaml_content = nsd_content
        descriptor.assigned_id = nsd_to_insert.nsd_id
        descriptor.save()




    def delete_nsd_by_name(self,name):
        for nsd in NSD_manager.NSD_list:
            if(nsd.name==name):
                NSD_manager.NSD_list.remove(nsd)
                Descriptor.objects.filter(type=1).filter(assigned_id=nsd.nsd_id).delete()
                return True
        return False

    def delete_all_nsd(self):
        NSD_manager.NSD_list.clear()


    def update_nsd(self,old_nsd,new_nsd):
        pass






    vnffgd_list=[]
    def get_all_vnffgd(self):
        return NSD_manager.NSD_list

    def find_vnffgd_by_name(self,name):
        for vnffgd in NSD_manager.vnffgd_list:
            if vnffgd.name==name:
                return vnffgd
        return None

    def upload_vnffdg(self,vnffgd_content):
        vnffgd=VNFFGD()
        vnffgd.init_from_web(vnffgd_content)
        for tmp in NSD_manager.vnffdg_list:
            if tmp.name==vnffgd.name :
                raise Exception("invalid vnffgd ,name conflict")
        return NSD_manager.vnffdg_list.append(vnffgd)
        NSD_manager.NSD_list.append(nsd_to_insert)
        # 生成模型，存储到数据库
        descriptor = Descriptor()
        descriptor.type = 2
        descriptor.yaml_content = vnffgd_content
        descriptor.assigned_id = vnffgd.vnffgd_id
        descriptor.save()

    def delete_vnffdg_by_name(self,name):
        for tmp in NSD_manager.vnffdg_list:
            if(tmp.name==name):
                NSD_manager.vnffdg_list.remove(tmp)
                Descriptor.objects.filter(type=2).filter(assigned_id=tmp.vnffgd_id).delete()
                return True
        return False

    def delete_all_vnffdg(self):
        NSD_manager.NSD_list.clear()


# 先从数据库获取最大的nsd的assigned_id


class NSD:
    def __init__(self):
        pass

    # 通过网页接口上传VNFFGD文件内容，分配id并进行解析
    def init_from_web(self,content):
        self.yaml_content=content
        self.nsd_id=get_next_nsd_id()
        self.dic_content = yaml.load(self.yaml_content)

        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid nsd ,no metadata or  template_name infomation")
        self.name = self.dic_content['metadata']['template_name']


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

        self.vnffg_list = []
        for (k, v) in self.dic_content['topology_template']['Groups'].items():
            if k.startswith('VNFFG'):
                tmp = {}
                tmp[k] = v
                self.vnffg_list.append(tmp)



    # 通过数据库上传已经加载的NSD文件内容，进行解析重铸
    def init_from_db(self,content,id):
        self.yaml_content=content
        self.nsd_id=id
        self.dic_content = yaml.load(self.yaml_content)

        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid nsd ,no metadata or  template_name infomation")
        self.name = self.dic_content['metadata']['template_name']



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

        self.vnffg_list = []
        for (k, v) in self.dic_content['topology_template']['Groups'].items():
            if k.startswith('VNFFG'):
                tmp = {}
                tmp[k] = v
                self.vnffg_list.append(tmp)

class VLD:
    def __init__(self,name,content):
        self.name=name
        self.content=content

# 先从数据库获取最大的vnffgd的assigned_id


class VNFFGD:
    def __init__(self):
        pass
    # 通过网络接口上传VNFFGD，分配id，并进行解析
    def init_from_web(self, yaml_content):
        self.yaml_content = yaml_content
        self.vnffgd_id=get_next_vnffgd_id()
        self.dic_content = yaml.load(yaml_content)

        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid vnfd ,no metadata or  name infomation")
        self.name = self.dic_content['metadata']['template_name']

        if 'topology_template' not in self.dic_content or 'node_templates' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  node_templates infomation")

        self.fp_list = []
        self.fp_vnfd_dic={}
        for (k, v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('Forwarding_path'):
                tmp = {}
                tmp[k] = v
                self.fp_list.append(tmp)
                vnfd_list=[]
                forward_list=v["properties"]["path"]
                for forward in forward_list:
                    vnfd_name=forward["forwarder"]
                    vnfd_list.append(vnfd_name)
                self.fp_vnfd_dic[tmp]=vnfd_list

        self.vnffg_list = []


        if 'topology_template' not in self.dic_content or 'groups' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  groups infomation")

        for (k, v) in self.dic_content['topology_template']['groups'].items():
            if k.startswith('VNFFG'):
                tmp = {}
                tmp[k] = v
                self.vnffg_list.append(tmp)

    # 通过数据库上传VNFFGD，并进行解析
    def init_from_db(self, yaml_content,id):
        self.yaml_content = yaml_content
        self.vnffgd_id=id
        self.dic_content = yaml.load(yaml_content)

        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid vnfd ,no metadata or  name infomation")
        self.name = self.dic_content['metadata']['template_name']

        if 'topology_template' not in self.dic_content or 'node_templates' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  node_templates infomation")

        self.fp_list = []
        self.fp_vnfd_dic={}
        for (k, v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('Forwarding_path'):
                tmp = {}
                tmp[k] = v
                self.fp_list.append(tmp)
                vnfd_list=[]
                forward_list=v["properties"]["path"]
                for forward in forward_list:
                    vnfd_name=forward["forwarder"]
                    vnfd_list.append(vnfd_name)
                self.fp_vnfd_dic[tmp]=vnfd_list

        self.vnffg_list = []


        if 'topology_template' not in self.dic_content or 'groups' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  groups infomation")

        for (k, v) in self.dic_content['topology_template']['groups'].items():
            if k.startswith('VNFFG'):
                tmp = {}
                tmp[k] = v
                self.vnffg_list.append(tmp)