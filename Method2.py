class Car:
    def __init__(self,brand):
        self.brand = brand
    def display(self):
        print("Brand:",self.brand)
car1 = Car("Toyota")
car1.display