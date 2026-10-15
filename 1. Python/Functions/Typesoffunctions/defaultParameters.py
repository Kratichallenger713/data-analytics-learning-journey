def hello(name="Guest"):
    print("Hello",name)

hello("Kratika")
hello("Arpit")
hello()    

#Keyword Arguments
def student(name, age):
    print(name, age)

student(age=20, name="Rahul")

#Variable-lenght Argument
def total(*nums):
    print(sum(nums))

total(10,20,30,40)    