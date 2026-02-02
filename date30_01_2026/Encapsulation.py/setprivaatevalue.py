class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age = age
        else:
            print("Age must be positive ")
s1 = Student("Ankit",26)
print(s1.get()) 

s1.set_age(24)
print(s1.get())