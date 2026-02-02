'''  Encapsulation is about protecting data inside a class.'''

class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age    #private property
p1 = person("Ankit",24)
print(p1.name)
print(p1.__age) # This will cause an error

    