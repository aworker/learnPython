#@Time : 2017/7/4 23:09
#@Author : lmy

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(type(d) == type(Animal()))
print(isinstance(a,Animal))
print(isinstance(d,Animal))
print(isinstance(h,Animal))

print(isinstance(d,(Husky,Animal)))  # isinstance 函数还可以判断其是不是N种中的一种
print(isinstance(a,(Husky,Dog)))





print(dir("ABC")) #dir()函数可以返回一个对象的所有方法和属性 在python 中__xx__的方法和属性都有特殊的用法比如一个对象的__len__() 方法，就会被len()函数调用
class MyLen(object):
    def __len__(self):
        return 9

print(len(MyLen()))




class MyObject(object):  #可以用hasattr、getattr、setattr方法来对一个对象的状态进行操作
    def __init__(self):
        self.x = 9
        self.__hide__ = 88

    def power(self):
        return  self.x * self.x

myObject = MyObject()
if hasattr(myObject,'x') :  #注意状态必须为字符串
    print(myObject.x)

if hasattr(myObject,'__hide__'):  #隐藏状态也可以检查出来的
    print(True)
else :
    print(False)

setattr(myObject,'ll',33)
print(myObject.ll)

#getattr(myObject,'ddd') #如果对象没有指定的状态，那么用getattr会报错
print(getattr(myObject,'ddd',404)) #可以传第三个参数,如果对象没有指定的状态，那么就返回第三个参数

print(hasattr(myObject,'power'))  #也可以获取对象的方法
fn = getattr(myObject,'power')
print(fn())












