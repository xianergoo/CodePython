# 列表推导式
x = 'ABC'
dummy = [ord(x) for x in x]
print('list comps:',  dummy)

# 生成器表达式

symbols = '$$^&*'
print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))


a, b, *rest = range(5)
print(a, b, *rest)

from collections import namedtuple
City = namedtuple('city', 'name country population coordinates')
tokyo = City('tokyo', 'JP', 36.933, (35.68, 139.69))
print(City._fields)
print(tokyo.population)