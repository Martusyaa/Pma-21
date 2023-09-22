class VectorValueError(Exception):
    "Wrong vector size"



def addition(vectorOne, vectorTwo):
    if haveSameLength(vectorOne, vectorTwo):
        result = []
        for i in range(len(vectorOne)):
            result.append(vectorOne[i]+vectorTwo[i])
        return result
    else:
        raise VectorValueError
    
def subtraction(vectorOne, vectorTwo):
    if haveSameLength(vectorOne, vectorTwo):
        result = []
        for i in range(len(vectorOne)):
            result.append(vectorOne[i] - vectorTwo[i])
        return result
    else:
        raise VectorValueError
    

def multiplication(vectorOne, vectorTwo):
    if haveSameLength(vectorOne, vectorTwo):
        result = []
        for i in range(len(vectorOne)):
            result.append(vectorOne[i] * vectorTwo[i])
        return result
    else:
        raise VectorValueError


def division(vectorOne, vectorTwo):
    if haveSameLength(vectorOne, vectorTwo):
        result = []
        for i in range(len(vectorOne)):
            result.append(vectorOne[i] / vectorTwo[i])
        return result
    else:
        raise VectorValueError

def haveSameLength(vectorOne, vectorTwo):
    if len(vectorOne) == len(vectorTwo):
        return 1
    else:
        return 0


def readFile(path:str, sep:str):
    
    try:
        with open(path, "r") as file:
            return [int(i) for i in list(file.read().split(sep))]
    except FileNotFoundError:
        print("File Not Found")
        
        
vectorOne = readFile("task_three/vector_one.txt", " ")
vectorTwo = readFile("task_three/vector_two.txt", " ")


def writeFile(vector):
    
    WRITE_PATH = "task_three/output.txt"
    try:
        with open(WRITE_PATH, "a") as file:
            file.write(f"{str(vector).strip('[]')}\n")
    except FileNotFoundError:
        print("File Not Found")
        
        
writeFile(addition(vectorOne, vectorTwo))
writeFile(subtraction(vectorOne, vectorTwo))
writeFile(multiplication(vectorOne, vectorTwo))
writeFile(division(vectorOne, vectorTwo))