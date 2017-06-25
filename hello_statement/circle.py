# -*- coding: utf-8 -*-

names=['hello','this','is','qingwen']
for name in names:
    print(name)

#range(x) 生成从0开始小于x的整数
sum = 0
for x in range(101):
    sum = sum+x
print(sum)

#while循环
msum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

for x in range(10):
    if x==5:
        print(x)
        break
    elif x==3:
        print(x)
        continue
    else:
        print('x',x)