import numpy as np

#创建ndarray对象
a = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]) #从列表中创建
a = np.array(((1,2),(3,4))) #从元组中创建
a = np.array(((1,2),[2,3])) #也支持元组和列表混合创建
a = np.arange(4) #创建从1到n-1的元素的一维 ndarray对象
a = np.ones((2,3,4),dtype=np.int64) #np.ones(shape,[dtype]) 根据shape 生成一个ndarray的对象，其中dtype可以指定具体的每个元素的类型 可以用np.int泛指一切numpy中的int类型
a = np.zeros((2,1)) #同ones方法用过相同，不过它赋的初值是0
a = np.full((2,3,4),12,dtype=np.float) #可以生成指定元素值和指定形状的ndarray对象
a = np.eye(3) #创建见一个n*n的矩阵，
a = np.ones_like(np.arange(12).reshape(2,3,2)) #按照传进去的ndarray对象的形状创建一个相同形状的ndarray对象，不过对象的所有元素的值都是1
# np.zeros_like(ndarrayObject) np.full_like(ndarrayObject, val) 的用法和ones_like大同小异
a = np.linspace(1,10,3) #从1 开始到10结束等距离的创建3个元素的ndarray对象
b = np.linspace(1,10,3,endpoint=False) #从1开始到10结束等级里的创建三个元素的ndarray对象，但是不包括10
c = np.concatenate((a,b)) # a b 两个ndarray对象收尾相连
print(a)

# ndarray 对象的属性
print(a.ndim)  # 维度
print(a.shape) # 形状
print(a.size) # 一共有多少个元素
print(a.dtype) # 元素的类型
print(a.itemsize) #其中元素的大小 单位是字节
'''
numpy 支持的元素类型
bool 布尔类型，True或False
intc 与C语言中的int类型一致，一般是int32或int64
intp 用于索引的整数，与C语言中ssize_t一致，int32或int64
int8 字节长度的整数，取值：[‐128, 127]
int16 16位长度的整数，取值：[‐32768, 32767]
int32 32位长度的整数，取值：[‐2 31 , 2 31 ‐1]
int64 64位长度的整数，取值：[‐2 63 , 2 63 ‐1]
uint8 8位无符号整数，取值：[0, 255]
uint16 16位无符号整数，取值：[0, 65535]
uint32 32位无符号整数，取值：[0, 2 32 ‐1]
uint64 32位无符号整数，取值：[0, 2 64 ‐1]
float16 16位半精度浮点数：1位符号位，5位指数，10位尾数
float32 32位半精度浮点数：1位符号位，8位指数，23位尾数
float64 64位半精度浮点数：1位符号位，11位指数，52位尾数
complex64 复数类型，实部和虚部都是32位浮点数
complex128 复数类型，实部和虚部都是64位浮点数
'''

#非同质的ndarray对象，非同质的ndarray对象不能发挥Numpy包的优势，要尽量避免使用
x =  np.array([[1,2,3,4],[1,2,3]]) # 元素个数不相同
print(x.shape)
print(x.dtype)
print(x.size)


#ndarray对象的一些属性变换
print("ndarray对象的一些属性变换")
b = np.array((2, 3, 4, 5, 6, 7))
b.reshape(2,3) #返回一个变形的的ndarray对象，但不改变b
b.resize(2,3) #同上，但是改变b的形状
print(b)
c = b.flatten() #返回一个将b降维成一维的ndarray对象，但是b不被改变
print(c)
d = c.astype(np.float) #拷贝ndarray对象c，返回一个np.float类型的ndarray对象
print(d)
a = d.tolist() #将ndarray对象转化成python中的列表
print(type(a))


#ndarray 对象的切片和索引
reshape = np.arange(24).reshape((2, 3, 4))
print(reshape[1][2][3]) #ndarray对象的索引和一般python的索引语法没有区别
print(reshape)
print(reshape[:,1:2,1:3]) #切获取子集的ndarray对象



#ndarray对象的运算
arange__reshape = np.arange(24).reshape((2, 4, 3))
print(arange__reshape * 4) #将每一个ndarray对象的元素和4相乘
'''
ndarray对象的一元运算符
np.rint(x) 计算数组各元素的四舍五入值
np.modf(x) 将数组各元素的小数和整数部分以两个独立数组形式返回
np.cos(x) np.cosh(x)
np.sin(x) np.sinh(x)
np.tan(x) np.tanh(x)
计算数组各元素的普通型和双曲型三角函数
np.exp(x) 计算数组各元素的指数值
np.sign(x) 计算数组各元素的符号值，1(+), 0, ‐1(‐)
'''

'''
ndarray对象的二元运算符
+ ‐ * / ** 两个数组各元素进行对应运算
np.maximum(x,y) np.fmax()
np.minimum(x,y) np.fmin()
元素级的最大值/最小值计算
np.mod(x,y) 元素级的模运算
np.copysign(x,y) 将数组y中各元素值的符号赋值给数组x对应元素
> < >= <= == != 算术比较，产生布尔型数组
'''



