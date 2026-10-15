try:
    a=int(input("Enter a :"))
    b=int(input("Enter b :"))
    print("Result is :",a/b)
except ZeroDivisionError:
    print("Error : Cannot divide bye zero")    


# ZeroDivisionError ek built-in exception hai jo tab raise hota
# hai jab kisi number ko 0 se divide karne ki
# koshish ki jaati hai.