import functools
import time

registry = []


def register(func):
    print("running register {}".format(func))
    registry.append(func)
    return func


# 实际上相当于先定义f1,再f1 = register(f1)
# 装饰器会在被装饰的函数定义之后立刻执行，包括被别的模块import
@register
def f1():
    print("running f1()")


# 变量作用域规则
a = 10


def test():
    print(a)  # 直接访问全局变量是ok的


test()


def test2():
    print(a)
    a = 20  # 一旦赋值，则会当成是局部变量，即使是在后面


# test2() wrong!


def test3():
    global a  # 用global声明a为全局变量即可
    print(a)


# 闭包


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)  # series是自由变量, 绑定在返回函数的__closure__属性中
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()

print(avg(2))
print(avg(3))


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total  # 必须使用nonlocal, 不然count和total会被认为是局部变量
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager2()

print(avg(2))
print(avg(3))


def my_decorator(func):
    @functools.wraps(func)  # 将原函数的属性赋值到wrapper
    def wrapper(*args, **kw):
        print("this is wrapper")
        func(*args, **kw)

    return wrapper


@my_decorator
def show():
    print("show")


print(show.__name__)  # 如果没有@functools.wraps会上打印出wrapper


# 缓存
@functools.lru_cache()  # 此处括号不能省略，因为装饰器有函数
def test(n):
    print("test")
    return n


print(test(1))
print(test(1))


# 叠放装饰器
# 相当于 f = a(b(f))
# @a
# @b
# def f():
# print('f')


# 参数化装饰器

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"

# clock是装饰器工厂函数
def clock(fmt=DEFAULT_FMT):
    def decorate(func):  # decorate才是装饰器
        def clocked(*_args):  # clocked是wrapper
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ",".join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))  # locals可以返回局部变量的dict
            return _result

        return clocked

    return decorate


@clock()  # 相当于先调用装饰器工厂函数返回一个装饰器再应用到函数上
def clock_test(seconds):
    time.sleep(seconds)


for i in range(3):
    clock_test(0.123)
