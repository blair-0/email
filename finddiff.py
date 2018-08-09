#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/8/3 14:53
# @Author   : YZH
# @Email    : you_zhihong@aliyun.com
# @File     : finddiff.py
# @Software : PyCharm

"""
将两个文件的不同内容写入新文件
Usage: ./script file1 file2 new_file
"""
import sys

with open(sys.argv[1]) as f1:
    f1_set = set(f1.read().splitlines())

with open(sys.argv[2]) as f2:
    f2_set = set(f2.read().splitlines())

if f1_set.issuperset(f2_set):
    f3_set = f1_set.difference(f2_set)
else:
    f3_set = f2_set.difference(f1_set)

with open(sys.argv[3], 'w') as f3:
    f3.write("\n".join(f3_set))