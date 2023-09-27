#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/9/21 21:36
# @Author : Z3
# @Email: xianergoo@gmail.com

from typing import Optional
def separator():
    print('*' * 25, 'this is separator', '*' * 25)
# 类的基本属性

class StudentsA():

    student = "college student"
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = StudentsA('A', 18)
stu2 = StudentsA('B', 19)

print(f'{stu1.name} is {stu1.age}, is a {stu1.student}')
print(f'{stu2.name} is {stu2.age}, is a {stu2.student}')


separator()
# 类方法
class StudentsB():

    student = "college student"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        print('%s could sing'.format(self.name))

    def jump(self):
        print(f'{self.name} could jump')
    def basketball(self):
        print(f'{self.name} like basketball')

stu1 = StudentsB('A', 19)
stu1.sing()
stu1.jump()
stu1.basketball()

separator()
'''
python中没有 public > default > protected > private 等属性来实现访问限制,
因此需要别的方法来控制访问限制，实现私有变量可以通过加上__
'''
class StudentsC():

    # student 是类属性，可以他通过 对象.__class__.student 访问
    student = "大学生"
    # init 是类的构造方法，在对象被创建的时候，就会自动调用这个方法
    def __init__(self, name, age):
        # 定义两个对象属性，这个属性在不同的对象中是不一样的
        self.name = name
        if age>150:
            raise ValueError("人的年龄无法达到 150 岁以上")
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age > 150:
            raise ValueError("人的年龄无法达到 150 岁以上")
        self.__age = age


stu1 = StudentsC("小红",18)
stu2 = StudentsC("小黄",19)
stu1.setAge(20)
try:
    print(stu1.__age)
except Exception as e:
    print(e)

print('%s/"s age is %d '.format(stu1.name, stu1.getAge()))

separator()

# 封装继承堕胎
## 继承

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # public func
    def bark(self):
        print(f"{self.name} bark")

class pipi(Dog):

    def play(self):
        print(f'{self.name} can play')

class dahuang(Dog):

    def other(self):
        print(f'{self.name} can sing')

dog1 = pipi('pipi', 2)
dog2 = dahuang('dahuang', 1)

dog1.bark()
dog1.play()
dog2.bark()
dog2.other()

separator()

# 方法覆盖
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} can bark")

    def eat(self):
        print(f"{self.name} 喜欢吃鸡肉")


class pipi(Dog):

    def play(self):
        print(f"{self.name} 会打滚")

    def eat(self):
        print(f"{self.name} 喜欢吃火腿")


dog1 = pipi("皮皮", 2)
dog1.eat()

## overload overwrite override

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} can bark")

    def eat(self):
        print(f"{self.name} 喜欢吃鸡肉")


class pipi(Dog):

    def __init__(self, name: str, age, size: Optional[str] = 'middle'):
        self.name = name
        self.age = age + 1
        self.size = size

    def play(self):
        print(f"{self.name} 会打滚")

    def eat(self):
        print(f"{self.name} 喜欢吃火腿")


dog1 = pipi("皮皮", 2)
dog1.eat()
print(dog1.size)
print(dog1.age)

separator()


# 根据封装程度
# 普通私有变量 __
class Retangle():

    # 内部访问，使用 hidden 任然可以被访问
    # 使用 __作为私有属性，是外部不可以被访问
    def __init__(self,width, height):
        self.__width = width
        self.__height = height

    def setWidth(self,width):
        self.__width = width

    def getWidth(self):
        return self.__width

    def setHeight(self,height):
        self.__height = height

    def getHeight(self):
        return self.__height

## 使用装饰器 封装

class Person():
    '''
        __xxxx 成为隐藏属性
        __name -> _Person__name

        使用 _xxx 作为私有属性，没有特殊需求，不要修改私有属性
        类一般使用属性或方法不可见可以使用单下划线
    '''
    # 使用一个
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        print(f'私有变量__name的地址 {id(self.__name)}')
        return self.__name


    '''
        setter
        getter 方法更好的使用
        @property，将一个 get 方法，转换为对象属性
        @属性名.setter 讲一个 set 方法，转换为对象属性
        两者缺一不可
    '''

    # setter 方法的的装饰器： @属性名.setter
    @name.setter
    def name(self, name):
        self.__name = name



p = Person('猴赛雷')

## 通过getter 获得属性name
p.__name = 'vvv'
print(f'私有变量的值: {p.name}')
print(f'动态变量__name的地址 {id(p.__name)}')
print(f'动态变量的值: {p.__name}')
'''
私有变量__name的地址 2303605420464
猴赛雷
动态变量__name的地址 2303605132720

这里可以看到p.__name在这里是动态变量就像下面的haha一样 改变p.__name并没有改变私有变量__name的值,
且两个值的地址是不同的
'''

p.haha = 'aaa'
print(p.haha)

separator()


# Syntax for inheritance

# A Python program to demonstrate working of inheritance
class Pet:
		#__init__ is an constructor in Python
		def __init__(self, name, age):	
				self.name = name
				self.age = age

# Class Cat inheriting from the class Pet
class Cat(Pet):		
    def __init__(self, name, age):
				# calling the super-class function __init__
				# using the super() function
	    super().__init__(name, age)
        # self.male = male
    
def CatMain():
		thePet = Pet("Pet", 1)
		jess = Cat("Jess", 3)
		
		# isinstance() function to check whether a class is
		# inherited from another class
		print("Is jess a cat? " +str(isinstance(jess, Cat)))
		print("Is jess a pet? " +str(isinstance(jess, Pet)))
		print("Is the pet a cat? "+str(isinstance(thePet, Cat)))
		print("Is thePet a Pet? " +str(isinstance(thePet, Pet)))
		print(jess.name)
          

separator()

# This program will reverse the string that is passed
# to it from the main function
class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(data)		

    def __iter__(self):
        return self
	
    def __next__(self):
        if self.index == 0:
             raise StopIteration
        self.index -= 1
        return self.data[self.index]

def ReverseMain():
	rev = Reverse('Drapsicle')
	for char in rev:
		print(char)

if __name__=='__main__':
	ReverseMain()












