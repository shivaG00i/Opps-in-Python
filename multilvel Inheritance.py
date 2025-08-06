# Multi Level Inheritance


# Grant parent
class Animal:

    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
# parents class
class Prey(Animal): # Animal class is inherited
    def flee(self):
        print(f'{self.name}  is fleeing')
class Predator(Animal): # Animal class is inherited
    def hunt(self):
        print(f'{self.name}  is hunting')


# child class

class Rabbit(Prey): # Prey class is inherited and Prey class inherits Animal class
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit=Rabbit("Bugs")
hawk=Hawk("Tony")
fish=Fish("Nemo")


rabbit.eat()
rabbit.sleep()
rabbit.flee()

hawk.eat()
hawk.sleep()
hawk.hunt()

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()


