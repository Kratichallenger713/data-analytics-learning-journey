def weight(num):
    if(num==0):
        print("Time Estimated: 0 Minutes")
    elif num>=2000 and num>0:
        print("Time Estimated:25 Minutes")
    elif num>2000 and num<=4000:
        print("Time Estimated:35 Minutes")  
    elif num>4000 and num<=7000:
        print("Time Estimated:45 Minutes")
    elif num>7000:
        print("OVERLOADED")    
    else:
        print("INVALID INPUT")    

n=int(input("enter weight :"))
weight(n)        