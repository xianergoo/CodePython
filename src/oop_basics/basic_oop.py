class Myclass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
myclass = Myclass()
print(myclass.f())


# 实例化操作（“调用”类对象）会创建一个空对象。 许多类喜欢创建带有特定初始状态的自定义实例。 为此类定义可能包含一个名为 __init__() 的特殊方法，就像这样:
# def __init__(self):
#     self.data = []

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3, 4.5)
print(x.r, x.i)

print('-' * 35)

# 一般来说，实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法:
# 下面的类中 kind是类变量 name是实例变量
class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('A')
e = Dog('B')

print(
d.kind, d.name, 
e.kind, e.name
)

class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

a = Dog('A')
b = Dog('b')

a.add_trick('roll over')
b.add_trick('play dead')

print(b.tricks)
print('-' * 35)
# 因为使用类变量所以这是Dog b拥有a,b的trick 这是不对的 所以这时应该这么定义Dog

class Dog:
    
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

a = Dog('A')
b = Dog('b')

a.add_trick('roll over')
b.add_trick('play dead')
print(b.tricks)



