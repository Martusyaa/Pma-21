import random

INPUT_FILE_NAME = "input.txt"
SEPARATOR = ","
OUTPUT_FILE_NAME = "output.txt"

line_number = 0


def read_vector():
    global line_number

    with open(INPUT_FILE_NAME, "r+") as file:
        lines = file.readlines()
        if line_number > len(lines):
            raise Exception("Enter new line!")
        current_line = lines[line_number].replace("\n", "")

        vector = [int(x) for x in current_line.split(SEPARATOR) if x.isdigit()]

        line_number += 1
        return vector


def write_vector_in_file(vector):
    with open(OUTPUT_FILE_NAME, "a") as file:
        file.write(str(vector) + "\n")


def summary_vector(vector_first, vector_second):
    if len(vector_first) != len(vector_second):
        raise Exception("Out of range!")
    else:
        for element in range(0, len(vector_first)):
            vector_first[element] += vector_second[element]


def minus_vector(vector_first, vector_second):
    if len(vector_first) != len(vector_second):
        raise Exception("Out of range!")
    else:
        for element in range(0, len(vector_first)):
            vector_first[element] -= vector_second[element]


def multiply_vector(vector_first, vector_second):
    if len(vector_first) == 3 and len(vector_second) == 3:
        matrix = []
        matrix.append(vector_first)
        matrix.append(vector_second)
        value_x = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
        value_y = (-1) * (matrix[0][0] * matrix[1][2] - matrix[1][0] * matrix[0][2])
        value_z = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        vector_first.clear()
        vector_first.append(value_x)
        vector_first.append(value_y)
        vector_second.append(value_z)

    else:
        raise Exception("Out of range!")


def division_vector(vector_first, vector_second):
    for i in range(0, len(vector_first)):

        if vector_second[i]!=0:
            value = vector_first[i] / vector_second[i]
            value = round(value, 2)
            vector_first[i] = value
        else:
            raise Exception ("Divided by zero!")



vector_first = read_vector()
vector_second = read_vector()

print(vector_first)
print(vector_second)
write_vector_in_file(vector_first)
write_vector_in_file(vector_second)
# summary_vector(vector,vector2)
# minus_vector(vector,vector2)
# multiply_vector(vector,vector2)
division_vector(vector_first, vector_second)
write_vector_in_file(vector_first)

