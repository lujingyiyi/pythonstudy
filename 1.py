print("******print的简单使用*******")
print(90)
a = 100
b = 20
print(a*b)
print("北京")
print(a,b,100)
print(chr(98))
print(ord("被"))
print('\u5317')
fp=open('note.txt','w')
print('欢迎来到python世界',file=fp)
fp.close()
print('北京'，end='--->')
print('欢迎你')
print(1+2)
print(2.24)
print(1,3,4,5)
print(124,233,23,3,sep='.')
#print('北京'+2022)会发生错误，需要把2022当做字符串处理
print('北京欢迎你'+'2022')
print("******输入和输出*******")
#variable=input('提示文字')
name=input('请输入您的姓名：')
print('您的姓名是：'+name)
num=int(input('亲，输入您的幸运数字：'))
print('您的幸运数字是：',num)







