from array_list import Array_list



def main():
    arr = Array_list(arr=[10,11,12], length=10)
    print(arr)
    for i in range(7):
        print(arr.last_element_index)
        arr.append(i)
    print(f"Array: {arr}; Array length before extension: {len(arr)}")
    arr.append(7)
    print(f"Array after extension: {arr}; Array length after extension: {len(arr)}")
    

main()