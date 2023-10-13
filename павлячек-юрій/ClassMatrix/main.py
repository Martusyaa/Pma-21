from Matrix import Matrix

input_file_path = "input_one.txt"
output_path = "output.txt"

matrices = Matrix.read_from_file(input_file_path)

result_sum = matrices[0]
result_diff = matrices[0]
result_mul = matrices[0]
result_div = matrices[0]
try:
    for matrix in matrices[1:]:
        result_sum += matrix
        result_diff -= matrix
        result_mul *= matrix
        result_div /= matrix
except:
    print("Error !", "Matrix 2 is zero")
try:
    with open("output.txt", "w") as output_file:
        output_file.write('Suma: \n{}'.format(result_sum))
        output_file.write('\nDif: \n{}'.format(result_diff))
        output_file.write('\nMulp: \n{}'.format(result_mul))
        output_file.write('\nDiv: \n{}'.format(result_div))
except:
    print("File is not found", "output.txt")
print("Результати записано у файл", output_path)
