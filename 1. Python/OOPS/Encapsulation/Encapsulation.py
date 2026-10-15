class student:
    __name = "ravi"

    def __init__(self):
        print(self.__name)
        self.__displayinfo()

    def __displayinfo(self):
        print("Hello gwalior")

    def itm(self):
        self.__displayinfo()
        print(self.__name)

obj = student()
# print(obj.__name)
obj.itm()



# Encapsulation getter and setter

class student:
    def __init__(self):
        self._name = ""

    def getname(self):
        return self._name

    def setname(self,name):
        self._name = name


obj = student()
obj.setname("raj")
# obj.setname("Kumar")
name = obj.getname() 
print(name)