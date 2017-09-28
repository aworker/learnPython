import itertools

natuals = itertools.count(step = 5) #迭代器 start表示开始的数字， step表示步长
# for i in natuals :
#     print(i)


cycles = itertools.cycle("ABC")  # cycle函数会循环枚举 其中的变量
# for i in cycles :
#     print(i)


repeat =  itertools.repeat("AA", 4) # repeat函数把 “AA” 循环4次
for i in repeat :
    print(i)


ns = itertools.takewhile(lambda x : x<= 10, natuals)  #虽然natuals是无限循环的，但是可以用takewhile函数对其作出限制
print(list(ns))


for key, group in itertools.groupby("AABBCCC"):  # groupby函数可以把其中的相同数据 归为一类 这个函数也可以由我们自己定义
    print(key,list(group))


for key, group in itertools.groupby('aAbbBB', lambda c: c.upper()):
    print(key,list(group))

