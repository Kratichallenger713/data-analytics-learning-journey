#Encapsulation:
#binding the data and methods together

class student:
    def __init__(self):
        self.name="vikas"
        self._course="python"
        self.__fees=50000

    def show_fees(self):
         return self.__fees


s1=student()
print(s1.name)
print(s1._course)
print(s1.show_fees())








# Abstraction 
# showing only the necessary details and hiding the unnecessary details

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("Car")

#abstract class


car1=car()
car1.start()

#abstract method