INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
STEPS_FILE = "steps.txt"
SEPERATOR = ", "
FILE_NOT_FOUND = "file not found"

try:
    with open(INPUT_FILE) as file:
        line = file.readline().split(SEPERATOR)
except FileNotFoundError:
    print(FILE_NOT_FOUND, INPUT_FILE)

try:
    with open(STEPS_FILE) as file:
        steps = int(file.read())
except FileNotFoundError:
    print(FILE_NOT_FOUND, STEPS_FILE)

line = [float(i) for i in line]

for i in range(0, steps - 2):
    line.append(line[-1] + line[-2])

try:
    with open(OUTPUT_FILE, "w") as file:
        file.writelines(str(line))
except FileNotFoundError:
    print(FILE_NOT_FOUND, OUTPUT_FILE)