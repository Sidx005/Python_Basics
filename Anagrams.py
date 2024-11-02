
empSet=[]
def checkLeng(set):
   for i in range(len(set)-1):
      # print(set[i])
      print(set[i])
      if(len(set[i])!=len(set[i+1])):
         return False
      else:
         return True

def checkAnag(set):
   if checkLeng(set):
      return sorted()==sorted()


set1=["bat","tan","man","ate"]
print(checkAnag(set1))