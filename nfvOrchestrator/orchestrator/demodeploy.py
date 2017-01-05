#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/5 9:58
# @Author  : mengyuGuo
# @Site    : 
# @File    : demodeploy.py
# @Software: PyCharm

# webdemo目前是vnffgd
# imsdemo目前是vnfd


from orchestrator import NFVO
from orchestrator import systemSettings
class Demo_deploy:
    def __init__(self):
        self.nfvo=NFVO.get_NFVO()
        # 上传webdemo的vnfd
        web_demo_vnfd_path_list=systemSettings.web_demo_vnfd_path_list.split(";")
        for path in web_demo_vnfd_path_list:
            web_demo_vnfd_path = path
            web_demo_vnfd_content = open(web_demo_vnfd_path).read()
            self.nfvo.upload_nsd(web_demo_vnfd_content)

        # 上传webdemo的vnffgd
        web_demo_vnffgd_path=systemSettings.web_demo_nsd_path
        web_demo_vnffgd_content = open(web_demo_vnffgd_path).read()
        self.nfvo.upload_nsd(web_demo_vnffgd_content)

        # 上传imsdemo的vnfd
        ims_demo_vnfd_path = systemSettings.ims_demo_nsd_path
        ims_demo_vnfd_content = open(ims_demo_vnfd_path).read()
        self.nfvo.upload_nsd(ims_demo_vnfd_content)
        pass
    def deploy_demo(self,demotype):
        print("demotype:" + str(demotype))
        result = {
            'webdemo': lambda x: self.deploy_webdemo(),
            'imsdemo': lambda x: self.deploy_imsdemo()
        }[demotype](demotype)
        print(result)

    def deploy_webdemo(self):
        # 获取webdemo的vnffgd
        web_demo_vnffgd=self.nfvo.find_vnffgd_by_name(systemSettings.web_demo_vnffgd_name)
        return self.nfvo.deploy_vnffgd(web_demo_vnffgd)


    def deploy_imsdemo(self):
        # 获取imsdemo的NSD
        ims_demo_nsd=self.nfvo.find_nsd_by_id(systemSettings.ims_demo_nsd_id)
        return self.nfvo.deploy_ns(ims_demo_nsd)