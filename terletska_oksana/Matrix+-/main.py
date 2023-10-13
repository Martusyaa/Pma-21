MATRIX_FIRST = "matrix_first.txt"
MATRIX_SECOND = "matrix_second.txt"
OUTPUT_TXT = "output.txt"
FILE_NOT_FOUND = "File not found"
try:
    with open(MATRIX_FIRST, 'r') as f:
        M1 = [[int(num) for num in line.split(' ')] for line in f]
    print(M1)
except FileNotFoundError:
    print(FILE_NOT_FOUND, MATRIX_FIRST)

try:
    with open(MATRIX_SECOND, 'r') as f:
        M2 = [[int(num) for num in line.split(' ')] for line in f]
    print(M2)
except FileNotFoundError:
    print(FILE_NOT_FOUND, MATRIX_SECOND)

M3 = [[0 for _ in range(len(M1[0]))] for _ in range(len(M1))]
M4 = [[0 for _ in range(len(M1[0]))] for _ in range(len(M1))]
M5 = [[0 for _ in range(len(M1[0]))] for _ in range(len(M1))]

try:
#Додавання
    for i in range(len(M1)):
        for k in range(len(M2)):
             M3[i][k] = M1[i][k] + M2[i][k]

    print("The sum of Matrix1 and Matrix2:")
    for d in M3:
        print(d)

#Віднімання
    for i in range(len(M1)):
        for k in range(len(M2)):
            M4[i][k] = M1[i][k] - M2[i][k]

    print("The difference of Matrix M1 and M2:")
    for d in M4:
        print(d)

#Множення
    for u in range(len(M1)):
        for o in range(len(M2[0])):
            for p in range(len(M2)):
                M5[u][o] += M1[u][p] * M2[p][o]

    print("The multiplication of matrix M1 and M2:")
    for d in M5:
        print(d)

except IndexError:
    print("Довжини різні")

#Ділення
def read_matrix(file_name):
    matrix = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                row = [float(x) for x in line.strip().split()]
                matrix.append(row)
        return matrix
    except FileNotFoundError:
        print(FILE_NOT_FOUND, MATRIX_SECOND," OR ", MATRIX_FIRST)
def inverse_matrix(matrix):
    n = len(matrix)
    identity = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for col in range(n):
        diagonal_element = matrix[col][col]
        for j in range(n):
            matrix[col][j] /= diagonal_element
            identity[col][j] /= diagonal_element
        for row in range(n):
            if row != col:
                factor = matrix[row][col]
                for j in range(n):
                    matrix[row][j] -= factor * matrix[col][j]
                    identity[row][j] -= factor * identity[col][j]
    return identity

matrix_A = read_matrix('matrix_first.txt')
matrix_B = read_matrix('matrix_second.txt')

inverse_B = inverse_matrix(matrix_B)
print(inverse_B)

M6 = [[sum(matrix_A[i][k] * inverse_B[k][j] for k in range(len(matrix_A[0]))) for j in range(len(inverse_B[0]))] for
          i in range(len(matrix_A))]

print("The division of Matrix1 and Matrix2:")
for row in M6:
    print(row)


try:
    with open("output.txt", "w") as f:

        f.write("The sum of Matrix1 and Matrix2:\n")
        for row in M3:
            f.write(" ".join(map(str, row)) + "\n")

        f.write("\nThe difference of Matrix M1 and M2:\n")
        for row in M4:
            f.write(" ".join(map(str, row)) + "\n")

        f.write("\nThe multiplication of Matrix M1 and M2:\n")
        for row in M5:
            f.write(" ".join(map(str, row)) + "\n")

        f.write("The division of Matrix1 and Matrix2:\n")
        for row in M3:
            f.write(" ".join(map(str, row)) + "\n")

except FileNotFoundError:
    print(FILE_NOT_FOUND, OUTPUT_TXT)


"""
1 3 2
2 3 1
3 1 2
"""


#Множення
"""
def matrix_multiplication(M1, M2):
    rows_M1 = len(M1)
    cols_M1 = len(M1[0])
    rows_M2 = len(M2)
    cols_M2 = len(M2[0])

    if cols_M1 != rows_M2:
        print("Неможна множити.")
        return None

    result = [[0 for _ in range(cols_M2)] for _ in range(rows_M1)]

    for i in range(rows_M1):
        for j in range(cols_M2):
            for k in range(cols_M1):
                result[i][j] += M1[i][k] * M2[k][j]

    return result

#A = [[1, 2, 3], [4, 3, 3], [-1, 3, 2]]
#B = [[2, 7, 3], [3, 9, 4], [1, 5, 3]]

result = matrix_multiplication(M1, M2)

print('The multiplication of matrix A and B :')
if result is not None:
    for row in result:
        print(row) """