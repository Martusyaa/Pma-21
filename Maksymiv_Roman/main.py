def read_matrix(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    matrix = []
    for line in lines:
        row = [int(num) for num in line.split()]
        matrix.append(row)
    return matrix


matrix_first_file = "matrix_1.txt"
matrix_second_file = "matrix_2.txt"
try:
 matrix_first = read_matrix(matrix_first_file)
 matrix_second = read_matrix(matrix_second_file)

 row_matrix_first = len(matrix_first)
 col_matrix_first = len(matrix_first[0])
 row_matrix_second = len(matrix_second)
 col_matrix_second = len(matrix_second[0])
 if row_matrix_first != row_matrix_second or col_matrix_first != col_matrix_second:
     raise ValueError("Matrices have different dimensions")
 summed_matrix = []
 dif_matrix = []

 for i in range(row_matrix_first):
    sum_row = []
    dif_row = []
    for j in range(col_matrix_first):
        sum_result = matrix_first[i][j] + matrix_second[i][j]
        dif_result = matrix_first[i][j] - matrix_second[i][j]
        sum_row.append(sum_result)
        dif_row.append(dif_result)
    summed_matrix.append(sum_row)
    dif_matrix.append(dif_row)
 with open("results.txt", 'a') as file:
        print(f"{matrix_first} + {matrix_second} = {summed_matrix}", file=file)
        print(f"{matrix_first} - {matrix_second} = {dif_matrix}", file=file)

except ValueError as e:
    print(f"ValueError: {e}")
