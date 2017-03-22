#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-22 下午2:39
# @Author  : mengyuGuo
# @Site    : 
# @File    : FG_manager.py
# @Software: PyCharm
from  orchestrator import OpenDayLightApi
from orchestrator.models import rsp
import re
class FG_manager:

    # sf的ip与sff的关系，这个应该有nfvi来管理，sf的ip为计算节点的ip，sff的name为路由节点的name
    ip_sffName_dic={}
    ip_sffName_dic["192.168.1.215"]='SFF1'
    ip_sffName_dic["192.168.1.214"] = 'SFF1'
    ip_sffName_dic["192.168.1.211"] = 'SFF1'
    ip_sffName_dic["192.168.1.208"] = 'SFF1'
    ip_sffName_dic["192.168.1.204"] = 'SFF1'

    @staticmethod
    def convert_rsp_name_to_rsp_id(rsp_name):
        # rsp中间有数字,把数字提取出来
        pattern = re.compile(r'\d+')
        match = pattern.search(rsp_name)
        if match:
            # 使用Match获得分组信息
            return (match.group())
        return None

    @staticmethod
    def convert_vnf_list_to_sfNameList(vnf_list):
        sf_name_list=[]
        for vnf in vnf_list:
            sf_name_list.append(vnf.vnf_name)
            vnf_list.append(vnf)
        return sf_name_list

    def get_sff_name(self,sf_ip):
        return FG_manager.ip_sffName_dic[sf_ip]

    def __init__(self):
        pass

    def set_nfvo(self,nfvo):
        self.nfvo=nfvo

    # do it with vim (odl)
    def deploy_sfc(self,sfc_solution):
        # 存储rsp info
        for rsp in sfc_solution.rsp_list:
            rsp_name=rsp.name
            sfp_name=rsp.sfp
            sfc_name=None
            vnf_list=None
            for sfp in sfc_solution.sfp_list:
                if sfp.sfp_name==sfp_name:
                    sfc_name=sfp.sfc_name
                    break
            for sfc in sfc_solution.sfc_list:
                if sfc.name==sfc_name:
                    vnf_list=sfc.vnf_list

            rsp_info=rsp()
            rsp_info.rspRequestId=FG_manager.convert_rsp_name_to_rsp_id(rsp_name)
            rsp_info.sfNameList=FG_manager.convert_vnf_list_to_sfNameList(vnf_list)
            rsp_info.save()


        # 向odl发送
        node_list=sfc_solution.node_list
        vnf_list=sfc_solution.vnf_list
        sff_list=sfc_solution.sff_list
        sfc_list=sfc_solution.sfc_list
        sfp_list=sfc_solution.sfp_list
        acl_list=sfc_solution.acl_list
        rsp_list=sfc_solution.rsp_list
        classifier_list=sfc_solution.classifier_list

        OpenDayLightApi.register_nodes(node_list)
        OpenDayLightApi.register_vnfs(vnf_list)
        OpenDayLightApi.register_sffs(sff_list)
        OpenDayLightApi.register_sfcs(sfc_list)
        OpenDayLightApi.register_sf_metadata_data()
        OpenDayLightApi.register_sfps(sfp_list)
        OpenDayLightApi.register_acls(acl_list)
        OpenDayLightApi.register_rsp(rsp_list)
        OpenDayLightApi.register_classifiers(classifier_list)

        sfc_instance=Sfc_instance(node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp_list,classifier_list)


        return self.nfvo.create_sfc(node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp_list,classifier_list)




class Sfc_instance:
    def __init__(self,node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp_list,classifier_list):
        self.node_list=node_list
        self.vnf_list=vnf_list
        self.sff_list=sff_list
        self.sfc_list=sfc_list
        self.sfp_list=sfp_list
        self.acl_list=acl_list
        self.rsp_list=rsp_list
        self.classifier_list=classifier_list


