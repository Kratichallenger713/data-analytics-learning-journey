# Write a function named count_vowels() that accepts a string and returns the total number of vowels in it.

def count_vowels(inp):
    cnt=0
    return inp.count("a")+inp.count("e")+inp.count("i")+inp.count("o")+inp.count("u")

inp=input("Enter string : ")    
print(count_vowels(inp))
