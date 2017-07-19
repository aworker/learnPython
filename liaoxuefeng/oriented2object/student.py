class Student(object):
    def __init__(self, name, score):
        self.__name = name;  # name变量是私有的。用__表示。score变量是共有的。
        self.score = score;
        self.__own__ = 'i believe what i can do!'

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

    def get_grade(self):
        if self.score > 80:
            print("A")
            return
        if self.score > 60:
            print('B')
            return
        print('C')

    def set_name(self, name):
        if len(name) > 4:
            raise ValueError('bad score')
        self.__name = name

    def get_name(self):
        return self.__name


stu = Student('wangweichao', 64)
# print(stu.__name)
print(stu.get_name())
stu.set_name("lim")
print(stu.get_name())
print(stu.__own__)
print(stu._Student__name)  # python 的私有变量不是不可以被访问的，也是有方法的。就像这个行的这个方法。
