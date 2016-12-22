#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16-12-22 下午8:32
# @Author  : mengyuGuo
# @Site    : 
# @File    : nsd_example.py
# @Software: PyCharm

{
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
}




nsd:nsd-catalog:
    nsd:
    -   id: cirros_2vnf_nsd
        name: cirros_2vnf_nsd
        short-name: cirros_2vnf_nsd
        description: Generated by OSM pacakage generator
        vendor: OSM
        version: '1.0'

        # Place the logo as png in icons directory and provide the name here
        logo: osm_2x.png

        # Specify the VNFDs that are part of this NSD
        constituent-vnfd:
            # The member-vnf-index needs to be unique, starting from 1
            # vnfd-id-ref is the id of the VNFD
            # Multiple constituent VNFDs can be specified
        -   member-vnf-index: 1
            vnfd-id-ref: cirros_vnfd
        -   member-vnf-index: 2
            vnfd-id-ref: cirros_vnfd


        vld:
        # Networks for the VNFs
            -   id: cirros_2vnf_nsd_vld1
                name: cirros_2vnf_nsd_vld1
                short-name: cirros_2vnf_nsd_vld1
                type: ELAN
                # vim-network-name: <update>
                # provider-network:
                #     overlay-type: VLAN
                #     segmentation_id: <update>
                vnfd-connection-point-ref:
                # Specify the constituent VNFs
                # member-vnf-index-ref - entry from constituent vnf
                # vnfd-id-ref - VNFD id
                # vnfd-connection-point-ref - connection point name in the VNFD
                -   nsd:member-vnf-index-ref: 1
                    nsd:vnfd-id-ref: cirros_vnfd
                    nsd:vnfd-connection-point-ref: eth0
                -   nsd:member-vnf-index-ref: 2
                    nsd:vnfd-id-ref: cirros_vnfd
                    nsd:vnfd-connection-point-ref: eth0