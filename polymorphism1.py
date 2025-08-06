
from abc import ABC, abstractmethod

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,raduis):
        self.raduis=raduis
    def area(self):
        return 3.14*self.raduis**2

class Square(Shape):
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        return  self.sides *4
class Traingle(Shape):
    def __init__(self, base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height *0.5

class pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping

        
shapes=[Circle(4),Square(4),Traingle(4,5),pizza('cheese',6)]

for i in shapes:
    print(i.area())