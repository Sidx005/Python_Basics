'''
dictionary is a collection which is unordered,changeable(mutable) and indexed
In Python dictionary ae written with curly brackets,and they have keys and values.
'''


mydict={101:"x",102:"y",103:"z"}
print(mydict)

mydict2={'x':'Sid','y':'Hello','z':123}
print(mydict2)


car={
 "brand":"Hyundai",
 "model":110,
 "year":2024

}

print(car["brand"])
x=car.get("brand")

print(x,car.get("model"))

car["year"]="2026"
print(car)

for i in mydict:
    print(mydict[i])  #values in dictionary,1st method


for i in mydict.values():
    print(i)     #prints only values,2nd method



for x,y in mydict.items():
    print(x,y)    

print("model" in car)


car["color"]="red"
print(car)


# del mydict
print(mydict)

#copy dictionary without copy function
mydict3=mydict2
print(mydict3)

#copy dictionary using copy function

mydict3=mydict.copy()
print(mydict3)