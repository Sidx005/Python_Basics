class A:
    x,y=10,20
    def m1(s):
         print(s.x+s.y)

 #single lvl inheritance
class B(A):
    a,b=200,100



    def printMsg(self):
        print(self.mesage)

    def m2(s):
        print(s.a+s.b)




bobj=B()
bobj.m1()
bobj.m2()


#Multi lvl inheritance

class C(B):
    i,j=5,2
    def m3(self):
     print(self.i*self.j)
     super().m2()

     


cobj=C()
cobj.m1()
cobj.m2()
  

class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")
x.printmessage()



#Overriding variables:

class Parent:
   name="Scott"

class Child(Parent):
   name="John"
   def test(self):
      print(super().name)



obj=Child()
print(obj.name)   

obj.test()



#overriing methods

class XBank():
   def rateOfInterest(self):
      return 10
   
class YBank():
   def rateOfInterest(self):
      return 12
   
class ZBank():
   def rateOfInterest(self):
      return 12
   
   
   objx=XBank()
   print(objx.rateOfInterest())

   
   objy=YBank()
   print(objy.rateOfInterest())

   


#POlymorphism


class Calculation:
   def add(self,a=0,b=0,c=0):
      print(a+b+c)



calcobj=Calculation()   
calcobj.add()
calcobj.add(10,20)
calcobj.add(10,200,100)