# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


B = Bus("School Volvo", 180, 12)
print(f'Vehicle Name: {B.name} Speed:{B.max_speed} Mileage:{B.mileage}')
