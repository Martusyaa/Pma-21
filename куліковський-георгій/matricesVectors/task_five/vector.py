from validators import vectorLenValidator


class Vector:
    
    def __init__(self, *args):
        if args == None:
            self.vector = []
        else:
            self.vector = list(args)
    
    
    def append(self, value):
        self.vector.append(value)
        
    
    def pop(self):
        return self.vector.pop()
    
    
    def __len__(self):
        return len(self.vector)
    
    
    def __repr__(self):
        return self.vector
        
    
    def __str__(self):
        return str([round(num, 2) for num in self.vector]).strip("[]")
        
    @vectorLenValidator
    def __add__(self, other):
        result = Vector()
        for i in range(len(self)):
            result.append(self.vector[i] + other.vector[i])
        return result
    
    
    @vectorLenValidator
    def __sub__(self, other):
        result = Vector()
        for i in range(len(self)):
            result.append(self.vector[i] - other.vector[i])
        return result
        
    
    @vectorLenValidator  
    def __mul__(self, other):
        result = Vector()
        for i in range(len(self)):
            result.append(self.vector[i] * other.vector[i])
        return result
        
    
    @vectorLenValidator
    def __truediv__(self, other):
        result = Vector()
        for i in range(len(self)):
            result.append(self.vector[i] / other.vector[i])
        return result   
    
    
    def writeFile(self, path):
    
        try:
            with open(path, "a") as file:
                file.write(f"{str(self)}\n")
        except FileNotFoundError:
            print("File Not Found")
            
            
    def readFile(self, path:str):
    
        try:
            with open(path, "r") as file:
                self.vector = ([float(i) for i in list(file.read().split())])
                return self
        except FileNotFoundError:
            print("File Not Found")