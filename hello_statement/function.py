# -*- coding: utf-8 -*-
#调用函数
print(abs(-2))

a=max(2,3,23)
print(a)

#定义函数
def hello(name):
    print('hello',name)


hello('qingwen')

##如果暂时还没有想好内容，那么可以用pass来进行占位，这样在调用的是偶不会出错
def secondhello(name):
    pass

secondhello("hello")

#多个返回值
def thirdHello(x):
    #参数验证
    if not isinstance(x,int):
        raise  TypeError('bad operated type')
    return x-1,x-2;

print(thirdHello(3))  #(2, 1)
#thirdHello('234')
#参数验证

