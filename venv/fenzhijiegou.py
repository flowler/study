#机器人随机生成一个数字
#个人猜数，机器人回复大一点还是小一点还是猜对啦
import random

computer_num=random.randint(1,101)
while True:
    person_num=int(input("请输入一个1-100间整数："))
    if person_num<computer_num:
        print("小一点")
    elif person_num>computer_num:
        print("大一点")
    elif person_num==computer_num:
        print("猜对啦")
        break







#while
# a=1
# while a==1:a=a+1
# else:
#     print("a!=1")
# print(a)
#
#
#
#
#
#
#
#
# #计算1——100求合
# result=0
# for i in range(1,101):
#     result=result+i
# print(result)
# #计算1——100间偶数求和
# print(sum(range(1,101,2)))
#
#
#
#
# #多重分支
# x=0
# if x>1:
#     y=3*x-5
# elif -1<=x<=1:
#     y=x+2
# elif x<-1:
#     y=5*x+3
# print(y)
#
# #分支结构
# x=-2
# if x>1:
#     y=3*x-5
# else:
#     if x>=-1:
#         y = x+2
#     else:
#         y=5*x+3
# print(y)
#
#
#
# a = 9
# if a==0:
#     print("a==0")
# elif a==1:
#     print("a==1")
# elif a==2:
#     print("a==2")
# else:
#     print("a==8")