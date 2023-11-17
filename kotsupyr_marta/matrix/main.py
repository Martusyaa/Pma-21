INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'
ERROR = "Error: Потрібно зчитати дві матриці з файлу."
TypeError="Error: Детермінант другої матриці дорівнює 0."
def read_two_matrices_from_file(INPUT_FILE):
    matrices = []
    matrix = []
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                row = [float(x) for x in line.split()]
                matrix.append(row)
                if len(matrix) == len(matrix[0]):
                    matrices.append(matrix)
                    matrix = []
    return matrices
def write_matrix_to_file(OUTPUT_FILE, matrix):
    with open(OUTPUT_FILE, 'a') as file:
        for row in matrix:
            if row is not None:
                row_str = ''
                for number in row:
                    row_str += str(number) + ''
                file.write(row_str.strip()+ "\n")
def add_matrices(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        return None
    result = []
    for i in range(len(first_matrix)):
        row = [x + y for x, y in zip(first_matrix[i], second_matrix[i])]
        result.append(row)
    return result
def subtract_matrices(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        return None
    result = []
    for i in range(len(first_matrix)):
        row = [x - y for x, y in zip(first_matrix[i], second_matrix[i])]
        result.append(row)
    return result
def mult_matrices(first_matrix,second_matrix):
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        return None
    result=[]
    for i in range(len(first_matrix)):
        temp=[]
        for j in range(len(second_matrix[0])):
            total=0
            for k in range (len(second_matrix)):
                total+=first_matrix[i][k]*second_matrix[k][j]
            temp.append(total)
        result.append(temp)
    return result
def matrix_determinant(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if num_rows != num_cols:
        return None
    if num_rows == 1:
        return matrix[0][0]
    if num_rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for col in range(num_cols):
        sign = (-1) ** col
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        sub_determinant = matrix_determinant(sub_matrix)
        determinant += sign * matrix[0][col] * sub_determinant
    return determinant
def matrix_inverse(matrix):
    determinant = matrix_determinant(matrix)
    if determinant == 0:
        return None
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if num_rows != num_cols:
        return None
    adjugate_matrix = []
    for i in range(num_rows):
        adjugate_row = []
        for j in range(num_cols):
            sign = (-1) ** (i + j)
            sub_matrix = [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
            sub_determinant = matrix_determinant(sub_matrix)
            adjugate_row.append(sign * sub_determinant)
        adjugate_matrix.append(adjugate_row)
    inverse_matrix = [[elem / determinant for elem in row] for row in adjugate_matrix]
    return inverse_matrix
def divide_matrices(first_matrix, second_matrix):
    num_cols_first_matrix = len(first_matrix[0])
    num_rows_second_matrix = len(second_matrix)
    if num_cols_first_matrix != num_rows_second_matrix:
        return None
    determinant = matrix_determinant(second_matrix)
    if determinant == 0:
        return None
    second_matrix_inverse = matrix_inverse(second_matrix)
    if second_matrix_inverse is None:
        return None
    result = [[0 for _ in range(num_cols_first_matrix)] for _ in range(len(first_matrix))]
    for i in range(len(first_matrix)):
        for j in range(num_cols_first_matrix):
            for k in range(len(second_matrix_inverse)):
                result[i][j] += first_matrix[i][k] * second_matrix_inverse[k][j]
    return result
matrices = read_two_matrices_from_file(INPUT_FILE)
if len(matrices) != 2:
    print(ERROR)
else:
    first_matrix = matrices[0]
    second_matrix = matrices[1]
    determinant_second_matrix = matrix_determinant(second_matrix)
    results = []
    results.append("Матриця 1:")
    results.append(first_matrix)
    results.append("Матриця 2:")
    results.append(second_matrix)
    result_add = add_matrices(first_matrix, second_matrix)
    results.append("Результат додавання:")
    results.append(result_add)
    result_subtract = subtract_matrices(first_matrix, second_matrix)
    results.append("Результат віднімання:")
    results.append(result_subtract)
    result_mult = mult_matrices(first_matrix, second_matrix)
    results.append("Результат множення: ")
    results.append(result_mult)
    if determinant_second_matrix != 0:
        result_div = divide_matrices(first_matrix, second_matrix)
        results.append("Результат ділення: ")
        results.append(result_div)
    else:
        print(TypeError)
    write_matrix_to_file(OUTPUT_FILE, results)
