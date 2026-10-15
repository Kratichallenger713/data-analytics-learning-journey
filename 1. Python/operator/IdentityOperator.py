a = [1, 2, 3]
b = [1, 2, 3]

# They are used to check whether two variables refer to the exact same object in memory, not whether they have the same value.
print(a is b) #Identity Operator
print(a == b) #Equality Operator
print(a is not b) #Identity Operator
print(a != b)   #Equality Operator

# Output of a is b is False because a and b are two different objects
# Output of a == b is True because a and b have same values

# Identity Operator
# Equality Operator
# Identity Operator
# Equality Operator