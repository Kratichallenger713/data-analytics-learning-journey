# dictionary Python ka ek data structure hai jo data ko Key
# Value Pair mein store karta hai.

# Jaise kisi student ki information:

student = {
    "name": "Ravi",
    # "name": "Amit",# duplicate key print nhi hoti
    "age": 21,
    "course": "BCA"
}


print(student)
print(student["name"])

# # Mutable Hai
# # Dictionary ko create karne ke baad update kar sakte hain.
student["age"] = 25

print(student["age"])

#Empty Dictionary
data={}
print(type(data))