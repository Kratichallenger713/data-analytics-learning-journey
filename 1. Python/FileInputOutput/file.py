f = open("FileInputOutput/student.txt","r")
# data = f.read()
# print(data)
# f.close()
for line in f:
    print(line.strip())

f.close()

