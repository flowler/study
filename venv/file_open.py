#将小说的主要人物写入在文件中
file1=open('name.txt','w')#操作文件时，先打开
#open('文件名，mode模式=r只读(默认) w写入(会把之前写入内容覆盖掉)  a再次写入')
file1.write('chenyuan\n')
file1.close()#写入之后关闭文件





#再次写入文件,mode值为a
file3=open('name.txt','a')
file3.write('fengfenghhh')
file3.close()


#读取文件
file2=open('name.txt')
print(str(file2.read())) #读取全部内容
file2.close()

#readlines逐行处理
file4=open('name.txt')
for line in file4.readlines():
    print(line)
#readline 读取一行
file5=open('name.txt')
print(str(file5.readline())) #读取一行内容
file5.close()



#tell()查看文件指针位置以及seek()操纵指针位置查看指针位置
file6=open('name.txt')
print('当前文件指针位置：%s'%file6.tell())
print('当前读取到了一个字符，字符内容是：%s'%file6.read(1))#读取一个参数
print('当前文件指针位置：%s'%file6.tell())
print('进行seek操作，移动指针到0的位置：%s'%file6.seek(0))
print('当前文件指针位置：%s'%file6.tell())
print('进行seek操作，从0开始偏移5个位置：%s'%file6.seek(199,0))
print('当前文件指针位置：%s'%file6.tell())
print('当前读取到了一个字符，字符内容是：%s'%file6.read(1))