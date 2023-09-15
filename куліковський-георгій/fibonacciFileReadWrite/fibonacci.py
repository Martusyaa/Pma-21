class Fibonacci:
    
    def __init__(self, row:list, maxNum:float):
        self.row = row
        self.maxNum = maxNum
    
    def fibonacci(self, row=[]):
        if row == []:
            resultRow = [*self.row,]
        else:
            resultRow = row
            
        if resultRow[-1] > self.maxNum:
            resultRow.pop()
            return resultRow
        else:
            resultRow.append(resultRow[-1] + resultRow[-2])
            return self.fibonacci(resultRow)
    
    def __str__(self):
        return str(self.fibonacci())