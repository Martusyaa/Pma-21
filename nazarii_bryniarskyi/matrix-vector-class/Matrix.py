import os.path

class Matrix:
    MATRIX_ERROR = "Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці."
    DETERMINANT_ERROR = "Детермінант дорівнює нулю"
    SEPARATOR = ','
    DEFAULT_MATRIX = [[0, 0], [0, 0]]

    def __init__(self, matrix_file):
        self.matrix_file = matrix_file
        self.matrix = self._get_matrix_from_file()

    def _get_matrix_from_file(self):
        if not os.path.isfile(self.matrix_file):
            return self.DEFAULT_MATRIX

        with open(self.matrix_file) as file:
            matrix = [[int(num) for num in line.split(self.SEPARATOR)] for line in file]

        return matrix

    @staticmethod
    def write_matrix_to_file(matrix, file_name):
        with open(file_name, 'w') as file:
            for row in matrix:
                file.write(','.join(map(str, row)) + '\n')

    def _check_matrix_dimensions(self, other):
        if len(self.matrix[0]) != len(other.matrix) or len(self.matrix) != len(other.matrix[0]):
            raise ValueError(self.MATRIX_ERROR)

    def __add__(self, other):
        self._check_matrix_dimensions(other)
        result = []

        for i in range(len(self.matrix)):
            row = []

            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])

            result.append(row)

        return result

    def __sub__(self, other):
        self._check_matrix_dimensions(other)
        result = []

        for i in range(len(self.matrix)):
            row = []

            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other.matrix[i][j])

            result.append(row)

        return result

    def transposeMatrix(self, m):
        return [list(row) for row in zip(*m)]

    def getMatrixMinor(self, m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def getMatrixDeterminant(self, m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.getMatrixDeterminant(self.getMatrixMinor(m, 0, c))
        return determinant

    def getMatrixInverse(self, m):
        determinant = self.getMatrixDeterminant(m)
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMatrixMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * self.getMatrixDeterminant(minor))
            cofactors.append(cofactorRow)
        cofactors = self.transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(self.MATRIX_ERROR)

        result = []

        for i in range(len(self.matrix)):
            row = []

            for j in range(len(other.matrix[0])):
                dot_product = sum(self.matrix[i][a] * other.matrix[a][j] for a in range(len(self.matrix[0])))
                row.append(dot_product)

            result.append(row)

        return result

    def __truediv__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(self.MATRIX_ERROR)

        determinant_other = self.getMatrixDeterminant(other.matrix)

        if determinant_other == 0:
            return -1

        result = []
        inverted_matrix = self.getMatrixInverse(other.matrix)
        current_matrix = self.matrix

        for i in range(len(self.matrix)):
            row = []

            for j in range(len(inverted_matrix[0])):
                dot_product = sum(current_matrix[i][a] * inverted_matrix[a][j] for a in range(len(current_matrix[0])))
                row.append(dot_product)

            result.append(row)

        return result
