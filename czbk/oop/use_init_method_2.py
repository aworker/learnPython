#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#__init__ 方法是python创建对象时候的内置方法

class Cat :
    def __init__(self,new_name):
        self.name = new_name
        print("this is initial method")

    def __del__(self):
        print("我将要被从内存中销毁了，销毁前要调用我")

    def __str__(self): #相当于java的toString方法
         return "my name is {%s}" % self.name


tom = Cat("Tome")
cat = Cat("Lazy cat")

#del cat # del关键字可以直接删除对象
print(tom.name)
print(tom)

#python 中 == 表示对象的值是否相等; is 表示 引用地址是否相等

print(tom is None) # 在python中 最好用is判断其是否为None


print(tom is cat)

