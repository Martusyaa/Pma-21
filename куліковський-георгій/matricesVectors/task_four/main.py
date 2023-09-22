from matrix import Matrix

        
matrixOne = Matrix().readFile("task_four/matrix_one.txt")
matrixTwo = Matrix().readFile("task_four/matrix_two.txt")

        
(matrixOne + matrixTwo).writeFile("task_four/output.txt")
(matrixOne - matrixTwo).writeFile("task_four/output.txt")
(matrixOne * matrixTwo).writeFile("task_four/output.txt")
(matrixOne / matrixTwo).writeFile("task_four/output.txt")