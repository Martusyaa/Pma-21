from matrix import *
from files import *

first_matrix = read_matrix(FIRST_MATRIX)
second_matrix = read_matrix(SECOND_MATRIX)

result = divide(first_matrix,second_matrix)

with open(RESULT, 'w') as file:
    file.write("Result:\n")
    write_matrix(file, result)