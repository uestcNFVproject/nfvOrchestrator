#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-22 下午4:52
# @Author  : mengyuGuo
# @Site    : 
# @File    : testNSDcatalogue.py
# @Software: PyCharm

import  json

from django.test import TestCase

class myTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_contains_new_vnfd(self):
        content='''{
   "name":"iperf-NS",
   "vendor":"Fokus",
   "version":"0.1",
   "vnfd":[
      {
         "vendor":"tbr",
         "version":"0.1",
         "name":"iperf-server",
         "type":"server",
         "endpoint":"generic",
         "configurations":{
            "name":"config_name",
            "configurationParameters":[]
         },
         "vdu":[
            {
               "vm_image":[
                  "ubuntu-14.04-server-cloudimg-amd64-disk1"
               ],
               "vimInstanceName":["vim-instance"],
               "scale_in_out":1,
               "vnfc":[
                  {
                     "connection_point":[
                        {
                           "virtual_link_reference":"private"
                        }
                     ]
                  }
               ]
            }
         ],
         "virtual_link":[
            {
               "name":"private"
            }
         ],
         "lifecycle_event":[
            {
               "event":"INSTANTIATE",
               "lifecycle_events":[
                  "install.sh",
          "start-srv.sh"
               ]
            }
         ],
         "deployment_flavour":[
            {
               "flavour_key":"m1.small"
            }
         ],
            "vnfPackageLocation":"https://github.com/openbaton/vnf-scripts.git"

      },
      {
         "vendor":"tbr",
         "version":"0.1",
         "name":"iperf-client",
         "type":"client",
         "endpoint":"generic",
         "configurations":{
            "name":"config_name",
            "configurationParameters":[

            ]
         },
         "vdu":[
            {
               "vm_image":[
                  "ubuntu-14.04-server-cloudimg-amd64-disk1"
               ],
               "vimInstanceName":["vim-instance"],
               "scale_in_out":2,
               "vnfc":[
                  {
                     "connection_point":[
                        {
                           "floatingIp":"random",
                           "virtual_link_reference":"private"
                        }
                     ]
                  },
                  {
                     "connection_point":[
                        {
                           "floatingIp":"random",
                           "virtual_link_reference":"private"
                        }
                     ]
                  }
               ]
            }
         ],
         "virtual_link":[
            {
               "name":"private"
            }
         ],
         "lifecycle_event":[
            {
               "event":"INSTANTIATE",
               "lifecycle_events":[
                  "install.sh"
               ]
            },
            {
               "event":"CONFIGURE",
               "lifecycle_events":[
                  "server_start-clt.sh"
               ]
            }
         ],
         "deployment_flavour":[
            {
               "flavour_key":"m1.small"
            }
         ],
          "vnfPackageLocation":"https://github.com/openbaton/vnf-scripts.git"
      }
   ],
   "vnffgd":[

   ],
   "vld":[
      {
         "name":"private"
      }
   ],
   "vnf_dependency":[
      {
         "source":{
            "name":"iperf-server"
         },
         "target":{
            "name":"iperf-client"
         },
         "parameters":[
            "private"
         ]
      }
   ]
}'''
        content_json=json.loads(content)
        print("vnfd" in content_json)