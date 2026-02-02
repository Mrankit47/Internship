# Super function that will make the child class inherit all the methods and properties from its parent


class parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_data(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
class Student(parent):
    def __init__(self, name, age,Gyear):
        super().__init__(name, age)
        self.year=2026

student = Student("Ankit Kushwah",24,2026)

student.show_data()
print(student.year)

        