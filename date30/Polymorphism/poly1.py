''' The word Polymorphism means many forms and in 
programming it refers to methods/function/operators 
with the same name that can be executed on many object 
or classes.'''


class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive")
class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sale")
class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly")

car1 = car("Suzuki","Swift")

boat1 = boat("bit","bitt")

plane1 = plane("Airbus","Airindia")

car1.move()
boat1.move()
plane1.move()        