# def bubble_test(lst):
#     n = len(lst)
#     if n <= 1 or n == '':
#         return lst
#     for i in range(0,n):
#         for j in range(0,n-i-1):
#             if lst[j]>lst[j+1]:
#                 ( lst[j],lst[j+1])=(lst[j+1],lst[j])
#     return lst
#
# x=input("请输入需要排序的数列: ")
#
# y=list(x)
# arr=[]
# for z in y:
#     arr.append(int(z))
# arr1=bubble_test(arr)
# print("排序后的：",arr1)
# #去重
# arr2=set(arr1)
# print(arr2)



def bubble1(lst):
    n=len(lst)
    if n<=1 or n=='':
        return lst
    for i in  range(0,n):
        for j in  range(0,n-i-1):
            if lst[j]>lst[j+1]:
                (lst[j],lst[j+1])=(lst[j+1],lst[j])
    return lst
x=input("请输入需要排序的数组：")
y=list(x)
arr=[]
for m in  y:
    arr.append(int(m))
arr1=bubble1(arr)
print(arr1)