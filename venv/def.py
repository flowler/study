

#默认参数

def function(str,age=67):
    print(str,age)
    print('hello',str)

function('cy',89)#如果给值时，未给，则用默认，给了则用已给


#匿名函数：
sum=lambda a,b : a+b
print(sum(10,20))

#return表达式
def sum1(a,b):
    total=a+b
    return total  #return表达式退出函数，没有return会返回none
print(sum1(2,3))


#不定长参数
def unknown(arg,*vartuple):
    print(arg)
    print(vartuple)
unknown(1,2,3,4,5)

a=int(input())
if a>6:
    pass #pass做占位符，缺少了就会报错
else:
    print(a)


matrix= [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
for row in matrix:
    for i in range(4):
        print(row[i])
print(row[i])