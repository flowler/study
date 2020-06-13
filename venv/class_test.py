
#面向过程编程
user1={'name':'tom','hp':100}
user1={'name':'jerry','hp':100}

def print_role(rolename):
    print('name is %s,hp is %s' %(rolename['name'],rolename['hp']))

print(print_role(user1))



#面向对象编程
class Player(): #定义一个类，相似内容进行归纳，类名第一个字大写
    def __init__(self,name,hp,occu):#init方法在类实例化后自动执行
        self.name=name #self表示Player示例话后的示例本身，比如user1和user2
        self.hp=hp #变量被称作属性
        self.occu=occu
    def print_role1(self): #定义一个方法
        print('%s %s'%(self.name,self.hp))

#'定义怪物类'
class Monster():



user1=Player('tom',100,'war') #引用这个类，叫类的实例化
user2=Player('jerry',100,'master')

user1.print_role1()
user2.print_role1()