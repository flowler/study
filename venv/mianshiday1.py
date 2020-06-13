#1.利用切片操作，实现一个trim()函数，
# 去除字符串首尾的空格，注意不要调用str的strip()方法.

def trim(s):
    while s[:1]=='':
        s=s[1:]
    while s[-1:]=='':
        s=s[:-1]
    return s

print("s=",trim('a '),'hh')


#去掉字符串前后空格
# def trim(l):
#     while l!=' ' and l[:1]==' ':
#         l=l[1:]
#         print('1',l)
#     while l!=' ' and l[-1:]==' ':
#         l=l[:-1]
#         print('-1',l)
#     while l==' ':
#         print(l)
#     print(l)

#trim(' a ')