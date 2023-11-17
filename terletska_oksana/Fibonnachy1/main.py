file1 = open("file1.txt", "r")
input_file = file1.read()
print(input_file)
file1.close()
numbers = []
fibonachi = []
numbers.append (input_file[0])
numbers.append(input_file[-1])
print(numbers)
first_number = float(numbers[0])
last_number = float(numbers[-1])
line = [0,1]
steps = 10
line = [float(i) for i in line]
for i in range(0, steps - 2):
    lenght = len(line)
    line.append(line[lenght - 1] + line[lenght - 2])
with open("file2.txt", "w") as output_file:
    output_file.write(str(line))
