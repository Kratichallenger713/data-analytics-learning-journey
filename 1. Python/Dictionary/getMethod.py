#Agar key naa mile to errror nhi aata 

student={
    "name":"Ravi",
    "age":21
}

#print(student.city)
print(student.get("city"))
student["city"] = "Ahmedabad" # add
student["age"] = 25 # update
#student.pop("age") # remove if we don't pass any key than it give us an error
#student.clear()
print(student)