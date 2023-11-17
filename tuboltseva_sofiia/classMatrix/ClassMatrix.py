INPUT_FILE_NAME = 'inpytM.txt'
class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.elements])

    def elementwise_add(self, other):
        if len(self.elements) != len(other.elements) or len(self.elements[0]) != len(other.elements[0]):
            raise ValueError("Матриці мають мати однакові розміри для додавання")

        result_elements = []

        for i in range(len(self.elements)):
            row = []
            for j in range(len(self.elements[0])):
                row.append(self.elements[i][j] + other.elements[i][j])
            result_elements.append(row)

        return result_elements

    def elementwise_subtract(self, other):
        if len(self.elements) != len(other.elements) or len(self.elements[0]) != len(other.elements[0]):
            raise ValueError("Матриці мають мати однакові розміри для віднімання")

        result_elements = []

        for i in range(len(self.elements)):
            row = []
            for j in range(len(self.elements[0])):
                row.append(self.elements[i][j] - other.elements[i][j])
            result_elements.append(row)

        return result_elements

    def elementwise_multiply(self, other):
        if len(self.elements[0]) != len(other.elements):
            raise ValueError("Кількість стовпців першої матриці має дорівнювати кількості рядків другої матриці.")

        result = []
        for i in range(len(self.elements)):
            row = [0] * len(other.elements[0])
            result.append(row)

        for i in range(len(self.elements)):
            for j in range(len(other.elements[0])):
                for k in range(len(self.elements[0])):
                    if other.elements[k][j] == 0:
                        raise ZeroDivisionError("Помилка: Ділення на 0")

                    result[i][j] += self.elements[i][k] * other.elements[k][j]

        return result

    def matrix_inverse(self):
        if len(self.elements) != len(self.elements[0]):
            raise ValueError("Обернена матриця може бути знайдена лише для квадратної матриці.")

        det = self.determinant()
        if det == 0:
            raise ValueError("Матриця не має оберненої матриці (детермінант дорівнює 0).")

        inv_det = 1.0 / det

        result_elements = [
            [
                ((self.elements[i][j] * self.cofactor(i, j).determinant()) * (-1) ** (i + j)) * inv_det
                for j in range(len(self.elements[i]))
            ]
            for i in range(len(self.elements))
        ]

        return Matrix(result_elements)

    def determinant(self):
        if len(self.elements) == 2:
            return self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0]

        det = 0
        for i in range(len(self.elements)):
            cofactor = self.cofactor(0, i)
            det += self.elements[0][i] * cofactor.determinant() * (-1) ** i
        return det

    def cofactor(self, row, col):
        sub_matrix = [
            [self.elements[i][j] for j in range(len(self.elements[i])) if j != col]
            for i in range(len(self.elements)) if i != row
        ]
        return Matrix(sub_matrix)

    def elementwise_divide(self, other):
        inv_other = other.matrix_inverse()
        if inv_other:
            result_elements = [
                [
                    sum(a * b for a, b in zip(row1, col2))
                    for col2 in zip(*inv_other.elements)
                ]
                for row1 in self.elements
            ]
            return result_elements
        else:
            raise ValueError("Ділення на нуль неможливе або обернена матриця не існує.")

try:
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found: ", INPUT_FILE_NAME)
    exit()

matrix1 = []
matrix2 = []

try:
    for line in lines:
        values = line.split()
        row = [float(value) for value in values]

        if len(matrix1) < 3:
            matrix1.append(row)
        else:
         matrix2.append(row)

    row_lengths1 = set(len(row) for row in matrix1)
    row_lengths2 = set(len(row) for row in matrix2)

    if len(row_lengths1) > 1 or len(row_lengths2) > 1:
        print("Матриці мають різну розмірність")
    else:

        print("Додавання:")
        add =Matrix(matrix1).elementwise_add(Matrix(matrix2))
        print(add)
        print("Віднімання:")
        sub =Matrix(matrix1).elementwise_subtract(Matrix(matrix2))
        print(sub)
        print("Множення:")
        mul = Matrix(matrix1).elementwise_multiply(Matrix(matrix2))
        print(mul)
        print("Ділення:")
        div = Matrix(matrix1).elementwise_divide(Matrix(matrix2))
        print(div)


        with open('resultM.txt', 'w') as output_file:
            output_file.write(f"{matrix1} + {matrix2} = {add}\n")
            output_file.write(f"{matrix1} - {matrix2} = {sub}\n")
            output_file.write(f"{matrix1} * {matrix2} = {mul}\n")
            output_file.write(f"{matrix1} / {matrix2} = {div}\n")

except ZeroDivisionError as e:
    print(e)  # Вивести повідомлення про помилку ділення на 0
except Exception as e:
    print("Інша помилка:", str(e))
