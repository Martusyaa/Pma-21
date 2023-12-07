from Dish import *

d = {"lasagna": Dish(23432),
     "carbonara": Dish(112441), }

def printD():
     print()
     for key,value in d.items():
          print(f"Dish:{key}, Price:{value}")



# d["gorilka"]=Dish(9999999)
# printD()
#
# d["gorilka"]=Dish(1111)
# printD()
#
#
# d.pop("gorilka")
# printD()







