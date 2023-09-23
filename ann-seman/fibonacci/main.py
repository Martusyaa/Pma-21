
INPUT_FILE = "fibonachi.txt"
OUTPUT_FILE = "output.txt"

with open(INPUT_FILE, "r") as file:
    last_two_numbers = file.readlines()
    a = int(last_two_numbers[0])
    b = int(last_two_numbers[1])

with open(OUTPUT_FILE, "w") as output_file:
    output_file.write(f"Число 1: {a}\n")
    output_file.write(f"Число 2: {b}\n")

    for i in range(3, 11):
        next_fibonacci = a + b
        output_file.write(f"Число {i}: {next_fibonacci}\n")

        a, b = b, next_fibonacci
