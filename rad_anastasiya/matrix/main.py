DIFFERENT_DIMENSION = "Dimensions are different"
INCOMPATIBLE_DIMENSION = "Incompatible dimensions for matrix multiplication"
DIVISION_BY_ZERO = "Division by zero is not allowed"

def parse_row(row):
    return [float(num) for num in row.split() if num.strip()]


def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = parse_row(line)
            matrix.append(row)
    return matrix


def write_matrix(matrix, file_name):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')


def matrix_dimension_check(first, second):
    if len(first) != len(second) or len(first[0]) != len(second[0]):
        raise Exception(DIFFERENT_DIMENSION)


def add_matrices(first: [[]], second: [[]]) -> [()]:
    matrix_dimension_check(first, second)

    result_matrix = [[first[i][j] + second[i][j] for j in range(len(first[0]))] for i in range(len(first))]
    return result_matrix


def subtract_matrices(first, second):
    matrix_dimension_check(first, second)

    result_matrix = [[first[i][j] - second[i][j] for j in range(len(first[0]))] for i in range(len(first))]
    return result_matrix


def multiply_matrices(first, second):
    if len(first[0]) != len(second):
        raise Exception(INCOMPATIBLE_DIMENSION)

    result_matrix = [[0 for _ in range(len(second[0]))] for _ in range(len(first))]

    for i in range(len(first)):
        for j in range(len(second[0])):
            for k in range(len(second)):
                result_matrix[i][j] += first[i][k] * second[k][j]

    return result_matrix


def divide_matrix(first, divisor):
    if divisor == 0:
        raise ZeroDivisionError(DIVISION_BY_ZERO)

    result_matrix = [[first[i][j] / divisor for j in range(len(first[0]))] for i in range(len(first))]
    return result_matrix


try:
    first = read_matrix("first_matrix.txt")
    second = read_matrix("second_matrix.txt")

    operations = ['+', '-', '*', '/']

    with open("result.txt", "a") as result_file:
        for operation in operations:
            result_file.write(f"Operation: {operation}\n")

            if operation == '+':
                result_matrix = add_matrices(first, second)
            elif operation == '-':
                result_matrix = subtract_matrices(first, second)
            elif operation == '*':
                result_matrix = multiply_matrices(first, second)
            elif operation == '/':
                divisor = 2
                result_matrix = divide_matrix(first, divisor)

            
            result_file.write(f"Result:\n")
            for row in result_matrix:
                result_file.write(' '.join(map(str, row)) + '\n')
            result_file.write("\n")

except Exception as e:
    with open("result.txt", "w") as result_file:
        result_file.write(str(e))
