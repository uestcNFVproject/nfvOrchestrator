#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/9 17:15
# @Author  : mengyuGuo
# @Site    : 
# @File    : localAgnet.py
# @Software: PyCharm
import os
# 无限循环，调用命令收集信息，发送给指定web接口
while True:
    top_res=os.popen('top').read()
    io_res=os.popen('iostat').read()
    df_res = os.popen('bf -hl').read()
    # 处理top_res

    # 处理io_res

    # 处理df_res