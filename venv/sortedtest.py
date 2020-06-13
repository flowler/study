#排序--可以对序列进行排序，可以接收一个key函数实现自定义的排序，
# 例如按绝对值大小排序：
s=sorted([-2,4,6,3],key=abs)
print(s)

#对字符串进行排序，
# 是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
s1=sorted(['bob', 'about', 'Zoo', 'Credit'])
print(s1)

#对字符串忽略大小写进行排序：
s2=sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(s2)

#按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L, key=by_name)
print(L2)