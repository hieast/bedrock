# -*- coding: utf-8 -*-
# @File    : lexer.py 
# @Time    : 2019/3/26 8:48 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
词法分析器
词法分析器从输入串读字符并形成词素，然后将词素 token 及 tokeval 传递给编译器的下一个阶段。
这里原来使用了字符串缓冲 lexbuf， Python 字符串不需要 0 字节来标识结尾，此处做了修改。
"""

import sys

from bedrock.translator import global_module
from bedrock.translator import symbol
from bedrock.translator import error

lexeme = b''  # 长度最大为 BSIZE，用于缓冲词素字符串


def lexan():
    global lexeme

    while True:
        t = global_module.getchar()
        if t == b' ' or t == b'\t':
            continue
        elif t == b'\n':
            global_module.lineno += 1
        elif global_module.isdigit(t):
            global_module.tokenval = global_module.scanf_num(t)
            return global_module.NUM
        elif global_module.isalpha(t):
            while global_module.isalnum(t):
                lexeme += t
                t = global_module.getchar()
                if len(lexeme) >= global_module.BSIZE:
                    error.error("compiler error")
            global_module.ungetc(t, sys.stdin)
            p = symbol.lookup(lexeme)
            if p == 0:
                symbol.insert(s=lexeme, t=global_module.ID)
            global_module.tokenval = lexeme
            token = global_module.symtable[lexeme]
            lexeme = b''
            return token  # lexeme 对应的 token
        elif t == b'':  # python 取不到真正的 EOF
            return global_module.DONE
        elif t == b';':
            global_module.tokenval = global_module.NONE
            return global_module.SEP
        else:
            global_module.tokenval = global_module.NONE
            return t
