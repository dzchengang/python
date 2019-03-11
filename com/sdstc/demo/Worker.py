class Worker(object):
    #限制该class实例能添加的属性
    #定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('name','age','job')

    def set_job(self,job):
        self.job=job

    def get_job(self):
        return self.job

    #用来设置属性  简便使用   @property本身又创建了另一个装饰器@job2.setter，负责把一个setter方法变成属性赋值
    @property
    def job2(self):
        return self.job

    @job2.setter
    def job2(self,value):
        self.job=value





worker=Worker()
worker.name='lisi'

# 报错
#worker.job2='xx'
worker.set_job("programer")
print(worker.get_job())

worker.job2=19
print(worker.job2)
