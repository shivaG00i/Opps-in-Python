class Animal:

    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")
class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeeking")

d=Dog('scobiee')
c=Cat('Tom')
m=Mouse('Micky')

print(d.eat(),d.sleep())
print(d.speak())
print()
print(c.eat(),c.sleep())
print(c.speak())
print()
print(m.eat(),m.sleep())
print(m.speak())