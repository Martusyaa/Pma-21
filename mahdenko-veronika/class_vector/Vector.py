class Vector:

    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def print_vector(self):
        print(self.data)

    def add_vector(self, vectorSecond: 'Vector'):
        if self.size != vectorSecond.size:
            raise ValueError("Довжина векторів повинна бути однаковою для додавання.")
        else:
            result_vector = Vector([x + y for x, y in zip(self.data, vectorSecond.data)])
            return result_vector


    def difference_vector(self, vectorSecond: 'Vector'):
        if self.size != vectorSecond.size:
            raise ValueError("Довжина векторів повинна бути однаковою для віднімання.")
        else:
            result_vector = Vector([x - y for x, y in zip(self.data, vectorSecond.data)])
        return result_vector


    def multiplication_vector(self, vectorSecond: 'Vector'):
        if self.size != vectorSecond.size:
            raise ValueError("Довжина векторів повинна бути однаковою для множення.")
        else:
            result_vector = Vector([x * y for x, y in zip(self.data, vectorSecond.data)])
        return result_vector


    def division_vector(self, vectorSecond: 'Vector'):
        if self.size != vectorSecond.size:
            raise ValueError("Довжина векторів повинна бути однаковою для ділення.")
        else:
            result_vector = Vector([x / y for x, y in zip(self.data, vectorSecond.data)])
            for i in range(len(result_vector.data)):
                result_vector.data[i] = round(result_vector.data[i], 2)
        return result_vector

    @staticmethod
    def read_vector_from_file(filename):
        with open(filename, 'r') as file:
            vector = file.readline().split(',')
            data = [float(i) for i in vector]
        v = Vector(data)
        return v

    def write_vector_to_file(self, filename, action):
        with open(filename, 'a+') as file:
            file.write(f"Result of {action}: \n")
            vector_str = ', '.join(map(str, self.data))
            file.write(vector_str + '\n')
            file.write("\n")
