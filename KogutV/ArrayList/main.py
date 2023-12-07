from list import ArrayList

list = ArrayList()

print("List elements:")
for i in range(16): 
    list.add(i)
    print(list.elements[i],list.capacity)