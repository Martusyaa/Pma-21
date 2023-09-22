OUTPUT_FILE = "output.txt"
INPUT_FILE = "input.txt"

firstVector = []
secondVector = []

with open(INPUT_FILE, "r") as file:
    lines = file.readlines()
    firstVector = [float(x) for x in lines[0].split()]
    secondVector = [float(x) for x in lines[1].split()]

def saveFile(vector):
    with open(OUTPUT_FILE, "a") as file:
        file.write("\n"+str(vector)+ "\n")

def vectorAdd(first, second):
    return [(first[i] + second[i]) for i in range(3)]

def vectorSubtract(first, second):
    return [(first[i] - second[i]) for i in range(3)]

def vectorMultiply(first, second):
    return [(first[i] * second[i]) for i in range(3)]

def vectorDivide(first, second):
    return [(first[i] / second[i]) for i in range(3)]

saveFile(vectorAdd(firstVector, secondVector))
saveFile(vectorSubtract(firstVector,secondVector))
saveFile(vectorDivide(firstVector, secondVector))
saveFile(vectorMultiply(firstVector, secondVector))






