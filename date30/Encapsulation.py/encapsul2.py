
class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age    #private property
    def show(self):
        return self.__age
p1 = person("Ankit",24)
print(p1.show())