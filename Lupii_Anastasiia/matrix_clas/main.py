class Matrix():
    def __init__(self, rows,cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            if not lines:
                print(f"File '{filename}' is empty.")
                return

            matrix = []

            for line in lines:
                row = [int(num) for num in line.strip().split()]
                matrix.append(row)

            self.data = matrix

        except FileNotFoundError:
            print(f"File '{filename}' is not found")


    def write_to_file(self, filename):
        with open(filename, 'a') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices should have the same dimensions for addition")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices should have the same dimensions for subtraction")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]

        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result

    def shift_element(self, lst, to_front):
        if to_front:
            lst.insert(0, lst.pop())
        else:
            lst.append(lst.pop(0))
    def calculate_determinant_part(self, to_front):
        result = 0
        for j in range(3):
            result_product = 1
            indices = [0, 1, 2]
            for i in range(3):
                result_product *= self.data[indices[j]][i]
                self.shift_element(indices, to_front)
            result += result_product

        return result



    def compute_algebraic_complement(self, row, col):
        submatrix = []
        for i in range(3):
            if i != row:
                subrow = []
                for j in range(3):
                    if j != col:
                        subrow.append(self.data[i][j])
                submatrix.append(subrow)

        determinant = submatrix[0][0] * submatrix[1][1] - submatrix[0][1] * submatrix[1][0]
        sign = 1 if (row + col) % 2 == 0 else -1
        return sign * determinant

    def transpose_matrix(self, data, determinant):
        transposed = []
        for i in range(3):
            transposed_row = []
            for j in range(3):
                transposed_row.append(data[j][i] / determinant)
            transposed.append(transposed_row)
        return transposed
    def inverse_matrix(self,other):
        determinant_self = self.calculate_determinant_part(False)
        determinant_other = other.calculate_determinant_part(True)

        if determinant_self == 0:
            raise ValueError("The matrix is singular and does not have an inverse.")

        determinant = determinant_self - determinant_other
        algebraicted_computed_matrix = [
            [
                self.compute_algebraic_complement( 0, 0),
                self.compute_algebraic_complement(0, 1),
                self.compute_algebraic_complement(0, 2)
            ],
            [
                self.compute_algebraic_complement( 1, 0),
                self.compute_algebraic_complement( 1, 1),
                self.compute_algebraic_complement( 1, 2)
            ],
            [
                self.compute_algebraic_complement( 2, 0),
                self.compute_algebraic_complement( 2, 1),
                self.compute_algebraic_complement( 2, 2)
            ]
        ]

        result = self.transpose_matrix(algebraicted_computed_matrix, determinant)
        return result

    def division(self, other):
        inverse_matrix_second = self.inverse_matrix(other)

        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * inverse_matrix_second[k][j]

        return result.data


matrix_first = Matrix(3, 3)
matrix_second = Matrix(3, 3)

try:
    matrix_first.read_from_file('first_matrix.txt')
    matrix_second.read_from_file('second_matrix.txt')

    result_addition = matrix_first.add(matrix_second)
    result_subtraction = matrix_first.subtract(matrix_second)
    result_multiplication = matrix_first.multiply(matrix_second)
    result_division = matrix_first.division(matrix_second)

    result_addition.write_to_file('result.txt')
    result_subtraction.write_to_file('result.txt')
    result_multiplication.write_to_file('result.txt')

    result_division_matrix = Matrix(3, 3)
    result_division_matrix.data = result_division

    # Write the result_division_matrix to the file
    result_division_matrix.write_to_file('result.txt')

except ValueError as e:
    print(f"An error occurred: {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")