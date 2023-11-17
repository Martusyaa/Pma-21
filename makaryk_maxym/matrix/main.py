from matrix import matrix_addition, matrix_subtraction, matrix_multiplication, divide
from read import read_matrix, write_matrix

matrix1 = read_matrix('matrix1.txt')
matrix2 = read_matrix('matrix2.txt')

result_add = matrix_addition(matrix1, matrix2)
result_substraction = matrix_subtraction(matrix1, matrix2)
result_multiplication = matrix_multiplication(matrix1, matrix2)
result_division = divide(matrix1, matrix2)

with open('results.txt', 'w') as file:
    file.write("Matrix Addition:\n")
    write_matrix(file, result_add)

    file.write("\nMatrix Subtraction:\n")
    write_matrix(file, result_substraction)

    file.write("\nMatrix Multiplication:\n")
    write_matrix(file, result_multiplication)

    file.write("\nMatrix Division:\n")
    write_matrix(file, result_division)
