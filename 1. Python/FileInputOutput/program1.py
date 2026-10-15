f =open("FileInputOutput/student.txt")

t = f.read()

if 'pninfosys' in t:
    print("present")
else:
    print("not pninfosys")

f.close()        