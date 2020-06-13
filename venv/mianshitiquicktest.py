def Quicktest(lst):
    def partition(arr,left,right): #分区函数
        key=left#定义一个key
        while left<right:
            while left<rigth and arr[right]>=arr[key]:
                right -=1
            while left<right and arr[left]<arr[key]:
                left +=1
            (arr[left],arr[right])=(arr[right],arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left],arr[key])=(arr[key],arr[left])

        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr,left,right): #递归交换子分区
        if left>=right:
            return
        #从基准区开始分区
        mid=partition(arr,left,right)
        #递归调用
        quicksort(arr,left,mid-1)
        quicksort(arr,mid+1,right)

    n=len(lst) #主函数判断，如果为空
    if n<=1:
        return lst
    quicksort(lst,0,n-1)
    return lst
