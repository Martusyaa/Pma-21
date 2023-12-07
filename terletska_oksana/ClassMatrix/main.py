FILE_NOT_FOUND_ERROR = 'File not found'
INDEX_ERROR = 'list index ot of range'
ZERO_DIVISION_ERROR = 'division by zero'
TYPE_ERROR = 'NoneType object is not subscriptable'
INPUT_MATRIX_A = 'matrix_first.txt'
INPUT_MATRIX_B = 'matrix_second.txt'
OUT_MATRIX = 'output.txt'


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        try:
            return [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                    range(len(self.matrix))]
        except IndexError:
            print(INDEX_ERROR)
            exit(-1)

    def __sub__(self, other):
        try:
            return [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                    range(len(self.matrix))]
        except IndexError:
            print(INDEX_ERROR)
            exit(-1)

    def __mul__(self, other):
        try:
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    product = 0
                    for v in range(len(self.matrix[i])):
                        product += self.matrix[i][v] * other.matrix[v][j]
                    row.append(product)
                result.append(row)
            return result
        except TypeError:
            print(TYPE_ERROR)
            exit(-1)

    def transpose_matrix(matrix):
        transpose = list(map(list, zip(*matrix)))
        return transpose

    def minor_matrix(matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

    def determinant_matrix(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        determinant = 0
        for c in range(len(matrix)):
            try:
                determinant += ((-1) ** c) * matrix[0][c] * Matrix.determinant_matrix(Matrix.minor_matrix(matrix, 0, c))
            except IndexError:
                print(INDEX_ERROR)
                exit(-1)
        return determinant

    def inverse_matrix(matrix):
        determinant = Matrix.determinant_matrix(matrix)
        if determinant == 0:
            return

        if len(matrix) == 2:
            return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                    [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]
        cofactors = []
        for r in range(len(matrix)):
            cofactor_row = []
            for c in range(len(matrix)):
                minor = Matrix.minor_matrix(matrix, r, c)
                cofactor_row.append(((-1) ** (r + c)) * Matrix.determinant_matrix(minor))
            cofactors.append(cofactor_row)

        result = Matrix.transpose_matrix(cofactors)

        for r in range(len(result)):
            for c in range(len(result)):
                try:
                    result[r][c] = result[r][c] / determinant
                except ZeroDivisionError:
                    print(ZERO_DIVISION_ERROR)
                    exit(-1)
        return result

    def __truediv__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(Matrix.inverse_matrix(other.matrix)[0])):
                product = 0
                for v in range(len(self.matrix[i])):
                    product += self.matrix[i][v] * Matrix.inverse_matrix(other.matrix)[v][j]
                row.append(product)
            result.append(row)
        return result

    def read(filename):
        try:
            with open(filename, 'r') as file:
                matrix = [[float(num) for num in line.split()] for line in file]
            return Matrix(matrix)
        except FileNotFoundError:
            print(FILE_NOT_FOUND_ERROR)
            exit(-1)

    def write(filename, text, matrix):
        try:
            with open(filename, 'a') as file:
                file.write(text)
                file.write(str(matrix))
                file.write('\n')
        except FileNotFoundError:
            print(FILE_NOT_FOUND_ERROR)
            exit(-1)


matrix_a = Matrix.read(INPUT_MATRIX_A)
matrix_b = Matrix.read(INPUT_MATRIX_B)
Matrix.write(OUT_MATRIX, 'Sum of matrix: ', matrix_a.__add__(matrix_b))
Matrix.write(OUT_MATRIX, 'Difference of matrix: ', matrix_a.__sub__(matrix_b))
Matrix.write(OUT_MATRIX, 'Multiplication of matrix: ', matrix_a.__mul__(matrix_b))
Matrix.write(OUT_MATRIX, 'Division of matrix: ', matrix_a.__truediv__(matrix_b))
