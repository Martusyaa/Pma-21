INPUT_FILE_MATRIXFIRST = "input_matrixfirst.txt"
INPUT_FILE_MATRIXSECOND = "input_matrixsecond.txt"
OUTPUT_FILE = "output.txt"
FILE_NOT_FOUND = "file not found"
PLUS_MINUS_IS_BROKEN = "suma and diffence can`t be"
MULTIPLICATION_ERROR = "mulyimlication error"
NEWLINE = "\n"

matrixfirst = []
matrixsecond = []

try:
    with open(INPUT_FILE_MATRIXFIRST) as file:
        for line in file:
            row_matrix = [float(i) for i in line.split()]
            matrixfirst.append(row_matrix)
except FileNotFoundError:
    print(FILE_NOT_FOUND)

try:
    with open(INPUT_FILE_MATRIXSECOND) as file:
        for line in file:
            row_matrix = [float(i) for i in line.split()]
            matrixsecond.append(row_matrix)
except FileNotFoundError:
    print(FILE_NOT_FOUND)

MATRIXFIRST_ROW_SIZE = len(matrixfirst[0])
MATRIXSECOND_ROW_SIZE = len(matrixsecond[0])
MATRIXFIRST_ROW_LEN_VALUES = len(matrixsecond)
MATRIXSECOND_ROW_LEN_VALUES = len(matrixsecond)
suma_matrix  = [[0 for i in range(MATRIXFIRST_ROW_SIZE)] for j in range(MATRIXFIRST_ROW_LEN_VALUES)]
diffence_matrix = [[0 for i in range(MATRIXFIRST_ROW_SIZE)] for j in range(MATRIXFIRST_ROW_LEN_VALUES)]
multiplication_matrix = [[0 for i in range(MATRIXFIRST_ROW_SIZE)] for j in range(MATRIXFIRST_ROW_LEN_VALUES)]
divison_matrix = [[0 for i in range(MATRIXFIRST_ROW_SIZE)] for j in range(MATRIXFIRST_ROW_LEN_VALUES)]

if MATRIXFIRST_ROW_LEN_VALUES == MATRIXSECOND_ROW_LEN_VALUES and MATRIXFIRST_ROW_SIZE == MATRIXSECOND_ROW_SIZE:
    for i in range(MATRIXFIRST_ROW_LEN_VALUES):
        for j in range(MATRIXFIRST_ROW_SIZE):
            suma_matrix[i][j] = matrixfirst[i][j] + matrixsecond[i][j]
    for i in range(MATRIXFIRST_ROW_LEN_VALUES):
        for j in range(MATRIXSECOND_ROW_SIZE):
            diffence_matrix[i][j] = matrixfirst[i][j] - matrixsecond[i][j]
else:
    print(PLUS_MINUS_IS_BROKEN)

try:
    with open(OUTPUT_FILE, "w") as file:
        file.write("Suma matrix: " + str(suma_matrix) + NEWLINE)
        file.write("Diffence matrix: " + str(diffence_matrix) + NEWLINE)
        file.write("Multiplication matrix: " + str(multiplication_matrix) + NEWLINE)
except FileNotFoundError:
    print(FILE_NOT_FOUND)

#if len(matrix1[0]) == len(matrix2):
#    for i in range(len(matrix1)):
#        for j in range(len(matrix2[0])):
#            for k in range(len(matrix2)):
#                multiplication_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
#else:
#    print(MULTIPLICATION_ERROR)
