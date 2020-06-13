def add(x,y):
    return x+y


def add(x,y):return x+y
lambda x,y: x+y

def fun2(item):
        return item[1]
dicta={'a':'aa','b':'bb'}
for i in dicta.items():#取字典的每个值
    print(i)

a=[1,4,6]
print(list(map(lambda x:x+1 ,a)))


from functools import reduce
print(reduce(lambda x,y:x+y,[2,3,4],1))




t1=(1,2,3)
t2=(4,5,6)
for i in zip(t1,t2):
    print(i)


d1={'bbb':'hhh','ccc':'jjj'}
d2=zip(d1.values(),d1.keys())
print(dict(d2))