list=[1,2,3,4]
l=iter(list)  #创建迭代器
print('输出第一个数',next(l))
print('输出下一个数',next(l))
for x in l:
    print(x)  #遍历x



def my_function(str):
    print(str)
    return

my_function('hh')
