# -*- coding: utf-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#通过get来获得对应的参数，同时设置如果没有参数的默认返回值
print(d.get('hello',0))

print(d)
#删除某个元素
d.pop("Tracy")
print(d)

