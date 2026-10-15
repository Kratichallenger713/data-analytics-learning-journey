class bikeShop:
    # stcok = 100

    def __init__(self,stock):
        self.stock =stock

    def displayBike(self):
        print("Total Bikes ", self.stock)

    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater the zero")

        elif q>self.stock:
            print("Enter the value (less the stock)")
        else:
            self.stock = self.stock-q
            print("Total prices ",q*100)            
            print("total Bikes ",self.stock)

while True:
    obj = bikeShop(100)
    uc = int(input(''' 
1 Display Stock
2 Rent a Bike
3 Exit
'''))    
    if uc==1:
        obj.displayBike()     
    elif uc==2:
        n = int(input("Enter qty"))
        obj.rentForBike(n)
    else: 
        break      