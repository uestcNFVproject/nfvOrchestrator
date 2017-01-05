#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-22 下午2:39
# @Author  : mengyuGuo
# @Site    : 
# @File    : FG_manager.py
# @Software: PyCharm
from  nfvOrchestrator.orchestrator import OpenDayLightApi
class FG_manager:
    def __init__(self,VIMProxy):
        self.VIMProxy=VIMProxy

    def deploy_vnffg(self,vnffg_solution):
    #     每个vnffg包含一个或多个sfp（sfc）
        for sfp_solution in vnffg_solution.sfp_solution_list:
            self.deploy_sfc(sfp_solution)

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

        return self.VIMProxy.create_sfc(node_list,vnf_list,sff_list,sfc_list,sfp_list,acl_list,rsp,classifier_list)

    def deploy_vnffg(self, vnffg_solution):
        pass


class sfc_instances:
    pass

class vnffg_instances:
    pass