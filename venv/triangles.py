#生成器舉例  
# def odd():
#     print('1')
#     yield
#     print('2')
#     yield
#     print('3')
#     yield#遇到yield就是一个生成器generator
#     print('4')
#     return 'done'
# o=odd()#调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
# print(next(o))#第一次调用next输出1
# print(next(o))#第二次调用next输出1
# print(next(o))#第三次调用next输出3
# #可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。


#杨辉三角
def triangles():
    l8=[1]
    while True:
        yield l8
        l8=[1]+[l8[n]+l8[1+n] for n in range(len(l8)-1)]+[1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

