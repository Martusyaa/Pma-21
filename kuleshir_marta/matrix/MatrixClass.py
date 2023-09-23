class Matrix:
    def __init__(self, rows, cols):
        if len(rows) == 0 or len(cols) == 0 or len(rows[0]) != len(cols):
            raise ValueError("Неправильні розміри матриць для ініціалізації.")

        self.rows = rows
        self.cols = cols

    def matrix_multiplication(self, other):
        if len(self.cols) != len(other.rows):
            raise ValueError("Довжини рядка та стовпця мають бути однаковими.")

        result = []
        for i in range(len(self.rows)):
            row = []
            for j in range(len(other.cols)):
                element = sum(self.rows[i][k] * other.rows[k][j] for k in range(len(self.cols)))
                row.append(element)
            result.append(row)

        return Matrix(result, [list(col) for col in zip(*other.cols)])

    def matrix_determinant(self):
        n = len(self.rows)

        if n == 1:
            return self.rows[0][0]

        if n == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]

        determinant = 0
        for j in range(n):
            submatrix = [self.rows[i][:j] + self.rows[i][j + 1:] for i in range(1, n)]
            determinant += (-1) ** j * self.rows[0][j] * Matrix(submatrix, submatrix).matrix_determinant()

        return determinant

    def matrix_inverse(self):
        n = len(self.rows)

        determinant = self.matrix_determinant()
        if determinant == 0:
            raise ValueError("Визначник матриці дорівнює нулю. Множення матриць неможливе.")

        empty_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                submatrix = [row[:j] + row[j + 1:] for row in (self.rows[:i] + self.rows[i + 1:])]
                cofactor = (-1) ** (i + j) * Matrix(submatrix, submatrix).matrix_determinant()
                empty_matrix[i][j] = cofactor / determinant

        return Matrix(empty_matrix, empty_matrix)


def matrix_multiply_a_inverse_b(matrix_a, matrix_b):
    try:
        inverse_b = matrix_b.matrix_inverse()
        return matrix_a.matrix_multiplication(inverse_b)
    except ValueError as e:
        raise ValueError("Помилка при множенні матриць A на обернену B: " + str(e))

def read_matrices(filename):
    try:
        with open(filename) as file:
            lines = file.read().split('\n')
    except FileNotFoundError:
        raise FileNotFoundError("Файл не знайдено.")

    delimiter = ""
    for i, line in enumerate(lines):
        if not line.strip():
            delimiter = i
            break

    a_matrix = []
    b_matrix = []

    for i in range(delimiter):
        row = list(map(int, lines[i].split()))
        a_matrix.append(row)

    for i in range(delimiter + 1, len(lines)):
        row = list(map(int, lines[i].split()))
        b_matrix.append(row)

    return [Matrix(a_matrix, list(zip(*b_matrix))), Matrix(b_matrix, list(zip(*a_matrix)))]


try:
    matrices = read_matrices('input.txt')
    matrix_a_input = matrices[0]
    matrix_b_input = matrices[1]

    with open('output.txt', 'a') as output_file:
        output_file.write('Перша матриця A:\n')
        for row_a in matrix_a_input.rows:
            output_file.write(' '.join(map(str, row_a)) + '\n')

        output_file.write('Друга матриця B:\n')
        for row_b in matrix_b_input.rows:
            output_file.write(' '.join(map(str, row_b)) + '\n')

        try:
            result_c = matrix_a_input.matrix_multiplication(matrix_b_input)
            output_file.write('Результат множення A і B:\n')
            for row_c in result_c.rows:
                output_file.write(' '.join(map(str, row_c)) + '\n')
        except ValueError as matrix_multiply_error:
            output_file.write('\n' + str(matrix_multiply_error))

        try:
            determinant_a = matrix_a_input.matrix_determinant()
            output_file.write('Визначник матриці A:\n')
            output_file.write(str(determinant_a) + '\n')
        except ValueError as determinant_a_error:
            output_file.write('\n' + str(determinant_a_error))

        try:
            inverse_b = matrix_b_input.matrix_inverse()
            output_file.write('Обернена матриця B:\n')
            for row_inverse_b in inverse_b.rows:
                output_file.write(' '.join(map(str, row_inverse_b)) + '\n')
        except ValueError as inverse_b_error:
            output_file.write('\n' + str(inverse_b_error))

        try:
            ab_inverse_b_result = matrix_multiply_a_inverse_b(matrix_a_input, matrix_b_input)
            output_file.write('Ділення матриць A на обернену B:\n')
            for row_ab_inverse_b in ab_inverse_b_result.rows:
                output_file.write(' '.join(map(str, row_ab_inverse_b)) + '\n')
        except ValueError as ab_inverse_b_error:
            output_file.write('\n' + str(ab_inverse_b_error))

except FileNotFoundError as file_not_found_error:
    print(file_not_found_error)
except ValueError as value_error:
    print(value_error)
