class DifferentLength (Exception):
    "raise exception if vectors or matrixes have different length"
    pass

class Empty (Exception):
    "raise exception if vector or matrix is empty"
    pass

class FalseLength(Exception):
    "raise exception if length of matrix is > 3"
    pass

class ZeroDeterminat(Exception):
    "raise exception if determinat is zero"
    pass