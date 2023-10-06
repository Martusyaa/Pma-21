from main import ArrayList
my_list = ArrayList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
print("List:",my_list)

my_list.insert(1,4)
print(my_list)
other_list = [5, 6]

my_list.reverse()
print("Inverse list:",my_list)

my_list.clean()
print("Clean list:",my_list)
