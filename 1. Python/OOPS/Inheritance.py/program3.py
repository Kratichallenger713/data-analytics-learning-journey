class BankAccount:
    def __init__(self,name,balance,pin):
        self.name = name #public
        self._balance = balance  #protected
        self.__pin = pin  #private

    # public method 
    def show_details(self):
        print("name : ",self.name)
        print("balance : ",self._balance)

    # private method 
    def __show_pin(self):
        print("pin :", self.__pin)

    # public method to access private method
    def access_pin(self):
        self.__show_pin()

# child class
class ATM(BankAccount):
    def withdraw(self,amount):
        if amount<=self._balance:  #1000<=5000
            self._balance -= amount  #5000-1000 = 4000
            print("Amount withdrawl successful")
            print("Remaining balance : ",self._balance)

        else:
              print("Insufficient balance")

#object creation
#first object
a = ATM("rahul",5000,1234)
a.show_details()  #public
a.withdraw(1000) #protected method 
a.access_pin()                
