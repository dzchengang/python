class Student(object):
    def __init__(self,name,score,age):
        self.name=name
        #score 是私有变量 外部无法访问
        self.__score=score
        #虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
        self._age=age
    def printScore(self):
        print("%s:%s"%(self.name,self.__score))

    #自定义类返回值
    def __str__(self):
        return "student object(%s)" % self.name

    __repr__=__str__

stu=Student("cheng",20,18)
stu.printScore()
print(stu.name)
#访问报错
#print(stu.__score)
print(stu._age)

print(stu)