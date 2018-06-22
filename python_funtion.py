# -*- coding:utf-8 -*-
import math

#函数是计算的抽象
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operate type')
    if x >= 0:
        return x;
    else:
        return -x;

def nop():
    pass

print(my_abs(-89))
# my_abs('a')

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100,100,60,math.pi/6)
print(x,y)
r = move(100,100,60,math.pi/6)
print(r)


#函数的参数，Python支持默认参数、可变参数和关键字参数
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#默认参数
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#其实就是传字典

#命名关键字参数，关键字参数不受限制，如果要知道到底传入了哪些，就需要在函数内部检查
#而为了限制这种情况，增加了命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))

#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。


#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

# 尾递归是指，在函数返回的时候，调用自身本身,如
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)







