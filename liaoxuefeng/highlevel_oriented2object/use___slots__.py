#@Time : 2017/7/10 21:18
#@Author : lmy

from types import MethodType

class Student(object):
    pass

s = Student()
s.name = "Michael"  #动态语言可以给实例在绑定新的属性
print(s.name)

def set_age(self,age):
    self.age = age

s.set_age = MethodType(set_age,s)  #也可以给方法实例绑定一个方法
s.set_age(34)
print(s.age)


s1 = Student()
# print(s1.name)  #给实例绑定方法和属性不会对此类的其他属性生效，如果想要对其他属性生效，可以给类绑定

Student.name = "eesma"
Student.set_age = set_age
print(s1.name)
s1.set_age(23)
print(s1.age)



class Teacher(object):
    __slots__ = ('name','age')  #用 __slots__ 变量绑定属性，没有绑定的属性不能被动态添加了;但是对其继承的子类是不起作用的

t = Teacher()
t.name = "lie"
t.age = 'age'
# t.faa = "dsds"



