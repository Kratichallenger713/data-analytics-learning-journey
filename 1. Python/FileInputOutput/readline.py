f=open("FileInputOutput/student.txt","r")
data = f.readline()  #if we add a number as a parameter  so it will represent size of text
print(f.readlines())
print(data)
f.close()