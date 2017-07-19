#@Time : 2017/7/7 22:56
#@Author : lmy

class Student(object):
     name = "student"    #这里的name相当于java里面的类变量啊
     __score__ = 56

a = Student()
print(a.name)
print(Student.name)
print(Student.__score__)
print(a.__score__)