#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-22 下午2:39
# @Author  : mengyuGuo
# @Site    : 
# @File    : FG_manager.py
# @Software: PyCharm
from  orchestrator import OpenDayLightApi
class FG_manager:
    # sf的ip与sff的关系，这个应该有nfvi来管理，sf的ip为计算节点的ip，sff的name为路由节点的name
    ip_sffName_dic={}
    ip_sffName_dic["192.168.1.215"]='SFF1'
    ip_sffName_dic["192.168.1.214"] = 'SFF1'
    ip_sffName_dic["192.168.1.211"] = 'SFF1'
    ip_sffName_dic["192.168.1.208"] = 'SFF1'
    ip_sffName_dic["192.168.1.204"] = 'SFF1'

    def get_sff_name(self,sf_ip):
        return FG_manager.ip_sffName_dic[sf_ip]

    def __init__(self):
        pass

    def set_nfvo(self,nfvo):
        self.nfvo=nfvo

    # do it with vim (odl)
    def deploy_sfc(self,sfc_solution):

        node_list=sfc_solution.node_list
        vnf_list=sfc_solution.vnf_list
        sff_list=sfc_solution.sff_list
        sfc_list=sfc_solution.sfc_list
        sfp_list=sfc_solution.sfp_list
        acl_list=sfc_solution.acl_list
        rsp=sfc_solution.rsp
        classifier_list=sfc_solution.classifier_list

        OpenDayLightApi.register_nodes(node_list)
        OpenDayLightApi.register_vnfs(vnf_list)
        OpenDayLightApi.register_sffs(sff_list)
        OpenDayLightApi.register_sfcs(sfc_list)
        OpenDayLightApi.register_sf_metadata_data()
        OpenDayLightApi.register_sfps(sfp_list)
        OpenDayLightApi.register_acls(acl_list)
        OpenDayLightApi.register_rsp(rsp)
        OpenDayLightApi.register_classifiers(classifier_list)

        sfc_instance=Sfc_instance(node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp,classifier_list)


        return self.nfvo.create_sfc(node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp,classifier_list)




class Sfc_instance:
    def __init__(self,node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp,classifier_list):
        self.node_list=node_list
        self.vnf_list=vnf_list
        self.sff_list=sff_list
        self.sfc_list=sfc_list
        self.sfp_list=sfp_list
        self.acl_list=acl_list
        self.rsp=rsp
        self.classifier_list=classifier_list


