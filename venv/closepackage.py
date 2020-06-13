def func():
    a=1
    b=2
    return a+b

def sum(a):
    def add(b):

        print('a',a,b)
        return a + b
    return add #外部函数return返回时要返回内部函数名
#如果单独使用add，叫函数的名称或者叫引用
#如果使用add() 调用函数

num1=func()
num2=sum(2)#num2相当于
print(num2(6))

print(type(num1)) #<class 'int'>

print(type(num2)) #<class 'function'>


#闭包实现计数器
def countercy():
    cnt=[0]
    def add_one1():
       cnt[0] += 1
       return cnt[0]

    return add_one1()

cy=countercy()
print(cy())