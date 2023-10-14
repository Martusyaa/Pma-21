def matrix_multiply(matrix_first, matrix_second):
    rows_first, columns_first = len(matrix_first), len(matrix_first[0])
    rows_second, columns_second = len(matrix_second), len(matrix_second[0])

    if columns_first != rows_second:
        return "Неможливо виконати множення: кількість стовпців першої матриці не дорівнює кількості рядків другої матриці."
    result_matrix = [[0] * columns_second for _ in range(rows_first)]
    for i in range(rows_first):
        for j in range(columns_second):
            for k in range(columns_first):
                result_matrix[i][j] += matrix_first[i][k] * matrix_second[k][j]
    return result_matrix
# n = rows ;
# m = columns;
def input_matrix(prompt):
    while True:
        n_m_input = input(f"{prompt} Введіть розміри матриці (рядки стовпців): ")
        n_m_values = n_m_input.split()
        if len(n_m_values) != 2:
            print("Помилка: Введіть два числа через пробіл (рядки та стовпці).")
            continue
        n, m = n_m_values
        if not n.isdigit() or not m.isdigit():
            print("Помилка: Введіть числа для рядків та стовпців.")
            continue
        n, m = int(n), int(m)
        matrix = []
        print(f"Введіть елементи матриці {prompt} рядок за рядком:")
        for _ in range(n):
            row_input = input().split()
            if len(row_input) != m:
                print("Помилка: Некоректна кількість елементів у рядку.")
                continue
            if all(elem.isdigit() for elem in row_input):
                integer_row = [int(elem) for elem in row_input]
                matrix.append(integer_row)
            else:
                print("Помилка: Введіть числа для елементів матриці.")
        return matrix
print("Введіть матрицю 1:")
matrix_first = input_matrix("Матриця 1")
print("Введіть матрицю 2:")
matrix_second = input_matrix("Матриця 2")
result = matrix_multiply(matrix_first, matrix_second)
if isinstance(result, str):
    print(result)
else:
    print("Результат множення матриць:")
    for row in result:
        print(*row)
