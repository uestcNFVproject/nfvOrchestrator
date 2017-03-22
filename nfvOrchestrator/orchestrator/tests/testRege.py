#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-22 下午4:28
# @Author  : mengyuGuo
# @Site    : 
# @File    : testRege.py
# @Software: PyCharm

import re


# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d+')

# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('wor123ld!')
if match:
    # 使用Match获得分组信息
    print(match.group())