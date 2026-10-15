#Multiple value ko ek tuple mein pack karna 
#Tuple packing 

student = "Ravi", 21, "BCA"

print(student)
print(type(student))

# Tuple Unpacking
# Tuple ki values alag variables mein store karna.
student = ("Ravi", 21, "BCA")

name, age, course = student

print(name)
print(age)
print(course)

#Nested Tuple
data=(
    ("Ravi",21),
    ("Amit",22),
    ("Priya", 20)
)

print(data[0])
print (data[1][0])