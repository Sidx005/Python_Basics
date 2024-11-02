""" A list is a collection which is ordered and changeable.In Python lists are written with square brackets
[]
List is mutable
Mutable:Values can be changed
"""

list1=[10,20,30,40,"Sid"]
myList=list()
myList.append("Hi")

print(len(myList))
myList=["Hello","Lol","Okay"]

print(myList)
print(myList[0:2]) #["Hello","Lol"]
print(myList[1:3])#[Lol,Okay]
print(myList[-2:-1])#[Okay,Lol]
print(list1[4])
print(len(myList))


myList[0]=2
print(myList)



for i in myList:
 print(i)



if "Hello" in myList:
  print('Yes')
else:
  print("No")   



#Insert in list
myList.append("Jdfg")
myList.insert(2,"AJzssdf")
print(myList)



#Delete list elements
myList.pop(0)
# myList.clear()

del(myList[2])
print(myList)
del myList[2]

mylist2=myList.copy()




print(mylist2,"This is list2")





#Copy list
myList3=["Apple","Banana"]
myList4=list(myList3)
# myList4=myList3
myList4=myList.copy()

print(myList4,"list4")





#using loop statement

list1=['a','b','c']
list2=[1,2,3]
for i in list2:
  list1.append(i)

print(list1)  



#using extend()

list1.extend(list2)

print(list1)