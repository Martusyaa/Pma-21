from Parser import ParseRow
from DifferentLengthsException import DifferentLengthsException
from NonValidDimensionsForMultiplicationException import NonValidDimensionsForMultiplicationException


class Vector:
    def init(self, vector=None):
        if (vector is None):
            self.vector = []
        else:
            self.vector = vector

    def getLength(self):
        return self.vector.len()

    def readFromFile(self, fileName):
        with open(fileName) as fileToReadFrom:
            lines = fileToReadFrom.readlines()
            if (lines.len() > 1):
                for line in lines:
                    currentRow = ParseRow(line)
                    if (currentRow == []): continue
                    for element in currentRow:
                        self.vector.append(float(element))
            else:
                self.vector = ParseRow(lines[0])

    def writeToFile(self, fileName):
        with open(fileName, "w") as fileToWriteTo:
            fileToWriteTo.write(str(self))

    def add(self, other):
        resultVector = []

        if (self.vector.len() != other.vector.len()):
            raise DifferentLengthsException('Lengths of vectors are different')

        for iterator in range(0, self.vector.len()):
            resultVector.append(float(self.vector[iterator]) + float(other.vector[iterator]))
        return Vector(resultVector)

    def sub(self, other):
        resultVector = []
        if (self.vector.len() != other.vector.len()):
            raise DifferentLengthsException('Lengths of vectors are different')
        for iterator in range(0, self.vector.len()):
            resultVector.append(float(self.vector[iterator]) - float(other.vector[iterator]))
        return Vector(resultVector)

    def str(self):
        result = ''
        for element in self.vector:
            result += str(element) + '\n'
        return result

    @staticmethod
    def addVectors_Static(firstVector, secondVector):
        return firstVector + secondVector

    @staticmethod
    def subVectors_Static(firstVector, secondVector):
        return firstVector + secondVector

    @classmethod
    def addVectors_NonStatic(self, other):
        return self + other

    @classmethod
    def subVectors_NonStatic(self, other):
        return self - other

    def mul(self, other):
        result = 0
        if (self.getLength() != other.getLength()):
            raise DifferentLengthsException('Lengths are different')
        for iterator in range(self.getLength()):
            result += float(self.vector[iterator]) * float(other.vector[iterator])
        return result

    def truediv(self, other):
        result = []
        if (self.getLength() != other.getLength()):
            raise DifferentLengthsException('Lengths are different')
        for iterator in range(self.getLength()):
            result.append(float(self.vector[iterator]) / float(other.vector[iterator]))
        return Vector(result)

    @staticmethod
    def multiplyVector_Static(firstVector, secondVector):
        return firstVector * secondVector

    def multiplyVector_NonStatic(self, other):
        return self * other

    @staticmethod
    def divideVectors_Static(firstVector, secondVector):
        return firstVector / secondVector

    def divideVector_NonStatic(self, other):
        return self / other
