from matrix import Matrix

        
matrixOne = Matrix()
matrixOne.readFile("matricesVectors/task_four/matrix_one.txt")
matrixTwo = Matrix()
matrixTwo.readFile("matricesVectors/task_four/matrix_two.txt")

        
(matrixOne + matrixTwo).writeFile("matricesVectors/task_four/output.txt")
(matrixOne - matrixTwo).writeFile("matricesVectors/task_four/output.txt")
(matrixOne * matrixTwo).writeFile("matricesVectors/task_four/output.txt")
(matrixOne / matrixTwo).writeFile("matricesVectors/task_four/output.txt")
