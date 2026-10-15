# same fxn name but different parameters
l = [10,20,30,40]
print(len(l))
s = "welcome"
print(len(s))

# overriding
class pn:
    def displayinfo(self,name=''):
        print("welcome to pninfosys")

class itm(pn):
    name="ram"
        # def displayinfo(self):
            # print("welcome to pninfosys123")

obj = itm()
obj.displayinfo() 



#overloading
class Area:
    def find_area(self,x=None, y=None):       
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj1 = Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)   #function same but 3 kam ek rah hai


# overriding
#overriding
class A:
    def showData(self):
        print("i m in A class")
class B(A):
    def showData(self):
        # super().showData()
        print("i m in B class")

obj=B()
obj.showData()

