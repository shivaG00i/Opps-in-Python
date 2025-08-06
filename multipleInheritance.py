# Multiple Inheritance

# parents class

class Prey:
    def flee(self):
        print('This animal is fleeing')
class Predator:
    def hunt(self):
        print('This animal is hunting')


# child class

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
# rabbit.hunt()
#hawk.flee()
hawk.hunt()

fish.flee()
fish.hunt()


