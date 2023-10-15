def read_matrix(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            row = [float(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix


def invert_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix must be square for inversion")
    n = len(matrix)
    identity = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1.0
    for i in range(n):
        if matrix[i][i] == 0:
            raise ValueError("Division by zero is impossible")
    for col in range(n):
        max_val = abs(matrix[col][col])
        max_row = col
        for i in range(col + 1, n):
            if abs(matrix[i][col]) > max_val:
                max_val = abs(matrix[i][col])
                max_row = i
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
        identity[col], identity[max_row] = identity[max_row], identity[col]
        pivot = matrix[col][col]
        for j in range(n):
            matrix[col][j] /= pivot
            identity[col][j] /= pivot
        for i in range(n):
            if i != col:
                factor = matrix[i][col]
                for j in range(n):
                    matrix[i][j] -= factor * matrix[col][j]
                    identity[i][j] -= factor * identity[col][j]

    return identity


try:
    matrix1 = read_matrix('first_matrix.txt')
    matrix2 = read_matrix('second_matrix.txt')

    inverted_matrix2 = invert_matrix(matrix2)

    if inverted_matrix2 is not None:
        result = [[0 for _ in range(len(inverted_matrix2[0]))] for _ in range(len(matrix1))]

        for i in range(len(matrix1)):
            for j in range(len(inverted_matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * inverted_matrix2[k][j]

        for row in result:
            print(row)
    else:
        print("Matrix2 doesn't have an inverse.")
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print(f"Mistake: {e}")
