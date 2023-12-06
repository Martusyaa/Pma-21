def validator(operation):
    def decorator(self, other_matrix):
        if len(self.data) != len(other_matrix.data):
            raise ValueError("Matrices have different sizes and can't be calculated")
        return operation(self, other_matrix)
    return decorator