import os

#列表生成式
#用循环将1，22之间的偶数生成list
l=[]
for i in range(1,22):
    if i % 2 == 0:
        l.append(i*i)
print(l)


#用列表生成式将1，22间偶数生成list,if放后面时不能加else
l1=[x*x for x in range(1,22) if x%2==0]
print(l1)
#if放前边时必须加else，
l12=[x*x if x%2==0 else 0 for x in range(1,22) ]
print('l12',l12)

#列出当前目录下的所有文件和目录名
file=[d for d in os.listdir('.')]
print(file)

#使用两层循环全排列,str不能算算数
l2=[int(m)*int(n) for m in '123' for n in '234']
print(l2)

#遍历dict，记住前后数据类型要保持一致
d={'a':'1','b':'2','c':'3'}
d1=[k+'='+v for k,v in d.items()]
print(d1)

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d2={'a':'1','b':'2','c':'3'}
for k ,v in d2.items():
    print(k,'=',v)


#把一个list中所有字符串变成小写lower方法
l3=['ABD','WDS','asd']
s1=[s.lower() for s in l3]
print(s1)

#判断list中数据是否是str，如果是，转换为小写
l3=['ABD','WDS',18,'asd']
s2=[ss.lower() if isinstance(ss,str) else ss for ss in l3 ]
print(s2)


