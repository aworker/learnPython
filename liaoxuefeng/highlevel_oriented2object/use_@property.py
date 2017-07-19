# @Time : 2017/7/10 21:45
# @Author : lmy

class Student(object):
    def __init__(self, score):
        self.__score = score
        self.__sex = 'male'

    @property  #用@property关键字可以把方法变成属性
    def score(self):
        print("get self.__score")
        return self.__score

    @score.setter   #用这个关键字把setter方法变成一个可以像属性一个一样的赋值方法
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score ust be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')

    @property
    def sex(self):
        return  self.__sex


s = Student(4)
print(s.score)
s.score = 45
print(s.score)
# s.score =109
print(s.sex)
