student={
    "name":"ram",
    "age":24,
    "course":"python"
}

print("Student Information")
print("Name : ",student["name"])
print("Age  : ",student["age"])
print("Course : ",student["course"])

for key,value in student.items():
    print(key,":",value)