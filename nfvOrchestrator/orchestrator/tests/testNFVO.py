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

    def test_all(self):
        nfvo=NFVO()
        vnfd=None
        nsd=None

        # step 1:user upload vnfd nsd vld vnffgd
        nfvo.upload_vnfd(vnfd=vnfd)
        nfvo.upload_nsd(nsd=nsd)

        # step 2 :user send ns deploy requset
        # step 2.1 :compute solution
        # step 2.2:deploy new nets
        # step 2.3:deploy new vms
        # step 2.4:deploy sfc net path
        # step 2.5:deply vnf
        # step 2.6:check vnf state
        # step 2.7 :check ns state
        nfvo.deploy_ns(nsd_name=nsd.nsd_name)

        pass

