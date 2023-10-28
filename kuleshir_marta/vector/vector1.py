try:
    with open('input.txt', 'r') as file:
        A = list(map(float, file.readline().split()))
        B = list(map(float, file.readline().split()))
except FileNotFoundError:
    with open('output.txt', 'w') as output_file:
        output_file.write('File not found.')

if len(A) != len(B):
    with open('output.txt', 'w') as output_file:
        output_file.write('Вектори мають різну довжину.')
else:
    addition = [x + y for x, y in zip(A, B)]
    subtraction = [x - y for x, y in zip(A, B)]
    scalar = sum(x * y for x, y in zip(A, B))
    division = [x / y for x, y in zip(A, B)]

    try:
        with open('output.txt', 'w') as output_file:
            output_file.write("Перший вектор: {}\n".format(A))
            output_file.write("Другий вектор: {}\n".format(B))
            output_file.write("Додавання векторів: {}\n".format(addition))
            output_file.write("Віднімання векторів: {}\n".format(subtraction))
            output_file.write("Скалярний добуток векторів: {}\n".format(scalar))
            output_file.write("Ділення першого вектора на другий вектор: {}\n".format(division))
    except FileNotFoundError:
        print('File not found.')
