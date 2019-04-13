# -*- coding: utf-8 -*-
# @File    : main.py 
# @Time    : 2019/3/26 8:42 PM
# @Author  : Hieast(caisudong@foxmail.com)

"""
龙书开头的翻译器 Python 实现。虽然一开始基于 2.7 写的，但是最后能在 3.6 跑通即可。
把用分号分隔的中缀表达式序列翻译为相应的后缀表达式序列。只支持 ascii 字符。

id ：由字母开始的非空字母数字序列
num：数字序列
eof：表示文件结束的字符
记号由空格、制表符和换行符分隔。


与 C 语言版相比，遇到以下问题：
1. Python 缺少函数预声明，函数运行的全局环境是使用 import * 语句是进行赋值的模块级别的环境，缺乏统一的全局环境。
2. Python 更难操作标准输入/输出流，很多基础的方法不提供，标识符不一致。

解决方法：
1. 只导入模块，不使用 from ... import ... 导入。
2. 写一套行为相似、同名的函数。将 sys.stdin 替换为输入的文件名里的内容。

调用方法：
使用相对引用的话可迁移性更好，相对引用使用 __name__ 来确定包的层次结构，作为脚本则为 __main__，所以无法使用脚本的方式调用。
而使用模块的方式调用则一般情况下无法使用 Pycharm 的 Debug 工具。
因此最后使用绝对路径。
调用方法为：在项目根目录下（添加项目根目录到 sys.path）运行 /path/to/python /path/to/bedrock/translator/main.py
"""

from bedrock.translator import init
from bedrock.translator import parser


def main():
    init.init()
    parser.parse()
    exit(0)


if __name__ == '__main__':
    main()
