#range在python2中返回列表，在python3中返回对象，节省内存
#求1-100的和
print(sum(range(101)))

#计算10以内偶数加和
total=0
for i in  range(0,10,2):
    total=total+i
    print(i)
print(total)