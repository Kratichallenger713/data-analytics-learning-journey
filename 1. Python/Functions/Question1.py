def Candies(num):
    N=10
    K=5
    if (num<=K and num>0) :
            print("Number of Candies sold :",num)
            print("Number of Candies Left :",N-num)
    else:
        print("INVALID INPUT")
        print("Number of Candies Left :",N)
            
Candies(0)
Candies(3)       
Candies(7)  
            
