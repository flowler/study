#格式化字符串
#小明成绩提升百分点
name='小明'
s1=75
s2=90
r=(s2-s1)/s1*100
print('小明成绩提升：%.3f%%' % r)
print(('hello,{0},成绩提升了,{1:.1f}%').format('小明',r))
print(f'hello,{name},成绩提升了,{r}%')
print('hello %s ,成绩提升了 %.4f%% '% ('name' , r))

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')


#字符串内建方法
a='abcdefghijklmnopqrstuvwxyz'
b=':'
print(a.capitalize())#第一个字母大写
print(len(a))#字符串长度
print(b.join(a))#以指定字符串b作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
print(a.center(50,'h'))#返回一个指定长度的居中字符串，长度不足用字符串补齐