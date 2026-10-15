# TYPES OF FUNCTIONS IN PYTHON
# Python me function ke types: Built-in, User-Defined, Lambda, Recursive,
# Generator, Nested, args, kwargs
# Built-in Functions Jo Python already provide karta hai

print("Hello")
print(len([1,2,3]))
print(type(10))
print(sum([10,20,30]))
print(max(5,8,2))

# User-Defined Function ke TYPES (MOST IMPORTANT)
# No Argument, No Return
def hello():
    print("Hello Python")
hello()

#Arguments,No return
def add(a,b):
    print(a+b)#output
add(3,5) #value pass

#No Arguments , with returns 
def get_number():
    return 10

print(get_number()) #call

#Arguments , with return 
def add(a,b):
    return a+b
d=add(4,7)
print(d)
