import numpy as np

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

firstMatrix = np.loadtxt(inputFile)
secondMatrix = np.loadtxt(inputSecondFile)

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

# def enterMatrix():
#     global firstRow, firstColumn, secondRow, secondColumn, firstMatrix, secondMatrix
#     firstRow = int(input("Enter size of first matrix: "))
#     firstColumn = int(input())
#     secondRow = int(input("Enter size of second matrix: "))
#     secondColumn = int(input())
#     firstMatrix = np.zeros((firstRow, firstColumn))
#     secondMatrix = np.zeros((secondRow, secondColumn))
#
#     print("\nEnter first matrix\n")
#
#     for i in range(firstRow):
#         for j in range(firstColumn):
#             firstMatrix[i][j] = int(input())
#
#     print("\n", firstMatrix)
#
#     print("\nEnter second matrix\n")
#
#     for i in range(secondRow):
#         for j in range(secondColumn):
#             secondMatrix[i][j] = int(input())
#
#     print("\n", secondMatrix)


def addMatrix(first, second, Row, Column):
    sum = np.zeros((Row, Column))
    for i in range(Row):
        for j in range(Column):
            sum[i][j] = first[i][j] + second[i][j]
    return sum


def subtractMatrix(first, second, Row, Column):
    subtract = np.zeros((Row, Column))
    for i in range(Row):
        for j in range(Column):
            subtract[i][j] = first[i][j] - second[i][j]
    return subtract


def multiplyMatrix(first, second, firstRow, firstColumn, secondRow, secondColumn):
    multiply = np.zeros((firstRow, secondColumn))
    for i in range(firstRow):
        for j in range(secondColumn):
            multiply[i][j] = 0
            for k in range(firstColumn):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def divideMatrix(first, second, firstRow, firstColumn, secondRow, secondColumn):
    divide = np.zeros((firstRow, secondColumn))
    try:
        invMatrix = np.linalg.inv(second)
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
            saveToFile(np.array_str(resultMatrix))
            print('\n', resultMatrix)
        else:
            print('\n', ERROR_TEXT)
    elif choice == 2:
        if firstRow == secondRow and firstColumn == secondColumn:
            resultMatrix = subtractMatrix(firstMatrix, secondMatrix, firstRow, firstColumn)
            saveToFile(np.array_str(resultMatrix))
            print('\n', resultMatrix)
        else:
            print('\n', ERROR_TEXT)
    elif choice == 3:
        if firstColumn == secondRow:
            resultMatrix = multiplyMatrix(firstMatrix, secondMatrix, firstRow, firstColumn, secondRow, secondColumn)
            saveToFile(np.array_str(resultMatrix))
            print('\n', resultMatrix, resultMatrix)
        else:
            print('\n', ERROR_TEXT)
    elif choice == 4:
        if firstColumn == secondRow:
            resultMatrix = divideMatrix(firstMatrix, secondMatrix, firstRow, firstColumn, secondRow, secondColumn)
            saveToFile(np.array_str(resultMatrix))
            print('\n', resultMatrix)
        else:
            print('\n', ERROR_TEXT)

    elif choice == 5:
        isOpened = False

