inputFile = "input.txt"
inputSecondFile = "inputSecond.txt"
matrixInfoFile = "rowsColumns.txt"
outputFile = "output.txt"
OPERATION_TEXT = """
Choose your math operation(Type only number): 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit       
"""

ERROR_TEXT = "Wrong size of matrix for this operation"

def readMatrixFromFile(inputFile):
    with open(inputFile) as matrixRead:
        return [[int(i)for i in line.split()] for line in matrixRead]

firstMatrix = readMatrixFromFile(inputFile)
secondMatrix = readMatrixFromFile(inputSecondFile)

resultMatrix = None
firstRow = 0
firstColumn = 0
secondRow = 0
secondColumn = 0
isOpened = True

with open(matrixInfoFile) as matrixInformation:
    firstRow = int(matrixInformation.readline().strip())
    firstColumn = int(matrixInformation.readline().strip())
    secondRow = int(matrixInformation.readline().strip())
    secondColumn = int(matrixInformation.readline().strip())

def saveToFile(strMatrix):
    with open(outputFile, 'a') as my_file:
        my_file.write("\n" + strMatrix + "\n")

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def addMatrix(first, second, Row, Column):
    # sum = np.zeros((Row, Column))
    sum = [[0]*Row for i in range(Column)]
    for i in range(Row):
        for j in range(Column):
            sum[i][j] = first[i][j] + second[i][j]
    return sum


def subtractMatrix(first, second, Row, Column):
    subtract = [[0] * Row for i in range(Column)]
    for i in range(Row):
        for j in range(Column):
            subtract[i][j] = first[i][j] - second[i][j]
    return subtract


def multiplyMatrix(first, second, firstRow, firstColumn, secondRow, secondColumn):
    multiply = [[0] * firstRow for i in range(secondColumn)]
    for i in range(firstRow):
        for j in range(secondColumn):
            multiply[i][j] = 0
            for k in range(firstColumn):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def divideMatrix(first, second, firstRow, firstColumn, secondRow, secondColumn):
    divide = [[0] * firstRow for i in range(secondColumn)]
    try:
        invMatrix = getMatrixInverse(second)
        divide = multiplyMatrix(first, invMatrix, firstRow, firstColumn, secondRow, secondColumn)
        return divide
    except Exception as ex:
        print('\n', ex, '\n')
        pass


while isOpened:
    print(OPERATION_TEXT)
    choice = int(input())

    if choice == 1:
        if firstRow == secondRow and firstColumn == secondColumn:
            resultMatrix = addMatrix(firstMatrix, secondMatrix, firstRow, firstColumn)
            strMatrix = ''.join([str(resultMatrix[i]) for i in range(len(resultMatrix))])
            saveToFile(strMatrix)
            print('\n', resultMatrix)
        else:
            print('\n', ERROR_TEXT)
    elif choice == 2:
        if firstRow == secondRow and firstColumn == secondColumn:
            resultMatrix = subtractMatrix(firstMatrix, secondMatrix, firstRow, firstColumn)
            strMatrix = ''.join([str(resultMatrix[i]) for i in range(len(resultMatrix))])
            saveToFile(strMatrix)
            print('\n', resultMatrix)
        else:
            print('\n', ERROR_TEXT)
    elif choice == 3:
        if firstColumn == secondRow:
            resultMatrix = multiplyMatrix(firstMatrix, secondMatrix, firstRow, firstColumn, secondRow, secondColumn)
            strMatrix = ''.join([str(resultMatrix[i]) for i in range(len(resultMatrix))])
            saveToFile(strMatrix)
            print('\n', resultMatrix, resultMatrix)
        else:
            print('\n', ERROR_TEXT)
    elif choice == 4:
        if firstColumn == secondRow:
            resultMatrix = divideMatrix(firstMatrix, secondMatrix, firstRow, firstColumn, secondRow, secondColumn)
            strMatrix = ''.join([str(resultMatrix[i]) for i in range(len(resultMatrix))])
            saveToFile(strMatrix)
            print('\n', resultMatrix)
        else:
            print('\n', ERROR_TEXT)

    elif choice == 5:
        isOpened = False

