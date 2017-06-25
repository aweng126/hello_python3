#记住字符编码用utf-8

#python3 字符串以unicode进行编码,也就是说支持多语言
print("包含中文的str")
#通过ord可以获得字符的整数表示 chr会把对应的编码转化为对应的字符
print(ord('A'))
print(chr(66))
#或者知道字符的整数编码，还可以使用16进制来写str
print('\u4e2d\u6587')

#通过len函数获得字符串长度
print(len('hello'))

#文件的格式化表示%s
print('hello,%s'%'my world')

print('this number is %d'%10)

#f前面的数字为几，就保留几位小数
print('this number is %.1f '%2.1234)
## %% 用来占位%
print('this number is %.1f %%' %3.1234)
