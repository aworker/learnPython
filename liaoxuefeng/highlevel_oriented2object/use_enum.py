#@Time : 2017/7/17 8:37
#@Author : lmy

from enum import Enum, unique

@unique   #此关键字可以保障枚举的类的value值唯一，如果不唯一就报错。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Sun)
print(Weekday.Fri.value)
print(Weekday(5))
