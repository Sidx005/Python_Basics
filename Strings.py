for char in range(ord('a'), ord('z') + 1):
    print(chr(char), char) 


print(ord('A'))    
print(max("abc","dce","axy"))
print (max("junex","abx"))


print("is123".isalnum())
print("is123".isidentifier())
print("is123".isalpha())
print("is123".isprintable())
print("is123".isupper())
print("is123".islower())
print("is123".upper())
print("is123" in "is123656")
print("title".title())
print("title".capitalize())


str="abc"
revstr=""
for i in str:
  revstr=i+revstr

print(revstr)   

str="welcome"
print(str[0:3]) #slice string includes 0 to index 2 characters

