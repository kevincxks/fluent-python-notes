
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
    print(a) # 直接访问全局变量是ok的

test()

def test2():
    print(a)
    a = 20 # 一旦赋值，则会当成是局部变量，即使是在后面

# test2() wrong!

def test3():
    global a # 用global声明a为全局变量即可
    print(a)


# 闭包

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value) # series是自由变量, 绑定在返回函数的__closure__属性中
        total = sum(series)
        return total/len(series)

    return averager


avg = make_averager()

print(avg(2))
print(avg(3))


def make_averager2():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total # 必须使用nonlocal, 不然count和total会被认为是局部变量
        count += 1
        total += new_value
        return total / count

    return averager

avg = make_averager2()

print(avg(2))
print(avg(3))
