#@Time : 2017/7/19 8:11
#@Author : lmy
import logging
logging.basicConfig(level=logging.INFO) #可以控制输出日志的级别 有 info，warning，debug，erro四个级别


def foo(n):
    num = int(n)
    assert n != 0, 'input cannot be zero' #assert 可以用来调试程序，还可以通过给python解释器在启动时候设置 参数 0 来决定assert语句是否生效
    print(10/n)

foo(2)



def fun(n):
    logging.info('n = %d' %n)
    print(10/n)

fun(0)

