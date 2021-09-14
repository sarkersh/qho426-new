class Person:
    def __init__(self, a, b=0):
        self.name = a
        self.age = b
        self.energy = 100

    def display(self):
        print(f'{self.name} is {self.age} years young, energy: {self.energy}')

    def use_energy(self, amount):
        self.energy = self.energy - amount

    def recharge(self):
        self.energy = 100

    def __repr__(self):
        return f'{self.name}:{self.age}'

    def __str__(self):
        return f'{self.name} is {self.age} years young'

    @staticmethod
    def hello():
        print('hohoho')


astudent = Person('James', 23)
astudent.display()

astudent2 = Person('Laura', 25)
astudent2.display()

astudent3 = Person('Bob')
astudent3.display()

astudent3.hello()
Person.hello()

print(astudent2)
print(repr(astudent2))

astudent2.use_energy(10)
astudent2.display()
astudent2.use_energy(50)
astudent2.display()
astudent2.recharge()
astudent2.display()