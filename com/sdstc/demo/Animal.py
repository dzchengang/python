class Animal(object):
    test='--test--'
    def run(self):
        print("--animal--run--")

class Bird(object):
    def fly(self):
        print("--bird--fly--")

#多重继承
class Bianfu(Animal,Bird):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def run(self):
        print("--dog--run--")
    def eat(self):
        print("--dog--eat--")

class Cat(Animal):
    def __init__(self, name):
        self.name = name


bianfu=Bianfu()
bianfu.fly()
bianfu.run()

dog=Dog("zhang")
dog.run()
dog.eat()
print(dog.test)

cat=Cat("li")

print(isinstance(dog,Cat))
print(type(dog))
print(type(cat))
#获取对象的所有属性和方法
print(dir(dog))
#判断属性是否存在
print(hasattr(dog,'name'))
#设置 属性
setattr(dog, 'age', 19)
#获取 属性
print(getattr(dog, 'age'))
#获取属性 如果没有则返回 404
print(getattr(dog, 'age2',404))

