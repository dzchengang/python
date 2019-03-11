#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test model'
__author__='cheng'

import  sys

def test():
    args=sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('tow args')
    else:
        print('too many args')

if __name__=='__main__':
    test()


'''
__xxx__  特殊变量 可以被直接引用

_xxx   __xxx  private 变量

'''