import random

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"
FILE_NOT_FOUND = "File not found"
NOT_DIVISION = "Not division."
def sum(first_matrix, second_matrix):
    sum_matrix = [[first_matrix[i][j] + second_matrix[i][j] for j in range(len(number))] for i in range(len(number))]
    return sum_matrix
def subtraction(first_matrix, second_matrix):
    subtraction_matrix = [[first_matrix[i][j] - second_matrix[i][j] for j in range(len(number))] for i in
                          range(len(number))]
    return subtraction_matrix
def multiplication(first_matrix, second_matrix):
    matrix_multiplication = [[0 for j in range(len(number))] for i in range(len(number))]
    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                matrix_multiplication[i][j] += first_matrix[i][k] * second_matrix[k][j]
    return matrix_multiplication
def determinant(matrix): # Функція для обчислення визначника матриці
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3:
        return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                       matrix[0][1] * matrix[1][2] * matrix[2][0] +
                       matrix[1][0] * matrix[0][2] * matrix[2][1] -
                       matrix[2][0] * matrix[1][1] * matrix[0][2] -
                       matrix[0][0] * matrix[2][1] * matrix[1][2] -
                       matrix[1][0] * matrix[0][1] * matrix[2][2])
    else:
        det = 0
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
            det += matrix[0][j] * ((-1) ** j) * determinant(minor)
        return det
def cofactor_matrix(matrix): # Функція для обчислення матриці алгебраїчних доповнень
    cofactors = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)
    return cofactors
def transpose(matrix): # Функція для транспонування матриці
    transposed = []
    for j in range(len(matrix)):
        transposed_row = [matrix[i][j] for i in range(len(matrix))]
        transposed.append(transposed_row)
    return transposed
# def inverse_matrix(matrix): # Обчислення оберненої матриці
#     det = determinant(matrix)
#     if det == 0:
#         inverse = NOT_DIVISION
#     else:
#         cofactors = cofactor_matrix(matrix)
#         adjugate = transpose(cofactors)
#         inverse = [[element / det for element in row] for row in adjugate]
#     return inverse
# def division(first_matrix, second_matrix):
#     try:
#         inverse_second_matrix = inverse_matrix(second_matrix)
#         division = multiplication(first_matrix, inverse_second_matrix)
#     except ZeroDivisionError:
#         division = NOT_DIVISION
#     return division

# Calculate the inverse of a matrix
def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        inverse = NOT_DIVISION
    else:
        cofactors = cofactor_matrix(matrix)
        adjugate = transpose(cofactors)
        inverse = [[element / det for element in row] for row in adjugate]
    return inverse

# Divide two matrices
def division(first_matrix, second_matrix):
    try:
        inverse_second_matrix = inverse_matrix(second_matrix)
        if inverse_second_matrix == NOT_DIVISION:
            division_result = NOT_DIVISION
        else:
            division_result = multiplication(first_matrix, inverse_second_matrix)
    except ZeroDivisionError:
        division_result = NOT_DIVISION
    return division_result

try:
    with open(INPUT_FILE_NAME, 'r') as file:
        number = [int(i) for i in file.readline().split()]
    with open(INPUT_FILE_NAME, 'r') as file:
        first_matrix = [[int(i) for i in file.readline().split()] for i in range(len(number))]
        second_matrix = [[int(i) for i in file.readline().split()] for i in range(len(number))]
except FileNotFoundError:
    print(FILE_NOT_FOUND, INPUT_FILE_NAME)
    first_matrix = [[random.randint(1, 11) for j in range(3)] for i in range(3)]
    second_matrix = [[random.randint(1, 11) for j in range(3)] for i in range(3)]
    number = first_matrix[0]

sum_matrix = sum(first_matrix, second_matrix)
subtraction_matrix = subtraction(first_matrix, second_matrix)
multiplication_matrix = multiplication(first_matrix, second_matrix)
division_matrix = division(first_matrix, second_matrix)

print("First matrix:")
for i in range(int(len(first_matrix))):
    print(first_matrix[i])
print('\nSecond matrix:')
for i in range(len(number)):
    print(second_matrix[i])
print('\nSum matrix:')
for i in range(len(number)):
    print(sum_matrix[i])
print('\nSubtraction matrix:')
for i in range(len(number)):
    print(subtraction_matrix[i])
print('\nMatrix multiplication:')
for i in range(len(number)):
    print(multiplication_matrix[i])
print('\nMatrix division:')
for i in range(len(number)):
    print(division_matrix[i])
def print_matrix(file, first_matrix, second_matrix, result_matrix, operation):
    for i in range(len(first_matrix)):
        if i == len(first_matrix) // 2:
            print(f"{first_matrix[i]} {operation} {second_matrix[i]} = {result_matrix[i]}", file = file)
        else:
            print(f"{first_matrix[i]}   {second_matrix[i]}   {result_matrix[i]}", file = file)
    file.write('\n')

with open(OUTPUT_FILE_NAME, 'w') as file:
    print_matrix(file, first_matrix, second_matrix, sum_matrix, '+')
    print_matrix(file, first_matrix, second_matrix, subtraction_matrix, '-')
    print_matrix(file, first_matrix, second_matrix, multiplication_matrix, '*')
    print_matrix(file, first_matrix, second_matrix, division_matrix, '/')