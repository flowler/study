class Person():
    name = "hhhh"

    def get_name(self):
        return self.name


print(Person.name)
p = Person()
print(p.name)
print(p.get_name())

p.name = 'cy'
print(p.name)
