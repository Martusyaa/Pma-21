INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
STEPS_FILE = "steps.txt"
SEPARATOR = ", "
FILE_NOT_FOUND = "file not found"

try:
    with open(INPUT_FILE) as file:
        lines = file.readlines()
    input_values = [int(line.strip()) for line in lines]
except FileNotFoundError:
    print(FILE_NOT_FOUND, INPUT_FILE)

try:
    with open(STEPS_FILE) as file:
        steps = int(file.read())
except FileNotFoundError:
    steps = 0

if steps > 1:
    line = input_values[:]
    for i in range(2, steps):
        line.append(line[-1] + line[-2])
else:
    line = input_values

try:
    with open(OUTPUT_FILE, "w") as file:
        file.writelines(SEPARATOR.join(map(str, line)))
except FileNotFoundError:
    print(FILE_NOT_FOUND, OUTPUT_FILE)




