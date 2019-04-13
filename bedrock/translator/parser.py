# -*- coding: utf-8 -*-
# @File    : parser.py 
# @Time    : 2019/3/26 8:51 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
语法分析器
"""

from bedrock.translator import global_module
from bedrock.translator import lexer
from bedrock.translator import emitter
from bedrock.translator import error

lookahead = 0  # single char


def match(t):
    global lookahead
    if lookahead == t:
        lookahead = lexer.lexan()
    else:
        error.error("symtax error match")


def parse():
    """分析并翻译表达式列表"""
    global lookahead
    lookahead = lexer.lexan()
    while lookahead != global_module.DONE:
        expr()
        match(global_module.SEP)
        emitter.emit(global_module.SEP, global_module.NONE)


def expr():
    global lookahead
    term()
    while 1:
        if lookahead in [b'+', b'-']:
            t = lookahead
            match(lookahead)
            term()
            emitter.emit(t, global_module.NONE)
            continue
        else:
            return


def term():
    global lookahead
    factor()
    while 1:
        if lookahead in [b'*', b'/', global_module.DIV, global_module.MOD]:
            t = lookahead
            match(lookahead)
            factor()
            emitter.emit(t, global_module.NONE)
            continue
        else:
            return


def factor():
    global lookahead
    if lookahead == b'(':
        match(b'(')
        expr()
        match(b')')
    elif lookahead in (global_module.ID, global_module.NUM):
        t = lookahead
        emitter.emit(t, global_module.tokenval)
        match(lookahead)
    else:
        error.error("symtax error factor")
