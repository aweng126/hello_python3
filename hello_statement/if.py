# -*- coding: utf-8 -*-

#注意有一个冒号：  同时注意python是通过缩进来判断语句块的
age=20
print("your name is", age)
if age>=18:
    print ('adult')
elif age>=6:
    print("teenager")
else:
    print("kins")

# 如果仅仅是简单的if判断,当条件是非零数值，非空字符串，非空list的时候
x=1
if x:
    print('true')