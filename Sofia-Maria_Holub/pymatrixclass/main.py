class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_element(self, row, col, value):
        self.data[row][col] = value

    def get_element(self, row, col):
        return self.data[row][col]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Error")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_element(i, j, self.get_element(i, j) + other.get_element(i, j))
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Error")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.set_element(i, j, self.get_element(i, j) - other.get_element(i, j))
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Error")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.get_element(i, k) * other.get_element(k, j)
                result.set_element(i, j, dot_product)
        return result

    def __truediv__(self, other):
        return self * other.inverse()

    def inverse(self):
        if self.rows != self.cols:
            raise ValueError("Error")

        determinant = self._determinant(self.data)
        if determinant == 0:
            raise ValueError("Error")

        cofactors = self._cofactor_matrix(self.data)
        adjugate = self._transpose(cofactors)
        self.data = self._scalar_multiply(adjugate, 1 / determinant)
        return self

    def _determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            determinant = 0
            for j in range(n):
                submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
                determinant += matrix[0][j] * ((-1) ** j) * self._determinant(submatrix)
            return determinant

    def _cofactor_matrix(self, matrix):
        n = len(matrix)
        cofactors = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                submatrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
                cofactors[i][j] = ((-1) ** (i + j)) * self._determinant(submatrix)
        return cofactors

    def _transpose(self, matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def _scalar_multiply(self, matrix, scalar):
        return [[scalar * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]


def save_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        file.write(str(matrix))


def read_matrices_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        rows1, cols1 = map(int, lines[0].strip().split())
        matrix_a_lines = lines[1:rows1 + 1]

        rows2, cols2 = map(int, lines[rows1 + 1].strip().split())
        matrix_b_lines = lines[rows1 + 2:]

        matrix_a = Matrix(rows1, cols1)
        matrix_b = Matrix(rows2, cols2)

        for i in range(rows1):
            elements = matrix_a_lines[i].strip().split()
            for j in range(cols1):
                matrix_a.set_element(i, j, float(elements[j]))

        for i in range(rows2):
            elements = matrix_b_lines[i].strip().split()
            for j in range(cols2):
                matrix_b.set_element(i, j, float(elements[j]))

        return matrix_a, matrix_b


def main():
    matrix_a, matrix_b = read_matrices_from_file("matricesClass.txt")

    result_addition = matrix_a + matrix_b
    result_subtraction = matrix_a - matrix_b
    result_multiplication = matrix_a * matrix_b
    result_division = matrix_a / matrix_b

    with open("matrix_resultClass.txt", 'w') as file:
        file.write("Matrix Addition:\n")
        file.write(str(result_addition))
        file.write("\n\nMatrix Subtraction:\n")
        file.write(str(result_subtraction))
        file.write("\n\nMatrix Multiplication:\n")
        file.write(str(result_multiplication))
        file.write("\n\nMatrix Division:\n")
        file.write(str(result_division))


if __name__ == "__main__":
    main()
