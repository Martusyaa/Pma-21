from exceptions import MatrixOperationError

        
def matrixSumValidator(method):
    def wrapper(self, other):
        if self.rows == other.rows         \
        and self.columns == other.columns:
            return method(self, other)
        else: 
            raise MatrixOperationError("Wrong matrix size") 
    return wrapper
        
        
def matrixMulValidator(method):
    def wrapper(self, other):
        if self.rows == other.columns        \
        and self.columns == other.rows:
            return method(self, other)
        else: 
            raise MatrixOperationError("Wrong matrix size") 
    return wrapper
        
        
def matrixInvertValidator(method):
    def wrapper(self):
        if self.rows == self.columns:
            return method(self)
        else:
            raise MatrixOperationError("Wrong matrix size")
    return wrapper
        
        
def matrixDivValidator(method):
    def wrapper(self, other):
        if self.rows == other.columns        \
        and self.columns == other.rows       \
        and self.rows == other.columns       \
        and self.columns == other.rows:
            return method(self, other)
        else: 
            raise MatrixOperationError("Wrong matrix size") 
    return wrapper