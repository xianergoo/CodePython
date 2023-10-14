
# 1.2.1 模拟数值类型 vertor

from math import hypot

class vertor:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    # 字符串表达形式如果没有定义__repr__函数，调用print(vertor(x, y))将会打印实例对象
    # <__main__.vertor object at 0x000002C61B984408>
    def __repr__(self):
        return 'Vertor(%r, %r)' %(self.x, self.y)

    # __repr__ 和 __str__ 的区别在于后者在str(class) 使用，或是在用print函数打印对象时被调用
    # 
    def __str__(self):
        return 'Vertor(%r, %r...)' %(self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def _bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return vertor(x, y)
    
    def __mul__(self, scalor):
        return vertor(self.x * scalor, self.y * scalor)
    
print(str(vertor('1', '2')))
    

