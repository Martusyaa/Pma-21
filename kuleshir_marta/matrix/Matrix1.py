try:
    with open('input.txt') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found.")

A = []
B = []
matrix = None

for line in lines:
    if line.strip():
        row = list(map(int, line.split()))
        if matrix is None:
            matrix = A if not A else B
        matrix.append(row)
    else:
        matrix = None

if len(A) == len(B) and len(A[0]) == len(B[0]):
    addition = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    try:
        with open('output.txt', 'a') as output_file:
            output_file.write('Перша матриця A:\n')
            for row in A:
                output_file.write(" ".join(map(str, row)) + "\n")

            output_file.write('\nДруга матриця B:\n')
            for row in B:
                output_file.write(" ".join(map(str, row)) + "\n")

            output_file.write('\nСума матриць A і B:\n')
            for row in addition:
                output_file.write(" ".join(map(str, row)) + "\n")

    except FileNotFoundError:
        print("File not found.")
else:
    print("Неможливо виконати додавання матриць.")

if len(A) == len(B) and len(A[0]) == len(B[0]):
    subtraction = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    try:
        with open('output.txt', 'a') as output_file:
            output_file.write('\nРізниця матриць A і B:\n')
            for row in subtraction:
                output_file.write(" ".join(map(str, row)) + "\n")

    except FileNotFoundError:
        print("File not found.")
else:
    print("Неможливо виконати віднімання матриць.")
