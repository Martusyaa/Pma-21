
    INPUT_TXT = "input.txt"

    OUTPUT_TXT = "output.txt"

    STEPS_TXT = "steps.txt"

    try:
        with open(INPUT_TXT, 'r') as file:
            elements = file.readline().split()
            elements = [float(i) for i in elements]
    except FileNotFoundError:
        raise FileNotFoundError("File not found: ", INPUT_TXT)

    try:
        with open(STEPS_TXT, 'r') as file:
            steps = int(file.readline())
    except FileNotFoundError:
        raise FileNotFoundError("File not found: ", STEPS_TXT)

    while len(elements) < steps:
        next_element = elements[-1] + elements[-2]
        elements.append(next_element)

    with open(OUTPUT_TXT, 'w') as file:
        for i in elements:
            file.write(str(i) + '\n')
