#**args(Tuple)VAriable Length Arguments

def add_number(*numbers):
    total=0
    for n in numbers:
        total+=n
    return total

print(add_number(20,30,40,6))     

#**kwargs (Dictionary)
def student_info(**data):
    print(data)

student_info(name="Kratika",course="python",fees=50000)    

