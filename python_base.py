# -*- coding:utf-8 -*-

#list:list列表是一种有序集合，可以随时添加和删除其中的元素
#example_1
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

#有序列表的添加
print(classmates)
classmates.append('Adam')
classmates.insert(2,'Jack')
print(classmates)
#有序链表的删除
classmates.pop()
print(classmates)
classmates.pop(2)
print(classmates)
#替换有序列表中某个元素
classmates[2] = 'json'
print(classmates)
#list有序列表中的元素也可以不同
L =  ['Apple',123,True]
print(L)
#list中的元素也可以是另外一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][1])


#这里介绍另外一种有序列表叫做元组:与list不同的是，tuple一旦初始化就不可以
#要创建一个内容也不变的tuple怎么做，那就必须保证tuple的每一个元素也不能变
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates[0])
print(classmates)
t = (1)
print(t)
t = (1,)
print(t)

#条件判断
age = 3
if age > 18:
    print("you age is",age)
    print('adult')
elif age > 10:
    print('you age is',age)
    print('teenager')
else:
    print('you age is',age)
    print('boy')

# str = input('number:')
# birth = int(str)
# if birth < 2000:
    # print('00前')
# else:
    # print("00后")

#循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
sum = 0 
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum += i
print(sum)

print(list(range(10)))

#while循环
sum = 0
n = 99
while n >0:
    sum += n
    n -=2 
print(sum)


# while True:
    # print('test')

#python内置了字典:即键值对或哈希表，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])  
print('Bob' in d)

print(d.get('Bod'))
print(d.get('Bod',5))

d.pop('Bob')
print(d)

#dict内部存放的顺序和key放入的顺序是没有关系的
#和list相比，dict有以下几个特点：
#   1.查找和插入的速度极快，不会随着key的增加而变慢
#   2.占用空间小，浪费内存很少

#set：集合 与dict类似，set也是一组key的集合，但是不存储value。由于key不能重复，所以在set中不存在重复的key 。
#要创建一个set,需要提供一个list作为输入集合

s  = set([1,2,3])
print(s)

s = set([2,1,3,2,1,3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

#set可以看做是一个无序、无重复的集合，当然就可以做数学上的交集和并集等
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)


a = ['c', 'b', 'a']
a.sort()
print(a)








