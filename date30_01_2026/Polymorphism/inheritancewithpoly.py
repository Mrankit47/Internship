class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive")
class car(Vehicle):
     pass
class boat(Vehicle):
    def move(self):
        print("Sale")
class plane(Vehicle):
    def move(self):
        print("Fly")

car1 = car("Suzuki","Swift")

boat1 = boat("bit","bitt")

plane1 = plane("Airbus","Airindia")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()