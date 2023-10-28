INPUT_FILE_NAME = 'mat.txt'

try:
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found: ", INPUT_FILE_NAME)

matrix1 = []
matrix2 = []

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
    summa = []
    sub = []

    for i in range(len(matrix1)):
        # Додавання
        row_summa = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        summa.append(row_summa)

        # Віднімання
        row_sub = [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]
        sub.append(row_sub)

    # Множення матриць
    result = []
    for i in range(len(matrix1)):
        row = [0] * len(matrix2[0])
        result.append(row)

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                result[i][j] += matrix1[i][k] * matrix2[k][j]


def matrix_inverse(matrix1):
    det = matrix1[0][0] * (matrix1[1][1] * matrix1[2][2] - matrix1[1][2] * matrix1[2][1]) - matrix1[0][1] * (
                matrix1[1][0] * matrix1[2][2] - matrix1[1][2] * matrix1[2][0]) + matrix1[0][2] * (
                         matrix1[1][0] * matrix1[2][1] - matrix1[1][1] * matrix1[2][0])

    if det == 0:
        print("Матриця не має оберненої матриці (детермінант дорівнює 0)")
    else:
        inv_det = 1.0 / det

        result = [
            [
                (matrix1[1][1] * matrix1[2][2] - matrix1[1][2] * matrix1[2][1]) * inv_det,
                (matrix1[0][2] * matrix1[2][1] - matrix1[0][1] * matrix1[2][2]) * inv_det,
                (matrix1[0][1] * matrix1[1][2] - matrix1[0][2] * matrix1[1][1]) * inv_det
            ],
            [
                (matrix1[1][2] * matrix1[2][0] - matrix1[1][0] * matrix1[2][2]) * inv_det,
                (matrix1[0][0] * matrix1[2][2] - matrix1[0][2] * matrix1[2][0]) * inv_det,
                (matrix1[0][2] * matrix1[1][0] - matrix1[0][0] * matrix1[1][2]) * inv_det
            ],
            [
                (matrix1[1][0] * matrix1[2][1] - matrix1[1][1] * matrix1[2][0]) * inv_det,
                (matrix1[0][1] * matrix1[2][0] - matrix1[0][0] * matrix1[2][1]) * inv_det,
                (matrix1[0][0] * matrix1[1][1] - matrix1[0][1] * matrix1[1][0]) * inv_det]
        ]

        return result


    matrix2_inv = matrix_inverse(matrix2)
    for row in matrix2_inv:
        print(row)

    print(' ')

    result = []
    for i in range(len(matrix1)):
        row = [0] * len(matrix2_inv[0])
        result.append(row)

    for i in range(len(matrix1)):
        for j in range(len(matrix2_inv[0])):
            for k in range(len(matrix1[0])):
                result[i][j] += matrix1[i][k] * matrix2_inv[k][j]

print("Ділення:")
for row in result:
    print('/', row)

    # Виведення результатів додавання
print("Додавання:")
for row in summa:
    print('+', row)

    # Виведення результатів віднімання
print("Віднімання:")
for row in sub:
    print('-', row)

print("Множення:")
for row in result:
    print('*', row)

    # Запис результатів у файл
    with open('result.txt', 'a') as output_file:
        output_file.write(f"{matrix1} + {matrix2} = {summa}\n")
        output_file.write(f"{matrix1} - {matrix2} = {sub}\n")
        output_file.write(f"{matrix1} * {matrix2} = {result}\n")

