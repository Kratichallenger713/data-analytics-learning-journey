class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # string method is a magic method which convert object into  human readable string
    # if we don't use it then it give us memory address 
    def __str__(self):
        return f"Name:{self.name},Age:{self.age}"

data = user("ram",20)      
print(data) 