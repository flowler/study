class Person:
    # 创建一个实例需要调用的构造方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f" name: {self.name}, age:{self.age},gender:{self.gender} 我在吃")
