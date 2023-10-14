class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            row_str = " ".join(map(str, row))
            matrix_str += f"{row_str}\n"
        return matrix_str

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матриці мають різні розміри і не можуть бути додані разом.")
        result = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матриці мають різні розміри і не можуть бути відняті одна від одної.")
        result = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Кількість стовпців першої матриці недорівнює кількості рядків другої матриці.")
        result = [[0] * other.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Ділення на нуль неможливе.")
        result = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.matrix[i][j] / scalar
        return Matrix(result)
    @classmethod
    def from_file (cls, filename):
        matrix = []
        with open(filename) as file:
            for line in file:
                row = [int(x) for x in line.strip().split()]
                matrix.append(row)
        return cls(matrix)

    def to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.matrix:
                file.write(' '.join(map(str, row)) + '\n')

matrix_a = Matrix.from_file('matrix_a.txt')
matrix_b = Matrix.from_file('matrix_b.txt')

print("Матриця A:")
print(matrix_a)
print("\nМатриця B:")
print(matrix_b)
result_addition = matrix_a + matrix_b
print("\nДодавання матриць A і B:")
print(result_addition)
result_subtraction = matrix_a - matrix_b
print("\nВіднімання матриць A і B:")
print(result_subtraction)
result_multiplication = matrix_a * matrix_b
print("\nМноження матриць A і B:")
print(result_multiplication)
result_division = matrix_a / 2
print("\nДілення матриці A на скаляр 2:")
print(result_division)
