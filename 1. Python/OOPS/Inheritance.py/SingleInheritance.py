class papa:
    bike ="007"

    def showDetails(self):
        print("This is an employee")

class son(papa):

    language = "Python"

    def getLanguage(self):
        print(f"The Language is {self.language}")

    # def showDetails(self):
    #     print("This is a programmer")
p = son()
print(p.bike)
p.showDetails()
p.getLanguage()
            
        