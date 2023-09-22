def print_matrix(matrix):
    for row in matrix:
        print(row)


def add_matrix(matrixFirst, matrixSecond):
    if len(matrixFirst) != len(matrixSecond) or len(matrixFirst[0]) != len(matrixSecond[0]):
        raise ValueError("Матриці повинні бути однакового розміру для додавання")

    rows = len(matrixFirst)
    cols = len(matrixFirst[0])

    result = [[matrixFirst[i][j] + matrixSecond[i][j] for j in range(cols)] for i in range(rows)]
    return result


def difference_matrix(matrixFirst, matrixSecond):
    if len(matrixFirst) != len(matrixSecond) or len(matrixFirst[0]) != len(matrixSecond[0]):
        raise ValueError("Матриці повинні бути однакового розміру для віднімання")

    rows = len(matrixFirst)
    cols = len(matrixFirst[0])

    result = [[matrixFirst[i][j] - matrixSecond[i][j] for j in range(cols)] for i in range(rows)]
    return result


def multiplication_matrix(matrixFirst, matrixSecond):
    rowsFirst = len(matrixFirst)
    colsFirst = len(matrixFirst[0])
    rowsSecond = len(matrixSecond)
    colsSecond = len(matrixSecond[0])

    if colsFirst != rowsSecond:
        raise ValueError("Неможливо виконати множення матриць. Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці.")

    result = [[0 for j in range(colsSecond)] for i in range(rowsFirst)]

    for i in range(rowsFirst):
        for j in range(colsSecond):
            for k in range(colsFirst):
                result[i][j] += matrixFirst[i][k] * matrixSecond[k][j]

    return result


def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(size):
            submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
            det += matrix[0][i] * determinant(submatrix) * (-1)**i
        return det


def matrix_inverse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if cols != rows:
        raise ValueError("Неможливо знайти обернену матрицю. Кількість стовпців повинна дорівнювати кількості рядків.")

    determinant_value = determinant(matrix)
    if determinant_value == 0:
        raise ValueError("Неможливо знайти обернену матрицю. Визначник дорівнює нулю.")

    inverse_matrix = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            submatrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            inverse_matrix[j][i] = determinant(submatrix) * (-1)**(i + j) / determinant_value

    return inverse_matrix


def divide_matrix(matrixFirst, matrixSecond):
    result_inverse = matrix_inverse(matrixSecond)
    if result_inverse:
        print("Результат транспонованої матриці:")
        print_matrix(result_inverse)

        divide_result = multiplication_matrix(matrixFirst, result_inverse)

        if divide_result:
            for i in range(len(divide_result)):
                for j in range(len(divide_result[i])):
                    divide_result[i][j] = round(divide_result[i][j], 2)
            return divide_result
        else:
            raise ValueError("Ділення неможливе!")


def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = [float(x) for x in line.split()]
            matrix.append(row)
    return matrix

def write_matrix_to_file(matrix, filename, action):
    with open(filename, 'a+') as file:
        file.write(f"Result of {action}: \n")#f - значення змінних у рядок
        for row in matrix:
            row_str = ', '.join(map(str, row))
            file.write(row_str + '\n')
        file.write("\n")


# def clear_file(filename):
#     with open(filename, 'w') as file:
#         file.write('')


if __name__ == "__main__":

    result_file = "Result.txt"
    # clear_file(result_file)
    try:
        matrixFirst = read_matrix_from_file("MatrixFirst.txt")
        matrixSecond = read_matrix_from_file("MatrixSecond.txt")

        try:
            add_result = add_matrix(matrixFirst, matrixSecond)
            print("Результат додавання: ")
            print_matrix(add_result)
            write_matrix_to_file(add_result, result_file, "addition")
        except ValueError as e:
            print(e)

        try:
            difference_result = difference_matrix(matrixFirst, matrixSecond)
            print("Результат віднімання:")
            print_matrix(difference_result)
            write_matrix_to_file(difference_result, result_file, "subtraction")
        except ValueError as e:
            print(e)

        try:
            multiplication_result = multiplication_matrix(matrixFirst, matrixSecond)
            print("Результат множення:")
            print_matrix(multiplication_result)
            write_matrix_to_file(multiplication_result, result_file, "multiplication")
        except ValueError as e:
            print(e)

        try:
            division_result = divide_matrix(matrixFirst, matrixSecond)
            print("Результат ділення:")
            print_matrix(division_result)
            write_matrix_to_file(division_result, result_file, "division")
        except ValueError as e:
            print(e)

    except FileNotFoundError as e:
        print(f"Файл не знайдено!")
    except Exception as e:
        print(f"Щось пішло не так: {e}")