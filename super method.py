from time import sleep


class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"{self.color} and {self.is_filled} ")

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

    def describe(self):
        super().describe()
        print(f"{3.14*self.radius*self.radius}")

class Tringle(Shape):
    def __init__(self, color, is_filled,base,height):
        super().__init__(color,is_filled)
        self.base = base
        self.height = height

    def describe(self):
        super().describe()
        print(f"{0.5*self.base*self.height}")

class Square(Shape):
    def __init__(self, color, is_filled,side):
        super().__init__(color,is_filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f"{self.side*4}")
sq=Square("Red",True,4)

print(sq.describe())