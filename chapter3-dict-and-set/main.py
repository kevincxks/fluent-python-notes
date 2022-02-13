import collections

codes = [(1, 'China'), (2, 'Japan')]


# 字典推导
country_codes = {country: code for code, country in codes}
print(country_codes)
print({code :country.upper() for country, code in country_codes.items()})



# 可以使用任意Ierable更新dict
country_codes.update([('Korea', 3), ('Singapore', 4)])
print(country_codes)


# 利用setdefault来优化代码,如果存在key则返回对应value如果不存在则设置新值并返回该值
# index.setdefault(word, []).append(location)
country_codes.setdefault('USA', 3)


# 也可以使用defaultdict来处理key不存在的情况
# 传入一个可调用对象
d = collections.defaultdict(list)


# 只会在__getitem__碰到找不到的键时被调用, 实际上是__missing__在发挥作用, 对get没影响
d['new-key'].append('test')
print(d['new-key'])

print(d.get('another-key')) # still None

# in实际上在调用__contains__()
print('new-key' in d)
print(d.__contains__('new-key'))


set_a = set([1, 2, 3])
set_b = set([2, 3, 4])

# 另一种字面量构造方式
set_c = {5, 6, 7}
print(set_c)

# 交集
print(set_a & set_b)
# 差集
print(set_a - set_b)
# 并集
print(set_a | set_b)


# 集合推导
set_d = {i for i in range(10)}
print(set_d)



d = dict()
# dict的键必须是可hash的，通过__hash__()得到的值不可变，且需要支持__eq__()检测相等性
# d[['test']] = 3  wrong!
