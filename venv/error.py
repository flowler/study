#捕获错误类型，并输出错误提示
try:
    print(1/0)
except ZeroDivisionError as e:
    print('0不能做除数%s'%e)



#捕获所有的内置错误类型
try:
    print(1/'a')
except Exception as e:
    print('%s' %e)


#自定义异常提示信息
try:
    raise NameError('helloError')
except NameError:
    print('my custom error')



try:
    c = open('name.txt')
except Exception as e:
    print(e)

finally:
    c.close()