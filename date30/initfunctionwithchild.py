class person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class student(person):
    def __init__(self, name):
         person.__init__(self,name)
s = student("ankit")
s.show()