# -*- coding: utf-8 -*-
# @File    : global.py 
# @Time    : 2019/3/26 9:05 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
全局变量, 包括辅助函数
"""

from __future__ import print_function

import sys
import string

# from collections import namedtuple

BSIZE = 128
NONE = -1
EOS = '\0'

NUM = 256
DIV = 257
MOD = 258
ID = 259
DONE = 260
SEP = 261

tokenval = 0
lineno = 0

# C 语言中数组使用 Struct 实现 symtable，Python 使用字典更方便，不需要定义 Entry 了
# Entry = namedtuple('entry', ['lexptr', 'token'])
symtable = {}


# IO 操作

def fprintf(file=sys.stderr, s=''):
    print(s, file=file)


def getchar():
    """从 sys.stdin.buffer 中取 1 个字符返回
    """
    return sys.stdin.buffer.read(1)


def ungetc(t=None, stdin=sys.stdin):
    """调用一次将 stdin buffer 指针往前移

    :param t: 其实没有用
    :param stdin: 标准输入，默认可以不传
    :return:
    """
    stdin.buffer.seek(-1, 1)


# 字符判断

def isdigit(t):
    """

    :param t: a single byte
    :return:
    """
    return bool(t) and t in string.digits.encode()


def isalpha(t):
    return bool(t) and t in string.ascii_letters.encode()


def isalnum(t):
    return bool(t) and t in (string.ascii_letters + string.digits).encode()


def scanf_num(t):
    digits = [t]
    t = getchar()
    while isdigit(t):
        digits.append(t)
        t = getchar()
    if bool(t):
        ungetc(t, sys.stdin)
    return int(b''.join(digits))
