class Vehicle:
    color = 'white'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        # print(self.name, self.max_speed, self.mileage,self.color)
        print(f'Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {12}')

class Bus(Vehicle):
    # def print_color(self):
    #     print(self.name, self.max_speed, self.mileage,self.color)
    pass

class Car(Vehicle):
    # def print_color(self,color='white'):
    #     self.color=color
    #     return color
    pass

b=Bus("School Volvo",180,12)
c=Car("Audi Q5",240,18)


