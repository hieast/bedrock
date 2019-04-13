# -*- coding: utf-8 -*-
# @File    : symbol.py 
# @Time    : 2019/3/26 8:52 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
符号表

原 C 语言实现使用了单独的数组 lexemes 来存储多个字符串，
用于存储形成标识符的词素，更节省空间。

不考虑性能问题的情况下，Python 使用 dict 更容易实现同样的功能。
"""

from bedrock.translator import global_module

# STRMAX = 999
# SYMMAX = 100
# lexemes = []
# lastchar = -1
symtable = global_module.symtable
lastentry = 0


def insert(s, t):
    symtable[s] = t
    return s


def lookup(s):
    return symtable.get(s, 0)
