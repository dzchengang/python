#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(x):
    return x*x

def fun2(x,y):
    return x+y

print(fun2(1,fun1(2)))


texts=[1,2,3,4,5,6]

def fun3(x):
    return x*x
# map
nums=map(fun3,texts)
print(list(nums))

def fun4(x):
    return x%2==0

# filter
nums2=filter(fun4,texts)
print(list(nums2))

#reduce



def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        # fs 保存了三个函数  注意 要写成 fs.append(f()) 否则会立即执行
        fs.append(f)
    return fs

print(count())


f1,f2,f3=count()
'''
结果全是9  但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3
'''
print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


# 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#装饰器
def log(func):
    def wrapper(*args, **kw):
        print(args)
        print(kw)
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now(*args, **kw):
    print('2017-01-23')

now(1,2,**{"a":1,"b":2})


#偏函数
import  functools
int2=functools.partial(int,base=2)
print(int2('10'))


