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


def main():
    try:
        first_matrix = read_matrix("first_matrix.txt")
        second_matrix = read_matrix("second_matrix.txt")
        operations = ['+', '-', '*', '/']

        with open("result.txt", "w") as result_file:
            for operation in operations:
                result_file.write(f"Operation: {operation}\n")
                try:
                    result_matrix = perform_operation(first_matrix, second_matrix, operation)
                    write_matrix(result_matrix, "result.txt")
                    result_file.write(str(result_matrix) + "\n")
                except ValueError as ve:
                    result_file.write(str(ve) + "\n")
                except ZeroDivisionError as zde:
                    result_file.write(str(zde) + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")


def add_matrices(first, second):
    matrix_dimension_check(first, second)

    result_matrix = [[first[i][j] + second[i][j] for j in range(len(first[0]))] for i in range(len(first))]
    return result_matrix


def subtract_matrices(first, second):
    matrix_dimension_check(first, second)

    result_matrix = [[first[i][j] - second[i][j] for j in range(len(first[0]))] for i in range(len(first))]
    return result_matrix


def multiply_matrices(first, second):
    if len(first[0]) != len(second):
        raise ValueError(INCOMPATIBLE_DIMENSION)

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


def perform_operation(first_matrix, second_matrix, operation):
    matrix_dimension_check(first_matrix, second_matrix)

    if operation == '+':
        result_matrix = add_matrices(first_matrix, second_matrix)
    elif operation == '-':
        result_matrix = subtract_matrices(first_matrix, second_matrix)
    elif operation == '*':
        result_matrix = multiply_matrices(first_matrix, second_matrix)
    elif operation == '/':
        divisor = 2
        result_matrix = divide_matrix(first_matrix, divisor)
    else:
        raise ValueError("Unsupported operation")

    return result_matrix


def matrix_dimension_check(first, second):
    if len(first) != len(second) or len(first[0]) != len(second[0]):
        raise ValueError(DIFFERENT_DIMENSION)


if __name__ == "__main__":
    main()
