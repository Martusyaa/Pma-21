def matrix_multiplication(row, col):
    if len(row) != len(col):
        raise ValueError("Довжини рядка та стовпця мають бути однаковими.")

    result = 0
    for i in range(len(row)):
        result += row[i] * col[i]

    return result


try:
    with open('input.txt') as file:
        lines = file.read().split('\n')
except FileNotFoundError:
    print("Файл не знайдено.")

delimiter = ""
for i, line in enumerate(lines):
    if not line.strip():
        delimiter = i
        break

A = []
B = []

for i in range(delimiter):
    row = list(map(int, lines[i].split()))
    A.append(row)

for i in range(delimiter + 1, len(lines)):
    row = list(map(int, lines[i].split()))
    B.append(row)

if len(A[0]) == len(B):

    def matrix_determinant(matrix):
        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for j in range(n):
            submatrix = [matrix[i][:j] + matrix[i][j + 1:] for i in range(1, n)]
            determinant += (-1) ** j * matrix[0][j] * matrix_determinant(submatrix)

        return determinant


    def matrix_inverse(matrix):
        n = len(matrix)

        determinant = matrix_determinant(matrix)
        if determinant == 0:
            raise ValueError("Визначник матриці A дорівнює нулю. Множення матриць неможливе.")

        empty_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                submatrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
                cofactor = (-1) ** (i + j) * matrix_determinant(submatrix)
                empty_matrix[i][j] = cofactor / determinant

        return empty_matrix


    try:
        with open('output.txt', 'a') as output_file:
            output_file.write('Перша матриця A:\n')
            for row in A:
                output_file.write(" ".join(map(str, row)) + "\n")

            output_file.write('\nДруга матриця B:\n')
            for row in B:
                output_file.write(" ".join(map(str, row)) + "\n")

            determinant_A = matrix_determinant(A)
            if determinant_A == 0:
                raise ValueError("Визначник матриці A дорівнює нулю. Множення матриць неможливе.")

            output_file.write('\nДобуток матриць A і B:\n')

            multiplication = [[matrix_multiplication(A[i], [B[k][j] for k in range(len(B))]) for j in range(len(B[0]))]
                              for i in range(len(A))]
            for row in multiplication:
                output_file.write(" ".join(map(str, row)) + "\n")

            output_file.write('\nВизначник матриці A:\n')
            output_file.write(str(determinant_A) + "\n")

            output_file.write('\nОбернена матриця B:\n')
            inverse_B = matrix_inverse(B)
            for row in inverse_B:
                output_file.write(" ".join(map(str, row)) + "\n")

            output_file.write('\nДілення матриць А і В:\n')
            multiplication_AB = [[matrix_multiplication(A[i], [inverse_B[k][j] for k in range(len(inverse_B))]) for j in
                                  range(len(inverse_B[0]))] for i in range(len(A))]
            for row in multiplication_AB:
                output_file.write(" ".join(map(str, row)) + "\n")

    except FileNotFoundError:
        print("Файл не знайдено.")
else:
    print("Неможливо виконати множення матриць.")
