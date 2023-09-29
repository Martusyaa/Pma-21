import random
from List import ArrayList

array = [random.randint(1, 11) for i in range(5)]
other = ArrayList()
# arr_list = ArrayList()
arr_list = ArrayList(array)
arr_list.print()
print('\n')
print(other)


arr_list.insert(4, 20)
arr_list.print()
print('\n')

arr_list.remove(3)
arr_list.print()
print('\n')

# arr_list.pop(20)
# arr_list.print()
# print('\n')

arr_list.clean()
arr_list.print()
