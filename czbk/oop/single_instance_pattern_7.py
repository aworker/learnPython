#!/usr/bin/env pyton3
#-*- coding:utf-8 -*-

class ShowNewMethodUse(object):


    @staticmethod
    def __new__(cls, *args, **kwargs): #object 类中的静态方法 一个*表示多值的元组参数 两个*表示多值的字典参数
        print("new 方法用来分配内存空间")

        instance = super().__new__(cls) #分配内存空间
        return instance  # new 方法一定要把内存的句柄返回


    def __init__(self):
        print("播放器初始化")


class MusicPlayer(object): #使用单例设计模式
    instance = None
    initFlag = False
    @staticmethod
    def __new__(cls, *args, **kwargs):  #分配内存执行一次
        if cls.instance is None :
            cls.instance = super().__new__(cls)

        return  cls.instance
    pass

    def __init__(self): #初始化动作执行一次
        if MusicPlayer.initFlag == True :
            return

        #执行初始化动作

        MusicPlayer.initFlag = True

player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)