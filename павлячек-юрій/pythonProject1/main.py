INPUT_TXT = "input.txt"
STEPS_TXT = "steps.txt"
OUTPUT_TXT = "output.txt"
FILE_IS_NOT_FOUND = "File is not found !"
SEPARATOR = '{} '

try:
    with open(STEPS_TXT, "r") as steps_file:
        steps = steps_file.read()
        steps = [int(i) for i in steps]
        nums = steps[0]
except:
    nums = 10
    print(FILE_IS_NOT_FOUND, STEPS_TXT)

try:
    with open(INPUT_TXT, "r") as input_file:
        array = input_file.readline().split()
        array = [int(i) for i in array]

        result = 0
except:
    number_one = 0
    number_two = 1
    print(FILE_IS_NOT_FOUND, INPUT_TXT)

try:
    with open(OUTPUT_TXT, "w") as output_file:
        if nums == 0:
            output_file.write('0')
        elif nums == 1:
            output_file.write(SEPARATOR.format(array[0]))
        else:
            output_file.write(SEPARATOR.format(array[0]))
            output_file.write(SEPARATOR.format(array[1]))

            for i in range(nums - 2):
                result = array[0] + array[1]
                output_file.write('{} '.format(result))
                array[0] = array[1]
                array[1] = result
except:
        print(FILE_IS_NOT_FOUND, OUTPUT_TXT)