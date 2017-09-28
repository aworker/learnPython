import hashlib

md5 = hashlib.md5()
md5.update("I am a good boy".encode("utf-8"))
print(md5.hexdigest())

md5 = hashlib.md5()   # 分开写和总体写结果是一样的
md5.update("I am a good ".encode("utf-8"))
md5.update("boy".encode("utf-8"))
print(md5.hexdigest())


md5 = hashlib.md5()
md5.update("123456".encode("utf-8"))
print(md5.hexdigest())

#md5 用来存储用户名 对应的密码是非常好的一种保密方式，这样即使黑客或者管理员拿到了其存储在数据库中的密码，但是也只是其md5的值。保证数据不会被泄露啊。