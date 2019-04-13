# -*- coding: utf-8 -*-
# @File    : error.py 
# @Time    : 2019/3/26 8:53 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
错误处理
"""
from __future__ import print_function

import sys

from bedrock.translator import global_module


def error(m):
    global_module.fprintf(sys.stderr, "line {}: {}\n".format(global_module.lineno, m))
    exit(1)
