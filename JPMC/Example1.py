class Student:

    def __init__(self,race,name):
        self._age=35
        self.race=race
        self.name=name
    @property
    def change_race(self):
        return self.race
    @change_race.setter
    def change_race(self,race):
        self.race=race

    def _printperson(self):
        print(f"{self.name} is {self.race} and is {self._age} year old")

    # def display(self):
    #

p=Student("Indian",'Manish')
print(p.race)
p.change_race="Persian"
p._printperson()