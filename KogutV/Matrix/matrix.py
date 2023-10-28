from Validator import *

class Matrix:
    def __init__(self, filename):
        self.data = self.read_from_file(filename)
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                matrix = []
                for line in lines:
                    row = [int(x) for x in line.strip().split()]
                    matrix.append(row)
                return matrix
        except FileNotFoundError:
            print(f"File {filename} is not  found.")
            return

    @validator
    def add(self, other_matrix):
        if len(self.data) != len(other_matrix.data) or len(self.data[0]) != len(other_matrix.data[0]):
            print("Matrices have different sizes and cant be calculated")
            return 

        result = []
        for i in range(len(self.data)):
            result_row = []
            for j in range(len(self.data[0])):
                result_row.append(self.data[i][j] + other_matrix.data[i][j])
            result.append(result_row)

        return result

    @validator
    def subtract(self, other_matrix):
        if len(self.data) != len(other_matrix.data) or len(self.data[0]) != len(other_matrix.data[0]):
            print("Can not perform substracting. Due to difference in size.")
            return 

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other_matrix.data[i][j])
            result.append(row)
        return result

    @validator
    def multiply(self, other_matrix):
        if len(self.data[0]) != len(other_matrix.data):
            print("Can not perform multiplying. Value of columns of first matrix does not match with value of rows of second matrix.")
            return 

        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other_matrix.data[0])):
                row.append(sum(self.data[i][k] * other_matrix.data[k][j] for k in range(len(other_matrix.data))))
            result.append(row)
        return result
    
    def print_matrix(self):
        for row in self.data:
            print(' '.join(map(str, row)))
    
    def inverse(self):
        if self.rows != self.cols:
            raise ValueError("Matrix is not square. Inverse does not exist.")

        n = self.rows
        matrix = [row[:] for row in self.data]
        identity = [[0] * n for _ in range(n)]

        for i in range(n):
            identity[i][i] = 1

        for i in range(n):
            pivot = matrix[i][i]
            if pivot == 0:
                raise ValueError("Matrix does not have a reversed analog")

            for j in range(n):
                matrix[i][j] /= pivot
                identity[i][j] /= pivot

            for k in range(n):
                if k != i:
                    factor = matrix[k][i]
                    for j in range(n):
                        matrix[k][j] -= factor * matrix[i][j]
                        identity[k][j] -= factor * identity[i][j]

        result_matrix = Matrix(None)
        result_matrix.data = identity
        result_matrix.rows = n
        result_matrix.cols = n

        return result_matrix

    def divide(self, other_matrix):
        inverse_other_matrix = other_matrix.inverse()
        if inverse_other_matrix is None:
            raise ValueError("Cannot perform matrix division. The second matrix is singular.")

        if self.cols != inverse_other_matrix.rows:
            raise ValueError("Cannot perform matrix division. Number of columns in the first matrix must be equal to the number of rows in the inverted second matrix.")
        
        result_data = self.multiply(inverse_other_matrix).data
        return Matrix(data=result_data)
    