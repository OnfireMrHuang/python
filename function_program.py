# -*- coding:utf-8 -*-

#函数式编程  -- 抽象计算
#引申，如果把函数本身赋值给变量呢
f = abs
print(f(-10))

#函数名是什么，函数名其实就是指向函数的变量，对于abs()这个函数，完全可以看做是abs这个变量指向了一个可以计算绝对值的函数
#将函数名指向其他变量后，要恢复则需要重启Python交互环境，要是abs=10在其他模块也生效，则使用
#import builtins;builtins.abs=10

def add_fun(x,y,f):
    return f(x) + f(y)

x=-5
y=6
f = abs
#将函数作为参数传参给另外一个函数
print(add_fun(x,y,f))

#map()与 reduce()函数
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(r)
print(list(r))

from functools import reduce

def sum(x,y):
    return x+y     

r = reduce(sum,[1,3,5,7,9])
print(r)


def is_odd(n):
    return n % 2 == 1;

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C',' '])))

#python 求素数
#构造从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

# for n in _odd_iter():
#     if(n >1000):
#         break;
#     print(n)
# it = _odd_iter()
# print(it)
# print(next(it))

#生成一个筛选函数
def _not_divisible(n):
    return lambda x: x % n >0

#最后，定义一个生成器
def primes():
    yield 2
    it = _odd_iter();
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# print(str(1234) == "1234")

#sroted排序函数
# print(list(sorted([36,-5,-12,9,21])))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))



