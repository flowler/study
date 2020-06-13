# #引入日历模块
# import calendar
#
# #输入指定年月
# yy=int(input("年份："))
# mm=int(input("月份："))
# calendar.setfirstweekday(firstweekday=6)
#
# print(calendar.month(yy,mm))



# #输出某一整年日历
# import calendar
# calendar.setfirstweekday(firstweekday=6)
# while True:
#     yy=int(input("年份："))
#     for i in range(12):
#         print(calendar.month(yy,i+1))
#         print("*"*20)


#prcal 全年日历
# import calendar
# yy=int(input("年份："))
# calendar.setfirstweekday(firstweekday=6)
# print(calendar.prcal(yy,2,1,6))


#calendar 返回年份日历
import calendar
calendar.calendar(2020,2,1,6)
