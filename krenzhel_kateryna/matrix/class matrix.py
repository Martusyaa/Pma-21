import random

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"
FILE_NOT_FOUND = "File not found"
NOT_DIVISION = "Not Division."
class Matrices:
    def __init__(self):
        try:
            with open(INPUT_FILE_NAME, 'r') as file:
                self.number = [int(i) for i in file.readline().split()]
            with open(INPUT_FILE_NAME, 'r') as file:
                self.first_matrix = [[int(i) for i in file.readline().split()] for i in range(len(self.number))]
                self.second_matrix = [[int(i) for i in file.readline().split()] for i in range(len(self.number))]
        except FileNotFoundError:
            print(FILE_NOT_FOUND, INPUT_FILE_NAME)
            self.first_matrix = [[random.randint(1, 11) for j in range(3)] for i in range(3)]
            self.second_matrix = [[random.randint(1, 11) for j in range(3)] for i in range(3)]
            self.number = self.first_matrix[0]

        self.sum_matrix = self.sum()
        self.subtraction_matrix = self.subtraction()
        self.multiplication_matrix = self.multiplication(self.first_matrix, self.second_matrix)
        self.division_matrix = self.division(self.first_matrix, self.second_matrix)

    def print_matrix(self, file, first_matrix, second_matrix, result_matrix, operation):
        for i in range(len(first_matrix)):
            if i == len(first_matrix) // 2:
                print(f"{first_matrix[i]} {operation} {second_matrix[i]} = {result_matrix[i]}", file=file)
            else:
                print(f"{first_matrix[i]}   {second_matrix[i]}   {result_matrix[i]}", file=file)
        file.write('\n')

    def print(self):
        print("\nFirst matrix:")
        for i in range(len(self.number)):
            print(self.first_matrix[i])
        print('\nSecond matrix:')
        for i in range(len(self.number)):
            print(self.second_matrix[i])
        print('\nSum matrix:')
        for i in range(len(self.number)):
            print(self.sum_matrix[i])
        print('\nSubtraction matrix:')
        for i in range(len(self.number)):
            print(self.subtraction_matrix[i])
        print('\nMultiplication matrix:')
        for i in range(len(self.number)):
            print(self.multiplication_matrix[i])
        print('\nDivision matrix:')
        for i in range(len(self.number)):
            print(self.division_matrix[i])
        with open(OUTPUT_FILE_NAME, 'w') as file:
            self.print_matrix(file, self.first_matrix, self.second_matrix, self.sum_matrix, '+')
            self.print_matrix(file, self.first_matrix, self.second_matrix, self.subtraction_matrix, '-')
            self.print_matrix(file, self.first_matrix, self.second_matrix, self.multiplication_matrix, '*')
            self.print_matrix(file, self.first_matrix, self.second_matrix, self.division_matrix, '/')

    def sum(self):
        sum = [[self.first_matrix[i][j] + self.second_matrix[i][j] for j in range(len(self.number))] for i in range(len(self.number))]
        return sum
    def subtraction(self):
        subtraction = [[self.first_matrix[i][j] - self.second_matrix[i][j] for j in range(len(self.number))] for i in range(len(self.number))]
        return subtraction
    def multiplication(self, first_matrix, second_matrix):
        multiplication = [[0 for j in range(len(self.number))] for i in range(len(self.number))]
        for i in range(len(self.number)):
            for j in range(len(self.number)):
                for k in range(len(self.number)):
                    multiplication[i][j] += first_matrix[i][k] * second_matrix[k][j]
        return multiplication

    def determinant(self, matrix):  # Функція для обчислення визначника матриці
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif len(matrix) == 3:
            return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                    matrix[0][1] * matrix[1][2] * matrix[2][0] +
                    matrix[1][0] * matrix[0][2] * matrix[2][1] -
                    matrix[2][0] * matrix[1][1] * matrix[0][2] -
                    matrix[0][0] * matrix[2][1] * matrix[1][2] -
                    matrix[1][0] * matrix[0][1] * matrix[2][2])
        else:
            det = 0
            for j in range(n):
                minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
                det += matrix[0][j] * ((-1) ** j) * self.determinant(minor)
            return det

    def cofactor_matrix(self, matrix):  # Функція для обчислення матриці алгебраїчних доповнень
        n = len(matrix)
        cofactors = []
        for i in range(n):
            cofactor_row = []
            for j in range(n):
                minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
                cofactor = ((-1) ** (i + j)) * self.determinant(minor)
                cofactor_row.append(cofactor)
            cofactors.append(cofactor_row)
        return cofactors

    def transpose(self, matrix):  # Функція для транспонування матриці
        n = len(matrix)
        m = len(matrix[0])
        transposed = []
        for j in range(m):
            transposed_row = [matrix[i][j] for i in range(n)]
            transposed.append(transposed_row)
        return transposed


    # Calculate the inverse of a matrix
    def inverse_matrix(self,matrix):
        det = self.determinant(matrix)
        if det == 0:
            inverse = NOT_DIVISION
        else:
            cofactors = self.cofactor_matrix(matrix)
            adjugate = self.transpose(cofactors)
            inverse = [[element / det for element in row] for row in adjugate]
        return inverse

    # Divide two matrices
    def division(self,first_matrix, second_matrix):
        try:
            inverse_second_matrix = self.inverse_matrix(second_matrix)
            if inverse_second_matrix == NOT_DIVISION:
                division_result = NOT_DIVISION
            else:
                division_result = self.multiplication(first_matrix, inverse_second_matrix)
        except ZeroDivisionError:
            division_result = NOT_DIVISION
        return division_result

obj = Matrices()
obj.print()
