import time

# print(time.time())

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间：%s秒' %(stop_time - start_time))
    return wrapper()


@timer #会把i_can_sleep函数传递到timer函数中
def i_can_sleep():
    time.sleep(3)




#闭包，传递变量，内部引用也是变量
#装饰器，传递函数，内部引用是函数