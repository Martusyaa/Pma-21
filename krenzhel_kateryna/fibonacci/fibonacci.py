INPUT_FILE_NAME = "input.txt"
SEPARATOR = ","
OUTPUT_FILE_NAME = "output.txt"
NUMBER_FILE_NAME = "number.txt"
FILE_NOT_FOUND = "File not found"

def fibonacci(line):
    sum = line[-1] + line[-2]
    if sum < number:
        line.append(sum)
        fibonacci(line)
    else:
        with open(OUTPUT_FILE_NAME, 'w') as file:
            file.write(str(line))

line = [0, 1]
number = 100
try:
    with open(INPUT_FILE_NAME) as file:
        line = file.readline().split(SEPARATOR)
except FileNotFoundError:
    print(FILE_NOT_FOUND, INPUT_FILE_NAME)
try:
    with open(NUMBER_FILE_NAME) as file:
        number = float(file.read())
except FileNotFoundError:
    print(FILE_NOT_FOUND, NUMBER_FILE_NAME)
line = [float(i) for i in line]
line.append(fibonacci(line))
