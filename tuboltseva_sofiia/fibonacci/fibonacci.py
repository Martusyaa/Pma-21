INPUT_FILE_NAME = 'input.txt'
SEPARATOR = ' '
OUTPUT_FILE_NAME = 'steps.txt'
try:
    with open(INPUT_FILE_NAME, 'r') as file:
        line = file.readline()
        values = line.split(' ')
except FileNotFoundError:
    print("File not found: ", INPUT_FILE_NAME)

value1 = int(values[0])
value2 = int(values[1])

with open('steps.txt', 'r') as file:
    n = int(file.readline())

fib_series = [value1, value2]


def tri_recursion(k):
    if (k > n):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 10
    return result


print("\n\nRecursion Example Results")


for i in range(2, result):
        #next_num = fib_series[-1] + fib_series[-2]
    fib_series.append(fib_series[-1] + fib_series[-2])

print(fib_series)

with open('result.txt', 'w') as output_file:
    output_file.write(str(fib_series))

