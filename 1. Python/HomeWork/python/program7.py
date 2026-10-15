# Write a function is_palindrome(text) that returns True if the given string is a palindrome; otherwise, return False.
def is_pallindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1       
        
    return True

s=input("Enter string : ")
if is_pallindrome(s) :
    print("True")
else:
    print("False")    
