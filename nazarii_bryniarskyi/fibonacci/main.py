READ_FILE = 'read.txt'
WRITE_FILE = 'write.txt'

with open(READ_FILE, 'r') as f:
    file_line = f.read()

array_of_numbers = [int(i) for i in file_line if i.isdigit()]

number_one = array_of_numbers[0]
number_two = array_of_numbers[1]
result_number = 0

with open(WRITE_FILE, "w") as result_file:
    result_file.write('{} '.format(number_one))
    result_file.write('{} '.format(number_two))

    for i in range(8):
        result_number = number_one + number_two

        result_file.write('{} '.format(result_number))

        number_one = number_two
        number_two = result_number

