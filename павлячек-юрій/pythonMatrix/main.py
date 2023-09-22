FILE_IS_NOT_FOUND = 'File is not found'
INPUT_FILE_ONE = "input_one.txt"
INPUT_FILE_TWO = "input_two.txt"
OUTPUT_FILE = "output.txt"
BRACKETS = '{}'
QUOTES = ' '

try:
    def inverse_matrix(matrix):
        n = len(matrix)
        augmented_matrix = [rows + [0] * n for rows in matrix]

        for i in range(n):
            augmented_matrix[i][n + i] = 1

        for i in range(n):
            pivot = augmented_matrix[i][i]
            for j in range(n * 2):
                augmented_matrix[i][j] /= pivot

            for k in range(n):
                if k == i:
                    continue
                factor = augmented_matrix[k][i]
                for j in range(n * 2):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

        inverse = [rows[n:] for rows in augmented_matrix]

        return inverse
    with open(INPUT_FILE_ONE) as input_one_file:
        matrix_one = []
        matrix_two = []
        for line in input_one_file:
            row = [int(i) for i in line.split()]
            matrix_one.append(row)
except:
    print(FILE_IS_NOT_FOUND, INPUT_FILE_ONE)

try:
    with open(INPUT_FILE_TWO, "r") as input_two_file:
        for line in input_two_file:

            row = [int(i) for i in line.split()]
            matrix_two.append(row)
except:
    print(FILE_IS_NOT_FOUND, INPUT_FILE_TWO)

try:
    with open(OUTPUT_FILE, "w") as output_file:
            output_file.write('Matrix 1\n')
            for row in matrix_one:
                output_file.write(BRACKETS. format(row))
                output_file.write('\n')

            output_file.write('Matrix 2\n')
            for row in matrix_two:
                output_file.write(BRACKETS.format(row))
                output_file.write('\n')

            result_sum = []
            for i in range(len(matrix_one)):
                row = []
                for j in range(len(matrix_one[0])):
                    row.append(matrix_one[i][j] + matrix_two[i][j])
                result_sum.append(row)

            output_file.write('Sum\n')
            for row in result_sum:
                output_file.write(QUOTES.join(map(str, row)) + '\n')

            result_dif = []
            for i in range(len(matrix_one)):
                row = []
                for j in range(len(matrix_one[0])):
                    row.append(matrix_one[i][j] - matrix_two[i][j])
                result_dif.append(row)

            output_file.write('Difference\n')
            for row in result_dif:
                output_file.write(QUOTES.join(map(str, row)) + '\n')

            result_mult = []
            for i in range(len(matrix_one)):
                row = []
                for j in range(len(matrix_one[0])):
                    mult = 0
                    for k in range(len(matrix_two)):
                        mult += matrix_one[i][k] * matrix_two[k][j]
                    row.append(mult)
                result_mult.append(row)

            output_file.write('Multiplication\n')
            for row in result_mult:
                output_file.write(QUOTES.join(map(str, row)) + '\n')

            inverse_matrix_two = inverse_matrix(matrix_two)
            if inverse_matrix_two is not None:

                result_division = []
                for i in range(len(matrix_one)):
                    row = []
                    for j in range(len(inverse_matrix_two[0])):
                        dot_product = 0
                        for k in range(len(matrix_two)):
                            dot_product += matrix_one[i][k] * inverse_matrix_two[k][j]
                        row.append(dot_product)
                    result_division.append(row)

                output_file.write('Division\n')
                for row in result_division:
                    output_file.write(QUOTES.join(map(str, row)) + '\n')
except:
    print(FILE_IS_NOT_FOUND, OUTPUT_FILE)

print("Результати записані у файл 'output.txt'.")