#汉诺塔递归函数
# def hannuota(n,a,b,c):
#     if n==1:
#         print(a,c)
#     else:
#         hannuota(n-1,a,c,b)
#         hannuota(1,a,b,c)
#         hannuota(n-1,b,a,c)
#     return
# print(hannuota(3,'a','b','c'))




#使用迭代查找一个list中最小和最大值，并返回一个tuple
def find(l):
    for i in l:
        max1=max(l)
        min1=min(l)
    return(max1,min1)
print(find([1,2,3]))