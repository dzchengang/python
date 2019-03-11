#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('zhangsan')
print('\t')
print('\"')
print(r'\t')
print(True)

print(ord('A'))
print(chr(66))
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode("utf-8"))

print(len('A'))
print(len(b'A'))
print(len('中'.encode('utf-8')))

print('名字 %s 年龄 %d 身高 %f ' % ('张三',12,23.67))

test=['zhangsan',12,['打篮球','踢足球']]
print(test[0],test[2][0])

names=('zhang',12,['a','b'])
names[2][0]='c'
#报错
#names[0]='li'
print(names[2][0])

dicts={"a":1,"b":2}
print(dicts['a'])
print(dicts.get('c',-1))

x,y=(12,14)
print(x)

#不定参数 和 关键字参数
def  fun1(name,age,*host,**addr):
    print("---fun1---")
    print(addr)

addr={"sheng":"山东","city":"济南"}

fun1("cheng",12,"footbox","basbox",**addr)


#列表生成式
xx=[x*x for x in range(1,10) if x%2==0]
print(xx)

#迭代器
ite=(x*x for x in range(1,10) if x%2==0)

'''
print(next(ite))
print(next(ite))

'''
for xx in ite:
    print(next(ite))

def testIte():
    yield 1
    yield 2
    yield 3

test=testIte()
print(next(test))
print(next(test))