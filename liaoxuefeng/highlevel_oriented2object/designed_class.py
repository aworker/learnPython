#@Time : 2017/7/11 21:53
#@Author : lmy

class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):  #__str__ 方法相当于java的toString方法
        return self.name

    def __repr__(self): #当在交互式编译环境中，要重写次 方法，才能让开发者看到爽爽的代码啊
        return self.name

s1 = Student("ll")
print(s1)
Student("eee")


class Fib(object):
    def __init__(self,limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):  #配合__next__方法实现 for ...in循环这样的每次for in都会 得到__iter__方法的一个返回值，然后调用这个返回值的__next__方法来得到下一个指，直到遇到StopInteration错误
        return  self

    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > self.limit:
            raise StopIteration()
        return self.a

for i in Fib(100):
    print(i)



class Fib1(object):
    def __getitem__(self,n):  #重写此方法，可以让类像数组那样使用
        a,b = 1,1
        for x in range(n) :
            a, b = b, a+b
        return a

print(Fib1()[0])



class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b, a+b
            return  a

        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            a,b = 1,1
            li = []
            if start is None:
                start = 0
            for i in range(stop):
                if i >= start:
                    li.append(a)
                a,b = b,a+b
            return li

fill = Fib2()
print(fill[1:100])


class Teacher(object):
    def __init__(self):
        self.name = "Machael"

    def __getattr__(self,attr):
        if attr == 'score':  #默认定义一个属性，如果类中没有这个属性，但是次方法中有这个属性，那么就用这个方法里面的。
            return  99
        if attr == "level":
            return lambda: "hha"  #也可以定义方法，只要把返回值的地方做下修改啊
        raise AttributeError("Teacher has no \'%s\' attribute" %attr)  #如果没有此行代码，那么调用 类没有的属性时候会返回None。定义此行后，会抛出异常


teacher = Teacher()
print(teacher.score)
print(teacher.level())
#print(teacher.lllll)


class Can(object):
    def __call__(selfs):
        print("dddd")

can = Can()
print(can())

print(callable(Teacher))



