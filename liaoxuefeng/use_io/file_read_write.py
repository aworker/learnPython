#@Time : 2017/7/20 21:53
#@Author : lmy

t = open('text.txt','r')
try :
    print(t.read())
finally:
    t.close()


with open('text.txt','r') as f:  # with 语句的写法简单但是和上面的有try catch语句的功能是一样的
    print(f.read(98))   #read函数中的数字表示要读取的字节数目。



# with open('text.jpg','rb') as picture: #读一张图片的时候，要用read binary ‘rb’ 方式来打开
#     print(picture.read())


with open('read','r',encoding='utf',errors='ignore') as tt:  #errors='ignore' 表示发生错误时候选择忽略错误
    print(tt.read())


with open('write','w',encoding='gbk') as w: #python里面的都读和写的写法差不多，唯一的区别是在方法的调用上面
    w.write('hello pthon')

