INPUT_FILE_MATRIXFIRST = "input_matrixfirst.txt"
INPUT_FILE_MATRIXSECOND = "input_matrixsecond.txt"
OUTPUT_FILE = "output.txt"
FILE_NOT_FOUND = "file not found"
PLUS_MINUS_IS_BROKEN = "Suma and difference can't be"
MULTIPLICATION_ERROR = "Multiplication error"
NEWLINE = "\n"
class Matrix:
    def __init__(self, input_file):
        self.matrix = []
        self.load_matrix(input_file)

    def load_matrix(self, input_file):
        try:
            with open(input_file) as file:
                for line in file:
                    row_matrix = [float(i) for i in line.split()]
                    self.matrix.append(row_matrix)
        except FileNotFoundError:
            print(FILE_NOT_FOUND)

    def add_matrices(self, other_matrix):
        if self.is_compatible_for_operation(other_matrix):
            result_matrix = [[a + b for a, b in zip(row1, row2)] for row1, row2 in
                             zip(self.matrix, other_matrix.matrix)]
            return result_matrix
        else:
            print(PLUS_MINUS_IS_BROKEN)
            return None

    def subtract_matrices(self, other_matrix):
        if self.is_compatible_for_operation(other_matrix):
            result_matrix = [[a - b for a, b in zip(row1, row2)] for row1, row2 in
                             zip(self.matrix, other_matrix.matrix)]
            return result_matrix
        else:
            print(PLUS_MINUS_IS_BROKEN)
            return None

    def is_compatible_for_operation(self, other_matrix):
        return len(self.matrix) == len(other_matrix.matrix) and all(
            len(row1) == len(row2) for row1, row2 in zip(self.matrix, other_matrix.matrix))

    def multiply_matrices(self, other_matrix):
        if self.is_multiplication_compatible(other_matrix):
            result_matrix = [[0 for i in range(len(other_matrix.matrix[0]))] for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other_matrix.matrix[0])):
                    for k in range(len(other_matrix.matrix)):
                        result_matrix[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
            return result_matrix
        else:
            print(MULTIPLICATION_ERROR)
            return None

    def is_multiplication_compatible(self, other_matrix):
        return len(self.matrix[0]) == len(other_matrix.matrix)

    def write_matrix(self, output_file, operation_name, result_matrix):
        try:
            with open(output_file, "a") as file:
                file.write(f"{operation_name} matrix: {str(result_matrix)}{NEWLINE}")
        except FileNotFoundError:
            print(FILE_NOT_FOUND)
