#简单实现range函数；
def frange(start,stop,step):
    while start<stop:
        yield start#记录当前执行的值，下次调用next后继续输出下一次的值
        start+=step


for i in  frange(10,20,2):
    print(i)
