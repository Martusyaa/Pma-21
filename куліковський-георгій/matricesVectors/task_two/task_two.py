class MatrixSizeError(Exception):
    "Matrix size error"
    
class MatrixDeterminantError(Exception):
    "Determinant equals zero"


def addition(matrixOne, matrixTwo):
    if isAdditionable(matrixOne, matrixTwo):
        result = [[None for j in range(len(matrixOne[0]))] for i in range(len(matrixOne))]
        for i in range(len(matrixOne)):
            for j in range(len(matrixOne[0])):
                result[i][j] = matrixOne[i][j] + matrixTwo[i][j]
        return result
    else:
        raise MatrixSizeError


def subtraction(matrixOne, matrixTwo):
    if isAdditionable(matrixOne, matrixTwo):
        result = [[None for j in range(len(matrixOne[0]))] for i in range(len(matrixOne))]
        for i in range(len(matrixOne)):
            for j in range(len(matrixOne[0])):
                result[i][j] = matrixOne[i][j] - matrixTwo[i][j]
        return result
    else:
        raise MatrixSizeError


def multiplication(matrixOne, matrixTwo):
    if isMultiplicationable(matrixOne, matrixTwo):
        result = [[0 for j in range(len(matrixOne[0]))] for i in range(len(matrixTwo))]
        for rowsOne in range(len(matrixOne)):
            for colsTwo in range(len(matrixTwo[0])):
                for rowsTwo in range(len(matrixTwo)):
                    result[rowsOne][colsTwo] += matrixOne[rowsOne][rowsTwo] * matrixTwo[rowsTwo][colsTwo]
        return result
    else:
        raise MatrixSizeError


def createIdentityMatrix(matrix):
    identityMatrix = []
    for i in range(len(matrix)):
        identityMatrix.append([])
        for j in range(len(matrix[0])):
            if i == j:
                identityMatrix[i].append(1)
            else:
                identityMatrix[i].append(0)

    return identityMatrix


def transponeMatrix(matrix):
    transponeMatrix = [[matrix[i] for j in range(len(matrix[i]))] for i in range(len(matrix))]
    return transponeMatrix


#gauss-jordan
def invertMatrix(matrix):
    identityMatrix = createIdentityMatrix(matrix)
    augmentedMatrix = [row + identityMatrix[i] for i, row in enumerate(matrix)]

    for row in range(len(matrix)):
        baseRow = row
        for i in range(row, len(matrix)):
            if abs(augmentedMatrix[i][row]) > abs(augmentedMatrix[baseRow][row]):
                baseRow = i

        determinant = augmentedMatrix[row][row]
        if determinant == 0:
            raise MatrixDeterminantError

        for j in range(row, 2 * len(matrix)):
            augmentedMatrix[row][j] /= determinant

        for i in range(len(matrix)):
            if i != row:
                multiplicationValue = augmentedMatrix[i][row]
                for j in range(row, 2 * len(matrix)):
                    augmentedMatrix[i][j] -= multiplicationValue * augmentedMatrix[row][j]
                    

    invertedMatrix = [[augmentedMatrix[i][len(matrix):] for j in range(len(matrix[0]))] for i in range(len(matrix))]

    return invertedMatrix


def division(matrixOne, matrixTwo):
    return multiplication(matrixOne, invertMatrix(matrixTwo))


def isAdditionable(matrixOne, matrixTwo):
    if len(matrixOne) == len(matrixTwo) and len(matrixOne[0]) == len(matrixTwo):
        return 1
    else:
        return 0
    
    
def isMultiplicationable(matrixOne, matrixTwo):
    if len(matrixOne[0]) == len(matrixTwo) and len(matrixOne) == len(matrixTwo[0]):
        return 1
    else:
        return 0



def readFile(path:str, sep:str):
    try:
        with open(path) as file:
            matrix = []
            matrix = [[int(i) for i in line.split(sep)] for line in file]
            return matrix
    except FileNotFoundError:
        print("File Not Found")


def prettyMatrix(matrix):
    matrixString = ''
    for i in matrix:
        for j in i:
            matrixString+=f"{round(j,ndigits=2):>4} "
        matrixString+="\n"
    matrixString+="\n"
    return matrixString
            

def writeFile(matrix):
    
    WRITE_PATH = "task_two/output.txt"
    
    try:
        with open(WRITE_PATH, "a") as file:
            file.write(prettyMatrix(matrix))
    except FileNotFoundError:
        print("File Not Found")
        

matrixOne = readFile("task_two/matrix_one.txt", " ")
matrixTwo = readFile("task_two/matrix_two.txt", " ")
        
        
writeFile(addition(matrixOne, matrixTwo))
writeFile(subtraction(matrixOne, matrixTwo))
writeFile(multiplication(matrixOne, matrixTwo))
writeFile(division(matrixOne, matrixTwo))
