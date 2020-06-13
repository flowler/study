var=123
g=222
def var_value():
    global g#定义为全局变量
    g=999
    var=456 #局部变量，里外互不影响
    print(var)
    print(g)


var_value()#里面值为456
print(g)#由于是全局变量，所以里外值一样
print(var)#函数外面值为123