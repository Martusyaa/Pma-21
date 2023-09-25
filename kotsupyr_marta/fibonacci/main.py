FILE_OUTPUT = 'result.txt'
INPUT_FILE = 'input.txt'
def fibonacci(n, a, b):
    if n <= 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n - 1, b, a + b)
try:
    with open(INPUT_FILE, 'r') as file:
        numbers = []
        for line in file:
            numbers.append(int(line.strip()))

    fibonacci1 = []
    for i in range(0, 11):
        fibonacci1.append(fibonacci(i, numbers[0], numbers[1]))

    with open(FILE_OUTPUT, 'w') as file:
        for num in fibonacci1:
            file.write(f"{num} ")

except FileNotFoundError:
    print("Error: The input file was not found.")
except ValueError:
    print("Error: Invalid data in the input file.")
