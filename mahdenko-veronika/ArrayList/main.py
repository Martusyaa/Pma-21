import random
from ArrayList import ArrayList

if __name__ == '__main__':
    array = ArrayList([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3])

    array.print_array()
    array.add_element(5)
    array.print_array()
    array.add_element(7)
    array.print_array()
    try:
        array.delete_element()
        array.print_array()
    except ValueError as e:
        print(e)
    try:
        array.add_index(2, 10)
        array.print_array()
        array.add_index(6, 5)
        array.print_array()
        array.add_index(4, 4)
        array.print_array()
    except ValueError as e:
        print(e)

    try:
        array.clear()
        array.print_array()
    except ValueError as e:
        print(e)