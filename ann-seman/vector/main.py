import numpy as np
INPUT_FILE = "input_vectors.txt"
OUTPUT_FILE = "output_results.txt"

with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()
    vector1 = np.array([float(x) for x in lines[0].strip().split()])
    vector2 = np.array([float(x) for x in lines[1].strip().split()])

addition = vector1 + vector2
subtraction = vector1 - vector2
multiplication = vector1 * vector2
division = vector1 / vector2

with open(OUTPUT_FILE, 'w') as file:
    file.write("Додавання:\n")
    np.savetxt(file, addition, fmt='%d')

    file.write("\nВіднімання:\n")
    np.savetxt(file, subtraction, fmt='%d')

    file.write("\nМноження (поелементне):\n")
    np.savetxt(file, multiplication, fmt='%d')

    file.write("\nДілення (поелементне):\n")
    np.savetxt(file, division, fmt='%.2f')
