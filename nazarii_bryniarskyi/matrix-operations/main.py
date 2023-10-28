MATRIX_ERROR = "Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці."
MATRIX_ONE_FILE = "matrix_one.txt"
MATRIX_TWO_FILE = "matrix_two.txt"
SEPARATOR = ','

def getMatrixFirstFromFile():
    with open(MATRIX_ONE_FILE) as file:
        matrix = [[int(num) for num in line.split(SEPARATOR)] for line in file]

    return matrix

def getMatrixSecondFromFile():
    with open(MATRIX_TWO_FILE) as file:
        matrix = [[int(num) for num in line.split(SEPARATOR)] for line in file]

    return matrix


def add(matrix_one, matrix_two):
    if len(matrix_one[0]) != len(matrix_two):
        raise ValueError(MATRIX_ERROR)

    result = []

    for i in range(len(matrix_one)):
        row = []

        for j in range(len(matrix_one[0])):
            row.append(matrix_one[i][j] + matrix_two[i][j])

        result.append(row)

    return result


def subtract(matrix_one, matrix_two):
    if len(matrix_one[0]) != len(matrix_two):
        raise ValueError(MATRIX_ERROR)

    result = []

    for i in range(len(matrix_one)):
        row = []

        for j in range(len(matrix_one[0])):
            row.append(matrix_one[i][j] - matrix_two[i][j])

        result.append(row)

    return result


def multiply(matrix_one, matrix_two):
    if len(matrix_one) != len(matrix_two[0]) or len(matrix_one[0]) != len(matrix_two):
        raise ValueError(MATRIX_ERROR)

    result = []

    for i in range(len(matrix_one)):
        row = []

        for j in range(len(matrix_two[0])):
            dot_product = sum(matrix_one[i][a] * matrix_two[a][j] for a in range(len(matrix_one[0])))
            row.append(dot_product)

        result.append(row)

    return result


def main():
    matrix_one = getMatrixFirstFromFile()

    matrix_two = getMatrixSecondFromFile()

    # print("matrix addition")
    # for k in add(matrix_one, matrix_two):
    #     print(k)
    #
    # print("\nmatrix subtracting")
    # for k in subtract(matrix_one, matrix_two):
    #     print(k)

    print("\nmatrix multiplication")
    for k in multiply(matrix_one, matrix_two):
        print(k)
    #
    # print("\nmatrix dividing")
    # for k in divide(matrix_one, matrix_two):
    #     print(k)

main()

