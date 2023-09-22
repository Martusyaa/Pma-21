import random
INPUT_FILE_NAME = "../../../learning/vector/input.txt"
SEPARATOR = ","
OUTPUT_FILE_NAME = "../../../learning/vector/output.txt"
line_number = 0
class Vector:
    def __init__(self):
        self.vector=[]
        self.read_vector()

    def read_vector(self):
        global line_number

        with open(INPUT_FILE_NAME, "r+") as file:
            lines = file.readlines()
            if line_number > len(lines):
                raise Exception("Enter new line!")
            current_line = lines[line_number].replace("\n", "")

            self.vector = [int(x) for x in current_line.split(SEPARATOR) if x.isdigit()]

            line_number += 1


    def write_vector_in_file(self):
        with open(OUTPUT_FILE_NAME, "a") as file:
            file.write(str(self.vector) +"\n")



    def summary_vector(self, vector_second):
        if len(self.vector) != len(vector_second.vector):
            raise Exception("Out of range!")
        else:
            for element in range(0, len(self.vector)):
                self.vector[element] += vector_second.vector[element]
    def minus_vector(self, vector_second):
        if len(self.vector) != len(vector_second.vector):
            raise Exception("Out of range!")
        else:
            for element in range(0, len(self.vector)):
                self.vector[element] -= vector_second.vector[element]

    def multiply_vector(self, vector_second):
        if len(self.vector) == 3 and len(vector_second.vector) == 3:
            matrix = []
            matrix.append(self.vector)
            matrix.append(vector_second.vector)
            value_x = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
            value_y = (-1) * (matrix[0][0] * matrix[1][2] - matrix[1][0] * matrix[0][2])
            value_z = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            self.vector.clear()
            self.vector.append(value_x)
            self.vector.append(value_y)
            self.vector.append(value_z)

        else:
            raise Exception("Out of range!")

    def division_vector(self, vector_second):
        for i in range(0, len(self.vector)):
            if vector_second[i] != 0:
                value = vector_first[i] / vector_second[i]
                value = round(value, 2)
                vector_first[i] = value
            else:
                raise Exception("Divided by zero!")

vector_first=Vector()
vector_second=Vector()

vector_first.write_vector_in_file()
vector_second.write_vector_in_file()


#Summary
# vector_first.summary_vector(vector_second)
# vector_first.write_vector_in_file()

#Minus
# vector_first.minus_vector(vector_second)
# vector_first.write_vector_in_file()

# Multiplication
# vector_first.multiply_vector(vector_second)
# vector_first.write_vector_in_file()

# Division
# vector_first.division_vector(vector_second)
# vector_first.write_vector_in_file()