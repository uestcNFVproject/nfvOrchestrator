#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-2-17 下午7:48
# @Author  : mengyuGuo
# @Site    : 
# @File    : testDesCatalugue.py
# @Software: PyCharm

import os
import time
import re
import json
import requests
monitor_ip='127.0.0.1'
monitor_PORT='8181'
monitor_url='/node_info/details/'
# monitor_url='/test/'
def get(host, port, uri):
    url='http://'+host+":"+port+uri
    r = requests.get(url)
    print(r)
    jsondata=json.loads(r.text)
    return jsondata

def put(host, port, uri, data, debug=False):
    '''Perform a PUT rest operation, using the URL and data provided'''

    url='http://'+host+":"+port+uri
    if debug == True:
        print("PUT %s" % url)
        print(json.dumps(data, indent=4, sort_keys=True))
    r = requests.put(url, data=json.dumps(data))
    if debug == True:
        print(r.text)
    r.raise_for_status()
    time.sleep(5)
def post(host, port, uri, data, debug=False):
    '''Perform a POST rest operation, using the URL and data provided'''

    url='http://'+host+":"+port+uri
    headers = {'Content-type': 'application/yang.data+json',
               'Accept': 'application/yang.data+json'}
    if debug == True:
        print("POST %s" % url)
        print(json.dumps(data, indent=4, sort_keys=True))
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r)
    if debug == True:
        print(r.text)
    r.raise_for_status()
    time.sleep(5)
