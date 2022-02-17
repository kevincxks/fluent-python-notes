from collections import namedtuple

s = "12345"

for i in filter(lambda x: x % 2 == 1, map(int, s)):
    print(i)


# 列表推导的魅力
l = [int(n) for n in s if int(n) % 2 == 1]
print(l)

colors = ["black", "white"]
sizes = ["S", "M", "L"]

# 笛卡尔积
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

# 换成括号就变成生成器表达式，节约开销
for tshirt in ("%s %s" % (color, size) for color in colors for size in sizes):
    print(tshirt)


# 任何Iterable都可以拆包
# 元组拆包
info = ("kevin", 24, "10000")
name, age, phone = info

print("%s/%s/%s" % info)

import os

# 不关心的拆包元素用_来接收
_, filename = os.path.split("/home/kevin/test.txt")
print(filename)


def show(*args):
    print(args)


# 拆包传参
show(*info)

# 用*来接收剩下的元素
a, b, *rest = range(5)
print(a, b, rest)


# 具名元组
City = namedtuple("City", ["name", "country"])

tokyo = City("Tokyo", "JP")
print(tokyo.name)
# 打印所有字段
print(City._fields)


# 切片
demo = "kevin 24 10000"
# [a:b:c] 相当于__getitem__(slice(a, b, c))
print(demo[:5])

# 利用命名切片增强语义
NAME = slice(0, 5)
AGE = slice(6, 8)
PHONE = slice(-5, -1)
print(demo[NAME])
print(demo[AGE])
print(demo[PHONE])


# 切片赋值
l = list(range(10))
l[2:5] = [20, 30]
del l[5:7]
print(l)
# 赋值的对象必须是一个Iterable
l[2:5] = [100]
print(l)

# + 和 *

a = [1, 2]

b = [3, 4]

# 新序列
print(a + b)  # [1, 2, 3, 4]

# 小心存放的是否是引用
print(a * 3)  # [1, 2, 1, 2, 1, 2]


# +=(*=)实际调用__iadd__(__imul__), 如果没有则调用__add__, 退化成a = a + b
a += b
print(a)
print(id(a))

t = (1, 2, 3)
t *= 2
# 退化, 实际上是一个新序列
print(t)

# list.sort和sorted

# sorted返回一个新的list
fruits = ["grape", "respberry", "apple", "banana"]
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))

# list.sort会就地排序
fruits.sort()
print(fruits)


# 利用bisect二分查找
import bisect

l = [1, 4, 5, 6, 7]

position = bisect.bisect(l, 3)
print(position)  # 1

# 利用insort直接插入保持有序
bisect.insort(l, 3)
print(l)


# array.array性能更强，几乎就是c数组


# collections.deque 头尾优化
