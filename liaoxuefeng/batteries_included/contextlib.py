import contextlib
import os
import re
#在python中打开文件需要写try finally语句来关闭打开的通道
str1 = os.getcwd()
os.chdir("E:\\pythonFiles\\learnPython\\liaoxuefeng\\use_io")
print(str1)

try:
    f = open("text.txt",'r')
    f.read()
finally:
    f.close()

with open("text.txt","r") as f :  # 这种写法可以避免麻烦的try catch 语句，只要实现 __enter__ 和 __exit__两个方法的就可以用 with as 语法来打开
    f.read()


# 定义一个类 包含 __enter__ 和__exit__方法

class Query(object) :
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print("Begin")
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print("Error")
        else :
            print("End")

    def query(self):
        print("Query info about the name: %s" %self.name)

query = Query("Bob")
query.query()

with  Query("Lily") as q: #只要实现类 __enter__  __exit__ 函数，就可以用 with as语法了啊
    q.query()









os.chdir(str1)