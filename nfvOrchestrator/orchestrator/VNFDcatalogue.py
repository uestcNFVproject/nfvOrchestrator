#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午4:30
# @Author  : mengyuGuo
# @Site    :
# @File    : VNFDcatalogue.py
# @Software: PyCharm
import yaml
from orchestrator.models import Descriptor


# 先从数据库获取最大的vnfd的assigned_id
next_vnfd_id=0
def set_next_id(next_id):
    global next_vnfd_id
    next_vnfd_id=next_id

def get_next_id():
    global next_vnfd_id
    next_vnfd_id+=1
    return next_vnfd_id

# provider VNFD management,inlcuding vnfd curd
class VNFD_manager:

    def __init__(self):
        # 从数据库读取
        max_assigned_id=-1
        vnfd_in_db=Descriptor.objects.filter(type=1).values_list('assigned_id','yaml_content')
        for e in vnfd_in_db:
            vnfd_to_insert = VNFD()
            vnfd_to_insert.init_from_db(e[1],e[0])
            if(int(e[0])>max_assigned_id):
                max_assigned_id=int(e[0])
            VNFD_manager.VNFD_list.append(vnfd_to_insert)
        if max_assigned_id!=-1:
            set_next_id(max_assigned_id+1)
        print('vnfd manager init over ')
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

    def upload_vnfd(self,vnfd_content):
        vnfd_to_insert=VNFD()
        vnfd_to_insert.init_from_web(vnfd_content)
        for vnfd in VNFD_manager.VNFD_list:
            if vnfd.name==vnfd_to_insert.name:
                raise Exception("invalid vnfd ,name conflict")
        VNFD_manager.VNFD_list.append(vnfd_to_insert)
        # 生成模型，存储到数据库
        descriptor=Descriptor()
        descriptor.type=1
        descriptor.yaml_content = vnfd_content
        descriptor.assigned_id=vnfd_to_insert.vnfd_id
        descriptor.save()


    def delete_vnfd(self,vnfd_to_delete):
        print(vnfd_to_delete)
        for vnfd in VNFD_manager.VNFD_list:
            if(vnfd.name==vnfd_to_delete.name):
                VNFD_manager.VNFD_list.remove(vnfd)
                Descriptor.objects.filter(type=1).filter(assigned_id=vnfd.vnfd_id).delete()
                return True
        raise Exception("no match  vnfd name")



class VNFD:
    def __init__(self):
        pass
    # 通过接口上传VNFD，分配vnfd_id，并解析
    def init_from_web(self, yaml_content):
        print('__init__1')
        # 存入数据库的信息
        self.yaml_content = yaml_content
        # 分配id
        self.vnfd_id = get_next_id()
        # 根据yaml提取
        self.dic_content = yaml.load(yaml_content)
        if not isinstance(self.dic_content, dict):
            raise Exception("invalid yaml")
        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid vnfd ,no metadata or  name infomation")
        self.name = self.dic_content['metadata']['template_name']

        if 'types' not in self.dic_content:
            raise Exception("invalid vnfd ,no type infomation")
        self.type = self.dic_content['types']

        if 'topology_template' not in self.dic_content or 'node_templates' not in self.dic_content['topology_template']:
            raise Exception("invalid vnfd ,no topology_template or  node_templates infomation")

        self.vdu_list = []
        for (k, v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('VDU'):
                tmp = {}
                tmp[k] = v
                self.vdu_list.append(tmp)

        self.cp_list = []

        for (k, v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('CP'):
                tmp = {}
                tmp[k] = v
                self.vdu_list.append(tmp)

        self.vl_list = []
        for (k, v) in self.dic_content['topology_template']['node_templates'].items():
            if k.startswith('VL'):
                tmp = {}
                tmp[k] = v
                self.vdu_list.append(tmp)
        # 如果解决方案中得出该VNFD的部署需要新的VNF载体，那么不设置此位，否则设置为复用的载体id
        self.vnf_carrier = None

    # 从数据库读取，重建VNFD对象
    def init_from_db(self,yaml_content,id):
        print('__init__2')
        # 存入数据库的信息
        self.yaml_content = yaml_content
        self.vnfd_id = id
        # 根据yaml
        self.dic_content = yaml.load(yaml_content)
        if not isinstance(self.dic_content,dict):
            raise Exception("invalid yaml")
        if 'metadata' not in self.dic_content or 'template_name' not in self.dic_content['metadata']:
            raise Exception("invalid vnfd ,no metadata or  name infomation")
        self.name=self.dic_content['metadata']['template_name']

        if 'types' not in self.dic_content :
            raise Exception("invalid vnfd ,no type infomation")
        self.type=self.dic_content['types']


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
        # 如果解决方案中得出该VNFD的部署需要新的VNF载体，那么不设置此位，否则设置为复用的载体id
        self.vnf_carrier=None
        pass
