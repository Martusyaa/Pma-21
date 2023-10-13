def read_matrix(filename):
    matrix = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = [float(x) for x in line.strip().split()]
                matrix.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не був знайдений.")
    return matrix


def write_matrix(matrix, filename):
    try:
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(' '.join(str(x) for x in row) + '\n')
    except FileNotFoundError:
        print(f"Файл {filename} не був знайдений.")


def multiply_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2:
        print("Матриці не були прочитані.")
        return None

    if len(matrix1[0]) != len(matrix2):
        print("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці.")
        return None

    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            product = 0
            for k in range(len(matrix2)):
                product += matrix1[i][k] * matrix2[k][j]
            row.append(product)
        result_matrix.append(row)

    return result_matrix


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
            det += matrix[0][j] * determinant(submatrix) * (-1) ** j  # Corrected the syntax here
        return det


def inverse_matrix(matrix):
    n = len(matrix)
    det = determinant(matrix)

    if det == 0:
        raise ValueError("Матриця є сингулярною і не має оберненої матриці.")

    adjugate = []
    for i in range(n):
        row = []
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor = determinant(submatrix) * (-1) ** (i + j)
            row.append(cofactor)
        adjugate.append(row)


    inverse = [[adjugate[j][i] / det for i in range(n)] for j in range(n)]

    return inverse

matrix1 = read_matrix("input3.txt")
matrix2 = read_matrix("input2.txt")

result_matrix = multiply_matrices(matrix1, matrix2)

if result_matrix:
    write_matrix(result_matrix, "output2.txt")
    print("Результат множення матриць записано у файл output2.txt.")

try:
    inv_matrix = inverse_matrix(matrix2)
    write_matrix(inv_matrix, "output2.txt")
    print("Обернена матриця записана у файл output2.txt.")
except ValueError as e:
    print(e)
