#Jab koi function khud ko hi baar baar call karta hai 
#when a function call itself 

#Print Hello 2 times 
def hello(n):
    if n==0:
        return 
    
    print("Hello")
    hello(n-1)

hello(2)
