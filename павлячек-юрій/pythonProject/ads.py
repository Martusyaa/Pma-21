SEPARATOR = '{}'
EROR = "Error !"

try:
    with open("input.txt", "r") as input_file:
        vector_one = input_file.readline().split()
        vector_two = input_file.readline().split()

        vector_one = [int(i) for i in vector_one]
        vector_two = [int(i) for i in vector_two]
except:
    print("File is not found", "input.txt")
try:
    with open("output.txt", "w") as output_file:
        output_file.write('Sum\n')
        if len(vector_one) != len(vector_two):
            print(EROR)
        result = [vector_one[i] + vector_two[i] for i in range(len(vector_one))]
        output_file.write(SEPARATOR.format(result))

        output_file.write('\nDifference\n')
        if len(vector_one) != len(vector_two):
            print(EROR)

        result = [vector_one[i] - vector_two[i] for i in range(len(vector_one))]
        output_file.write(SEPARATOR.format(result))

        output_file.write('\nMultiplication\n')
        if len(vector_one) != len(vector_two):
            print(EROR)

        result = [vector_one[i] * vector_two[i] for i in range(len(vector_one))]
        output_file.write(SEPARATOR.format(result))

        output_file.write('\nDivision\n')
        if len(vector_one) != len(vector_two):
            print(EROR)

        result = [vector_one[i] / vector_two[i] for i in range(len(vector_one))]
        output_file.write(SEPARATOR.format(result))
except:
    print("File is not found", "output.txt")