def read_matrix_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            matrix = []
            for line in lines:
                row = [int(num) for num in line.strip().split()]
                matrix.append(row)
            return matrix
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

matrix1 = read_matrix_from_file('matrixes.txt')
matrix2 = read_matrix_from_file('readmatrix.txt')

if matrix1 is not None and matrix2 is not None:
    result_matrix = subtract_matrices(matrix1, matrix2)
    if result_matrix is not None:
        print("Resulting matrix:")
        for row in result_matrix:
            print(row)
    else:
        print("Matrices cannot be added due to different dimensions.")
else:
    print("Failed to read one or both matrices from the file.")
