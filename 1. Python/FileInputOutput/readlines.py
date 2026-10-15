f=open("FileInputOutput/student.txt","r")
print(f.readlines(4))  # readlines return list 

f.close()

#list return kr rha hai 
#har ek line ko ek string me store kr rha hai
#last me \n bta rha hai ki line yha khatm ho rhi hai 
# or vo last me ek empty string de rha hai 
# kyuki usne last me koi value read nhi ki
