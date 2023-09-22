import random

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"
FILE_NOT_FOUND = "File not found"
NOT_DIVISION = "Division imposible."

try:
    with open(INPUT_FILE_NAME, 'r') as file:
        first_vector = [int(i) for i in file.readline().split()]
        second_vector = [int(i) for i in file.readline().split()]
except FileNotFoundError:
    print(FILE_NOT_FOUND, INPUT_FILE_NAME)
    first_vector = [random.randint(1, 11) for j in range(3)]
    second_vector = [random.randint(1, 11) for j in range(3)]

sum_vector = [first_vector[i]+second_vector[i] for i in range(len(first_vector))]
print(f"\nSum vectors: {sum_vector}")

subtraction_vector = [first_vector[i]-second_vector[i] for i in range(len(first_vector))]
print(f"\nSubtraction vectors: {subtraction_vector}")

multiplication_vector = [first_vector[i]*second_vector[i] for i in range(len(first_vector))]
print(f"\nMultiplication vectors: {multiplication_vector}")

try:
    division_vector = [first_vector[i] / second_vector[i] for i in range(len(first_vector))]
except ZeroDivisionError:
    division_vector = NOT_DIVISION

print(f"\nDivision vectors: {division_vector}")

with open('output.txt', 'w') as file:
    print(f"{first_vector} + {second_vector} = {sum_vector}", file = file)
    print(f"{first_vector} - {second_vector} = {subtraction_vector}", file=file)
    print(f"{first_vector} * {second_vector} = {multiplication_vector}", file=file)
    print(f"{first_vector} / {second_vector} = {division_vector}", file=file)
# multiplication = 0
# for i in range(len(first_vector):
#     multiplication += first_vector[i]*second_vector[i]
# print(f"\nMultiplication vectors: {multiplication}")