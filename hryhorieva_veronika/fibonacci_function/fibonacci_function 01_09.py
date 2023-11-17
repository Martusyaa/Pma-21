INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"
def fibonacci(fibonacci_of, quantity):
    new_list = []
    for i in range(quantity):
        new_value = 0
        if i == 0 or i == 1:
            pass
        else:
            new_value = fibonacci_of[i - 1] + fibonacci_of[i - 2]
            fibonacci_of.append(new_value)
    with open(OUTPUT_FILE_NAME, "w") as output:
        for i in fibonacci_of:
            output.write(str(i) + "\n")
        output.close()


with open(INPUT_FILE_NAME) as input:
    data = input.read().replace(",", "")
    list_of_numbers = []
    for i in data:
        list_of_numbers.append(i)
    print(list_of_numbers)
integer = [int(i) for i in list_of_numbers]
fibonacci(integer, 10)
