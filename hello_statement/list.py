# -*- coding: utf-8 -*-

classmates=['michael','hello','world']
#直接打印整个链表
print(classmates)
#通过索引获得链表对应位置的元素
print(classmates[0])
#链表长度
print(len(classmates))
#如果链表越界会怎么样呢？报错信息 out of range
#print(classmates[3])
#可以逆向获取对应位置的元素,对应的最后一个是-1，倒数第二个是-2
print(classmates[-1])

#向list中追加元素到末尾
classmates.append("yeah")
print(classmates)

#把元素插入到指定的位置
classmates.insert(1,"hi")
print(classmates)

#删除末尾的元素
classmates.pop()
print(classmates)

#删除指定位置的元素
classmates.pop(1)
print(classmates)

classmates[1]="want to say"
print(classmates)
