# create a class for with parameters like car name model name color ,tyre size and brand

class Car:

    def __init__(self,carName,model,color,tyreSize,carBrand):
        self.carName=carName
        self.model=model
        self.color=color
        self.tyreSize=tyreSize
        self.carBrand=carBrand

    def displyInfo(self):
        print(f"{self.carName}\n { self.model}\n{self.color}\n{self.tyreSize}\n{self.carBrand}")
v=Car('tata','SUV','Red',5,'TATA')

print(v.displyInfo())