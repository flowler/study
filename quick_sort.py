#快速排序
#取一个基准数(一般为第一个数)，
# 把比基准数大的数放在前面，比基准数小的数放后面
#https://blog.csdn.net/weixin_43250623/article/details/88931925?depth_1-utm_source=distribute.pc_relevant.none-task
#https://blog.csdn.net/weixin_41571493/article/details/81875088

def quick_sort(lst):
    def partition(arr,start,end):
        pivot=arr[start]
        low=start
        high=end
        if low>=high:#递归结束条件
            return
        while low<high:
             while low<high and arr[high]>=pivot:
                high -=1
             lst[low]=lst[high]

             while low<high and arr[low]<pivot:
                low +=1
             lst[high]=lst[low]

        lst[low]=pivot

        partition(arr,start,low-1)
        partition(arr,low+1,end)

    n = len(lst)
    if n <= 1:
        return lst
    partition(lst, 0, n - 1)
    return lst

a=input('请输入要排序数列\n')
# if len(a)<=1 or a==' ':
#     print('hhhhhh')
# else:
arry = []
for i in a:
   arry.append(i)
print('排序后',quick_sort(arry))
