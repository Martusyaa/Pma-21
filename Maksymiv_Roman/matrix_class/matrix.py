class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    @staticmethod
    def zero_matrix(rows, cols):
        return Matrix([[0 for j in range(cols)] for i in range(rows)])

    def print_matrix(self):
        for row in self.data:
            print(row)
        print("\n")

    def add_matrix(self, matrix_second: 'Matrix'):
        if self.cols != matrix_second.cols or self.rows != matrix_second.rows:
            raise ValueError("Матриці повинні бути однакові за розміром")

        result_mat = Matrix.zero_matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result_mat.data[i][j] = self.data[i][j] + matrix_second.data[i][j]

        return result_mat

    def difference_matrix(self, matrix_second: 'Matrix'):
        if self.cols != matrix_second.cols or self.rows != matrix_second.rows:
            raise ValueError("Матриці повинні бути однакові за розміром")

        result_mat = Matrix.zero_matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result_mat.data[i][j] = self.data[i][j] - matrix_second.data[i][j]

        return result_mat

    def multiplication_matrix(self, matrix_second: 'Matrix'):
        if self.cols != matrix_second.rows:
            raise ValueError("Неможливо виконати множення матриць. Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці.")

        result_mat = Matrix.zero_matrix(min(self.rows, matrix_second.rows), min(self.cols, matrix_second.cols))

        for i in range(result_mat.rows):
            for j in range(result_mat.cols):
                for k in range(result_mat.cols):
                    result_mat.data[i][j] += self.data[i][k] * matrix_second.data[k][j]

        return result_mat


    @classmethod
    def determinant(cls, matrix: 'Matrix'):
        n = len(matrix.data)
        if n == 1:
            return matrix.data[0][0]
        elif n == 2:
            return matrix.data[0][0] * matrix.data[1][1] - matrix.data[0][1] * matrix.data[1][0]
        else:
            det = 0
            for i in range(n):
                sub_matrix = Matrix([row[:i] + row[i + 1:] for row in matrix.data[1:]])
                det += matrix.data[0][i] * cls.determinant(sub_matrix) * (-1)**i
            return det

    def matrix_inverse(self):
        rows = self.rows
        cols = self.cols

        if cols != rows:
            raise ValueError("Неможливо знайти обернену матрицю. Кількість стовпців повинна дорівнювати кількості рядків.")

        determinant_value = Matrix.determinant(self)
        if determinant_value == 0:
            raise ValueError("Неможливо знайти обернену матрицю. Визначник дорівнює нулю.")

        inverse_data = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                sub_matrix = Matrix([row[:j] + row[j + 1:] for row in (self.data[:i] + self.data[i + 1:])])
                inverse_data[j][i] = Matrix.determinant(sub_matrix) * (-1)**(i + j) / determinant_value

        inverse_matrix = Matrix(inverse_data)
        return inverse_matrix


    def divide_matrix(self, matrix_second: 'Matrix'):
        result_inverse = matrix_second.matrix_inverse()
        if result_inverse:
            print("Result inverse matrix")
            result_inverse.print_matrix()

            divide_result = self.multiplication_matrix(result_inverse)

            if divide_result:
                for i in range(len(divide_result.data)):
                    for j in range(len(divide_result.data[i])):
                        divide_result.data[i][j] = round(divide_result.data[i][j], 2)
                return divide_result
            else:
                raise ValueError("Ділення неможливе!")

    @staticmethod
    def read_matrix_from_file(filename):
        m = []
        with open(filename, 'r') as file:
            for line in file:
                row = [float(x) for x in line.split()]
                m.append(row)
        matrix = Matrix(m)
        return matrix

    def write_matrix_to_file(self, filename, action):
        with open(filename, 'a+') as file:
            file.write(f"Result of {action}: \n")
            for row in self.data:
                row_str=", ".join(map(str, row))
                file.write(row_str + '\n')
            file.write("\n")