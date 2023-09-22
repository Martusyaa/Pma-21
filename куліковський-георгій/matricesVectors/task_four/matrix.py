from __future__ import annotations
from validators import matrixSumValidator, matrixDivValidator, matrixMulValidator, matrixInvertValidator
from exceptions import MatrixReadFileError

class Matrix:
        
    
    def __init__(self, rows=0, columns=0):
        self.rows = rows
        self.columns = columns
        if rows == 0 and columns == 0:
            self.matrix = []
        else:
            self.matrix = [[0 for i in range(self.columns)] for i in range(self.rows)]
            
        
    def readFile(self, path):
    
        try:
            with open(path) as file:
                try:
                    self.matrix = [[float(i) for i in line.split(' ')] for line in file]
                    self.rows = len(self.matrix)
                    self.columns = len(self.matrix[0])
                    return self
                except MatrixReadFileError:
                    print("Matrix can not be read")
        except FileNotFoundError:
            print("File Not Found")
        
        
    def __str__(self, *args):
        result = ""
        result += str(f"{args}\n\n").strip("()")
        for i in range(self.rows):
            for j in range(self.columns):
                result += f"{round(self.matrix[i][j], ndigits=2):^3} "
            result += '\n'
        return result
    
    
    def __repr__(self):
        return f"Matrix({self.rows}, {self.columns})"
         
          
    @matrixSumValidator
    def __add__(self, other):
        result = Matrix(self.rows, self.columns)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result
        
       
    @matrixSumValidator 
    def __sub__(self, other):
        result = Matrix(self.rows, self.columns)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return result
    
        
    @matrixMulValidator
    def __mul__(self:Matrix, other:Matrix):
        result = Matrix(max(self.rows, other.rows), max(self.columns, other.columns))
        for rowsOne in range(self.rows):
            for colsOne in range(other.columns):
                for rowsTwo in range(other.rows):
                    result.matrix[rowsOne][colsOne] += self.matrix[rowsOne][rowsTwo] * other.matrix[rowsTwo][rowsOne]
        return result
        
        
    def createIdentityMatrix(self):
        identityMatrix = []
        for i in range(len(self.matrix)):
            identityMatrix.append([])
            for j in range(len(self.matrix[0])):
                if i == j:
                    identityMatrix[i].append(1)
                else:
                    identityMatrix[i].append(0)

        return identityMatrix


    #gauss-jordan
    @matrixInvertValidator
    def invertMatrix(self):
        identityMatrix = self.createIdentityMatrix()
        extendedMatrix = [row + identityMatrix[i] for i, row in enumerate(self.matrix)]

        for row in range(self.rows):
            baseRow = row
            for i in range(row, self.rows):
                if abs(extendedMatrix[i][row]) > abs(extendedMatrix[baseRow][row]):
                    baseRow = i

            baseElement = extendedMatrix[row][row]

            for j in range(row, 2 * self.rows):
                extendedMatrix[row][j] /= baseElement

            for i in range(self.rows):
                if i != row:
                    multiplicationValue = extendedMatrix[i][row]
                    for j in range(row, 2 * self.rows):
                        extendedMatrix[i][j] -= multiplicationValue * extendedMatrix[row][j]
                        

        invertedArray = [[extendedMatrix[i][self.rows] for j in range(self.columns)] for i in range(self.rows)]
        invertedMatrix = Matrix(len(invertedArray), len(invertedArray[0]))
        invertedMatrix.matrix = invertedArray

        return invertedMatrix


    @matrixDivValidator
    def __truediv__(self: Matrix, other: Matrix):
        return self * other.invertMatrix()
        
        
    def writeFile(self, path):

        try:
            with open(path, "a") as file:
                file.write(str(self))
        except FileNotFoundError:
            print("File Not Found")