from vector import Vector



vectorOne = Vector().readFile("matricesVectors/task_five/vector_one.txt")
vectorTwo = Vector().readFile("matricesVectors/task_five/vector_two.txt")

        
(vectorOne + vectorTwo).writeFile("matricesVectors/task_five/output.txt")
(vectorOne - vectorTwo).writeFile("matricesVectors/task_five/output.txt")
(vectorOne * vectorTwo).writeFile("matricesVectors/task_five/output.txt")
(vectorOne / vectorTwo).writeFile("matricesVectors/task_five/output.txt")
