def addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrix dimensions do not match for addition.")
        exit(-1)

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtraction(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0])))

    return result

def inverse_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Матриця не є квадратною")

    n = len(matrix)
    identity = [[0] * n for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1

    for i in range(n):
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("Матриця не має оберненої")
        
        for j in range(n):
            matrix[i][j] /= pivot
            identity[i][j] /= pivot
        
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n):
                    matrix[k][j] -= factor * matrix[i][j]
                    identity[k][j] -= factor * identity[i][j]

    return identity

def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [float(x) for x in line.split()]
            matrix.append(row)
    return matrix

def write_matrix(file, result):
    for row in result:
        file.write(' '.join(map(str, row)) + '\n')

def divide(matrix1,matrix2):
    inversion = inverse_matrix(matrix2)
    result = multiply_matrices(matrix1, inversion)

    return result

