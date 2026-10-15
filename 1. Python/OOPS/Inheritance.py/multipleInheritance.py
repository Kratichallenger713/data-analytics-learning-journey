class Employee:
    car = "pninfosys"
    ecode = 120

class Freelancer:
    car="google"
    level = 0

    def upgradelevel(self):
        self.level +=1

class Programmer(Employee,Freelancer):
    # car = "abcd"
    name = "Vikas"

p = Programmer()
print(p.car)
p.upgradelevel()
print(p.level)                    