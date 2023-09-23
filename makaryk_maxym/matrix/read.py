def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [float(x) for x in line.split()]
            matrix.append(row)
    return matrix

def write_matrix(file, result):
    for row in result:
        file.write(' '.join(map(str, row)) + '\n')