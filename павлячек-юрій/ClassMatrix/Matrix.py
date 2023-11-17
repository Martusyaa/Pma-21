class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.rows])

    def __add__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices must be the same size for addition..")
        result_rows = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, other.rows)]
        return Matrix(result_rows)

    def __sub__(self, other):
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices must have the same size for subtraction.")
        result_rows = [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, other.rows)]
        return Matrix(result_rows)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result_rows = [[a * other for a in row] for row in self.rows]
            return Matrix(result_rows)
        elif isinstance(other, Matrix):
            if len(self.rows[0]) != len(other.rows):
                raise ValueError("columns != rows !")
            result_rows = [[sum(a * b for a, b in zip(row1, col)) for col in zip(*other.rows)] for row1 in self.rows]
            return Matrix(result_rows)
        else:
            raise TypeError("Error !")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result_rows = [[a * other for a in row] for row in self.rows]
            return Matrix(result_rows)
        elif isinstance(other, Matrix):
            if len(self.rows[0]) != len(other.rows):
                raise ValueError("columns != rows !")
            result_rows = [[sum(a / b for a, b in zip(row1, col)) for col in zip(*other.rows)] for row1 in self.rows]
            return Matrix(result_rows)
        else:
            raise TypeError("Error !")

    @classmethod
    def read_from_file(cls, file_path):
        matrices = []
        with open(file_path) as file:
            lines = file.readlines()
            matrix_data = []
            for line in lines:
                if line.strip():
                    components = [int(i) for i in line.strip().split()]
                    matrix_data.append(components)
                else:
                    matrices.append(cls(matrix_data))
                    matrix_data = []
            if matrix_data:
                matrices.append(cls(matrix_data))
        return matrices