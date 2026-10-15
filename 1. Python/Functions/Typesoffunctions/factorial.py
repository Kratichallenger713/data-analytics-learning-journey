#factorial

def factorial(n):
    fact=1
    for i in range(1,n+1): # range(1,n)
        fact*=i  # fact=i*fact
    return fact

print("factoral is :",factorial(5))    
