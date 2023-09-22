INPUT_FILE_PATH = "input.txt"
OUTPUT_FILE = "output.txt"

with open(INPUT_FILE_PATH, "r") as inputFile:
    fibonachiNumbers = [int(line.strip()) for line in inputFile]

    for i in range(10):
        fibonachiNumbers.append(fibonachiNumbers[i]+ fibonachiNumbers[i+1])

    with open(OUTPUT_FILE, 'w') as outputFile:
        for num in fibonachiNumbers:
            outputFile.write("%s\n" %num)

