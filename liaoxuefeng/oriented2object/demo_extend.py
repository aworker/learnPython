class Animal(object):
    def run(self):
        print('Animal is running...')

class Cat(Animal):

    def run(self):
        print("Dog is running...")
    pass


def run_twice(animal):  #因为python是动态语言，其不没有类型校验，只要参数annimal 有run方法都可以调用这个函数。
    animal.run()
    animal.run()

class Timer(object):
    def run(self):
        print('a Timer is running...')


cat = Cat()
cat.run()
print(isinstance(cat,Animal))
print(isinstance(cat,Cat))
print(isinstance(cat,object))
run_twice(Animal())
run_twice(Timer())
