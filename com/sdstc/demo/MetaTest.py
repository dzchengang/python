#元类测试


'''
使用type 创建类

'''
def fn(self,name='world'):
    print('hello %s'% name)

# 第一个参数 类名
# 第二个参数 类继承
# 第三个参数 方法和属性
Hello=type('Hello',(object,),dict(hello=fn))

h=Hello()
h.hello()

'''
metaclass  是创建类的类
'''

class ListMetaclass(type):
    #
    # 第二个参数 类名
    # 第三个参数 类继承
    # 第四个参数 方法和属性
    def __new__(cls, name,bases,attrs):
        attrs['say_'+name]=lambda self,value,saying=name:print(saying+","+value+"!")
        return type.__new__(cls,name,bases,attrs)


class MyList(list,metaclass=ListMetaclass):
    pass

l=MyList()
l.say_MyList('ss')


'''
orm 实例

'''

class Field(object):
    def __int__(self,name,column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    pass



