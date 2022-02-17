def factorial(n: int) -> int:
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# 赋值给变量
fact = factorial
print(fact(5))


words = ["hello", "world"]

# 高阶函数,实际上可以用列表推导生成器表达式代替
print(list(map(str.upper, words)))
# lambda只能是纯表达式,作用比较有限
print(list(filter(lambda x: x == "hello", words)))

# 每个都是真才返回True
print(all([True, False]))
# 有一个为真就可以
print(any([True, False]))


class MyClass:

    # 调用类(创建实例)时会先运行该方法再运行__init__
    # def __new__(cls):

    # 定义该方法使得实例可以直接调用
    def __call__(self):
        print("I'm being called")


c = MyClass()
c()

# 判断是否是可调用类型
print(callable(c))
print(dir(factorial))

# 可以得到注解信息，这也是python唯一会对注解所做的事情
print(factorial.__annotations__)


# 函数式编程
import operator
from typing import MutableMapping

l = [("kevin", 24), ("bob", 30)]

# 利用itemgetter提取元素
print(list(map(operator.itemgetter(0), l)))


from collections import namedtuple

Student = namedtuple("Student", "name age")

s = Student("kevin", 24)

# 利用attrgetter来提取属性
print(operator.attrgetter("name")(s))


from operator import mul
from functools import partial


# 利用partial来冻结参数, 类似cpp的bind
triple = partial(mul, 3)
print(triple(7))
