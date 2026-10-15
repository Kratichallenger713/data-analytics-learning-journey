with open("FileInputOutput/student.txt","r") as f:
    a=f.read()

print(a)

with open("FileInputOutput/student.txt","a") as f:
    a=f.write("Hi Miss Kratika Bathav")

print(a)


          