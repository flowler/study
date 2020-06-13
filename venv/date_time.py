#输入日期， 判断这一天是这一年的第几天？


import datetime

year=input("请输入年份：")
month=input("请输入月份：")
day=input("请输入天：")

#输入年月日返回一个date类型的时间
date1=datetime.date(year=int(year),month=int(month),day=int(day))
#该年份的1月1
date2=datetime.date(year=int(year),month=1,day=1)
#date类型对象之间可以相减，返回值是俩者之间的间隔的天数
#.days是具体的天数
daycount=(date1-date2).days+1
print(daycount)
print("date1",date1)
print("date2",date2)
print(type(daycount))

# if __name__ == '__main__':
#     dayofyear()
