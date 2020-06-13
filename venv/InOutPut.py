name=input('请输入\n你的名字：\n')#输入
work=input('请输入你的工作：')#输出
print()
input('\n\n按下enter后退出')
#print(values,sep,end,file,flush)

#输出
#连接符
print('\n\n','#连接符用法')
print('hhh''aaa''哈哈哈哈哈哈')#无对象，只有字符串时，可以无连接符，输出无空格
print('hhh'+'aaa'+'哈哈哈哈哈哈')#用+号连接输出无空格
print('hhh','aaa','哈哈哈哈哈哈')#用逗号连接会自动带空格


##连接类型：对象、字符串、浮点型、整型
print('\n\n','#连接符可以连接的类型')
print('hhh','hhh',6,0.5,work)# ,可以连接任意类型
print('hhh''aaa''哈哈哈哈哈哈')#无对象，只有字符串时，才可以无连接符
print('hhh'+name)# +只可以连接string，不能连接int和float



#end结尾,必须放在最后
print('\n\n','#end用法')
print('www','baidu','com',end='.')#用.结尾
print('www','baidu','com',end='')#去掉默认换行
print('www','baidu','com',end='',sep='.')#位置参数跟在关键字参数后面


##sep 设置间隔符
print('\n\n','#sep 设置间隔符')
print('www','baidu','com',1,sep='.')#元素间都会以.分隔


#换行
print('\n\n','#换行与非换行')
print('my name is：',name,'\nmy work is:',work)#一个print实现换行，用\n换行符
print('hello换行'+'hh'+'jhhh',name,end='')#print默认换行，不需要换行时，用end=''
print('不换行',name,end='\n')#end='\n',代表换行
print()#默认换行
print('\n','\n')#\n换行符
print('work,换行',work)

#file参数
# file=sys.stdout
# 设置输出设备，及把print中的值打印到什么地方，默认输出到准端，可以设置
# file = 文件储存对象，把内容存到该文件中，如下：
f = open('/Users/chenyuan/Desktop/test.txt', 'w')
print('hello word', file=f)
f.close()

#flush
#flush=False该参数主要是刷新， 默认False，不刷新，Ture时刷新
# 正常情况下print到f中的内容先从到内存中，当文件对象关闭时才把内容输出到
# test.txt 中，当flush=True时它会立即把内容刷新存到 test.txt 中
f = open('test.txt', 'w')
print('hello world',file=f,flush=True)
1
