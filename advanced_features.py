#slice 操作符
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[-1:])

L = list(range(100))
print(L)
#取后10个数,直接填0并不对
print(L[-10:])
#取前10个数
print(L[0:10])
#取前11-20个数
print(L[11:20])
#前10个数，每两个取一个
print(L[0:10:2])
#所有数，每5个取一个
print(L[::5])


#iteration 迭代器
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)
for key,value in d.items():
    print(key,value)

for ch in 'ABC':
    print(ch)

#判断一个对象是不是可迭代对象
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
#python中内置的enumreta函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
    print(i,value)

#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2 ==0])

#还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k,v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#generator 生成器，在Python中，可以通过一边循环一边计算出的机制

#要创建一个generator，第一种方法很简单，只需要把一个列表生成式的[]改成()，就创建了一个generator
#按我的理解，生成器保存的是算法
g = (x*x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#生成器第二种定义方法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
#这里能将函数做成生成器的奥义是在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
while True:
    try:
        x = next(f)
        print('f',x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种
# 一类是数据集合，如list、tuple、dict、set、str
# 一类是生成器
# 这些可以直接作用于for循环的对象统称为可迭代对象:Iterable
#迭代器：Iterator

