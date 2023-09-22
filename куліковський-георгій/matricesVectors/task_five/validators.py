from exceptions import VectorOperationError


def vectorLenValidator(func):
    def wrapper(vectorOne, vectorTwo):
        if len(vectorOne) == len(vectorTwo):
            return func(vectorOne, vectorTwo)
        else:
            raise VectorOperationError
    return wrapper