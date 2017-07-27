#@Time : 2017/7/21 7:42
#@Author : lmy

import os

print(os.name)  #nt说明操作系统类型是windows  posix说明操作系统是linux unix 或者mac os x
#print(os.uname())  #os.uname 在windows上是不提供的啊。只在linux上提供
print(os.environ)  #操作系统的环境变量
print(os.environ.get('TMP'))


print(os.path.abspath('./text.txt')) #查看text.txt 文件的绝对路径
print(os.path.abspath('.'))  #查看当前目录的绝对路径

#在当前路径下创建一个新的目录
join = os.path.join(os.path.abspath('.'), 'testdir') #通过join而不是自己乱写路径可以避免不同操作系统上'/'和'\'的差异
print(join)
# os.mkdir(join)
#os.rmdir(join)

split = os.path.split(join) #类似于不要用自己用字符串操作符来组装文件路径一样。文件路径的分隔也最后是通过path.solit 函数来进行
print(split)

print(os.path.splitext(join)) #获取文件拓展名

# rename = os.rename('aa.txt', 'test11.txt') #重命名啊
# print(rename)


#列出当前路径下的所有文件夹

for x in os.listdir('.'):
    print(x)

[x for x in os.listdir('.') if os.path.isdir(x)]  #这是什么写法啊


