class Vector:
    def __init__(self, n=1):
        self.size = n
        self.vector = [0 for i in range(self.size)]

    def read(self, filename):
        with open(filename) as f:
            line = f.readlines()
            self.vector = []
            for i in line:
                items = i.split()
                for j in items:
                    self.vector.append(int(j))
            self.size = len(self.vector)

    # def write (self, filename):
    #     s=[str(i) for i in self.vector]
    #     with open (filename,"w") as f:
    #         f.write(" ".join(s))

    def addvector(self, a):
        if self.size != a.size:
            raise ValueError("Diferent size ")
        res = Vector(self.size)
        for i in range(self.size):
            res.vector[i] = self.vector[i] + a.vector[i]
        return res

    def substructvector(self, a):
        if self.size != a.size:
            raise ValueError("Diferent size ")
        res = Vector(self.size)
        for i in range(self.size):
            res.vector[i] = self.vector[i] - a.vector[i]
        return res

    def multiplication(self, a):
        if self.size != a.size:
            raise ValueError("Diferent size ")
        res = 0
        for i in range(self.size):
            res += self.vector[i] * a.vector[i]
        return res

    def division(self, a):
        if self.size != a.size:
            raise ValueError("Diferent size ")
        res = Vector(self.size)
        for i in range(self.size):
            res.vector[i] = self.vector[i] / a.vector[i]
        return res

    def write(self, filename, result1=None, result2=None, result3=None, result4=None):
        with open(filename, "w") as f:
            if result1 is not None:
                f.write("Result addition: " + " ".join(map(str, result1.vector)) + "\n")
            if result2 is not None:
                f.write("Result multiplication: " + str(result2) + "\n")
            if result3 is not None:
                f.write("Result subtraction: " + " ".join(map(str, result3.vector)) + "\n")
            if result4 is not None:
                f.write("Result division: " + " ".join(map(str, result4.vector)) + "\n")