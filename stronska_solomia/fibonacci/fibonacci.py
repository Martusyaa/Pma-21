INPUT_FILE = 'inp6ut.txt'
OUTPUT_FILE = 'output.txt'

try:

   with open(INPUT_FILE, 'r') as input_file:
    line = input_file.readline()
    numbers = [float(i) for i in line.split()]



    try:

      with open(OUTPUT_FILE, 'a') as output_file:

        for _ in range(8):
            numbers.append(numbers[-1] + numbers[-2])

        output_file.write(str(numbers))
    except FileNotFoundError:
      print("File not found:", OUTPUT_FILE)

except FileNotFoundError:
    print("File not found:", INPUT_FILE)
