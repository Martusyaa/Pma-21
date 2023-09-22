
with open("input.txt", "r") as file:

    file_content = file.read()


n=10
with open("input.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    fib_sequence = []



    for i in range(n):
        fib_sequence.append(first_number)
        first_number, second_number = second_number, first_number + second_number

for num in fib_sequence:
    print(num)



with open("output.txt", 'w', encoding='utf-8') as file:
    file.write("Ряд Фібоначчі:\n")
    for num in fib_sequence:

        file.write(str(num) + "\n")
