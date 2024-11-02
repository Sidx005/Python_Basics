class MyClass:
    name="John"

    def __init__(self,name):
     print(name)
     print(self.name)

mc=MyClass("David")


class empClass:
   #constructor:e_id,name,salary
   #display()
#   eid=""
#   ename=""
#   sal=""



  def __init__(self,eid,name,salary):
      self.eid=eid
      self.ename=name
      self.sal=salary


  def __str__(self):   #String Constructor ,returns string elements automatically when Object is invoked
     return (self.ename)


  def display(self):
     print(self.ename,self.eid,self.sal) 


emp=empClass(145,"Sid",1000)
emp.display()

emp=empClass("1451sdfew","Siddharth",1000)
emp.display()
print(emp)

# num=123
# print(type(str(num)))





### Inheritance
# Aquiring all the attributes(variables) and behaviour(methods) from one class to another class is called as inheritnce

### class A--->a,b,c m1() m2()--->A is parent of B class
### class B(A)--->x,y,z m3()--->B is child of A class



