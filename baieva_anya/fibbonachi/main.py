def fibonacci(start_list,amount):
    final_list = []
    for i in range(amount):
        new_value = 0
        if i<=1:
            print("Inccorect input")
        else:
            new_value = start_list[i-1]+start_list[i-2]
            print(new_value)
            start_list.append(new_value)
    print(final_list)
    with open("../../../01.09.fibonachi/output.txt", "w") as output:
        for i in start_list:
            output.write(str(i)+"\n")
        output.close()


with open("../../../01.09.fibonachi/input.txt") as file:
    numbers = file.read().replace(",","")
    list_of_numbers = []
    for i in numbers:
        list_of_numbers.append(i)
    print(list_of_numbers)

    integer = [int(i) for i in list_of_numbers]

    fibonacci(integer,1)