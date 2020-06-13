# Python内建的filter()函数用于过滤序列。
#
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#
# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def filter_test(n):
    if n%2==1:
        return n
f=list(filter(filter_test,[1,2,3,4]))
print(f)

#删除list空格 （strip删除字符串中首尾指定的字符）
def filter_test1(n1):
    return n1 and n1.strip()
f1=list(filter(filter_test1,['A','    ','1','']))
print(f1)

#用filter求素数
#1、创建一个以3为开头的序列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
#2、定义一个筛选器
def _not_divisible(n):
    return lambda x:x%n>0
#3、定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter()#初始化序列
    while True:
        n=next(it)#返回序列第一个数
        yield n
        it=filter(_not_divisible,it)
#由于primes是一个无限序列，给出终止循环条件
for n in primes():
    if n<100:
       print(n)
    else:
        break



