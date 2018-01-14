#!/usr/bin/env pyton3
# -*- coding:utf-8 -*-

# 本例子主要讲解类属性和类方法的定义
class Tool(object):
    #使用赋值语句就可以定义类属性了
    count = 0

    @classmethod #告诉python解释器，这是一个类方法
    def class_method(cls): #类方法传递的参数必须是 ‘cls’（class的缩写）
         print("this is a class method")
    
    @classmethod
    def show_count_num(cls):
        print("class instance number is %s" % cls.count)#在类内部用cls调用类属性

    def __init__(self):

        #类属性的值加1
        Tool.count += 1 #用来统计一共有此类一共创建了多色个实例


tool1 = Tool()
tool2 = Tool()

print(Tool.count)
print(tool2.count)#在python中最好使用 类名.类属性 的方式来访问类属性。
print(Tool.show_count_num())
