#фібоначі
suma = 0
fibonacci = []
symbols = []
SEPARATOR = ","

with open('input.txt', 'r') as file:
    line = file.readline().split(SEPARATOR)
line = [float(i) for i in line]


while len(line) < 10:
    line.append(suma)
    suma += line[-2]
print(line)

with open('output.txt', 'w') as file:
    print(line, file = file)
