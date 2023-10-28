def add_matrices(firstmatrix, secondmatrix):
    if len(firstmatrix) != len(secondmatrix) or len(firstmatrix[0]) != len(secondmatrix[0]):
        raise ValueError("Розміри матриць повинні бути однаковими")

    result = []
    for i in range(len(firstmatrix)):
        row = []
        for j in range(len(firstmatrix[0])):
            row.append(firstmatrix[i][j] + secondmatrix[i][j])
        result.append(row)
    return result

def subtract_matrices(firstmatrix, secondmatrix):
    if len(firstmatrix) != len(secondmatrix) or len(firstmatrix[0]) != len(secondmatrix[0]):
        raise ValueError("Розміри матриць повинні бути однаковими")

    result = []
    for i in range(len(firstmatrix)):
        row = []
        for j in range(len(firstmatrix[0])):
            row.append(firstmatrix[i][j] - secondmatrix[i][j])
        result.append(row)
    return result

def multiply_matrices(firstmatrix, secondmatrix):
    if len(firstmatrix[0]) != len(secondmatrix):
        raise ValueError("Розміри матриць повинні бути сумісними для множення")

    result = []
    for i in range(len(firstmatrix)):
        row = []
        for j in range(len(secondmatrix[0])):
            element = 0
            for k in range(len(secondmatrix)):
                element += firstmatrix[i][k] * secondmatrix[k][j]
            row.append(element)
        result.append(row)
    return result

def divide_matrices(firstmatrix, secondmatrix):
    if len(firstmatrix[0]) != len(secondmatrix):
        raise ValueError("Розміри матриць повинні бути сумісними для множення")

    result = []
    for i in range(len(firstmatrix)):
        row = []
        for j in range(len(secondmatrix[0])):
            element = 0
            for k in range(len(secondmatrix)):
                element += firstmatrix[i][k] / secondmatrix[k][j]
            row.append(element)
        result.append(row)
    return result

def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

matrix_a = read_matrix_from_file('matrix_a')
matrix_b = read_matrix_from_file('matrix_b')

sum_matrix = add_matrices(matrix_a, matrix_b)
with open('result.txt', 'w') as result_matrix_file:
    for row in sum_matrix:
        result_matrix_file.write(' '.join(map(str, row)) + '\n')

difference_matrix = subtract_matrices(matrix_a, matrix_b)
with open('result.txt', 'a') as result_matrix_file:
    result_matrix_file.write('\n')
    for row in difference_matrix:
        result_matrix_file.write(' '.join(map(str, row)) + '\n')

product_matrix = multiply_matrices(matrix_a, matrix_b)
with open('result.txt', 'a') as result_matrix_file:
    result_matrix_file.write('\n')
    for row in product_matrix:
        result_matrix_file.write(' '.join(map(str, row)) + '\n')

#scalar = 2  скаляр тут
try:
    quotient_matrix = divide_matrices(matrix_a, matrix_a)
    with open('result.txt', 'a') as result_matrix_file:
        result_matrix_file.write('\nDivision ' +  ':\n')
        for row in quotient_matrix:
            result_matrix_file.write(' '.join(map(str, row)) + '\n')
except DivisionError as e:
    with open('result.txt', 'a') as result_matrix_file:
        result_matrix_file.write('\nDivision error: ' + str(e) + '\n')
