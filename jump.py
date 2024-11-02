i=1

for i in range(i,10,2):
    if i==5:
     continue
    if i==7:
       break

    print(i)


print(id(i))
print(id(i+1))
