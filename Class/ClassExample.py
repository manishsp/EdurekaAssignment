class Person:
    alive='Alive'
    def __init__(self):
        self.name='Manish'

    def display(self):
        print(f"{self.name} is {Person.alive}")

p=Person()
p.display()
