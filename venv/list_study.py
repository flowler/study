# #列表List
# list1=['hhh',20,0.2,77,99]
# del list1[2]#删除第二个元素
# print(list1)
# print(list1[0],list1[1:2])#输出第0个元素，第一个元素
# print(list1[0:2])#输出0开始的两个元素，即前两个
# print(list1[-1])#输出最后一个元素
# list1[1]=30+2#将下标为1的元素值改为 30+2，输出后会直接输出32
# print(list1)
#
# #列表操作符
# print(len(list1))#输出列表长度
# print(len([1,2,3,4,5]))#输出列表长度
# list2=list1+[';',31,4,3]#两个列表连接成一个列表
# print(list2)
# print(list1+list2)#两个列表连接为一个列表
# print((list1+list2)*3)#两个列表连成一个后*3重复列表3次
# print([1,2,3,4]*4)#重复列表4次
# a=3 in list1 #3是否在列表中
# print(a)
# for x in list1: #遍历数组
#     print(x,end='')


#列表拼接与截取
list2=['c','h','e','n']
list1=['y','u','a','n','90']
print(list1+list2)#将两个列表拼接在一起
print(list2[:2])#截取下标从0开始的两个元素，0可以省略
print(list2[1:])#截取下标从1开始后面的所有元素
print(list2[-2])#截取倒数第二个元素
print(list2[2])#截取第三个元素
print([1,2,3]+[2,3,4])

#列表中函数
list3=[list2,list1]
print(list3)
print(len(list1))
print(max(list1))
print(min(list1))


#列表中方法
list4=['a','n','b','a','b']
list6=list4.copy()
print('复制list4',list6)
list5=['a','n','b','a','b']
list5.clear()
print(list5)
s=sorted(list4)
print('排序list4的值不变',list4)
print('排序s为最终排序结果',s)
list4.remove('a')#删除列表中第一个元素a
print('删除a',list4)
list4.pop(-3)
print('删除index=-3',list4)
c=list4[ : ]#先复制一个list4
a=c.sort()#sort是对内部进行排序
print('哈哈哈',a)#由于sort是对内部进行排序的，返回的是None，所有a的值是none
print(c)
list1.append(7)#在列表末尾添加元素
print(list1)
print('c出现的次数为：',list2.count('c'))#某元素在列表中的出现的个数
c=list4[ : ]
a=list4.sort()#sort是对内部进行排序
print(a)#由于sort是对内部进行排序的，返回的是None，所有a的值是none
print(list4)
b=c.reverse()
print(b)
print(c)
c.remove('a')#删除列表中第一个元素a
print('删除a',c)
c.pop(-1)
print('删除index=-3',c)
c.insert(3,'y')
print('在下标为3处插入y',c)


#元组
t=(1,2,3,3,42,3)
print(t)
for x in t:
    print(str(x),end=''+",")
t1=sorted(t)
print(t1)

