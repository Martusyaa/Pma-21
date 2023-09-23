INPUT_FILE_NAME = 'vkt.txt'

try:
    with open(INPUT_FILE_NAME, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found: ", INPUT_FILE_NAME)

vectors = []
for line in lines:
    values = line.split()
    vector = [float(value) for value in values]
    vectors.append(vector)

vector_lengths = set(len(vector) for vector in vectors)
if len(vector_lengths) > 1:
    print(" вектори мають різну довжину")
else:
    vector1 = vectors[0]
vector2 = vectors[1]

summa = [vector1[i] + vector2[i] for i in range(len(vector1))]
sub = [vector1[i] - vector2[i] for i in range(len(vector1))]
mult = [vector1[i] * vector2[i] for i in range(len(vector1))]
div = [vector1[i] / vector2[i] for i in range(len(vector1))]

print('+', summa)
print('-', sub)
print('*', mult)
print('/', div)

with open('result.txt', 'w') as output_file:
    output_file.write(f"{vector1} + {vector2} = {summa}\n")
    output_file.write(f"{vector1} - {vector2} = {sub}\n")
    output_file.write(f"{mult}\n")
    output_file.write(f"{div}\n")
