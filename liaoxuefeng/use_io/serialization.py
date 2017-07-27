#@Time : 2017/7/27 8:03
#@Author : lmy


import pickle  #pickle 包里面的序列化方法只是为python自己所使用和识别的，不同语言间不可以通用，而且不同的python版本也不可以通用的啦。
d = dict(name="bob",age = 19,score = 48)
print(pickle.dumps(d))   #python 对 对象的序列化方法

with open('dump.txt','wb') as f:  #python 里面把对象 序列化到 硬盘
    # f.write("dahaoren")
    pickle.dump(d,f)

with open('dump.txt','rb') as r:
    load = pickle.load(r)

print(load)


