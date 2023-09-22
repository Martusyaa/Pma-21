def read(self, filename):
    with open(filename) as f:
        line = f.readlines()
        self.vector = []
        for i in line:
            items = i.split()
            for j in items:
                self.vector.append(int(j))
            self.size = len(self.vector)


#     # def write (self, filename):
#     #     s=[str(i) for i in self.vector]
#     #     with open (filename,"w") as f:
#     #         f.write(" ".join(s))


def add_vectors(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Different vector sizes")
    result = [x + y for x, y in zip(vec1, vec2)]
    return result


def subtract_vectors(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Different vector sizes")
    result = [x - y for x, y in zip(vec1, vec2)]
    return result


def multiply_vectors(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Different vector sizes")
    result = sum(x * y for x, y in zip(vec1, vec2))
    return result


def divide_vectors(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Different vector sizes")
    result = [x / y for x, y in zip(vec1, vec2)]
    return result
