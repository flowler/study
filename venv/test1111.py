import sys



# list1=[0,1,2,3,4,3]
# print(len(list1))
# s=list(set(list1))
# print(type(s))
# print(s)


#去掉字符串前后空格
def trim(l):
    while l!=' ' and l[0]==' ':
        l=l[1:]
        print('1',l)
    while l!=' ' and l[-1]==' ':
        l=l[:-1]
        print('-1',l)
    print(l)

# if trim('hello  ') != 'hello':
#
#     print('测试失败1!')
#
# elif trim('  hello') != 'hello':
#
#     print('测试失败2!')
#
# elif trim('  hello  ') != 'hello':
#
#     print('测试失败哈哈哈哈!')
#
# elif trim('  hello  world  ') != 'hello  world':
#
#     print('测试失败4!')
#
# elif trim('') != '':
#
#     print('测试失败5!')
#
# elif trim('    ') != '':
#
#     print('测试失败6!')
#
# else:
#
#     print('测试成功!')


trim('  hello  word  ')


#递归函数:在函数内部调用函数本身就是递归
def fact(n):
        if n == 1:
            return 1
        return n * fact(n - 1)
sys.setrecursionlimit(10000) #import sys库，可以手动调整递归调用深度，不然会报错
print(fact(1000))