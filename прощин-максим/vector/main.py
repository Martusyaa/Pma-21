INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
SEPARATOR = ", "
FILE_NOT_FOUND = "file not found"
NEWLINE = "\n"
ZERO_ERROR = "cant to devision"

try:
    with open(INPUT_FILE) as file:
        lines = file.readlines()
except FileNotFoundError:
    print(FILE_NOT_FOUND, INPUT_FILE)

vector1 = [float(i) for i in lines[0].split(SEPARATOR)]
vector2 = [float(i) for i in lines[1].split(SEPARATOR)]
sum_vector = []
diffence_vector = []
multiplication_vector = []
division_vector = []

for i in range(len(vector1)):
    sum_vector.append(vector1[i] + vector2[i])

for i in range(len(vector1)):
    diffence_vector.append(vector1[i] - vector2[i])

for i in range(len(vector1)):
    multiplication_vector.append(vector1[i] * vector2[i])

try:
    for i in range(len(vector1)):
        division_vector.append(vector1[i] / vector2[i])
except ZeroDivisionError:
    print(ZERO_ERROR)

try:
    with open(OUTPUT_FILE, "w") as file:
        file.write(str(sum_vector) + NEWLINE)
        file.write(str(diffence_vector) + NEWLINE)
        file.write(str(multiplication_vector) + NEWLINE)
        file.write(str(division_vector) + NEWLINE)
except FileNotFoundError:
    print(FILE_NOT_FOUND,OUTPUT_FILE)