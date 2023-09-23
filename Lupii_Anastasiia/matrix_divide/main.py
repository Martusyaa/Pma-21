def read_matrix_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    matrix = []

    for line in lines:
        row = [int(num) for num in line.strip().split()]
        matrix.append(row)

    return matrix


def write_matrix_to_file(matrix, file):
    for row in matrix:
        file.write(' '.join(map(str, row)) + '\n')


def write_matrices_and_result(matrix1, matrix2, result):
    with open("result.txt", "a" , encoding="utf-8") as file:
        file.write("Matrix first:\n")
        write_matrix_to_file(matrix1, file)

        file.write("\n Matrix second:\n")
        write_matrix_to_file(matrix2, file)

        file.write("\nDivision:\n")
        write_matrix_to_file(result, file)

def write_matrices_and_result_mult(matrix_first, matrix_second, result):
    with open("result.txt", "a" , encoding="utf-8") as file:
        file.write("Matrix first:\n")
        write_matrix_to_file(matrix_first, file)

        file.write("\n Matrix second:\n")
        write_matrix_to_file(matrix_second, file)

        file.write("\nMultiplication:\n")
        write_matrix_to_file(result, file)

def shift_element(lst, to_front):
    if to_front:
        lst.insert(0, lst.pop())
    else:
        lst.append(lst.pop(0))


def calculate_determinant_part(matrix, to_front):
    try:
        result = 0
        for j in range(3):
            result_product = 1
            indices = [0, 1, 2]
            print('--------')
            for i in range(3):
                result_product *= matrix[indices[j]][i]
                print('element', matrix[indices[j]][i], ' index:', indices[j], i)
                shift_element(indices, to_front)
            result += result_product
        print(result)
        if result == 0:
            print("Error: Determinant is zero, and division by zero is not allowed.")
            return None

        return result
    except IndexError:
        print("Error: Index out of range while accessing the matrix.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def compute_algebraic_complement(matrix, row, col):
    submatrix = []
    for i in range(3):
        if i != row:
            subrow = []
            for j in range(3):
                if j != col:
                    subrow.append(matrix[i][j])
            submatrix.append(subrow)

    determinant = submatrix[0][0] * submatrix[1][1] - submatrix[0][1] * submatrix[1][0]
    sign = 1 if (row + col) % 2 == 0 else -1
    return sign * determinant


def transpose_matrix(matrix, determinant):
    transposed = []
    for i in range(3):
        transposed_row = []
        for j in range(3):
            transposed_row.append(matrix[j][i]/determinant)
        transposed.append(transposed_row)
    return transposed

def inverse_matrix(matrix):
    determinant= calculate_determinant_part(matrix, False) - calculate_determinant_part(matrix, True)

    algebraicted_computed_matrix = [
        [
            compute_algebraic_complement(matrix, 0, 0),
            compute_algebraic_complement(matrix, 0, 1),
            compute_algebraic_complement(matrix, 0, 2)
        ],
        [
            compute_algebraic_complement(matrix, 1, 0),
            compute_algebraic_complement(matrix, 1, 1),
            compute_algebraic_complement(matrix, 1, 2)
        ],
        [
            compute_algebraic_complement(matrix, 2, 0),
            compute_algebraic_complement(matrix, 2, 1),
            compute_algebraic_complement(matrix, 2, 2)
        ]
    ]

    result = transpose_matrix(algebraicted_computed_matrix, determinant)
    return result


def multiply(matrix_first, matrix_second):
    result = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix_first[i][k] * matrix_second[k][j]


    return result
def divide_matrices(matrix_first, matrix_second):
    inverse_matrix_second = inverse_matrix(matrix_second)
    result = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix_first[i][k] * inverse_matrix_second[k][j]


    return result

matrix_first = read_matrix_from_file("first_matrix.txt")
matrix_second = read_matrix_from_file('second_matrix.txt')
result = divide_matrices(matrix_first, matrix_second)
write_matrices_and_result(matrix_first, matrix_second, result)
result_mult = multiply(matrix_first, matrix_second)
write_matrices_and_result_mult(matrix_first,matrix_second,result_mult)

# matrix = [
#         [4, 2, 3],
#         [7, 5, 3],
#         [9, 4, 6]]
# calculate_determinant_part(matrix,False)
# print('re')
# m_d = ['00','11','22']
# c_t1 = ['10','21','02']
# c_t2 = ['20','01','12']

# 1 ітерація
# j = 0, i = 0
# indices = [0, 1, 2]
# result_product *= matrix[0][0]

# 2 ітерація
# j = 0, i = 1
# indices = [ 1, 2, 0]
# result_product *= matrix[1][1]

# 3 ітерація
# j = 0, i = 1
# indices = [ 2, 0, 1,]
# result_product *= matrix[2][2]

# 4 ітерація
# j = 1, i = 0
# indices = [0, 1, 2]
# result_product *= matrix[1][0]

# 5 ітерація
# j = 1, i = 1
# indices = [ 1, 2,0,]
# result_product *= matrix[2][1]