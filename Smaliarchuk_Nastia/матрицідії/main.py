def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            row = [int(x) for x in line.split()]
            matrix.append(row)
        return matrix

def write_matrix(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def add_matrices(matrixfirst, matrixsecond):
    if len(matrixfirst) != len(matrixsecond) or len(matrixfirst[0]) != len(matrixsecond[0]):
        print("Неможливо додавати матриці різних розмірів.")
        return None
    result_matrix = []
    for i in range(len(matrixfirst)):
        row = []
        for j in range(len(matrixfirst[0])):
            row.append(matrixfirst[i][j] + matrixsecond[i][j])
        result_matrix.append(row)
    return result_matrix

def subtract_matrices(matrixfirst, matrixsecond):
    if len(matrixfirst) != len(matrixsecond) or len(matrixfirst[0]) != len(matrixsecond[0]):
        print("Неможливо віднімати матриці різних розмірів.")
        return None
    result_matrix = []
    for i in range(len(matrixfirst)):
        row = []
        for j in range(len(matrixfirst[0])):
            row.append(matrixfirst[i][j] - matrixsecond[i][j])
        result_matrix.append(row)
    return result_matrix

def multiply_matrices(matrixfirst, matrixsecond):
    if len(matrixfirst[0]) != len(matrixsecond):
        print("Неможливо перемножити матриці з такими розмірами.")
        return None
    result_matrix = []
    for i in range(len(matrixfirst)):
        row = []
        for j in range(len(matrixsecond[0])):
            sum = 0
            for k in range(len(matrixsecond)):
                sum += matrixfirst[i][k] * matrixsecond[k][j]
            row.append(sum)
        result_matrix.append(row)
    return result_matrix

def divide_matrices(matrixfirst, matrixsecond):
    if len(matrixfirst) != len(matrixsecond) or len(matrixfirst[0]) != len(matrixsecond[0]):
        print("Неможливо ділити матриці різних розмірів.")
        return None
    result_matrix = []
    for i in range(len(matrixfirst)):
        row = []
        for j in range(len(matrixfirst[0])):
            if matrixsecond[i][j] == 0:
                print("Ділення на нуль неможливе.")
                return None
            row.append(matrixfirst[i][j] / matrixsecond[i][j])
        result_matrix.append(row)
    return result_matrix

matrix_a = read_matrix('matrix_first.txt')
matrix_b = read_matrix('matrix_second.txt')

result_add = add_matrices(matrix_a, matrix_b)
write_matrix(result_add, 'result_add.txt')

result_subtract = subtract_matrices(matrix_a, matrix_b)
write_matrix(result_subtract, 'result_subtract.txt')

result_multiply = multiply_matrices(matrix_a, matrix_b)
write_matrix(result_multiply, 'result_multiply.txt')

result_divide = divide_matrices(matrix_a, matrix_b)

if result_divide is not None:
    write_matrix(result_divide, 'result_divide.txt')
else:
    print("Не вдалося виконати ділення матриць.")
