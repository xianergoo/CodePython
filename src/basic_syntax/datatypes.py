# from tools import print_separator

def print_separator():
    print('-' * 30)
# Numbers
# +、-、*、/
# 整数（比如 2、4、20 ）有 int 类型，有小数部分的（比如 5.0、1.6 ）有 float 类型。在这个手册的后半部分我们会看到更多的数值类型。
# 除法运算 (/) 永远返回浮点数类型。如果要做 floor division 得到一个整数结果（忽略小数部分）你可以使用 // 运算符；如果要计算余数，可以使用 %

print(17/3)

print(17//3)

print(17%3)

print_separator()

# 在Python中，可以使用 ** 运算符来计算乘方 1

print(5**2)
print(2**7)

print_separator()

# String

print('hello')

print('\"yes, \"')

s = 'First line. \nSecond Line.'
print(s)

print('C:\some\name')
print(r'C:\some\name')
print(f'C:\some\name')
print_separator()

word = 'Python'
print(word)
print(word[0])
try:
    print(word[1])
    word[1] = '3'
    print(word[1])
except Exception as e:
    print(e)
    print(type(e))

print_separator()
# List

squares = [1, 4, 9, 16, 25]
print(squares)
for item in squares:
    print(item)

print_separator()

print(squares[0])
print(squares[-1])
print(squares[3:])
print(squares[-3:])

# 所有的切片操作都返回一个新列表，这个新列表包含所需要的元素。就是说，如下的切片会返回列表的一个新的(浅)拷贝:
print(squares[:])
a = squares
print(id(a))
a = squares[:]
print(id(a))

print_separator()
# List 加法
print(squares + [36, 49, 64, 81, 100])

# for i, item in squares:
#     print(i, item)

# 与 immutable 的字符串不同, 列表是一个 mutable 类型，就是说，它自己的内容可以改变:
print(squares)
print(squares[1])
squares[1] = 23
print(squares[1])
print(squares)

print_separator()

# 也可以嵌套列表 (创建包含其他列表的列表), 比如说:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])


# Tuple 

# Dictonary

