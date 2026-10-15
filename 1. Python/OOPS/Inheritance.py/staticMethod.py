class Employee:
    company = "google"

    def itm(self,a):
        print(f"Hello , {self.company} ITM Gwalior {a}")

    @staticmethod  #it is used when we want to use a method in a class but  #we don't want to use self or cls
    def rjit(a):
        #print(f"Hello , {self.company} ITM Gwalior {a}")
        print(a)    

rohit = Employee()
# rohit.itm("delhi")
rohit.rjit("ram")        