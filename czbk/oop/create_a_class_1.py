#!/usr/bin/n python3
# -*- coding: utf-8 -*-


#dir 函数可以列出python对象的所有内置方法和成员变量
# 在python中一切 皆为对象

# class 类名   (类名要符合 大驮峰命名法 首字母要大写）
#   def 方法1(self,参数列表):  （第一个参数必须是self,self 相当于java中的this)
#       pass
#   def 方法2(self,参数列表):
#       pass


#   对象变量 = 类名()  这样来完成创建一个对象

class Cat:
    def eat(self):
        print("%s爱吃鱼"%self.name)

    def drink(self):
        print("%s要喝水"%self.name)

#创建一个猫对象
tom = Cat()

tom.name ="Tom" #在python中可以直接给对象添加方法
tom.eat()
tom.drink()
print(tom)
print(id(tom)) #id函数可以直接获得 python对象的十进制内存地址



print(tom.name)















