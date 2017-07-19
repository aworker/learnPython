#@Time : 2017/7/18 8:20
#@Author : lmy

try :  #python里面的try 语句
    print("Try")
    i = 10/0
    print("result:",i)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally')

print("End")


try:
    print('Try')
    r = 10 /2
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
else:   #可以加个else语句，如果没有出错误就执行else语句里面的内容
    print('fortunately, no error raise')
finally:
    print('finally...')

print('End')



class FooError(ValueError):  #我们也可以自己定义错误类型啊然后通过 raise 抛出异常
    pass

def foo(value):
    if value == 0:
        raise FooError()

foo(0)



