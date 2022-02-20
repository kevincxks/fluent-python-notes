from typing import Iterable, Iterator
from array import array
import reprlib
import numbers
import functools
import operator


# 任意维度的向量, 不可变类
class Vector:

    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # 可以限制生成的字符串长度，省略号
        components = reprlib.repr(self._components)
        components = components[components.find("[") : -1]
        return "Vector({})".format(components)

    def __str__(self):
        # 利用__iter__实际上
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + bytes(self._components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # 不能简单的委托给array，这样会导致切片直接返回array
        # return self._components.__getitem__(index)
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=cls))

    shortcutnames = "xyzt"

    # 实现该方法使得可以通过属性名访问前几个元素
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = self.shortcutnames.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        # 此处的!r表示repr(x)
        msg = "{.__name__!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls, name))

    # 也要实现该方法防止为属性赋值时设置了一个新实例属性
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in self.shortcutnames:
                error = "readonly attribute {attr_name}"
            elif name.islower():
                error = "can't  set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(clas_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __eq__(self, other):

        # 一种比较直接的写法
        # if len(self) != len(other):
        #     return False
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True

        # 一种比较pythonic的写法
        # zip函数可以生成一个元组构成的生成器，元组内的每个元素来自各个Iterable，一旦一个序列终止则停止生成值
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        # 第三个参数是初始值，如果序列为空直接返回，否则把它作为第一个参数
        return functools.reduce(operator.xor, hashes, 0)


v = Vector([1, 2, 3])


a = array("d", [1, 2, 3])
a[0] = 2
print(a)


# 切片的实质
class MySeq:
    def __getitem__(self, index):
        print(index)


m = MySeq()

# 传入int就是int
m[1]  # 1
m[1:5]  # slice(1, 5, None)
m[1:5:2]  # slice(1, 5, 2)
m[1:5:2, 1:5]  # (slice(1, 5, 2), slice(1, 5, None))

v2 = Vector(range(10))
print(v2[-1])
print(repr(v2[1:4]))
print(v2.x)
print(hash(v2))
