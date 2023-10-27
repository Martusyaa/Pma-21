class Fibonacci:
    
    def __init__(self, row:list, maxNum:float):
        self.row = row
        self.maxNum = maxNum
    
    def fibonacci(self, row=[]):
        
        fibonacci_operation = lambda a, b: (b, a + b)
        
        if row == []:
            resultRow = [*self.row,]
        else:
            resultRow = row
            
        if resultRow[-1] > self.maxNum:
            resultRow.pop()
            return resultRow
        else:
            a, b = fibonacci_operation(resultRow[-2], resultRow[-1])
            resultRow.append(b)
    
    
    def __str__(self):
        return str(self.fibonacci())