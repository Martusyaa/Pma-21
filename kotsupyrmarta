INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'result.txt'
ERROR = 'Error:Matrices are not the same length'
TypeError='Error:Determinant is 0'

class Matrix:
    def __init__(self, data):
        self.rows = len(data)
        self.columns = len(data[0])
        self.data = data
    def read_matrix_from_file(self, input_file):
        matrices = []
        matrix_data = []
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    row = [float(x) for x in line.split()]
                    matrix_data.append(row)
                    if len(matrix_data) == len(matrix_data[0]):
                        matrices.append(self(matrix_data))
                        matrix_data = []
        return matrices

    def matrix_determinant(self):
        num_rows = self.rows
        num_cols = self.columns
        if num_rows != num_cols:
            return None
        if num_rows == 0:
            return ValueError
        if num_rows == 1:
            return self.data[0][0]
        if num_rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        determinant = 0
        for col in range(num_cols):
            sign = (-1) ** col
            sub_matrix_data = [[self.data[i][j] for j in range(num_cols) if j != col] for i in range(1, num_rows)]
            sub_matrix = Matrix(sub_matrix_data)
            sub_determinant = sub_matrix.matrix_determinant()
            determinant += sign * self.data[0][col] * sub_determinant

        return determinant

    def matrix_inverse(self):
        determinant = self.matrix_determinant()
        if determinant == 0:
            return None
        num_rows = self.rows
        num_cols = self.columns
        if num_rows != num_cols:
            return None
        adjugate_data = []
        for i in range(num_rows):
            adjugate_row = []
            for j in range(num_cols):
                sign = (-1) ** (i + j)
                sub_matrix_data = [[self.data[x][y] for y in range(num_cols) if y != j] for x in range(num_rows) if
                                   x != i]
                sub_matrix = Matrix(sub_matrix_data)
                sub_determinant = sub_matrix.matrix_determinant()
                adjugate_row.append(sign * sub_determinant)
            adjugate_data.append(adjugate_row)
        adjugate_matrix = Matrix(adjugate_data)
        inverse_matrix_data = [[elem / determinant for elem in row] for row in adjugate_matrix.data]
        return Matrix(inverse_matrix_data)

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return None
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result_data)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return None
        result_data = [[self.data[i][j] - other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result_data)

    def __mul__(self, other):
        if self.columns != other.rows:
            return None
        result_data = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.columns)) for j in range(other.columns)] for i
            in range(self.rows)]
        return Matrix(result_data)

    def divide(self, other):
        inverse_matrix = other.matrix_inverse()
        if inverse_matrix is None:
            return None
        return self * inverse_matrix
def write_matrix_to_file(OUTPUT_FILE, matrices):
        with open(OUTPUT_FILE, 'a') as file:
            for matrix in matrices:
                if isinstance(matrix, Matrix):
                    for row in matrix.data:
                        row_str = ' '.join(map(str, row))
                        file.write(row_str + "\n")
                else:
                    file.write(str(matrix) + "\n")
matrices = Matrix.read_matrix_from_file(Matrix,INPUT_FILE)
if len(matrices) != 2:
    print(ERROR)
else:
    first_matrix = matrices[0]
    second_matrix = matrices[1]
    determinant_second_matrix = second_matrix.matrix_determinant()
    result_add = first_matrix + second_matrix
    result_subtract = first_matrix - second_matrix
    result_multiply = first_matrix * second_matrix
    result_divide = first_matrix.divide(second_matrix)
results=[]
results.append("Матриця 1:")
results.append(first_matrix)
results.append("Матриця 2:")
results.append(second_matrix)
results.append("Результат додавання:")
results.append(result_add)
results.append("Результат віднімання:")
results.append(result_subtract)
results.append("Результат множення: ")
results.append(result_multiply)
if determinant_second_matrix != 0:
        results.append("Результат ділення: ")
        results.append(result_divide)
else:
        print(TypeError)
write_matrix_to_file(OUTPUT_FILE, results)
