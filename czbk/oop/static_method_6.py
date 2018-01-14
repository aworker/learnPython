#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Dog(object):
    name = "" #类属性

    @staticmethod
    def run():   #如果一个类不使用类属性，也不使用实例属性，那么就可以定义成类方法
        print("a dog is running")

    def __init__(self):
        color = "yellow" #实例属性

dog = Dog()
print(Dog.run())