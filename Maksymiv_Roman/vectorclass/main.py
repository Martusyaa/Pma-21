from Matrix import Matrix
from Vector import Vector
from DifferentDimensionsException import DifferentDimensionsException
from NonValidDimensionsForMultiplicationException import NonValidDimensionsForMultiplicationException
from DifferentLengthsException import DifferentLengthsException
resultForMatrices = open('resultForMatrices.txt', 'a')
resultForVectors = open('resultForVectors.txt', 'a')

try:
    firstMatrix = Matrix()
    secondMatrix = Matrix()

    firstMatrix.readFromFile("first_matrix.txt")
    secondMatrix.readFromFile("second_matrix.txt")

    resultMatrix = firstMatrix.divideMatrices_NonStatic(secondMatrix)
    resultMatrix.writeToFile("out.txt")
    print('Two matrices are multiplied')
except DifferentDimensionsException as e:
    resultForMatrices.write(str(e))
except NonValidDimensionsForMultiplicationException as e:
    resultForMatrices.write(str(e))

try:
    firstVector = Vector()
    secondVector = Vector()

    firstVector.readFromFile('first_vector.txt')
    secondVector.readFromFile('second_vector.txt')
    resultVector = Vector.divideVectors_Static(firstVector, secondVector)
    resultOfMultiplication = Vector.multiplyVector_Static(firstVector, secondVector)
    resultVector.writeToFile('resultForVectors.txt')

    resultForVectors.write('result of multiplication: ' + str(resultOfMultiplication))
    resultForVectors.close()
except DifferentLengthsException as e:
    resultForVectors.write(str(e))

