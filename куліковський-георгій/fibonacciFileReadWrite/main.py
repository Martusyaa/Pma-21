from fibonacci import Fibonacci


def readRow():
    
    
    PATH = "fibonacciFileReadWrite/input.txt"
    
    
    try:
        with open(PATH) as file:
            nums = [float(i) for i in file.read().split()]
            return nums   
    except FileNotFoundError:
        print("File Not Found")
        

def readMax():
    

    PATH = "fibonacciFileReadWrite/maxNum.txt"
    
    
    try:
        with open(PATH) as file:
            maxNum = int(file.read())
            return maxNum
    except FileNotFoundError:
        print("File not found")
    
    

def writeFile(string):
    
    PATH = "fibonacciFileReadWrite/output.txt"
    
    
    try:
        with open(PATH, "a") as file:
            file.write(f"{string}\n")
    except FileNotFoundError:
        print("File Not Found")
    

fibonacci = Fibonacci(row=readRow(), maxNum=readMax())
writeFile(fibonacci.fibonacci())
print(fibonacci.row)