import random
#змінні and constants #завдання
#operations #завдання
#print() # завдання
#input() #завдання
#if else elif #завдання
#range
#for while
#comments
#import
#file(with open)
#functions def(1,2,3,4,5)
#list,set,tuple,dictionary #можна поки пропустити все крім ліста
#matrix
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


class Matrix:

    def __init__(self, row, column):
        self.rows = row
        self.columns = column
        self.matrix = []
        self.fulfill_matrix()

    def print_matrix(self):
        for r in self.matrix:
            for c in r:
                print(c, end="\t")
            print()

    def fulfill_matrix(self):
        self.matrix.clear()
        for r in range(self.rows):
            row_in_matrix = []
            for c in range(self.columns):
                value = random.randint(1, 10)
                row_in_matrix.append(value)
            self.matrix.append(row_in_matrix)

    def check_for_add_and_sub(self,matrix_to_act):
        if len(self.matrix) != len(matrix_to_act.matrix):
            err = "You`re matrix are not equal! (row)"
            raise Exception(err)

        if len(self.matrix[0]) != len(matrix_to_act.matrix[0]):
            raise Exception("You`re matrix are not equal! (columns)")

    def add(self,matrix_to_add):
        self.check_for_add_and_sub(matrix_to_add)
        result = []

        for row in range(len(self.matrix)):
            list_to_result = []
            for column in range(len(self.matrix[row])):
                element_in_list_to_result = self.matrix[row][column] + matrix_to_add.matrix[row][column]
                list_to_result.append(element_in_list_to_result)
            result.append(list_to_result)

        self.matrix.clear()
        for row in matrix_to_add.matrix:
            self.matrix.append(row)

    def subtract(self,matrix_to_subtract):
        self.check_for_add_and_sub(matrix_to_subtract)
        result = []

        for row in range(len(self.matrix)):
            list_to_result = []
            for column in range(len(self.matrix[row])):
                element_in_list_to_result = self.matrix[row][column] - self.matrix[row][column]
                list_to_result.append(element_in_list_to_result)
            result.append(list_to_result)

        self.matrix.clear()
        for row in result:
            self.matrix.append(row)

    def check_matrix_multiply(self,matrix_to_act):
        if len(self.matrix[0]) != len(matrix_to_act.matrix):
            raise Exception("Matrix1 columns aren`t equal to Matrix2 rows!")

    def multiply(self,matrix_to_multiply):
        self.check_matrix_multiply(matrix_to_act=matrix_to_multiply)



        







m = Matrix(row=3, column=3)
m.fulfill_matrix()
m1= Matrix(row=3,column=1)
m.print_matrix()
m1.print_matrix()
m.check_for_add_and_sub(m1)
