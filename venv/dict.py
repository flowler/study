dict={'d':1,'i':2,'c':3,'t':4,'d':5}
print(dict)  #{'d': 1, 'i': 2, 'c': 3, 't': 4}
print(len(dict)) #输出字典长度，有重复只算一个
print(str(dict))
dict.pop('d')
print('删除了d',dict)
dict['d']='change'
print(dict)  #{'d': 'change', 'i': 2, 'c': 3, 't': 4}
d={3:1,2:2}
d.pop(2)
print(d)
del(d[3]) #删除字典中的key ，必须通过key值删除，因为key值唯一
print(str(d))
print(type(d))
print(type(str(d)))
d.clear() #清空字典
print(d)
del(d)  #删除字典d


