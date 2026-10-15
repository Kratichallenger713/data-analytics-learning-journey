# Write a function find_largest(numbers) that takes a list of numbers as input and returns the largest number in the list.
# Do not use the built-in max() function. Use a loop to find the largest number.
def find_largest(num):
    maxi=0
    for i in num:
        if i>maxi:
            maxi=i
    return maxi

num=[]
i=5
while i>0:
    temp=int(input("Enter Number:"))
    num.append(temp)
    i-=1

print(find_largest(num))