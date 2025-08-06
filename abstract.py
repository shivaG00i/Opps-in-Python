#abstract

from abc import ABC,abstractmethod

class Vehicle:
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print('you drive the Car')


    def stop(self):
        print('you stop the Car')


class Motorcycle(Vehicle):

    def go(self):
        print('you drive the bike')

    def stop(self):
        print('you stop the bike')


c=Car()
c.go()
c.stop()

b=Motorcycle()
b.go()
b.stop()