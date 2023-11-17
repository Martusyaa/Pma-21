def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrix dimensions do not match for addition.")
        exit()

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


def matrix_subtraction(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result


def matrix_multiplication(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])
    result = [[0 for row in range(cols_matrix2)] for col in range(rows_matrix1)]
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def transpose(matrix):
    # Реалізація транспонування
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            result[i][j] = matrix[j][i]
    return result


def det(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        raise ValueError("Matrix is not square, determinant cannot be calculated.")

    if rows == 2 and cols == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif rows == 3 and cols == 3:
        # Реалізація обчислення детермінанта для 3x3 матриці
        # ...
        pass
    else:
        raise ValueError("Determinant calculation is not implemented for this matrix size.")


def inverse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        raise ValueError("Matrix is not square, inverse cannot be calculated.")

    determinant = det(matrix)

    if determinant == 0:
        raise ValueError("Matrix has a determinant of 0, inverse cannot be calculated.")

    if rows == 2 and cols == 2:
        # Обчислення оберненої матриці для 2x2 матриці
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        inv_determinant = 1 / determinant
        result = [[d * inv_determinant, -b * inv_determinant],
                  [-c * inv_determinant, a * inv_determinant]]
        return result
    elif rows == 3 and cols == 3:
        if len(matrix) != 3 or len(matrix[0]) != 3:
            raise ValueError("Inverse calculation is only implemented for 3x3 matrices.")

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    if determinant == 0:
        raise ValueError("Matrix has a determinant of 0, inverse cannot be calculated.")

    inv_determinant = 1 / determinant

    result = [
        [(e * i - f * h) * inv_determinant, (c * h - b * i) * inv_determinant, (b * f - c * e) * inv_determinant],
        [(f * g - d * i) * inv_determinant, (a * i - c * g) * inv_determinant, (c * d - a * f) * inv_determinant],
        [(d * h - e * g) * inv_determinant, (b * g - a * h) * inv_determinant, (a * e - b * d) * inv_determinant]
    ]

    return result


def divide(matrix1, matrix2):
    rows_matrix_a = len(matrix1)
    cols_matrix_a = len(matrix1[0])
    rows_matrix_b = len(matrix2)
    cols_matrix_b = len(matrix2[0])

    if cols_matrix_a != rows_matrix_b:
        raise ValueError("Cannot divide matrices with incompatible dimensions.")

    inverse_matrix2 = inverse(matrix2)

    result = matrix_multiplication(matrix1, inverse_matrix2)

    return result