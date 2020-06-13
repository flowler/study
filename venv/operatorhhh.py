#逻辑运算符 and  or
zodiac_sign='鼠、牛、虎、兔、蛇、马、羊、猴、鸡、狗、猪'
year='2019、狗'
c='狗'in zodiac_sign
d='哈'not in zodiac_sign
e=year and zodiac_sign
f=year or zodiac_sign #从左到右，都为假值，返回最后一个假值，有真值，返回第一个真值
print(c)
print(d)
print(e)
print(f)
g=10
h=20
print(g and h)#都为真，返回最后一个真值，有假值，返回第一个假值
print(not(g and h))
print(not g==h)
print(10//6)



