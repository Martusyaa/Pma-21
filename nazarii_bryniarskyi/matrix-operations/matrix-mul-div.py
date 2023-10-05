import os.path

MATRIX_ERROR = "Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці."
DETERMINANT_ERROR = "Детермінант дорівнює нулю"
SEPARATOR = ','
DEFAULT_MATRIX = [[0, 0], [0, 0]]

def _get_matrix_from_file(matrix_file):
    if not os.path.isfile(matrix_file):
        return DEFAULT_MATRIX

    with open(matrix_file) as file:
        matrix = [[int(num) for num in line.split(SEPARATOR)] for line in file]

    return matrix

def write_matrix_to_file(matrix, file_name):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(','.join(map(str, row)) + '\n')

def transposeMatrix(m):
    return [list(row) for row in zip(*m)]


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeterminant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeterminant(getMatrixMinor(m, 0, c))

    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeterminant(m)
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def mul(matrix_one, matrix_two):
    if len(matrix_one[0]) != len(matrix_two):
        raise ValueError(MATRIX_ERROR)

    result = []

    for i in range(len(matrix_one)):
        row = []

        for j in range(len(matrix_two[0])):
            dot_product = sum(matrix_one[i][a] * matrix_two[a][j] for a in range(len(matrix_one[0])))
            row.append(dot_product)

        result.append(row)

    return result


def truediv(matrix_one, matrix_two):
    if len(matrix_one) != len(matrix_two):
        raise ValueError(MATRIX_ERROR)

    if getMatrixDeterminant(matrix_two) == 0:
        return -1

    result = []
    inverted_matrix = getMatrixInverse(matrix_two)

    current_matrix = matrix_one

    for i in range(len(matrix_one)):
        row = []

        for j in range(len(inverted_matrix[0])):
            dot_product = sum(current_matrix[i][a] * inverted_matrix[a][j] for a in range(len(current_matrix[0])))
            row.append(dot_product)

        result.append(row)

    return result


def main():
    matrix_one = _get_matrix_from_file("matrix_one.txt")
    matrix_two = _get_matrix_from_file("matrix_two.txt")

    with open("result.txt", "w") as result_file:
        result_file.write("mul result\n")
        for row in mul(matrix_one, matrix_two):
            result_file.write(','.join(map(str, row)) + '\n')

        result_file.write("\ndiv result\n")
        if truediv(matrix_one, matrix_two) == -1:
            result_file.write(DETERMINANT_ERROR)
        else:
            for row in truediv(matrix_one, matrix_two):
                result_file.write(','.join(map(str, row)) + '\n')


main()
