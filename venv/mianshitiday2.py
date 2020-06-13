#将排序好的列表打乱random.shuffle
import random
alist=[1,2,3,4,5]
random.shuffle(alist)
print(alist)

#字典以value排序
dv={'d':1,'b':20,'c':5}
print(dv)
d1=sorted(dv.items(),key=lambda x:x[1])
print(d1)
dk={'d':1,'b':20,'c':5}
d2=sorted(dk.items(),key=lambda x:x[0])
print(d2)

dv={key:value for (key,value) in iterable}
print(dv)
