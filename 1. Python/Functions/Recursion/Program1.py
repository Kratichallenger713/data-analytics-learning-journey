def hello(n):
    if n==0:
        return  #function stop here
    
    print("Start",n)  #start1 start2
    hello(n-1)  #hello Hello 

    print("End",n)  #end1 end2 

hello(2)    