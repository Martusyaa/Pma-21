INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
STEPS_FILE = "steps.txt"
COMMA = ","

input = [0, 1]
steps = 10

try:
    with open(INPUT_FILE, "r") as file:
        input = file.read().split(COMMA)
except FileNotFoundError:
    print("input.txt is missing")

try:
    with open(STEPS_FILE, "r") as file:
        steps = int(file.read())
except FileNotFoundError:
    print("steps.txt is missing")
except ValueError:
    print("Steps is not number")
    exit(-1)

try:
    input = [float(i) for i in input]
except ValueError:
    print("inpt data is incorrect")
    exit(-1)

for i in range(0, steps):
    length = len(input)
    next = input[length - 1] + input[length - 2]
    input.append(next)

with open(OUTPUT_FILE, "w") as file:
    file.write(str(input))
