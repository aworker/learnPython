#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class Woman:
    def __init__(self):
        self.__age = 19 # __定义的变量是对象的私有属性
        pass

    def __secret(self):  #__开头的是私有方法
        print("my age is 19")

woman = Woman()

age = woman._Woman__age #可以用这种方法访问python对象的私有方法和私有属性
print(age)



