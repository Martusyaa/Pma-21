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

def suma(first, second):
    return [(first[i] + second[i]) for i in range(3)]

def minus(first, second):
    return [(first[i] - second[i]) for i in range(3)]

def mnoj(first, second):
    return [(first[i] * second[i]) for i in range(3)]

def dil(first, second):
    return [(first[i] / second[i]) for i in range(3)]

saveFile(suma(firstVector, secondVector))
saveFile(minus(firstVector,secondVector))
saveFile(dil(firstVector, secondVector))
saveFile(mnoj(firstVector, secondVector))
