class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("МАтриці мають бути однакового розміру.")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must match the number of rows in the second matrix.")

        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.columns))
        return result

    def determinant(self):
        n = self.rows
        if n == 1:
            return self.data[0][0]
        elif n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        else:
            det = 0
            for j in range(n):
                submatrix = [row[:j] + row[j + 1:] for row in self.data[1:]]
                det += self.data[0][j] * Matrix(submatrix).determinant() * (-1) ** j
            return det

    def inverse_matrix(self):
        n = self.rows
        det = self.determinant()

        if det == 0:
            raise ValueError("Матриця є сингулярною і не має оберненої матриці.")

        adjugate = []
        for i in range(n):
            row = []
            for j in range(n):
                submatrix = [row[:j] + row[j + 1:] for row in (self.data[:i] + self.data[i + 1:])]
                cofactor = Matrix(submatrix).determinant() * (-1) ** (i + j)
                row.append(cofactor)
            adjugate.append(row)

        inverse = [[adjugate[j][i] / det for i in range(n)] for j in range(n)]

        return inverse

def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    rows = len(lines)
    columns = len(lines[0].split())
    matrix = Matrix(rows, columns)

    for i, line in enumerate(lines):
        row = list(map(int, line.split()))
        matrix.data[i] = row

    return matrix


def write_matrix(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix.data:
            file.write(' '.join(map(str, row)) + '\n')



matrix1 = read_matrix('input5.txt')
matrix2 = read_matrix('input6.txt')


result_addition = matrix1.add(matrix2)


write_matrix(result_addition, 'output5.txt')

result_substracion = matrix1.subtract(matrix2)


write_matrix(result_substracion, 'output5.txt')


result_myltiply = matrix1.multiply(matrix2)


write_matrix(result_myltiply, 'output5.txt')





result_inverse = matrix1.inverse_matrix


write_matrix(result_inverse, 'output5.txt')


