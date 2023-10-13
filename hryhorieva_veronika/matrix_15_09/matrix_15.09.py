
import random
import numpy as np
INPUT_FILE_NAME = "input.txt"
SEPARATOR = ","
OUTPUT_FILE_NAME = "output.txt"
vector_first = []
rows = 0
collons = 0
vector_second = []
start_index=0

def summary_matrix(matrix_first, matrix_second):
    if len(matrix_first) != len(matrix_second) or len(matrix_first[0]) != len(matrix_second[0]):
        error = "ERROR! rows1!=rows2 or colluns1!=colluns2"
        raise Exception(error)
    for row in range(len(matrix_first)):
        for collon in range(0, len(matrix_first[0])):
            matrix_first[row][collon] += matrix_second[row][collon]

def read_matrix_from_file(matrix):
    global start_index
    with open(INPUT_FILE_NAME, "r+") as file:
        file_lines=file.readlines()
        quantity_of_lengths=len(file_lines)
        if start_index>=len(file_lines):
            return
        else:
            lines=file_lines[start_index].replace("\n","")
            array=[int(x) for x in lines.split(",") if x.isdigit()]
            if len(array)==0:
                start_index+=1
                return
            matrix.append(array)
            start_index+=1


            return read_matrix_from_file(matrix)

def write_matrix_in_file(matrix):
    with open(OUTPUT_FILE_NAME, "a") as file:
        for rows in matrix:
            for element in rows:
                file.write(str(element) + ",")
            file.write("\n")
        file.write("\n")



def minus_matrix(matrix_first, matrix_second):
    if len(matrix_first) != len(matrix_second) or len(matrix_first[0]) != len(matrix_second[0]):
        error = "ERROR! rows1!=rows2 or colluns1!=colluns2"
        raise Exception(error)
    for row in range(len(matrix_first)):
        for collon in range(0, len(matrix_first[0])):
            matrix_first[row][collon] -= matrix_second[row][collon]


def multiplication_matrix(matrix_first, matrix_second):
    if len(matrix_first[0]) != len(matrix_second):
        error = "ERROR! rows1!=colluns2"
        raise Exception(error)
    result = []
    for row_first_matrix in range(len(matrix_first)):
        matrixResult = []
        for collon_second_matrix in range(0, len(matrix_first[0])):
            value = 0
            for collonFirst_rowSecond in range(0, len(matrix_first[0])):
                value += matrix_first[row_first_matrix][collonFirst_rowSecond] * matrix_second[collonFirst_rowSecond][
                    collon_second_matrix]
            matrixResult.append(value)
        result.append(matrixResult)
    matrix_first.clear()
    for row in result:
        matrix_first.append(row)


def division_matrix(matrix_first, matrix_second):
    if len(matrix_first[0]) != len(matrix_second):
        error = "ERROR! rows1!=colluns2"
        raise Exception(error)
    matrix_second_reserved = np.linalg.inv(matrix_second).round(2)
    matrix_first_new = np.matmul(matrix_first, matrix_second_reserved)
    matrix_first_new = matrix_first_new.round(2)
    matrix_first.clear()
    for row in matrix_first_new:
        matrix_first.append(row)


def fill_matrix(matrix, rows, collons):
    for r in range(rows):
        row_for_matrix = []
        for element in range(collons):
            # value=random.randint(1,20)
            row_for_matrix.append(random.randint(1, 20))
        matrix.append(row_for_matrix)


def print_matrix(matrix):

    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()


matrix_first=[]
matrix_second=[]
#matrix first
read_matrix_from_file(matrix_first)
write_matrix_in_file(matrix_first)
#matrix second
read_matrix_from_file(matrix_second)
write_matrix_in_file(matrix_second)

# #multiplication
# multiplication_matrix(matrix_first, matrix_second)
# write_matrix_in_file(matrix_first)

# #division
# division_matrix(matrix_first, matrix_second)
# write_matrix_in_file(matrix_first)

# #summary
# summary_matrix(matrix_first, matrix_second)
# write_matrix_in_file(matrix_first)

#minus
minus_matrix(matrix_first, matrix_second)
write_matrix_in_file(matrix_first)