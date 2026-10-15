class student:
    def __init__(self,name):
            self.n = name 
    
    def show(self):
        print("hello college")

    def team(self,name1):
        print("Welcome",self.n,name1)

data = student("Kratika")
data.show()
data.team("Arpit")            