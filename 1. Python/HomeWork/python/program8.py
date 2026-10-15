# Check whether two strings are anagrams using sets and other string operations.
s1=input("Enter first string : ")
s2=input("Enter Second string : ")

set1=set(s1)
set2=set(s2)

if len(set1)==len(set2):
    check = set1.intersection(set2)
    if check==set1 and check==set2:
        print("Strings are anagram.")

    else:
         print("Strings are not  anagram.")       
else:
    print("Strings are not  anagram.")
