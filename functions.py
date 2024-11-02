'''
Functions are set of stateme ts prerfrming task


Types of functions:
1.does not take arguments,not return any value
function does not take arguments but return some value
function takes arguments and also return value
'''

def hello(a):
    print(a)


hello("sid")



def calc(a,b):
    return a+b
x=calc(20,30)
print(x)


def func():
  print('Hwllo')
func()


#Variables
global_va=10
def func():
   global_va=5
   var=4
   print(var,global_va)


func()   





xy=100
def scope():
   global xy
   xy=400
   print(xy)



scope() #global variable xy in scope func changes xy to 400
print(xy) #output:400 due to scope() function,if not called then xy output is 100


def cool():
  global x #global variables can be created inside the function using global keyword
  x=100
  print(x)

cool()
print(x)





def func(i,j):
 return i,j


print(func(20,30)) #positional arguments

print(func(j=40,i=20))


def func2(i,j=200): #function with default values
  print(i,j)


func2(100)  
func2(100,200) #overwrites def value with 200


def greet(grretmsg,name):
  return(grretmsg+" "+name)
  # return(print(grretmsg+name))

print(greet("Hello","Siddharth")  )
print(greet(name='Sid' , grretmsg='Hello'))

def myFunc(a,b,c):
  print(a,b,c)



# myFunc(10,c=20,30)#error: positional args must appear before keyword args

def largest(a,b):
  return(max(a,b))

print(max(10,20))
