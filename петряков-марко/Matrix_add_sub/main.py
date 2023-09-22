import numpy as np


# matrix
start_file_index = 0
def enter_input_from_file(your_matrix):
    global start_file_index
    with open("matrix.txt", "r") as file:
        file_lines = file.readlines()
        e = len(file_lines)
        if start_file_index >= len(file_lines):
            return
        else:
            lines = file_lines[start_file_index].replace("\n","")
            v = [int(x) for x in lines.split(",") if x.isdigit()]
            if len(v) == 0:
                start_file_index+=1
                return
            else:
                your_matrix.append(v)
                start_file_index = start_file_index+1

            return enter_input_from_file(your_matrix)

def output_in_file(matrix1):
    with open("matrix_output.txt", "a") as file:
        for row in matrix1:
            for element in row:
                file.write(str(element)+",")
            file.write("\n")
        file.write("\n")



def print_matrix(your_matrix):
    for row in your_matrix:
        for element in row:
            print(element, end="\t   ")
        print()

def check_row_column_sub_add(first_matrix, second_matrix):

    if len(first_matrix) != len(second_matrix):
        err = "The matrix ratio is not equal!!! (row)"
        raise Exception(err)

    length_first = len(first_matrix[0])
    length_second = len(second_matrix[0])
    similar_lines_counter = 0

    for i in first_matrix:
        if length_first == len(i):
            similar_lines_counter += 1

    if similar_lines_counter == len(first_matrix):
        print("All is okay")
    else:
        length_first=0
        print("All is bad")

    similar_lines_counter = 0
    for i in second_matrix:
        if length_second == len(i):
            similar_lines_counter += 1

    if similar_lines_counter == len(second_matrix):
        print("All is okay")
    else:
        length_second = 0
        print("All is bad")

    if length_second!=length_first:
        raise Exception("You`re matrix are not equal! (columns)")


# def check_row_col_multiplication(first_matrix, second_matrix):
#
#     length_first = len(first_matrix[0])
#     length_second = len(second_matrix[0])
#     length_row_second = len(second_matrix)
#     similar_lines_counter = 0
#
#     for i in second_matrix:
#         if length_second == len(i):
#             similar_lines_counter += 1
#
#     if similar_lines_counter == len(second_matrix):
#         pass
#     else:
#         length_second = 0
#
#     similar_lines_counter = 0
#     columns_in_first_matrix = 0
#     for i in first_matrix:
#         if length_first == len(i):
#             similar_lines_counter += 1
#
#     if similar_lines_counter == len(first_matrix):
#
#         for i in first_matrix[0]:
#             columns_in_first_matrix += 1
#     else:
#         length_first = 0
#     if columns_in_first_matrix != length_row_second:
#         raise Exception("The rows in first matrix and columns in second aren`t equal!!")


def adding(first_matrix, second_matrix):
    check_row_column_sub_add(first_matrix, second_matrix)
    result = []

    for row in range(len(first_matrix)):
        list_to_result = []
        for column in range(len(first_matrix[row])):
            element_in_list_to_result = first_matrix[row][column] + second_matrix[row][column]
            list_to_result.append(element_in_list_to_result)
        result.append(list_to_result)

    first_matrix.clear()
    for row in result:
        first_matrix.append(row)


def subtraction(first_matrix, second_matrix):

    check_row_column_sub_add(first_matrix, second_matrix)
    result = []

    for row in range(len(first_matrix)):
        list_to_result = []
        for column in range(len(first_matrix[row])):
            element_in_list_to_result = first_matrix[row][column] - second_matrix[row][column]
            list_to_result.append(element_in_list_to_result)
        result.append(list_to_result)

    first_matrix.clear()
    for row in result:
        first_matrix.append(row)


# def multiplication(first_matrix, second_matrix):
#     check_row_col_multiplication(first_matrix,second_matrix)
#     result = []
#     for row_for_first in range(len(first_matrix)):
#         list_for_result = []
#         for column_for_second in range(len(second_matrix[0])):
#             value=0
#             for column_for_first_and_row_for_second in range(len(second_matrix)):
#                 value += (first_matrix[row_for_first][column_for_first_and_row_for_second] * second_matrix[column_for_first_and_row_for_second][column_for_second])
#             list_for_result.append(value)
#         result.append(list_for_result)
#     first_matrix.clear()
#     for row in result:
#         first_matrix.append(row)
#
#
# def division(first_matrix, second_matrix):
#     check_row_col_multiplication(first_matrix,second_matrix)
#
#     second_matrix_inverse = np.linalg.inv(second_matrix).round(2)
#     first_matrix_new = np.matmul(first_matrix,second_matrix_inverse)
#     first_matrix_new = first_matrix_new.round(2)
#     first_matrix.clear()
#     for row in first_matrix_new:
#         first_matrix.append(row)


matrix_first= []
enter_input_from_file(matrix_first)
matrix_second = []
enter_input_from_file(matrix_second)

print("Matrix1")
print_matrix(matrix_first)
print("Matrix2")
print_matrix(matrix_second)
output_in_file(matrix_first)
output_in_file(matrix_second)


adding(matrix_first,matrix_second)
output_in_file(matrix_first)

