from Files import VECTOR_ERROR

def validator(func):
    def wrapper(vector_one, vector_two):
        if len(vector_one) != len(vector_two):
            raise ValueError(VECTOR_ERROR)
        return func(vector_one, vector_two)
    return wrapper