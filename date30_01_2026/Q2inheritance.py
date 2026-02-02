#create parent and child class
class person:
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname
    def show(self):
        print(self.fname, self.lname)
class Student(person):
    pass

S = Student("Ankit","kushwah")
S.show()
    