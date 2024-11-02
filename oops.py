

class MyClass:
    def myfun(self):
        pass
    def display(self,name):
        print(name)

mc1=MyClass()
mc1.myfun()
mc1.display('H')



class MyClass2:
    def m1(self,num):
        print("This is instance method",num)
    @staticmethod
    def m2(self,num):
        print(num)




m=MyClass2()
m.m1(100)
m.m2(100,200)
MyClass2.m2(200,100) 




#Class variables

class Variables:
    def __init__(self):
        print("This is variable class")
    a,b=10,20 #class variables
    def add(self):
        print(self.a+self.b)


    def mul(self,a,b):
        print(a*b) #Local variables mentioned in function parameters
        print(self.a*self.b,'this is class variables')




mc=Variables()
mc.add()
mc.mul(20,30)
