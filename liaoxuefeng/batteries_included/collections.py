# 主要学习python的内置collecitons模块
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple("Point",['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point)) #此处打印true，表示p是Point的一个实例
print(isinstance(p,tuple)) #此处打印true，表示p也是tuple的一个实例

#举个例子，如果想表示一个不可以改变的圆的位置和大小信息可以如下：
Circle = namedtuple("Circle",['x','y','radius'])

q  = deque(['a','b','c']) #deque数据结构用双链表实现，所以利于插入和删除
q.append('x')
print(q)
q.appendleft('y')
print(q)


#看一下defaultdict 这种数据结构，其可以定义默认的返回值，而不是不存在key对应的值时候抛出keyError
dd = defaultdict(lambda:"NULL")
dd['key1'] =  "wahaha"
print(dd['key1'])
print(dd['key2'])#对于defualtdict不存在的value，其返回在定义时候默认的值

d = dict([('a',1),('b',2),('d',4)])
print(d['a'])
# print(d['c']) # 这里dict会抛出一个KeyError表示'c'对应的value是不存在的
print(d) #可以通过打印看到dict的输出是没有顺序的



od = OrderedDict([('z',1),('y',2),('x',3)])
print(od) # OrderedDict 会按照其输入顺序来输出
print(od.keys()) # key值也会按照这个顺序输出

cd =defaultdict(lambda:0)
for char in "programming":
    cd[char] = cd[char] + 1
print(cd)

counter = Counter()
print(counter['dd']) #Counter类时默认值为0的defaultDict，我的理解
for char in "programming":
    counter[char] = counter[char] + 1
print(counter)  #Counter 类就是一种用来计数的字典


counter_1 = Counter("aadbdeeldgjl")
print(counter_1) #可以直接统计啊











































