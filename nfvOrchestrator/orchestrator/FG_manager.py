#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-22 下午2:39
# @Author  : mengyuGuo
# @Site    : 
# @File    : FG_manager.py
# @Software: PyCharm

class FG_manager:
    def __init__(self,VIMProxy):
        self.VIMProxy=VIMProxy
    pass
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

        return self.VIMProxy.create_sfc(node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp,classifier_list)
