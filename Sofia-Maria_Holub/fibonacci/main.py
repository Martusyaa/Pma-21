"""with open('steps', 'r') as steps_file:
    num_steps = int(steps_file.readline().strip())

with open('input.txt', 'r') as input_file:
    num1, num2 = map(int, input_file.readline().split())

fibonacci = [num1, num2]

while len(fibonacci) < num_steps:
    next_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_num)

with open('output.txt', 'w') as output_file:
    for num in fibonacci:
        output_file.write(str(num) + '\n')

print("Результат:", end=' ')
for num in fibonacci:
    print(num, end=' ')"""

steps = 10
with open("input.txt") as file:
    line = file.readline().split(",")
for i in range(0, len(line)):
    line[i] = float(line[i])
for i in range(0, steps - 2):
    length = len(line)
    temp = line[length - 1] + line[length - 2]
    line.append(temp)

with open("output.txt", "w") as file:
    file.write(str(line))
