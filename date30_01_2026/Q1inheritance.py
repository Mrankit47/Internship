#create a parent class
class person:
    def __init__(self,name,lname):
        self.name = name
        self.lname = lname
    def show(self):
        print(self.name , self.lname)

p = person("ankit","kushwah")
p.show()
        