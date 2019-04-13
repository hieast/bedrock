# -*- coding: utf-8 -*-
# @File    : init.py 
# @Time    : 2019/3/26 8:52 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
初始化模块
"""

from __future__ import print_function
from bedrock.translator import global_module

keywords = {
    b'div': global_module.DIV,
    b'mod': global_module.MOD,
    0: 0
}


def init():
    global_module.symtable.update(keywords)
