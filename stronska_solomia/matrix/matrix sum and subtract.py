def read_matrix(filename):
    matrix = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = [int(x) for x in line.strip().split()]
                matrix.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return matrix

def write_matrix(matrix, filename):
    try:
        with open(filename, 'w') as file:
            for row in matrix:
                file.write(' '.join(str(x) for x in row) + '\n')
    except FileNotFoundError:
        print(f"File {filename} not found.")

matrix1 = read_matrix("input.txt")
matrix2 = read_matrix("input2.txt")

if not matrix1 or not matrix2:
    print("One or both input files could not be read.")
elif len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    print("Матриці мають різні розмірності, додавання неможливе.")
else:
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)

    write_matrix(result_matrix, "output.txt")
    print("Результат додавання матриць записано у файл output.txt.")