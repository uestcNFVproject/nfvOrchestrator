#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-2-19 上午10:15
# @Author  : mengyuGuo
# @Site    : 
# @File    : testAlgorithmM.py
# @Software: PyCharm
import datetime
import os
import sys
def f(content,name):
    print(content)
    print(name)
    # 检查是否重名
    # list = os.listdir(os.getcwd())
    # for line in list:
    #     print(line)
    #     if line==name+'.py':
    #         raise RuntimeError('name complict')
    # 创建name.py文件
    file = open(name+'.py', 'w')
    head_str='''#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : time
# @Author  : mengyuGuo
# @Site    :
# @File    : file_name
# @Software: dynamic create
'''
    head_str=head_str.replace('time',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    head_str=head_str.replace('file_name', name+'.py')
    file.write(head_str)
    class_str='''
class class_name:
    @staticmethod
    def get_solution_for_ns(nsd, nfvo, ns_name):
func_content
    '''
    class_str=class_str.replace('class_name',name)
    class_str = class_str.replace('func_content', content)
    file.write(class_str)
    file.close()


    sys.path.append(sys.path[0])
    module = __import__(name)
    print(module)
    alclass=getattr(module, name)
    Foo = type(name, (), {'get_solution_for_ns': alclass.get_solution_for_ns})
    print(Foo)
    # Foo.get_solution_for_ns('arg0','arg1','arg2')

    print(Foo.__name__)
    print(Foo)
funcContent='''
        aaa
        print(\'ok\')'''

f(funcContent,'abc488')



