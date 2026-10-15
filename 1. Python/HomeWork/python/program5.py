# Given a dictionary of student names and marks, print the name of the student with the highest marks.
student={
    "komal":87,
    "khushi":85,
    "arnav":96,
    "arjun":94
}

maxi=-1

for key,value in student.items():
    if value>maxi:
        maxi=max(maxi,value)

print(maxi)   
