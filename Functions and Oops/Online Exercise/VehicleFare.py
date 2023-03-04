import os
import datetime


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        # print(super(Bus, self).fare())
        total_fare = super().fare()
        return ((10 / 100) * (total_fare) + total_fare)


School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))
print(isinstance(School_bus, Vehicle))
print("Total Bus fare is:", School_bus.fare())
print(os.getppid())
print(os.path.isdir('D:\VM2'))

now = datetime.datetime(2022, 12, 23, 12, 30)
past = datetime.datetime(1987, 12, 23, 12, 30)
print(past - now)
time=datetime.time

