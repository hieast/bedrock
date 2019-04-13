# -*- coding: utf-8 -*-
# @File    : emitter.py 
# @Time    : 2019/3/26 8:52 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
输出模块
"""
from __future__ import print_function
from bedrock.translator import global_module

end = ' '

handler_mapping = {
    global_module.DIV: lambda tval: f"DIV{end}",
    global_module.MOD: lambda tval: f"MOD{end}",
    global_module.NUM: lambda tval: f"{tval}{end}",
    global_module.ID: lambda tval: f"{global_module.symtable[tval]}{end}",
    global_module.SEP: lambda tval: '\n'
}
for t in (b'+', b'-', b'*', b'/'):
    handler_mapping[t] = lambda tval, t=t: f"{t.decode()}{end}"


def emit(t, tval):
    """生成输出"""
    handler = handler_mapping.get(
        t, lambda tval: f"token {t.decode()}, tokenval {tval}"
    )
    print(handler(tval=tval), end='')

