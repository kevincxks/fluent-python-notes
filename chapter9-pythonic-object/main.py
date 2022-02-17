from array import array
import math


class Vector2d:

    typecode = "d"

    def __init__(self, x, y) -> None:
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):  # 把实例变成可迭代的对象,可以直接拆包
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return "{}({}, {})".format(class_name, self.x, self.y)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):  # 比较两个实例是否相等
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


v = Vector2d(3, 4)
print(tuple(v))

# 直接拆包
a, b = v
print(a, b)


# @classmethod 和 @staticmethod的区别：
# 1. @classmethod 第一个参数就是类本身
# 2. @staticmethod 没有自带参数，相当于定义在类内的普通函数
class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


d = Demo()
print(d.klassmeth())
print(d.statmeth())


class NewVector2d:

    # 默认情况下，在__dict__中存储实例属性, 使用__slots__可以用节约内存
    __slots__ = ("__x", "__y")

    def __init__(self, x, y) -> None:
        # 私有变量x和y 实际上只是把名字变成_NewVector2d__x
        self.__x = float(x)
        self.__y = float(y)

    # 使得x和y变成只读
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)


v = NewVector2d(3, 4)
v2 = NewVector2d(3.1, 4.2)
v3 = NewVector2d(3, 4)
print(hash(v))
print(hash(v2))

print(set([v, v2, v3]))  # 必须实现__eq__和__hash__

# print(v.__dict__)
print(v.__slots__)
