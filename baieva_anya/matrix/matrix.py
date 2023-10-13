import numpy as np

INPUT_MATRIX = "input_matrix.txt"
OUTPUT_MATRIX = "output_matrix.txt"

start_file_index = 0 #

def read_from_file(matrix):
    global start_file_index #щоб вязти змінну з мейну
    with open (INPUT_MATRIX, "r") as file:
        file_lines = file.readlines()
        lines_counter = len(file_lines)
        if start_file_index >= lines_counter:
            return
        else:
            current_line = file_lines[start_file_index].replace("\n","")
            row = [int(x) for x in current_line.split(",") if x.isdigit()]
            if len(row)==0:
                start_file_index += 1
                return
            else:
                matrix.append(row)
                start_file_index += 1

            return read_from_file(matrix)

def write_to_file(matrix):
    with open(OUTPUT_MATRIX,"a") as file:
        for row in matrix:
            for element in row:
                file.write(str(element)+",")
            file.write("\n")
        file.write("\n")

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

def check_matrix_add(matrix_first, matrix_second):
    lenght_first = len(matrix_first)
    lenght_second = len(matrix_second)
    if lenght_first != lenght_second:
        raise Exception("You cannot do anything with this matrixes")
    lenght_first_column = len(matrix_first[0])
    lenght_second_column = len(matrix_second[0])
    if lenght_first_column != lenght_second_column:
        raise Exception("You cannot do anything with this matrixes")

def add_matrix(matrix_first,matrix_second):
    check_matrix_add(matrix_first, matrix_second)
    result = []
    for row in range(len(matrix_first)):
        row_to_result = []
        for element in range(len(matrix_first)):
            value_result = matrix_first[row][element]+matrix_second[row][element]
            row_to_result.append(value_result)
        result.append(row_to_result)
    matrix_first.clear()
    for row in result:
        matrix_first.append(row)

def subtract_matrix(matrix_first,matrix_second):
    check_matrix_add(matrix_first, matrix_second)
    result = []
    for row in range(len(matrix_first)):
        row_to_result = []
        for element in range(len(matrix_first)):
            value_result = matrix_first[row][element]-matrix_second[row][element]
            row_to_result.append(value_result)
        result.append(row_to_result)
    matrix_first.clear()
    for row in result:
        matrix_first.append(row)

def check_matrix_multiply(matrix_first,matrix_second):
    lenght_column = len(matrix_first[0])
    lenght_row = len(matrix_second)
    if lenght_column != lenght_row:
        raise Exception("You cannot multiply matrixes")

def multiply_matrix(matrix_first,matrix_second):
    check_matrix_multiply(matrix_first, matrix_second)
    result = []
    for row_first in range(len(matrix_first)):
        row_to_result = []
        for column_second in range(len(matrix_second[0])):
            value = 0
            for column_first_and_row_second in range(len(matrix_second)):
                value+=matrix_first[row_first][column_first_and_row_second]*matrix_second[column_first_and_row_second][column_second]
            row_to_result.append(value)
        result.append(row_to_result)
    matrix_first.clear()
    for row in result:
        matrix_first.append(row)

def divide_matrix(matrix_first, matrix_second):
    check_matrix_multiply(matrix_first, matrix_second)
    matrix_second_inverse = np.linalg.inv(matrix_second).round(2)
    matrix_first_new = np.matmul(matrix_first, matrix_second_inverse)
    matrix_first_new = matrix_first_new.round(2)
    matrix_first.clear()
    for row in matrix_first_new:
        matrix_first.append(row)





matrix_first = []
matrix_second = []
read_from_file(matrix_first)
read_from_file(matrix_second)

# #SUM
# write_to_file(matrix_first)
# add_matrix(matrix_first, matrix_second)
# write_to_file(matrix_second)
# write_to_file(matrix_first)

# #Subtract
# write_to_file(matrix_first)
# subtract_matrix(matrix_first, matrix_second)
# write_to_file(matrix_second)
# write_to_file(matrix_first)

# #Multiply
# write_to_file(matrix_first)
# multiply_matrix(matrix_first, matrix_second)
# write_to_file(matrix_second)
# write_to_file(matrix_first)

# #Divide
# write_to_file(matrix_first)
# divide_matrix(matrix_first, matrix_second)
# write_to_file(matrix_second)
# write_to_file(matrix_first)


# 1,2,3,4
# 3,3,4,4
# 6,6,5,5
#
# 2,3,5,6
# 3,4,5,6
# 1,1,1,2
# 1,2,3,4


# 1,2,3,
# 5,6,7,
# 9,1,2,
#
# 1,2,3
# 3,4,5
# 6,7,8

# 1,1,1
# 1,2,3
#
# 1,3,4
# 1,3,5