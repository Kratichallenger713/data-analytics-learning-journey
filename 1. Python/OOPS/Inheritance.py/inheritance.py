# class animal:
#     def eat(self):
#         print("Eating")

#     def sleep(self):
#         print("sleeping")


# class dog(animal):

#     def bark(self):
#         print("Barking")

# d = dog()
# d.eat()
# d.sleep()     

class person:
    def walk(self):
        print("walking")

class student(person):
    def study(self):
        print("studying")   

s = student()
s.walk()
s.study()                        