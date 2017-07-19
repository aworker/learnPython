#@Time : 2017/7/17 21:59
#@Author : lmy

class Hello(object):
    def hello(self,name='World'):
        print("Hello,%s."  %name)

h = Hello()
h.hello()
print(type(Hello))  #type函数可以查看类或者实例的类型，如果是类为参数，那么返回的就是 type 类型
print(type(h))    #如果是实例为参数，返回的就是该实例所属的类的类型。


def fn(self,name="World"):
    print('Hello, %s.' %name)  #可以利用type函数来动态定义类

Hello1 = type('Hello',(object,),dict(hello=fn))

h1 = Hello1()
h1.hello()
