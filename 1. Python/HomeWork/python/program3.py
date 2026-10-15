# Write a program to input 10 numbers into a list. Convert the list into a set and display the unique numbers.
list1=[]
i=10
while i>0:
    num=int(input("Enter Number:"))
    list1.append(num)
    i-=1

unique=set(list1)
print("Unique number are :",unique)

