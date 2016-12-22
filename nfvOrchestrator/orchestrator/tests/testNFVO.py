#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-21 下午11:04
# @Author  : mengyuGuo
# @Site    : 
# @File    : testNFVO.py
# @Software: PyCharm
from django.test import TestCase
from orchestrator.NFVO import NFVO

class myTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    '''
    Step 1: NFVO从NSD catalogue和VNFD catalogue获取相关NSD和VNFD
    Step 2: 调用Algorithm Manager进行调度，Algorithm Manager根据NS catalogue和NFVI catalogue获取现有NS服务运行情况和底层NFVI资源情况，根据设定的算法计算出部署方案
    Step 3: NFVO根据部署方案，调用VNFM创建网络和VNF，VNFM根据方案创建VNF实例：如果需要，调用VIM创建新VM来承载VNF实例，如果复用旧VM，在旧VM上部署相关VNF实例。创建好vm后，VNFM对VM进行初始化配置。
    Step 4：NFVO根据部署方案，调用FG Manager创建NS所需的网络转发链路
    Step 5：创建好vm和ns的net后，NFVO根据部署方案，调用VNFM对VNF进行检测
    Step 6：NFVO对NS服务进行检测

    '''
    # def test_all(self):
    #     nfvo=NFVO()
    #     vnfd=None
    #     nsd=None
    #     nfvo.upload_vnfd(vnfd=vnfd)
    #     nfvo.upload_nsd(nsd=nsd)
    #     nfvo.deploy_ns(nsd_name=nsd.nsd_name)
    #
    #     pass



