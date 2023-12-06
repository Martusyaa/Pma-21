from matrix import *

first_matrix = Matrix('first_matrix.txt')
second_matrix = Matrix('second_matrix.txt')

result = first_matrix.add(second_matrix)
if result:
    print("Result:")
    for row in result:
        print(' '.join(map(str, row)))

    with open('result.txt', 'w') as file:
        for row in result:
            file.write(' '.join(map(str, row)) + '\n')
    print("result has been written in result.txt")

