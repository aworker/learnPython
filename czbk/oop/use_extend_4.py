#!usr/bin/env python3
# -*- coding:utf-8 -*-

class Animal:
    def eat(self):
        print("Animal can eat")

    def drink(self):
        print("Animal drink")


class Dog(Animal): #python继承用的是()语法,python支持多继承，如下(Animal,ClassB),如果父类中有同名方法，按照mro的顺序查找方法
    
    def drink(self):
        super().drink() # python中这样调用夫类的方法
        Animal.drink(self) # python2用的是这样的方法调用，这种方式并不推荐
        print("Dog drink")


dog = Dog()

dog.eat()
dog.drink()

print(Dog.__mro__) #类是按照mro属性的先后顺序来确定方法的调用。



class ClassA(object): #如果一个类没有指定的父类，那么可以添加object为父类，这样可以保证ClassA为新式类，保证此代码可以在python2 python3中都可以运行.python3自动会给创建的新类继承自object类
    pass