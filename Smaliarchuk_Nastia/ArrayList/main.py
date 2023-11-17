from ArrayList import ArrayList


result_file = 'result.txt'


def add_to_file(*sentences):
 print(*sentences, f"size {arList.max_size}")
 with open(result_file, "a") as file:
        file.write("\n")
        for elem in sentences:
         file.write(f"{elem}\n")


with open(result_file, "w") as file:
    file.write("")


arList = ArrayList()
arList.add(2, 2, 2)
add_to_file("ArrayList:", arList)
add_to_file("add 1:", arList.add(1))
add_to_file("add 5:", arList.add(5))
add_to_file("add [3,2,-2]:", arList.add(*[3, 2, -2, 0]))
add_to_file("delete element with index: 2:", arList.delete(2))
add_to_file("delete element with index: -3:", arList.delete(-3))
add_to_file("count entries of 2:", arList.count(2))
add_to_file("remove all entries of 2:", arList.remove_entries(2, -1))
add_to_file("insert 'nastia' after index 1", arList.insert(2, 'nastia'))

