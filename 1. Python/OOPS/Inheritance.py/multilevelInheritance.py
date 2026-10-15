# what is super method , why we use it 

class Person:
    country = "India"

    def takeBreath(self):
        print("gwalior")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print("Salary 10000")

    def takeBreath(self):
        super().takeBreath()
        print("pninfosys")    

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a programmar and I am so lucky")        


p = Programmer()
p.takeBreath()