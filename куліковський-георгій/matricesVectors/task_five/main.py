from vector import Vector



vectorOne = Vector().readFile("task_five/vector_one.txt")
vectorTwo = Vector().readFile("task_five/vector_two.txt")

        
(vectorOne + vectorTwo).writeFile("task_five/output.txt")
(vectorOne - vectorTwo).writeFile("task_five/output.txt")
(vectorOne * vectorTwo).writeFile("task_five/output.txt")
(vectorOne / vectorTwo).writeFile("task_five/output.txt")
