class car:
    def __init__(self,brand,model):
        self.model = model
        self.brand = brand

# it return string 
    def __str__(self):
        return f"{self.brand} {self.model}" 


c1 = car("BMW","abc")
print(c1)        