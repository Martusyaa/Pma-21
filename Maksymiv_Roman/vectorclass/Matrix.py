from Parser import ParseRow
from DifferentDimensionsException import DifferentDimensionsException
from NonValidDimensionsForMultiplicationException import NonValidDimensionsForMultiplicationException


class Matrix:
    def init(self, _matrix=None):
        if (_matrix is None):
            self.matrix = []
        else:
            self.matrix = _matrix

    def readFromFile(self, fileName):
        fileToReadFrom = open(fileName)
        lines = fileToReadFrom.readlines()
        for line in lines:
            currentRow = ParseRow(line)
            if (currentRow != []): self.matrix.append(currentRow)

    def writeToFile(self, fileName):
        fileToWriteTo = open(fileName, "w")
        rowCount = self.matrix.len()
        for rowIterator in range(0, rowCount):
            currentLine = ''
            for element in self.matrix[rowIterator]:
                currentLine += str(element) + ' '
            fileToWriteTo.write(currentLine + '\n')
        fileToWriteTo.close()

    def add(self, other):
        resultMatrix = []
        rowCount1 = self.matrix.len()
        columnCount1 = self.matrix[0].len()
        rowCount2 = other.matrix.len()
        columnCount2 = other.matrix[0].len()

        if (rowCount1 != rowCount2 or columnCount1 != columnCount2):
            raise DifferentDimensionsException('Dimensions of two matrices are different')
        for rowIterator in range(0, rowCount1):
            currentRow = []
            for columnIterator in range(0, columnCount1):
                currentRow.append(
                    float(self.matrix[rowIterator][columnIterator]) + float(other.matrix[rowIterator][columnIterator]))
            resultMatrix.append(currentRow)
        return Matrix(resultMatrix)

    def getRowsCount(self):
        return self.matrix.len()

    def getColumnsCount(self):
        return self.matrix[0].len()

    def sub(self, other):
        resultMatrix = []
        rowCount1 = self.matrix.len()
        columnCount1 = self.matrix[0].len()
        rowCount2 = other.matrix.len()
        columnCount2 = other.matrix[0].len()
        if (rowCount1 != rowCount2 or columnCount1 != columnCount2):
            raise DifferentDimensionsException('Dimensions of two matrices are different')
        for rowIterator in range(0, rowCount1):
            currentRow = []
            for columnIterator in range(0, columnCount1):
                currentRow.append(
                    float(self.matrix[rowIterator][columnIterator]) - float(other.matrix[rowIterator][columnIterator]))
            resultMatrix.append(currentRow)
        return Matrix(resultMatrix)

    def mul(self, other):
        if (self.getColumnsCount() != other.getRowsCount()):
            raise NonValidDimensionsForMultiplicationException(
                'Impossible to multiply matrices because of incorrent dimensions')
        resultMatrix = Matrix()
        rows = self.getRowsCount()
        columns = other.getColumnsCount()
        resultMatrix.initEmptyMatrix(rows, columns)
        for firstIterator in range(rows):
            for secondIterator in range(columns):
                for thirdIterator in range(self.getColumnsCount()):
                    resultMatrix.matrix[firstIterator][secondIterator] += float(
                        self.matrix[firstIterator][thirdIterator]) * float(other.matrix[thirdIterator][secondIterator])
        return resultMatrix

    @staticmethod
    def addMatrices_Static(firstMatrix, secondMatrix):
        return (firstMatrix + secondMatrix)

    @staticmethod
    def subtractMatrices_Static(firstMatrix, secondMatrix):
        return (firstMatrix - secondMatrix)

    def addMatrices_NonStatic(self, other):
        return self + other

    def subMatrices_NonStatic(self, other):
        return self - other

    def initEmptyMatrix(self, rows, columns):
        self.matrix = [[0 for columnIterator in range(columns)] for rowIterator in range(rows)]

    @staticmethod
    def multiplyMatrices_Static(firstMatrix, secondMatrix):
        return (firstMatrix * secondMatrix)
    def multiplyMatrices_NonStatic(self, other):
        return self * other

    def getReversedMatrix(self):
        resultMatrix = Matrix()
        resultMatrix.initEmptyMatrix(self.getColumnsCount(), self.getColumnsCount())
        for rowIterator in range(self.getRowsCount()):
            for columnIterator in range(self.getColumnsCount()):
                resultMatrix.matrix[columnIterator][rowIterator] = self.matrix[rowIterator][columnIterator]
        return resultMatrix

    def truediv(self, other):
        return self * other.getReversedMatrix()

    @staticmethod
    def divideMatrices_Static(firstMatrix, secondMatrix):
        return firstMatrix / secondMatrix

    def divideMatrices_NonStatic(self, other):
        return self / other
