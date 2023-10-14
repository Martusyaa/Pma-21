def read_matrix_from_file(filename):
    try:
        with open(filename) as file:
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

def add_matrices(matrix_first, matrix_second):
    if len(matrix_first) != len(matrix_second) or len(matrix_first[0]) != len(matrix_second[0]):
        return None
    result = []
    for i in range(len(matrix_first)):
        row = []
        for j in range(len(matrix_first[0])):
            row.append(matrix_first[i][j] + matrix_second[i][j])
        result.append(row)
    return result

matrix_first = read_matrix_from_file('matrixes.txt')
matrix_second = read_matrix_from_file('readmatrix.txt')

if matrix_first is not None and matrix_second is not None:
    result_matrix = add_matrices(matrix_first, matrix_second)
    if result_matrix is not None:
        print("Resulting matrix:")
        for row in result_matrix:
            print(row)
    else:
        print("Matrices cannot be added due to different dimensions.")
else:
    print("Failed to read one or both matrices from the file.")
