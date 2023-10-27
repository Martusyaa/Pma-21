from MatrixClass import Matrix

INPUT_FILE_MATRIXFIRST = "firstmatrix.txt"
INPUT_FILE_MATRIXSECOND = "secondmatrix.txt"
OUTPUT_FILE = "output.txt"


matrix_first = Matrix(INPUT_FILE_MATRIXFIRST)
matrix_second  = Matrix(INPUT_FILE_MATRIXSECOND)

suma_result = matrix_first.add_matrices(matrix_second)
if suma_result:
    matrix_first.write_matrix(OUTPUT_FILE, "Suma", suma_result)

difference_result = matrix_first.subtract_matrices(matrix_second)
if difference_result:
    matrix_second.write_matrix(OUTPUT_FILE, "Difference", difference_result)

multiplication_result = matrix_first.multiply_matrices(matrix_second)
if multiplication_result:
    matrix_first.write_matrix(OUTPUT_FILE, "Multiplication", multiplication_result)