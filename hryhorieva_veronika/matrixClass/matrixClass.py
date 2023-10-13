INPUT_FILE_NAME= "../../../learning/matrix/input.txt"
OUTPUT_FILE_NAME= "../../../learning/matrix/output.txt"
start_index=0
import random
import numpy as np
class Matrix:
    def __init__(self):

        self.matrix=[]
        self.read_matrix_from_file()



    def read_matrix_from_file(self):
        global start_index
        with open(INPUT_FILE_NAME, "r+") as file:
            file_lines = file.readlines()
            quantity_of_lengths = len(file_lines)
            if start_index >= len(file_lines):
                return
            else:
                lines = file_lines[start_index].replace("\n", "")
                array = [int(x) for x in lines.split(",") if x.isdigit()]
                if len(array) == 0:
                    start_index += 1
                    return
                else:
                    self.matrix.append(array)
                    start_index += 1

                return self.read_matrix_from_file()

    def write_matrix_in_file(self):
        with open(OUTPUT_FILE_NAME, "a") as file:
            for rows in self.matrix:
                for element in rows:
                    file.write(str(element) + ",")
                file.write("\n")
            file.write("\n")

    def summary_matrix(self, matrix_second):
        if len(self.matrix) != len(matrix_second.matrix) or len(self.matrix[0]) != len(matrix_second.matrix[0]):
            error = "ERROR! rows1!=rows2 or colluns1!=colluns2"
            raise Exception(error)
        for row in range(len(self.matrix)):
            for collon in range(0, len(self.matrix[0])):
                self.matrix[row][collon] += matrix_second.matrix[row][collon]

    def minus_matrix(self, matrix_second):
        if len(self.matrix) != len(matrix_second.matrix) or len(self.matrix[0]) != len(matrix_second.matrix[0]):
            error = "ERROR! rows1!=rows2 or colluns1!=colluns2"
            raise Exception(error)
        for row in range(len(self.matrix)):
            for collon in range(0, len(self.matrix[0])):
                self.matrix[row][collon] -= matrix_second.matrix[row][collon]

    def multiplication_matrix(self, matrix_second):
        if len(self.matrix[0]) != len(matrix_second.matrix):
            error = "ERROR! rows1!=colluns2"
            raise Exception(error)
        result = []
        for row_first_matrix in range(len(self.matrix)):
            matrixResult = []
            for collon_second_matrix in range(0, len(matrix_second.matrix[0])):
                value = 0
                for collonFirst_rowSecond in range(0, len(matrix_second.matrix)):
                    value += self.matrix[row_first_matrix][collonFirst_rowSecond] * matrix_second.matrix[collonFirst_rowSecond][collon_second_matrix]
                matrixResult.append(value)
            result.append(matrixResult)
        self.matrix.clear()
        for row in result:
            self.matrix.append(row)

    def division_matrix(self,matrix_second):
         if len(self.matrix[0]) != len(matrix_second.matrix):
            error = "ERROR! rows1!=colluns2"
            raise Exception(error)
         matrix2_reversed = np.linalg.inv(matrix_second.matrix).round(2)
         matrix1_new = np.matmul(self.matrix, matrix2_reversed)
         matrix1_new = matrix1_new.round(2)
         self.matrix.clear()
         for row in matrix1_new:
            self.matrix.append(row)

matrix_first=Matrix()
matrix_first.write_matrix_in_file()

print("Matrix1 is ")
matrix_first.print_matrix()

matrix_second=Matrix()
print("Matrix2 is ")
matrix_second.print_matrix()
matrix_second.write_matrix_in_file()

#Summary
# print("Summary is ")
# matrix_first.summary_matrix(matrix_second)
# matrix_first.print_matrix()
# matrix_first.write_matrix_in_file()

#Multiplication
print("Multiplication is ")
matrix_first.multiplication_matrix(matrix_second)
matrix_first.print_matrix()
matrix_first.write_matrix_in_file()

#Division
# print("Division is ")
# matrix_first.division_matrix(matrix_second)
# matrix_first.print_matrix()
# matrix_first.write_matrix_in_file()
#Minus
# print("Minus is ")
# matrix_first.minus_matrix(matrix_second)
# matrix_first.print_matrix()
# matrix_first.write_matrix_in_file()